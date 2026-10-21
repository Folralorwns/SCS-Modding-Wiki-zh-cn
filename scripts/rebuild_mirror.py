#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One command to rebuild the whole mirror: fetch -> markdown -> layout.

    python scripts/rebuild_mirror.py              # full rebuild (~35 min, 757 pages + 675 images)
    python scripts/rebuild_mirror.py --force      # ignore cached pages/images
    python scripts/rebuild_mirror.py --skip-fetch # only re-convert / re-layout

The final tree is Markdown-only (default output: src/English_Ver):

    src/English_Ver/
    ├── README.md
    ├── index.md
    ├── manifest.json
    ├── pages/<group>/…​.md
    └── images/…
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent


def run(script: str, *args: str) -> None:
    cmd = [sys.executable, str(HERE / script), *args]
    print("+ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=PROJECT, check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description="Rebuild src/ (Markdown mirror)")
    ap.add_argument("--out", default="src/English_Ver")
    ap.add_argument("--force", action="store_true", help="refetch pages and images")
    ap.add_argument("--skip-fetch", action="store_true", help="reuse cached html/ (not available after md-only run)")
    ap.add_argument("--md-only", action="store_true", default=True, help="keep only Markdown (default)")
    ap.add_argument("--clone-to", default="", help="optionally copy the result to another folder (overwrites)")
    args = ap.parse_args()

    out = args.out
    if not args.skip_fetch:
        extra = ["--force"] if args.force else []
        run("fetch_wiki_sources.py", "--out", out, *extra)
    run("html_to_markdown.py",
        "--src", f"{out}/html/wiki",
        "--out", f"{out}/md/wiki",
        "--manifest", f"{out}/manifest.json")
    run("organize_layout.py", "--root", out, "--md-only")
    run("relocate_images.py", "--root", out)
    if args.clone_to:
        import shutil
        target = Path(args.clone_to)
        print(f"+ clone {out} -> {target}", flush=True)
        shutil.copytree(PROJECT / out, PROJECT / target, dirs_exist_ok=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
