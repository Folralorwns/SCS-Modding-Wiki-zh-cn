#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert the mirrored HTML pages (scr/html/wiki) into Markdown (scr/md/wiki).

The Markdown keeps the same directory layout and depth as the HTML tree, so the
already-rewritten relative links to ../images/ keep working. Only ".html" link
targets are rewritten to ".md".

Usage:
    python scripts/html_to_markdown.py                # full conversion
    python scripts/html_to_markdown.py --limit 5      # quick check
"""

from __future__ import annotations

import argparse
import html as html_mod
import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, unquote

from bs4 import BeautifulSoup, NavigableString, Tag

INLINE_TAGS = {
    "a", "b", "strong", "i", "em", "code", "tt", "kbd", "samp", "img", "br",
    "span", "sup", "sub", "small", "big", "font", "u", "s", "strike", "mark",
    "time", "var", "cite", "dfn", "abbr", "q", "del", "ins", "wbr", "bdi", "bdo",
}
BLOCK_TAGS = {
    "p", "div", "section", "center", "ul", "ol", "li", "table", "pre", "dl",
    "blockquote", "h1", "h2", "h3", "h4", "h5", "h6", "figure", "hr", "form",
}
SKIP_TAGS = {"script", "style", "input", "label", "button", "noscript"}


def squeeze(text: str) -> str:
    return re.sub(r"[ \t\r\n\u00a0]+", " ", text)


TAG_LIKE = re.compile(r"<(/?)([A-Za-z][A-Za-z0-9-]*)(\s*/?)>")


def escape_angle(text: str) -> str:
    """Keep literal <tag>-looking text from turning into inline HTML."""
    return TAG_LIKE.sub(lambda m: f"&lt;{m.group(1)}{m.group(2)}{m.group(3)}&gt;", text)


def fix_href(href: str) -> str:
    href = (href or "").strip()
    if not href or href.startswith("#") or re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I):
        return href
    base, sep, frag = href.partition("#")
    if base.lower().endswith(".html"):
        base = base[:-5] + ".md"
    # parentheses break the markdown link syntax unless encoded
    base = base.replace("(", "%28").replace(")", "%29").replace(" ", "%20")
    return base + sep + frag


@dataclass
class Ctx:
    shift: int = 0
    pulse: int = 0


class Converter:
    def __init__(self, shift: int) -> None:
        self.ctx = Ctx(shift=shift)

    # ------------------------------------------------------------------ #
    # inline
    # ------------------------------------------------------------------ #
    def inline(self, node: Tag) -> str:
        out: list[str] = []
        for child in node.children:
            if isinstance(child, NavigableString):
                out.append(escape_angle(squeeze(str(child))))
            elif child.name in SKIP_TAGS:
                continue
            elif child.name in INLINE_TAGS:
                out.append(self.render_tag(child))
            else:
                out.append(self.inline(child))
        return "".join(out)

    def render_tag(self, el: Tag) -> str:
        """Render a single inline element (a, b, img, …) including its own markup."""
        name = el.name
        if name in ("b", "strong"):
            inner = self.inline(el).strip()
            return f"**{inner}**" if inner else ""
        if name in ("i", "em", "cite", "var", "dfn"):
            inner = self.inline(el).strip()
            return f"*{inner}*" if inner else ""
        if name in ("code", "tt", "kbd", "samp"):
            text = squeeze(el.get_text()).strip()
            if not text:
                return ""
            fence = "`"
            while fence in text:
                fence += "`"
            pad = " " if text.startswith("`") or text.endswith("`") else ""
            return f"{fence}{pad}{text}{pad}{fence}"
        if name == "a":
            text = self.inline(el).strip()
            href = fix_href(el.get("href", ""))
            if not href or href.startswith("#"):
                return text
            if text:
                return f"[{text}]({href})"
            return f"<{href}>"
        if name == "img":
            return self.image(el)
        if name == "br":
            return "<br>"
        if name in ("sup", "sub"):
            return f"<{name}>{self.inline(el).strip()}</{name}>"
        if name == "pre":
            return self.pre_inline(el)
        if name in ("ul", "ol", "table", "dl", "figure"):
            return "<br>" + re.sub(r"\s*\n\s*", "<br>", self.block(el)).strip()
        if name == "p":
            inner = self.inline(el).strip()
            return inner + "<br>" if inner else ""
        return self.inline(el)

    def image(self, el: Tag) -> str:
        src = (el.get("src") or "").strip()
        if not src:
            return ""
        alt = squeeze(el.get("alt") or "").strip()
        if not alt:
            alt = unquote(src.rsplit("/", 1)[-1])
            alt = re.sub(r"^\d+px-", "", alt)
        return f"![{alt}]({src})"

    def pre_inline(self, el: Tag) -> str:
        """Code block rendered inside a table cell / list item."""
        text = el.get_text().replace("\r\n", "\n").replace("\r", "\n").rstrip()
        lines = [html_mod.escape(ln, quote=False) for ln in text.split("\n")]
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        return "<br><code>" + "<br>".join(lines) + "</code>"

    def caption_of(self, el: Tag) -> str:
        cap = el.find("figcaption") or el.find(class_="thumbcaption") or el.find(class_="thumbcaption")
        if cap is None:
            return ""
        text = re.sub(r"\s+", " ", self.inline(cap)).strip()
        text = re.sub(r"^\[\s*\]\s*", "", text)  # magnify stub
        return text

    def figure(self, el: Tag) -> str:
        img = el.find("img")
        if img is None:
            return ""
        md = self.image(img)
        cap = self.caption_of(el)
        if cap:
            md += f"\n\n*{cap}*"
        return md + "\n\n"

    # ------------------------------------------------------------------ #
    # blocks
    # ------------------------------------------------------------------ #
    def blocks(self, node: Tag, indent: int = 0) -> str:
        parts: list[str] = []
        buf: list[str] = []

        def flush() -> None:
            if not buf:
                return
            text = re.sub(r"\s+", " ", "".join(buf)).strip()
            text = re.sub(r"^(?:<br>\s*)+", "", text)
            text = re.sub(r"(?:\s*<br>)+$", "", text).strip()
            if text:
                parts.append(text + "\n\n")
            buf.clear()

        for child in node.children:
            if isinstance(child, NavigableString):
                text = escape_angle(squeeze(str(child)))
                if text.strip():
                    buf.append(text)
            elif child.name in SKIP_TAGS:
                continue
            elif child.name in INLINE_TAGS:
                buf.append(self.render_tag(child))
            else:
                flush()
                parts.append(self.block(child, indent))
        flush()
        return "".join(p for p in parts if p)

    def block(self, el: Tag, indent: int = 0) -> str:
        name = el.name
        if name in SKIP_TAGS:
            return ""
        classes = set(el.get("class") or [])

        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = min(int(name[1]) + self.ctx.shift, 6)
            text = self.inline(el).strip()
            return f"{'#' * level} {text}\n\n" if text else ""

        if name == "p":
            text = self.inline(el).strip()
            text = re.sub(r"^(?:<br>\s*)+", "", text)
            text = re.sub(r"(?:\s*<br>)+$", "", text).strip()
            return f"{text}\n\n" if text else ""

        if name in ("ul", "ol"):
            return self.list_block(el, indent)

        if name == "dl":
            return self.dl_block(el)

        if name == "table":
            return self.table_block(el)

        if name == "pre":
            return self.pre_block(el)

        if name == "figure":
            return self.figure(el)

        if name == "blockquote":
            inner = self.blocks(el).strip()
            if not inner:
                return ""
            quoted = "\n".join("> " + line if line else ">" for line in inner.split("\n"))
            return quoted + "\n\n"

        if name == "hr":
            return "---\n\n"

        if name == "img":
            md = self.image(el)
            return f"{md}\n\n" if md else ""

        if name in ("div", "section", "center", "main", "body"):
            if "toc" in classes or "toctitle" in classes:
                return ""
            if "thumb" in classes or classes & {"floatright", "floatleft", "tright", "tleft"}:
                if el.find("img") is not None and el.find(class_="thumbcaption") is not None:
                    return self.figure(el)
            if classes & {"notification", "tip", "note", "warning", "ambox"} or "tutorial_navigation" in classes:
                inner = self.blocks(el).strip()
                if not inner:
                    return ""
                quoted = "\n".join("> " + line if line else ">" for line in inner.split("\n"))
                return quoted + "\n\n"
            return self.blocks(el, indent)

        if name in ("span", "small", "big", "font", "u", "s", "strike", "mark", "time"):
            text = self.inline(el).strip()
            return f"{text}\n\n" if text else ""

        # unknown container: recurse
        return self.blocks(el, indent)

    def list_block(self, el: Tag, indent: int = 0) -> str:
        ordered = el.name == "ol"
        start = 1
        try:
            start = int(el.get("start") or 1)
        except ValueError:
            start = 1
        lines: list[str] = []
        index = start
        for li in el.find_all("li", recursive=False):
            nested: list[Tag] = []
            chunks: list[str] = []
            for child in li.children:
                if isinstance(child, NavigableString):
                    chunks.append(squeeze(str(child)))
                elif child.name in ("ul", "ol"):
                    nested.append(child)
                elif child.name in SKIP_TAGS:
                    continue
                elif child.name == "pre":
                    chunks.append(self.pre_inline(child))
                elif child.name in INLINE_TAGS:
                    chunks.append(self.render_tag(child))
                else:
                    chunks.append(self.inline(child) if child.name not in BLOCK_TAGS else self.block(child).strip())
            text = re.sub(r"\s+", " ", "".join(chunks)).strip()
            marker = f"{index}." if ordered else "-"
            lines.append(" " * indent + f"{marker} {text}".rstrip())
            index += 1
            for sub in nested:
                sub_text = self.list_block(sub, indent + 2).rstrip("\n")
                if sub_text:
                    lines.append(sub_text)
        return "\n".join(lines) + "\n\n"

    def dl_block(self, el: Tag) -> str:
        lines: list[str] = []
        for child in el.find_all(["dt", "dd"], recursive=False):
            text = re.sub(r"\s+", " ", self.inline(child)).strip()
            if not text:
                continue
            if child.name == "dt":
                lines.append(f"**{text}**")
            else:
                lines.append(f": {text}")
        return ("\n".join(lines) + "\n\n") if lines else ""

    def pre_block(self, el: Tag) -> str:
        text = el.get_text().replace("\r\n", "\n").replace("\r", "\n")
        lines = [ln.rstrip() for ln in text.split("\n")]
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        body = "\n".join(lines)
        fence = "```"
        while fence in body:
            fence += "`"
        return f"{fence}\n{body}\n{fence}\n\n"

    def cell_md(self, cell: Tag) -> str:
        text = self.inline(cell)
        text = re.sub(r"\s+", " ", text).strip()
        return text.replace("|", "\\|")

    def table_block(self, el: Tag) -> str:
        rows = [r for r in el.find_all("tr") if r.find_parent("table") is el]
        if not rows:
            return ""
        grid = [[c for c in r.find_all(["th", "td"]) if c.find_parent("tr") is r] for r in rows]
        grid = [r for r in grid if r]
        if not grid:
            return ""
        if any(c.get("colspan") or c.get("rowspan") for row in grid for c in row):
            return self.html_table(el)

        width = max(len(r) for r in grid)
        grid = [r + [None] * (width - len(r)) for r in grid]

        has_header = all(c.name == "th" for c in grid[0]) if grid[0] else False
        if has_header:
            header, body = grid[0], grid[1:]
        else:
            header, body = [None] * width, grid

        def line(cells: list[Tag | None]) -> str:
            return "| " + " | ".join(self.cell_md(c) if c is not None else "" for c in cells) + " |"

        out: list[str] = []
        cap = el.find("caption")
        if cap is not None:
            cap_text = re.sub(r"\s+", " ", self.inline(cap)).strip()
            if cap_text:
                out.append(f"*{cap_text}*")
                out.append("")
        out.append(line(header))
        out.append("| " + " | ".join("---" for _ in range(width)) + " |")
        for row in body:
            out.append(line(row))
        return "\n".join(out) + "\n\n"

    def html_table(self, el: Tag) -> str:
        raw = str(el)
        raw = re.sub(r'href="([^"]*)"', lambda m: f'href="{fix_href(m.group(1))}"', raw)
        return raw + "\n\n"


# --------------------------------------------------------------------------- #
# document level
# --------------------------------------------------------------------------- #
META_RE = re.compile(r"<!-- source: (.*?) \| revision: (.*?) \| captured: (.*?) -->")


def convert_file(src: Path, dst: Path) -> tuple[str, int]:
    soup = BeautifulSoup(src.read_text(encoding="utf-8"), "html.parser")
    main = soup.find("main")
    if main is None:
        return "", 0
    title_el = main.find("h1", class_="page-title")
    title = squeeze(title_el.get_text()).strip() if title_el is not None else src.stem
    for junk in main.select("h1.page-title, p.page-sub"):
        junk.decompose()

    shift = 1 if main.find("h1") is not None else 0
    conv = Converter(shift)
    body = conv.blocks(main)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"^(?:<br>\s*)+", "", body, flags=re.M)
    body = re.sub(r"(?<=[^\s\[(])!\[", " ![", body)

    # metadata from the html footer
    source = revid = captured = ""
    footer = main.find_next("footer")
    if footer is not None:
        links = footer.find_all("a", href=True)
        source = links[0]["href"] if links else ""
        text = footer.get_text(" ", strip=True)
        m = re.search(r"revision (\S+)", text)
        revid = m.group(1) if m else ""
        m = re.search(r"Captured ([0-9: -]+)", text)
        captured = m.group(1).strip() if m else ""

    md = f"# {title}\n"
    if body:
        md += f"\n{body}\n"
    if source:
        md += f"\n<!-- source: {source} | revision: {revid} | captured: {captured} -->\n"
    md = re.sub(r"\n{3,}", "\n\n", md)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(md, encoding="utf-8", newline="\n")
    return title, len(md)


def build_index(entries: list[dict], out_root: Path, ns_names: dict[int, str], generated: str) -> str:
    by_ns: dict[int, list[dict]] = {}
    for e in entries:
        by_ns.setdefault(e["ns"], []).append(e)

    lines = [f"# SCS Modding Wiki — 离线索引\n",
             f"共 {len(entries)} 个页面，抓取于 {generated}。HTML 版本见 [`../html/wiki/`](../html/wiki/)，"
             f"原始 wikitext 见 [`../wikitext/`](../wikitext/)，图片见 [`../images/`](../images/)。\n"]
    for ns in sorted(by_ns):
        items = sorted(by_ns[ns], key=lambda e: e["title"].lower())
        lines.append(f"## {ns_names.get(ns, ns)} ({len(items)})\n")
        for e in items:
            rel = e["md"].split("wiki/", 1)[-1]
            dest = quote(f"wiki/{rel}", safe="/-._~")
            lines.append(f"- [{e['title']}]({dest})")
        lines.append("")
    out_root.mkdir(parents=True, exist_ok=True)
    path = out_root / "index.md"
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    return str(path)


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert scr/html/wiki to scr/md/wiki")
    ap.add_argument("--src", default="scr/html/wiki")
    ap.add_argument("--out", default="scr/md/wiki")
    ap.add_argument("--manifest", default="scr/manifest.json")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    src_root = Path(args.src).resolve()
    out_root = Path(args.out).resolve()
    files = sorted(src_root.rglob("*.html"))
    if args.limit:
        files = files[:args.limit]

    okay = failed = 0
    entries: list[dict] = []
    for i, src in enumerate(files, 1):
        rel = src.relative_to(src_root)
        dst = out_root / rel.with_suffix(".md")
        try:
            title, size = convert_file(src, dst)
            okay += 1
            entries.append({"title": title, "src": str(src), "md": str(dst), "bytes": size})
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"  FAILED {src}: {exc!r}", flush=True)
        if i % 100 == 0:
            print(f"  {i}/{len(files)}", flush=True)

    # enrich the manifest with md paths
    man_path = Path(args.manifest)
    if man_path.exists():
        man = json.loads(man_path.read_text(encoding="utf-8"))
        md_map = {Path(e["src"]).resolve(): e["md"] for e in entries}
        for page in man.get("pages", []):
            hp = Path("scr") / page["html"]
            try:
                key = hp.resolve()
            except OSError:
                continue
            if key in md_map:
                page["md"] = str(Path(md_map[key]).relative_to(Path("scr").resolve())).replace("\\", "/")
        man.setdefault("counts", {})["markdown"] = okay
        man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

        ns_names = {int(k): v for k, v in enumerate(
            ["Article", "Talk", "User", "User talk", "Project", "Project talk", "File", "File talk",
             "MediaWiki", "MediaWiki talk", "Template", "Template talk", "Help", "Help talk",
             "Category", "Category talk"])}
        idx_entries = []
        for page in man.get("pages", []):
            if "md" not in page:
                continue
            idx_entries.append({"title": page["title"], "ns": page["ns"], "md": page["md"]})
        generated = man.get("generated", "")
        idx = build_index(idx_entries, Path("scr/md"), ns_names, generated)
        print(f"index: {idx}")

    print(f"converted {okay} pages, failed {failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
