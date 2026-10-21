#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reorganise the flat scrape (scr/html/wiki, scr/md/wiki, scr/wikitext) into a
namespace-based layout:

    scr/
    ├── README.md
    ├── index.md / index.html
    ├── manifest.json
    ├── pages/                Markdown, grouped by namespace
    │   ├── articles/  files/  templates/  users/  user_talk/
    │   └── talk/  project/  mediawiki/  category/
    ├── html/                 rendered HTML, same grouping
    ├── wikitext/             raw wikitext, same grouping
    └── images/

Every relative link (page -> page, page -> image, html -> wikitext) is rewritten
so the mirror keeps working.  Safe to run once; it is a no-op when the layout is
already organised.

Usage:
    python scripts/organize_layout.py [--root scr]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from pathlib import Path
from urllib.parse import quote, unquote

from bs4 import BeautifulSoup

GROUPS = {
    0: ("articles", ""),
    1: ("talk", "Talk:"),
    2: ("users", "User:"),
    3: ("user_talk", "User talk:"),
    4: ("project", "SCS Modding:"),
    5: ("project_talk", "SCS Modding talk:"),
    6: ("files", "File:"),
    7: ("file_talk", "File talk:"),
    8: ("mediawiki", "MediaWiki:"),
    9: ("mediawiki_talk", "MediaWiki talk:"),
    10: ("templates", "Template:"),
    11: ("template_talk", "Template talk:"),
    12: ("help", "Help:"),
    13: ("help_talk", "Help talk:"),
    14: ("category", "Category:"),
    15: ("category_talk", "Category talk:"),
}

INVALID = set('<>:"\\|?*')


def safe_name(text: str) -> Path:
    parts = []
    for seg in text.split("/"):
        seg = "".join("_" if (c in INVALID or ord(c) < 32) else c for c in seg).strip().rstrip(".")
        parts.append(seg or "_")
    return Path(*parts)


def rel_link(target: Path, from_file: Path) -> str:
    rel = os.path.relpath(target, from_file.parent).replace(os.sep, "/")
    return quote(rel, safe="/:@$&*+,;=~-._")


def move(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.exists() and src.resolve() != dst.resolve():
        os.replace(src, dst)


# --------------------------------------------------------------------------- #
# link rewriting
# --------------------------------------------------------------------------- #
def rewrite_html(path: Path, old_path: Path, mapping: dict[Path, Path]) -> int:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    changed = 0

    def fix(value: str) -> str:
        nonlocal changed
        value = value.strip()
        if not value or value.startswith(("#", "mailto:", "javascript:", "data:")):
            return value
        if re.match(r"^[a-z][a-z0-9+.-]*:", value, re.I) or value.startswith("//"):
            return value
        base, sep, frag = value.partition("#")
        old_target = (old_path.parent / unquote(base)).resolve()
        new_target = mapping.get(old_target)
        if new_target is None:
            if not old_target.exists():
                return value
            new_target = old_target
        new_value = rel_link(new_target, path) + ((sep + frag) if sep else "")
        if new_value != value:
            changed += 1
        return new_value

    for tag in soup.find_all(["a", "img", "source", "video", "audio", "track"]):
        for attr in ("href", "src", "poster"):
            if tag.has_attr(attr):
                tag[attr] = fix(tag[attr])
        if tag.has_attr("srcset"):
            items = []
            for item in tag["srcset"].split(","):
                item = item.strip()
                if not item:
                    continue
                bits = item.split()
                bits[0] = fix(bits[0])
                items.append(" ".join(bits))
            tag["srcset"] = ", ".join(items)

    path.write_text(str(soup), encoding="utf-8", newline="\n")
    return changed


MD_LINK = re.compile(r"\]\(([^()\s]+)\)")


def rewrite_md(path: Path, old_path: Path, mapping: dict[Path, Path]) -> int:
    text = path.read_text(encoding="utf-8")
    changed = 0

    def repl(match: re.Match) -> str:
        nonlocal changed
        value = match.group(1)
        if value.startswith(("#", "mailto:")) or re.match(r"^[a-z][a-z0-9+.-]*:", value, re.I):
            return match.group(0)
        base, sep, frag = value.partition("#")
        old_target = (old_path.parent / unquote(base)).resolve()
        new_target = mapping.get(old_target)
        if new_target is None:
            if not old_target.exists():
                return match.group(0)
            new_target = old_target
        new_value = rel_link(new_target, path) + ((sep + frag) if sep else "")
        if new_value != value:
            changed += 1
        return f"]({new_value})"

    new_text = MD_LINK.sub(repl, text)
    if changed:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return changed


# --------------------------------------------------------------------------- #
# index files
# --------------------------------------------------------------------------- #
def build_index_md(pages: list[dict], root: Path, generated: str, md_only: bool) -> str:
    groups: dict[str, list[dict]] = {}
    for p in pages:
        groups.setdefault(p["group"], []).append(p)

    if md_only:
        note = ("本页是唯一入口；图片在 [`../images/`](../images/)，"
                "修订信息（revid / 原文 URL）见 [`manifest.json`](manifest.json)。")
    else:
        note = ("HTML 版见 [`index.html`](index.html)，原始抓取见 [`html/`](html/) 与 "
                "[`wikitext/`](wikitext/)，图片见 [`images/`](images/)。")
    out = [f"# SCS Modding Wiki — 离线索引\n",
           f"共 **{len(pages)}** 个页面，抓取于 {generated}。{note}\n"]
    for name in sorted(groups):
        items = sorted(groups[name], key=lambda p: p["title"].lower())
        out.append(f"## {name} ({len(items)})\n")
        for p in items:
            out.append(f"- [{p['title']}]({quote(p['md'], safe='/-._~')})")
        out.append("")
    (root / "index.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8", newline="\n")
    return str(root / "index.md")


def build_index_html(pages: list[dict], root: Path, generated: str) -> str:
    groups: dict[str, list[dict]] = {}
    for p in pages:
        groups.setdefault(p["group"], []).append(p)

    sections = []
    for name in sorted(groups):
        items = sorted(groups[name], key=lambda p: p["title"].lower())
        rows = "\n".join(
            f'<li><a href="{quote(p["html"], safe="/-._~")}">{p["title"]}</a></li>' for p in items
        )
        sections.append(f'<section><h2>{name} <small>({len(items)})</small></h2><ul>\n{rows}\n</ul></section>')

    doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SCS Modding Wiki — 离线镜像索引</title>
<style>
:root{{color-scheme:light}}
body{{margin:0;font-family:-apple-system,"Segoe UI","Microsoft YaHei",Arial,sans-serif;line-height:1.6;color:#202122}}
main{{max-width:60rem;margin:0 auto;padding:1.5rem 1.2rem 3rem}}
h1{{font-size:1.6rem;margin:0 0 .3rem}}
h2{{font-size:1.15rem;margin:1.8rem 0 .4rem;border-bottom:1px solid #eaecf0;padding-bottom:.2em}}
h2 small{{color:#72777d;font-weight:400;font-size:.75em}}
ul{{margin:0;padding-left:1.3rem;columns:2;column-gap:2.5rem}}
li{{break-inside:avoid;margin:.1rem 0}}
a{{color:#3366cc;text-decoration:none}}a:hover{{text-decoration:underline}}
p.meta{{color:#54595d;font-size:.9rem}}
@media(max-width:720px){{ul{{columns:1}}}}
</style>
</head>
<body><main>
<h1>SCS Modding Wiki — 离线镜像</h1>
<p class="meta">抓取于 {generated} · 共 {len(pages)} 个页面 · Markdown 版见 <a href="index.md">index.md</a></p>
{''.join(sections)}
</main></body></html>
"""
    (root / "index.html").write_text(doc, encoding="utf-8", newline="\n")
    return str(root / "index.html")


def build_readme(pages: list[dict], root: Path, generated: str, counts: dict, md_only: bool) -> str:
    per_group = {}
    for p in pages:
        per_group[p["group"]] = per_group.get(p["group"], 0) + 1
    group_lines = "\n".join(f"| `{name}/` | {per_group[name]} |" for name in sorted(per_group))
    scripts_rel = os.path.relpath(Path(__file__).resolve().parent, root).replace(os.sep, "/")
    root_name = root.name

    if md_only:
        layout = f"""{root_name}/
├── README.md            本说明
├── index.md             ★ 全站索引（从这里进入）
├── manifest.json        机器清单（标题 / URL / 分组 / revid / 时间戳）
├── pages/               ★ 正文 Markdown（翻译工作区）
│   ├── articles/          主条目，保留 Documentation/… 层级
│   ├── files/             文件页（原 File: 前缀已去掉）
│   ├── templates/         模板页
│   ├── users/             用户页
│   ├── user_talk/         用户讨论页
│   ├── talk/              条目讨论页
│   ├── project/           项目命名空间页
│   ├── mediawiki/         界面消息页
│   └── category/          分类页
└── (无 images/；图片统一存放在上一级 ../images/<分组>/<页面路径>/)"""
        pipeline = ("python scripts/rebuild_mirror.py                # 抓取 → 转换 → 整理（约 35 分钟）\n"
                    "python scripts/share_images.py --root src       # 图片合并到 src/images/")
        note = ("每个 `.md` 末尾保留 `<!-- source: … | revision: … -->` 注释，"
                "可据此判断上游是否更新。")
    else:
        layout = f"""{root_name}/
├── README.md
├── index.md / index.html
├── manifest.json
├── pages/               Markdown
├── html/                渲染 HTML
├── wikitext/            原始 wikitext
└── images/"""
        pipeline = """python scripts/fetch_wiki_sources.py --out scr
python scripts/html_to_markdown.py
python scripts/organize_layout.py"""
        note = "每个文件只保存当前修订。"

    return f"""# {root_name} — SCS Modding Wiki 离线镜像（Markdown）

由 [`{scripts_rel}/rebuild_mirror.py`]({scripts_rel}/rebuild_mirror.py) 生成：
抓取（fetch_wiki_sources）→ 转换（html_to_markdown）→ 整理（organize_layout）。
**请勿手工编辑**，需要更新时重跑脚本即可。

- 抓取时间：{generated}
- 页面：{len(pages)}（全部命名空间中的现存页面，仅 Markdown）
- 图片：{counts.get('images', 0)} 个文件
- 入口：[`index.md`](index.md)

## 目录结构

```
{layout}
```

| 分组 | 页面数 |
| --- | --- |
{group_lines}

`pages/` 按命名空间分区，图片按「引用它的页面」归档在上一级 `../images/<分组>/<页面路径>/`，
所有语言版本共享同一份图片。页面内链接均为相对路径；移动目录或重命名页面时请用脚本重算链接。

## 抓取范围

- **包含**：主条目、File 文件页、Template 模板、User 用户页、Talk 讨论页、Project、MediaWiki 命名空间页面。
- **不含**：`Special:` 动态页面、历史版本、编辑页（`robots.txt` 亦禁止）。
- {note}

## 更新流程（在仓库根目录执行）

```bash
{pipeline}
```

## 版权

Wiki 内容版权归 SCS Software 及各位编辑者所有，本目录仅作离线翻译参考，不再分发。
"""


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Reorganise the mirror by namespace")
    ap.add_argument("--root", default="scr")
    ap.add_argument("--md-only", action="store_true",
                    help="keep only pages/ + images/ + index.md + manifest.json")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    man_path = root / "manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8"))
    pages = man["pages"]
    generated = man.get("generated", "")
    md_only = args.md_only or all("html" not in p for p in pages)

    used: set[str] = set()
    mapping: dict[Path, Path] = {}
    plan = []
    for page in pages:
        ns = page["ns"]
        title = page["title"]
        group, prefix = GROUPS[ns]
        sub = title[len(prefix):] if title.startswith(prefix) else title
        rel = safe_name(sub)
        key = f"{group}/{rel}".lower()
        n = 2
        while key in used:
            rel = rel.with_name(f"{rel.name} ({n})")
            key = f"{group}/{rel}".lower()
            n += 1
        used.add(key)

        md_new = Path("pages") / group / (str(rel) + ".md")
        html_new = Path("html") / group / (str(rel) + ".html")
        wiki_new = Path("wikitext") / group / (str(rel) + ".wiki")
        md_old = root / page["md"]
        html_old = (root / page["html"]) if page.get("html") else None
        wiki_old = (root / page["wikitext"]) if page.get("wikitext") else None

        mapping[md_old.resolve()] = root / md_new
        if html_old and html_old.exists():
            mapping[html_old.resolve()] = root / html_new
        if wiki_old and wiki_old.exists():
            mapping[wiki_old.resolve()] = root / wiki_new

        plan.append((html_old, html_new, wiki_old, wiki_new, md_old, md_new))
        page["group"] = group
        page["md"] = md_new.as_posix()
        if md_only:
            page.pop("html", None)
            page.pop("wikitext", None)
        else:
            page["html"] = html_new.as_posix()
            page["wikitext"] = wiki_new.as_posix()

    moved = 0
    for html_old, html_new, wiki_old, wiki_new, md_old, md_new in plan:
        pairs = [(md_old, md_new)]
        if not md_only:
            if html_old:
                pairs.append((html_old, html_new))
            if wiki_old:
                pairs.append((wiki_old, wiki_new))
        for old, new in pairs:
            if old is not None and old.exists():
                move(old, root / new)
                moved += 1

    links = 0
    for html_old, html_new, wiki_old, wiki_new, md_old, md_new in plan:
        if not md_only and html_old is not None:
            links += rewrite_html(root / html_new, html_old, mapping)
        links += rewrite_md(root / md_new, md_old, mapping)

    # drop legacy layout remnants
    stale_index = root / "md" / "index.md"
    if stale_index.exists():
        stale_index.unlink()
    if md_only:
        shutil.rmtree(root / "html", ignore_errors=True)
        shutil.rmtree(root / "wikitext", ignore_errors=True)
        (root / "index.html").unlink(missing_ok=True)
    for legacy in (root / "html" / "wiki", root / "md", root / "wikitext" / "wiki"):
        if legacy.exists():
            for path in sorted(legacy.rglob("*"), reverse=True):
                if path.is_dir():
                    try:
                        path.rmdir()
                    except OSError:
                        pass
            try:
                legacy.rmdir()
            except OSError:
                pass

    counts = dict(man.get("counts", {}))
    counts["markdown"] = len(pages)
    man["counts"] = counts
    man["layout"] = {"version": 3 if md_only else 2, "md_only": md_only,
                     "groups": sorted({p["group"] for p in pages})}
    man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

    build_index_md(pages, root, generated, md_only)
    if not md_only:
        build_index_html(pages, root, generated)
    (root / "README.md").write_text(build_readme(pages, root, generated, counts, md_only),
                                    encoding="utf-8", newline="\n")

    print(f"moved {moved} files, rewrote {links} links, pages {len(pages)}, md_only={md_only}")
    for name in sorted({p["group"] for p in pages}):
        print(f"  {name:<12} {sum(1 for p in pages if p['group'] == name):>4}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
