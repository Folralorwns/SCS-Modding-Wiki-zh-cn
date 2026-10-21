#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-home every referenced image into a folder named after the page using it.

    scr/images/8/88/Foo.png              (wiki hash layout)
 -> scr/images/articles/Documentation/Tools/Foo.png

The Markdown page `pages/articles/Documentation/Tools.md` gets
`images/articles/Documentation/Tools/…`, so a translator sees exactly the
assets of the page they are working on.

- shared images are copied into every page folder that uses them
- two different images with the same basename get a `-2`, `-3` suffix
- a link whose file went missing is resolved by basename from anywhere in images/
- unreferenced files (srcset variants) are dropped
- all Markdown links are rewritten; parentheses are percent-encoded so the
  links stay parseable

Idempotent: running it twice leaves the layout unchanged.

Usage:
    python scripts/relocate_images.py [--root scr] [--dry-run]
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path
from urllib.parse import quote, unquote

SAFE = "/:@$&*+,;=~-._"


def rel_link(target: Path, from_file: Path) -> str:
    rel = os.path.relpath(target, from_file.parent).replace(os.sep, "/")
    return quote(rel, safe=SAFE)


def scan_links(text: str):
    """Yield (start, end, destination) for every `](…)` inline link.

    Handles balanced parentheses inside the destination.
    """
    i = 0
    while True:
        j = text.find("](", i)
        if j < 0:
            return
        k = j + 2
        depth = 0
        start = k
        while k < len(text):
            ch = text[k]
            if ch == "(":
                depth += 1
            elif ch == ")":
                if depth == 0:
                    break
                depth -= 1
            elif ch in " \n\t":
                break
            k += 1
        yield start, k, text[start:k]
        i = k + 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Move images into per-page folders")
    ap.add_argument("--root", default="scr")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    pages_root = root / "pages"
    images_root = root / "images"
    staging = root / ".images_staging"

    if not pages_root.exists():
        print("no pages/ directory")
        return 1

    by_name: dict[str, Path] = {}
    for path in sorted(images_root.rglob("*")):
        if path.is_file():
            by_name.setdefault(path.name, path)

    pages: list[tuple[Path, list[tuple[int, int, str, Path]]]] = []
    unresolved = 0
    for md in sorted(pages_root.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        refs = []
        for start, end, href in scan_links(text):
            if "/images/" not in href or re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I):
                continue
            target = md.parent / unquote(href.partition("#")[0])
            if not target.exists():
                fallback = by_name.get(unquote(href).rsplit("/", 1)[-1])
                if fallback is None:
                    unresolved += 1
                    continue
                target = fallback
            refs.append((start, end, href, target.resolve()))
        if refs:
            pages.append((md, refs))

    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    allocated: dict[tuple[str, Path], str] = {}
    copied = 0
    for md, refs in pages:
        rel_dir = md.relative_to(pages_root).with_suffix("")
        out_dir = staging / rel_dir
        used: dict[str, Path] = {}
        for _s, _e, _h, source in refs:
            key = (str(rel_dir), source)
            if key in allocated:
                continue
            stem, suffix = source.stem, source.suffix
            name, n = source.name, 2
            while name in used and used[name] != source:
                name = f"{stem}-{n}{suffix}"
                n += 1
            used[name] = source
            allocated[key] = name
            out_dir.mkdir(parents=True, exist_ok=True)
            dest = out_dir / name
            if not dest.exists():
                shutil.copy2(source, dest)
                copied += 1

    if args.dry_run:
        print(f"would copy {copied} images for {len(pages)} pages "
              f"({len(allocated)} page/image pairs), unresolved {unresolved}")
        shutil.rmtree(staging)
        return 0

    rewritten = 0
    for md, refs in pages:
        rel_dir = md.relative_to(pages_root).with_suffix("")
        text = md.read_text(encoding="utf-8")
        edits = []
        for start, end, href, source in refs:
            name = allocated[(str(rel_dir), source)]
            new_target = images_root / rel_dir / name
            frag = href.partition("#")[2]
            new_href = rel_link(new_target, md) + (("#" + frag) if frag else "")
            if new_href != href:
                edits.append((start, end, new_href))
        for start, end, new_href in reversed(edits):
            text = text[:start] + new_href + text[end:]
            rewritten += 1
        md.write_text(text, encoding="utf-8", newline="\n")

    shutil.rmtree(images_root)
    staging.rename(images_root)

    files = sum(1 for p in images_root.rglob("*") if p.is_file())
    man_path = root / "manifest.json"
    if man_path.exists():
        import json
        man = json.loads(man_path.read_text(encoding="utf-8"))
        man.setdefault("counts", {})["images"] = files
        man["image_layout"] = "per-page"
        man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print(f"copied {copied}, pages {len(pages)}, links {rewritten}, "
          f"files {files}, unresolved {unresolved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
