#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Keep one shared image folder for all language versions.

    src/English_Ver/images/…   ┐
    src/Chinese_Ver/images/…   ├─>  src/images/…
                                    ┘

Every Markdown page under `src/<version>/pages/` keeps the same relative
image paths; the links are rewritten to point at `src/images/`.
Idempotent: safe to run after every rebuild.

Usage:
    python scripts/share_images.py --root src
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
    ap = argparse.ArgumentParser(description="Move images to a shared folder and fix links")
    ap.add_argument("--root", default="src", help="folder that contains the language versions")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    image_root = root / "images"
    versions = sorted(d for d in root.iterdir() if d.is_dir() and (d / "pages").exists())
    if not versions:
        print("no language versions found")
        return 1

    # 1. consolidate the first images/ folder into root/images
    source = next((v / "images" for v in versions if (v / "images").exists()), None)
    if source is not None:
        if image_root.exists():
            shutil.copytree(source, image_root, dirs_exist_ok=True)
            print(f"merged {source} -> {image_root}")
        else:
            source.rename(image_root)
            print(f"moved {source} -> {image_root}")

    # 2. rewrite image links in every version
    rewritten = 0
    for version in versions:
        for md in sorted((version / "pages").rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            edits = []
            for start, end, href in scan_links(text):
                if "/images/" not in href or re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I):
                    continue
                base, _, frag = href.partition("#")
                suffix = unquote(base).split("/images/", 1)[1]
                new_href = rel_link(image_root / suffix, md) + (("#" + frag) if frag else "")
                if new_href != href:
                    edits.append((start, end, new_href))
            if edits:
                for start, end, new_href in reversed(edits):
                    text = text[:start] + new_href + text[end:]
                    rewritten += 1
                md.write_text(text, encoding="utf-8", newline="\n")

    # 3. drop the per-version copies
    for version in versions:
        shutil.rmtree(version / "images", ignore_errors=True)

    files = sum(1 for p in image_root.rglob("*") if p.is_file()) if image_root.exists() else 0
    print(f"versions={len(versions)} links rewritten={rewritten} images={files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
