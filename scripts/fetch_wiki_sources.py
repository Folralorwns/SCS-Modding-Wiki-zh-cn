#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mirror every page of https://modding.scssoft.com/ into ./scr/.

For every existing page (all namespaces) the script stores:

  scr/html/wiki/<Title>.html       rendered article HTML, offline-ready
                                   (images + internal links rewritten to locals)
  scr/wikitext/<Title>.wiki        raw wikitext of the current revision
  scr/images/...                   mirrored files from /images/
  scr/index.html                   browsable index of every captured page
  scr/manifest.json                machine readable inventory (revids, sizes...)
  scr/README.md                    short description of the dump

Usage:
    python scripts/fetch_wiki_sources.py                 # incremental
    python scripts/fetch_wiki_sources.py --force         # refetch everything
    python scripts/fetch_wiki_sources.py --no-images     # skip images
"""

from __future__ import annotations

import argparse
import html as html_mod
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse

import requests
from bs4 import BeautifulSoup

SITE = "https://modding.scssoft.com"
API = SITE + "/api.php"
UA = "SCS-Modding-Wiki-zh-cn/1.0 (one-off offline mirror for translation work)"

NAMESPACES = {
    0: "Article", 1: "Talk", 2: "User", 3: "User talk", 4: "Project",
    5: "Project talk", 6: "File", 7: "File talk", 8: "MediaWiki",
    9: "MediaWiki talk", 10: "Template", 11: "Template talk", 12: "Help",
    13: "Help talk", 14: "Category", 15: "Category talk",
}

INVALID_CHARS = set('<>:"\\|?*')


# --------------------------------------------------------------------------- #
# small helpers
# --------------------------------------------------------------------------- #
def log(msg: str = "") -> None:
    print(msg, flush=True)


def norm_title(title: str) -> str:
    """Normalise a MediaWiki title for link lookups."""
    t = title.replace("_", " ").strip()
    t = re.sub(r"\s+", " ", t)
    return (t[:1].upper() + t[1:]) if t else t


def safe_segment(seg: str) -> str:
    """Make one path segment safe on Windows."""
    s = "".join("_" if (c in INVALID_CHARS or ord(c) < 32) else c for c in seg)
    s = s.replace("/", "_").strip().rstrip(".")
    if not s:
        s = "_"
    if s.upper() in {"CON", "PRN", "AUX", "NUL"} or re.fullmatch(r"(COM|LPT)[0-9]", s.upper()):
        s = "_" + s
    return s


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def rel_url(target: Path, from_file: Path) -> str:
    rel = os.path.relpath(target, from_file.parent).replace(os.sep, "/")
    return quote(rel, safe="/:@!$&'()*+,;=~-._")


class RateLimiter:
    """Global, thread-safe request pacing with adaptive slowdown."""

    def __init__(self, interval: float) -> None:
        self.interval = interval
        self._last = 0.0
        self._lock = threading.Lock()

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            delta = self._last + self.interval - now
            if delta > 0:
                time.sleep(delta)
            self._last = time.monotonic()

    def slow_down(self) -> None:
        with self._lock:
            self.interval = min(self.interval * 1.5 + 0.05, 3.0)


class Wiki:
    def __init__(self, interval: float = 0.2) -> None:
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": UA})
        self.limiter = RateLimiter(interval)
        self.requests_made = 0

    def api(self, **params: object) -> dict:
        params.setdefault("format", "json")
        params.setdefault("formatversion", "2")
        last_err = ""
        for attempt in range(6):
            self.limiter.wait()
            try:
                r = self.s.post(API, data=params, timeout=120)
                self.requests_made += 1
            except requests.RequestException as exc:  # network hiccup
                last_err = repr(exc)
                time.sleep(min(2 ** attempt, 20))
                continue
            if r.status_code == 200:
                try:
                    return r.json()
                except ValueError:
                    last_err = "invalid JSON"
                    time.sleep(2)
                    continue
            if r.status_code == 429 or r.status_code >= 500:
                retry_after = r.headers.get("Retry-After", "")
                self.limiter.slow_down()
                wait = float(retry_after) if retry_after.isdigit() else min(2 ** attempt + 1, 20)
                last_err = f"HTTP {r.status_code}"
                time.sleep(wait)
                continue
            raise RuntimeError(f"API error HTTP {r.status_code}: {params.get('action')} {params.get('list', '')}")
        raise RuntimeError(f"API request failed after retries: {last_err}")

    # -- listings ---------------------------------------------------------- #
    def list_pages(self) -> list[dict]:
        pages: list[dict] = []
        for ns in range(16):
            cont: dict = {}
            while True:
                data = self.api(action="query", list="allpages", apnamespace=ns,
                                aplimit="max", **cont)
                pages.extend(data.get("query", {}).get("allpages", []))
                cont = data.get("continue") or {}
                if not cont:
                    break
            log(f"  namespace {ns:>2} ({NAMESPACES[ns]:<14}) {sum(1 for p in pages if p['ns'] == ns):>4} pages")
        return pages

    def list_images(self) -> list[dict]:
        images: list[dict] = []
        cont: dict = {}
        while True:
            data = self.api(action="query", list="allimages", ailimit="max",
                            aiprop="url|size", **cont)
            images.extend(data.get("query", {}).get("allimages", []))
            cont = data.get("continue") or {}
            if not cont:
                break
        return images

    # -- bulk wikitext ----------------------------------------------------- #
    def fetch_wikitext(self, titles: list[str]) -> dict[str, dict]:
        meta: dict[str, dict] = {}
        chunks = [titles[i:i + 50] for i in range(0, len(titles), 50)]
        for i, chunk in enumerate(chunks, 1):
            data = self.api(action="query", prop="revisions|info",
                            titles="|".join(chunk),
                            rvprop="content|ids|timestamp", rvslots="main")
            for page in data.get("query", {}).get("pages", []):
                title = page.get("title", "")
                entry = meta.setdefault(title, {"missing": True})
                if page.get("missing"):
                    continue
                revs = page.get("revisions") or []
                if not revs:
                    continue
                rev = revs[0]
                slot = (rev.get("slots") or {}).get("main") or {}
                entry.update({
                    "missing": False,
                    "revid": rev.get("revid"),
                    "timestamp": rev.get("timestamp"),
                    "content": slot.get("content", ""),
                })
            log(f"  wikitext chunk {i}/{len(chunks)} ({len(chunk)} pages)")
        return meta

    # -- rendered html ----------------------------------------------------- #
    def parse_html(self, title: str) -> tuple[str, int | None]:
        data = self.api(action="parse", page=title, prop="text",
                        disablelimitreport=1, disableeditsection=1)
        err = data.get("error")
        if err:
            raise RuntimeError(err.get("info", "parse error"))
        return data["parse"]["text"], data["parse"].get("revid")


# --------------------------------------------------------------------------- #
# html post processing
# --------------------------------------------------------------------------- #
IMG_ATTRS = ("src", "poster", "data-src")


class Rewriter:
    def __init__(self, out: Path, html_paths: dict[str, Path], norm: dict[str, str]) -> None:
        self.out = out
        self.images_root = out / "images"
        self.html_paths = html_paths
        self.norm = norm
        self.image_jobs: dict[Path, str] = {}
        self.internal_hits = 0
        self.broken = 0

    # -- urls -------------------------------------------------------------- #
    def image_local(self, url_path: str) -> tuple[Path | None, str]:
        """Map /images/<...> to a local path + the relative-to-images key."""
        path = unquote(url_path.split("?")[0].split("#")[0])
        if not path.startswith("/images/"):
            return None, ""
        parts = [safe_segment(p) for p in path[len("/images/"):].split("/") if p]
        if not parts:
            return None, ""
        return Path(*parts), "/images/" + "/".join(parts)

    def resolve(self, href: str, from_file: Path) -> str | None:
        h = href.strip()
        if not h or h.startswith("#") or h.startswith(("mailto:", "javascript:", "tel:", "data:")):
            return None

        frag = ""
        if h.startswith("//"):
            h = "https:" + h

        if h.startswith(("http://", "https://")):
            p = urlparse(h)
            if p.netloc.lower().lstrip("www.") not in ("modding.scssoft.com",):
                return None
            path, query, frag = p.path, p.query, p.fragment
        elif h.startswith("/"):
            p = urlparse(h)
            path, query, frag = p.path, p.query, p.fragment
        else:
            return None

        title = None
        if path.startswith("/wiki/"):
            title = unquote(path[len("/wiki/"):])
        elif path in ("/index.php", "/w/index.php"):
            qs = parse_qs(query)
            if "title" not in qs:
                return None
            if any(k in qs for k in ("action", "oldid", "diff", "redlink")):
                return SITE + h if h.startswith("/") else h
            title = qs["title"][0]
        elif path.startswith("/images/"):
            local, _ = self.image_local(path)
            if local is None:
                return None
            self.image_jobs[local] = SITE + path
            return rel_url(self.images_root / local, from_file) + (("#" + frag) if frag else "")

        if title is None:
            return SITE + path + (("?" + query) if query else "") + (("#" + frag) if frag else "")

        key = self.norm.get(norm_title(title).lower())
        if key and key in self.html_paths:
            self.internal_hits += 1
            target = self.html_paths[key]
            return rel_url(target, from_file) + (("#" + frag) if frag else "")
        if title.startswith(("Special:", "MediaWiki:")):
            return SITE + "/wiki/" + quote(title)
        self.broken += 1
        return SITE + "/wiki/" + quote(title.replace(" ", "_"))

    def rewrite(self, soup: BeautifulSoup, from_file: Path) -> None:
        for a in soup.find_all("a", href=True):
            new = self.resolve(a["href"], from_file)
            if new:
                a["href"] = new

        for tag in soup.find_all(["img", "source", "video", "audio", "track"]):
            for attr in IMG_ATTRS:
                value = tag.get(attr)
                if not value:
                    continue
                new = self.resolve(value, from_file)
                if new and new.startswith(("../", "./")):
                    tag[attr] = new
            srcset = tag.get("srcset")
            if srcset:
                out = []
                for item in srcset.split(","):
                    item = item.strip()
                    if not item:
                        continue
                    bits = item.split()
                    new = self.resolve(bits[0], from_file)
                    if new and new.startswith(("../", "./")):
                        bits[0] = new
                    out.append(" ".join(bits))
                tag["srcset"] = ", ".join(out)


# --------------------------------------------------------------------------- #
# page rendering
# --------------------------------------------------------------------------- #
CSS = """
:root{color-scheme:light}
*{box-sizing:border-box}
body{margin:0;background:#fff;color:#202122;font-family:-apple-system,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans","Microsoft YaHei",Arial,sans-serif;font-size:15px;line-height:1.65}
a{color:#3366cc;text-decoration:none}
a:hover{text-decoration:underline}
a.new{color:#d73333}
.mirror-bar{position:sticky;top:0;z-index:20;display:flex;flex-wrap:wrap;gap:.75rem;align-items:center;padding:.45rem 1rem;background:#f8f9fa;border-bottom:1px solid #c8ccd1;font-size:.85rem}
.mirror-bar .mirror-ns{color:#54595d}
.mirror-bar .mirror-links{margin-left:auto;display:flex;gap:.9rem}
main{max-width:62rem;margin:0 auto;padding:1.4rem 1.1rem 3.5rem}
h1.page-title{font-family:"Linux Libertine",Georgia,"Times New Roman",serif;font-weight:400;font-size:1.9rem;line-height:1.25;margin:0 0 .35rem;padding-bottom:.35rem;border-bottom:1px solid #a2a9b1}
.page-sub{color:#54595d;font-size:.85rem;margin:0 0 1.4rem}
h2,h3,h4,h5,h6{font-family:"Linux Libertine",Georgia,"Times New Roman",serif;font-weight:400;line-height:1.3;margin:1.4em 0 .5em}
h2{font-size:1.5rem;border-bottom:1px solid #eaecf0;padding-bottom:.2em}
h3{font-size:1.22rem}
h4{font-size:1.08rem}
p{margin:.55em 0}
ul,ol{margin:.4em 0 .6em 1.6em;padding:0}
li{margin:.15em 0}
img{max-width:100%;height:auto}
figure{margin:.6em 0}
table{border-collapse:collapse;font-size:14px}
table.wikitable{border:1px solid #a2a9b1;margin:1em 0;background:#fff}
.wikitable>tbody>tr>th,.wikitable>tbody>tr>td{border:1px solid #a2a9b1;padding:.25em .55em;vertical-align:top}
.wikitable>tbody>tr>th{background:#eaecf0;text-align:left}
pre,code,kbd,samp,.mw-code{font-family:"Cascadia Mono",Consolas,"Courier New",monospace}
pre{border:1px solid #eaecf0;background:#f8f9fa;padding:.8em 1em;overflow:auto;line-height:1.45;font-size:13px;border-radius:2px}
code{background:#f8f9fa;padding:.1em .28em;border-radius:2px;font-size:.9em}
pre code{padding:0;background:none;font-size:inherit}
.toc{display:inline-block;border:1px solid #a2a9b1;background:#f8f9fa;padding:.45em 1.1em;margin:.6em 0 1.2em;font-size:.92em;min-width:14em}
.toc ul{margin:.15em 0 .15em 1.1em;padding:0;list-style:none}
.toc li{margin:.1em 0}
.toc .tocnumber{color:#54595d;padding-right:.45em}
.thumb{margin:.5em 0 1.4em;max-width:100%}
.thumb.tright{float:right;clear:right;margin-left:1.4em}
.thumb.tleft{float:left;clear:left;margin-right:1.4em}
.thumbinner{border:1px solid #c8ccd1;background:#f8f9fa;padding:3px;overflow:hidden;max-width:100%}
.thumbcaption{font-size:.88em;line-height:1.45;padding:.25em .2em}
.mw-empty-elt{display:none}
.mw-collapsible-toggle{font-size:.9em}
.reference,sup.reference{font-size:.8em}
ol.references{font-size:.9em}
blockquote{margin:.8em 0 .8em 1.6em;padding-left:1em;border-left:4px solid #eaecf0;color:#404244}
hr{border:0;border-top:1px solid #c8ccd1;margin:1.2em 0}
.mirror-foot{max-width:62rem;margin:0 auto;padding:1rem 1.1rem 2.5rem;border-top:1px solid #eaecf0;color:#72777d;font-size:.8rem}
.mirror-foot p{margin:.25em 0}
.file-preview{margin:0 0 1.4em;padding:.6em;border:1px solid #eaecf0;background:#fbfbfb;display:inline-block;max-width:100%}
.file-preview img{max-height:420px;width:auto;border:1px solid #c8ccd1;background:#fff;padding:2px}
.file-preview figcaption{font-size:.82em;color:#54595d;margin-top:.4em}
@media (max-width:720px){.thumb.tright,.thumb.tleft{float:none;margin:1em 0}}
"""

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - SCS Modding Wiki</title>
<meta name="description" content="Offline copy of {title} from the SCS Modding Wiki">
<link rel="canonical" href="{url}">
<style>{css}</style>
</head>
<body>
<header class="mirror-bar">
<a class="mirror-home" href="{rel_index}">SCS Modding Wiki &middot; offline</a>
<span class="mirror-ns">{ns}</span>
<span class="mirror-links"><a href="{rel_wiki}">wikitext</a><a href="{url}">original &#8599;</a></span>
</header>
<main>
<h1 class="page-title">{title}</h1>
{sub_block}
{preview}
{body}
</main>
<footer class="mirror-foot">
<p>Captured {when} &middot; revision {revid} &middot; {size}</p>
<p>Source: <a href="{url}">{url}</a></p>
<p>Content of the SCS Modding Wiki; all rights remain with SCS Software and the wiki contributors.</p>
</footer>
</body>
</html>
"""


def render_page(*, title: str, ns: int, meta: dict, body: str, html_path: Path,
                wiki_path: Path | None, out: Path, preview: str = "") -> str:
    rel_index = rel_url(out / "index.html", html_path)
    rel_wiki = rel_url(wiki_path, html_path) if wiki_path else SITE + "/wiki/" + quote(title)
    url = SITE + "/wiki/" + quote(title.replace(" ", "_"))
    ts = (meta.get("timestamp") or "")[:19].replace("T", " ")
    sub_bits = [NAMESPACES.get(ns, "")]
    if ts:
        sub_bits.append(f"last edited {ts}")
    if meta.get("redirect_target"):
        sub_bits.append(f"redirects to {html_mod.escape(meta['redirect_target'])}")
    sub_block = f'<p class="page-sub">{" &middot; ".join(b for b in sub_bits if b)}</p>'
    return PAGE_TMPL.format(
        title=html_mod.escape(title), url=url, css=CSS, rel_index=rel_index,
        rel_wiki=rel_wiki, ns=html_mod.escape(NAMESPACES.get(ns, "Page")), sub_block=sub_block,
        preview=preview, body=body, when=meta.get("fetched", ""), revid=meta.get("revid", "?"),
        size=meta.get("size_label", ""),
    )


# --------------------------------------------------------------------------- #
# index / manifest / readme
# --------------------------------------------------------------------------- #
def build_index(pages: list[dict], html_paths: dict[str, Path], out: Path,
                stats: dict, generated: str) -> str:
    by_ns: dict[int, list[str]] = {}
    for p in pages:
        by_ns.setdefault(p["ns"], []).append(p["title"])

    def tree(titles: list[str]) -> dict:
        root: dict = {"page": None, "children": {}}
        for t in titles:
            node = root
            for seg in t.split("/"):
                node = node["children"].setdefault(seg, {"page": None, "children": {}})
            node["page"] = t
        return root

    def render_node(name: str, node: dict, out_dir: Path, depth: int) -> str:
        lines = []
        label = html_mod.escape(name)
        if node["page"]:
            lines.append(f'<a href="{rel_url(html_paths[node["page"]], out_dir / "index.html")}">{label}</a>')
        else:
            lines.append(f"<span class='dir'>{label}</span>")
        kids = node["children"]
        if kids:
            lines.append("<ul>")
            for key in sorted(kids, key=lambda s: (kids[s]["page"] is None, s.lower())):
                lines.append("<li>" + render_node(key, kids[key], out_dir, depth + 1) + "</li>")
            lines.append("</ul>")
        return "".join(lines)

    sections = []
    for ns in sorted(by_ns):
        titles = sorted(by_ns[ns], key=str.lower)
        body = render_node(NAMESPACES.get(ns, str(ns)) + f" ({len(titles)})", tree(titles), out, 0)
        # the root node itself is not a page -> strip its <span>
        body = body.split("</span>", 1)[-1] if body.startswith("<span") else body
        sections.append(
            f'<section><h2>{NAMESPACES.get(ns, ns)} <small>({len(titles)})</small></h2><div class="tree">{body}</div></section>'
        )

    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SCS Modding Wiki - offline index</title>
<style>{CSS}
.tree ul{{list-style:none;margin:.1em 0 .2em 1.05em;padding:0;border-left:1px dotted #c8ccd1}}
.tree>ul{{margin-left:0}}
.tree li{{margin:.08em 0;line-height:1.5}}
.tree .dir{{color:#54595d;font-weight:600}}
section{{margin:0 0 2rem}}
section h2{{font-size:1.3rem}}
section h2 small{{color:#72777d;font-weight:400;font-size:.75em}}
</style>
</head>
<body>
<header class="mirror-bar">
<a class="mirror-home" href="index.html">SCS Modding Wiki &middot; offline</a>
<span class="mirror-ns">{stats['total']} pages</span>
<span class="mirror-links"><a href="manifest.json">manifest.json</a><a href="{SITE}/">original &#8599;</a></span>
</header>
<main>
<h1 class="page-title">SCS Modding Wiki &mdash; offline mirror</h1>
<p class="page-sub">Captured {generated} &middot; {stats['total']} pages &middot; {stats['images']} images</p>
<p>Every page of <a href="{SITE}/">{SITE.replace('https://', '')}</a> that exists in the wiki was downloaded as a
standalone HTML file (rendered article + mirrored images + rewritten internal links). The raw wikitext of each
page sits next to it under <code>wikitext/</code>.</p>
{''.join(sections)}
</main>
<footer class="mirror-foot"><p>Static copy for translation reference. Special: pages, revision history and
edit views are not mirrored.</p></footer>
</body>
</html>
"""


def make_readme(stats: dict, generated: str, args: argparse.Namespace) -> str:
    return f"""# scr — SCS Modding Wiki 抓取存档

本目录由 [`scripts/fetch_wiki_sources.py`](../scripts/fetch_wiki_sources.py) 从
<{SITE}/> 抓取生成，作为中文翻译项目的原文参考。**请勿手工编辑**，需要更新时重新运行脚本即可。

- 抓取时间：{generated}
- 页面总数：{stats['total']}（全部 16 个命名空间中现存的所有页面）
- 图片：{stats['images']} 个文件，下载失败 {stats['image_failures']} 个
- 渲染失败 / 缺失：{stats['page_failures']} 页

## 目录结构

| 路径 | 内容 |
| --- | --- |
| `html/wiki/` | 每个页面一独立 HTML（正文 + 内联样式），站内链接与图片已改写为相对路径，可离线浏览 |
| `wikitext/` | 与 `html/` 同构的原始 wikitext（`.wiki`），适合做翻译、diff 与批量处理 |
| `images/` | `/images/` 下的图片与缩略图镜像 |
| `md/wiki/` | 由 `html/wiki/` 转换而来的 Markdown（同构目录，站内链接已改为 `.md`，图片路径可直接使用） |
| `md/index.md` | Markdown 版页面索引 |
| `index.html` | 全部页面的可浏览索引（按命名空间分组） |
| `manifest.json` | 机器可读清单：标题、URL、命名空间、本地路径、revid、时间戳、字节数 |

命名空间页面数：{stats['ns_line']}。

## 抓取范围

- **包含**：主条目、File 文件页、Template 模板、User 用户页、Talk 讨论页、Project、MediaWiki 命名空间页面。
  File 页面会在正文上方附带原图预览与「original file」链接。
- **不含**：`Special:` 动态页面（最近更改、全部页面等）、历史版本、编辑页、`action=raw` 视图；
  这些页面由服务器实时生成或属于操作界面，且 `robots.txt` 明确禁止抓取 `Special:`。
- 每个 HTML 只保存当前修订版本；原始 wikitext 同样只保存当前修订。

## 重新抓取

```bash
python scripts/fetch_wiki_sources.py            # 断点续抓（已存在的 html 会跳过）
python scripts/fetch_wiki_sources.py --force    # 全部重新抓取
python scripts/fetch_wiki_sources.py --no-images
```

脚本对 API 做了限速与 429 退避；全量抓取 757 页 + 675 张图片约需 35-40 分钟。

## 版权

Wiki 内容版权归 SCS Software 及各位编辑者所有，本目录仅作离线翻译参考，不再分发。
"""


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Mirror modding.scssoft.com into ./scr/")
    ap.add_argument("--out", default="scr")
    ap.add_argument("--threads", type=int, default=3)
    ap.add_argument("--delay", type=float, default=0.2)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--no-images", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="only the first N pages (testing)")
    args = ap.parse_args()

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    started = time.time()

    wiki = Wiki(args.delay)
    log(f"Mirroring {SITE} -> {out}")

    log("Listing pages ...")
    pages = wiki.list_pages()
    if args.limit:
        pages = pages[:args.limit]
    titles = [p["title"] for p in pages]
    log(f"  total pages: {len(titles)}")

    log("Listing images ...")
    images = wiki.list_images()
    log(f"  total images: {len(images)}")

    # deterministic local paths -------------------------------------------------
    html_paths: dict[str, Path] = {}
    wiki_paths: dict[str, Path] = {}
    used: set[str] = set()
    for t in sorted(titles, key=str.lower):
        segs = [safe_segment(s) for s in t.split("/")]
        rel = Path(*segs)
        base = rel
        n = 2
        while str(rel).lower() in used:
            rel = base.with_name(f"{base.name} ({n})")
            n += 1
        used.add(str(rel).lower())
        html_paths[t] = out / "html" / "wiki" / (str(rel) + ".html")
        wiki_paths[t] = out / "wikitext" / (str(rel) + ".wiki")

    norm: dict[str, str] = {}
    for t in titles:
        norm.setdefault(norm_title(t).lower(), t)

    # --- wikitext ----------------------------------------------------------- #
    log("Downloading wikitext ...")
    meta = wiki.fetch_wikitext(titles)
    page_set = set(titles)
    missing_meta = [t for t in titles if meta.get(t, {}).get("missing", True)]
    if missing_meta:
        log(f"  warning: {len(missing_meta)} titles without content, e.g. {missing_meta[:3]}")

    for t in titles:
        info = meta.get(t, {})
        if info.get("missing"):
            continue
        content = info.get("content", "")
        m = re.match(r"\s*#\s*redirect\s*:?\s*\[\[([^\]|#]+)", content, re.I)
        info["redirect_target"] = m.group(1).strip() if m else ""
        info["content_bytes"] = len(content.encode("utf-8"))
        write_text(wiki_paths[t], content)
    log("  wikitext written")

    # --- rendered html ------------------------------------------------------ #
    rewriter = Rewriter(out, html_paths, norm)
    ns_of = {p["title"]: p["ns"] for p in pages}
    images_root = out / "images"
    file_images: dict[str, Path] = {}
    for img in images:
        local, _ = rewriter.image_local(urlparse(img.get("url", "")).path)
        if local is not None:
            # MediaWiki stores file names with underscores; page titles use spaces.
            file_images[img.get("name", "").replace("_", " ")] = images_root / local
    todo = [t for t in titles if args.force or not html_paths[t].exists()]
    log(f"Rendering html for {len(todo)} pages ({len(titles) - len(todo)} already present) ...")

    failures: list[dict] = []
    done = 0
    for t in titles:
        if t not in todo:
            meta.setdefault(t, {})["fetched"] = "cached"
    lock = threading.Lock()

    def work(title: str) -> tuple[str, str | None, str | None]:
        try:
            body, revid = wiki.parse_html(title)
            return title, body, None
        except Exception as exc:  # noqa: BLE001
            return title, None, repr(exc)

    with ThreadPoolExecutor(max_workers=max(1, args.threads)) as pool:
        futures = [pool.submit(work, t) for t in todo]
        for fut in as_completed(futures):
            title, body, error = fut.result()
            done += 1
            if error:
                failures.append({"title": title, "stage": "parse", "error": error})
                log(f"  [{done}/{len(todo)}] FAILED {title}: {error}")
                continue
            try:
                soup = BeautifulSoup(body, "html.parser")
                html_path = html_paths[title]
                rewriter.rewrite(soup, html_path)
                info = meta.setdefault(title, {})
                info["fetched"] = generated
                info["size_label"] = f"{info.get('content_bytes', 0) / 1024:.1f} KB wikitext"
                preview = ""
                if ns_of.get(title) == 6 and ":" in title:
                    fname = title.split(":", 1)[1]
                    local = file_images.get(fname)
                    if local is not None and local.exists():
                        rel_img = rel_url(local, html_path)
                        kb = local.stat().st_size / 1024
                        orig = SITE + "/wiki/File:" + quote(fname.replace(" ", "_"))
                        preview = (
                            f'<figure class="file-preview"><a href="{rel_img}">'
                            f'<img src="{rel_img}" alt="{html_mod.escape(fname)}" loading="lazy"></a>'
                            f'<figcaption>{html_mod.escape(fname)} &middot; {kb:.0f} KB &middot; '
                            f'<a href="{orig}">original file</a></figcaption></figure>'
                        )
                doc = render_page(title=title, ns=ns_of.get(title, 0),
                                  meta=info, body=str(soup), html_path=html_path,
                                  wiki_path=wiki_paths.get(title), out=out, preview=preview)
                write_text(html_path, doc)
            except Exception as exc:  # noqa: BLE001
                failures.append({"title": title, "stage": "render", "error": repr(exc)})
                log(f"  [{done}/{len(todo)}] RENDER FAILED {title}: {exc!r}")
            if done % 25 == 0 or done == len(todo):
                rate = done / max(time.time() - started, 1e-6)
                log(f"  [{done}/{len(todo)}] {title} ({rate:.1f} pages/s)")

    # --- images ------------------------------------------------------------- #
    image_failures: list[dict] = []
    image_count = 0
    if not args.no_images:
        jobs: dict[Path, str] = {}
        for img in images:
            url = img.get("url", "")
            if "/images/" not in url:
                continue
            path = urlparse(url).path
            local, _ = rewriter.image_local(path)
            if local is not None:
                jobs.setdefault(local, url)
        jobs.update({k: v for k, v in rewriter.image_jobs.items() if k not in jobs})
        log(f"Downloading {len(jobs)} images ...")
        images_root = out / "images"

        def fetch_image(item: tuple[Path, str]) -> tuple[Path, str | None]:
            rel, url = item
            dest = images_root / rel
            if dest.exists() and dest.stat().st_size > 0 and not args.force:
                return rel, None
            for attempt in range(4):
                wiki.limiter.wait()
                try:
                    r = wiki.s.get(url, timeout=120)
                except requests.RequestException as exc:
                    if attempt == 3:
                        return rel, repr(exc)
                    time.sleep(2 ** attempt)
                    continue
                if r.status_code == 200 and r.content:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(r.content)
                    return rel, None
                if r.status_code == 404:
                    return rel, "HTTP 404"
                time.sleep(2 ** attempt + 1)
            return rel, f"HTTP {r.status_code}"

        with ThreadPoolExecutor(max_workers=max(1, args.threads)) as pool:
            for rel, error in pool.map(fetch_image, jobs.items()):
                if error:
                    image_failures.append({"path": str(rel), "error": error})
                else:
                    image_count += 1
        log(f"  images on disk: {sum(1 for _ in images_root.rglob('*') if _.is_file()) if images_root.exists() else 0}")

    # --- inventory ---------------------------------------------------------- #
    ns_counts: dict[str, int] = {}
    for p in pages:
        ns_counts[NAMESPACES[p["ns"]]] = ns_counts.get(NAMESPACES[p["ns"]], 0) + 1
    stats = {
        "total": len(titles),
        "images": image_count,
        "image_failures": len(image_failures),
        "page_failures": len(failures),
        "ns_line": "、".join(f"{k} {v}" for k, v in sorted(ns_counts.items())),
    }

    entries = []
    for p in pages:
        t = p["title"]
        info = meta.get(t, {})
        hp = html_paths[t]
        entries.append({
            "title": t,
            "ns": p["ns"],
            "ns_name": NAMESPACES[p["ns"]],
            "url": SITE + "/wiki/" + quote(t.replace(" ", "_")),
            "html": hp.relative_to(out).as_posix(),
            "wikitext": wiki_paths[t].relative_to(out).as_posix(),
            "revid": info.get("revid"),
            "timestamp": info.get("timestamp"),
            "redirect_to": info.get("redirect_target") or None,
            "wikitext_bytes": info.get("content_bytes"),
            "html_bytes": hp.stat().st_size if hp.exists() else None,
        })

    manifest = {
        "site": SITE,
        "generated": generated,
        "tool": "scripts/fetch_wiki_sources.py",
        "counts": {
            "pages": len(titles),
            "namespaces": ns_counts,
            "images": image_count,
            "image_failures": len(image_failures),
            "page_failures": len(failures),
        },
        "pages": entries,
        "image_failures": image_failures,
        "page_failures": failures,
    }
    write_text(out / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=1))
    write_text(out / "README.md", make_readme(stats, generated, args))
    write_text(out / "index.html", build_index(pages, html_paths, out, stats, generated))

    elapsed = time.time() - started
    log("")
    log(f"Done in {elapsed / 60:.1f} min — {len(titles)} pages, {image_count} images, "
        f"{len(failures)} page failures, {len(image_failures)} image failures, "
        f"{wiki.requests_made} API/HTTP requests")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
