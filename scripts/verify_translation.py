#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check translated pages against their English source (structure must match).

    python scripts/verify_translation.py [--fix-report]

Compares every src/Chinese_Ver/pages/*.md with src/English_Ver/pages/<same path>:

- same number of markdown links and identical link destinations
- same number of code fences, table rows, headings, list markers
- identical trailing <!-- source: … | revision: … --> comment
- file must contain Chinese text (unless the source has no prose)
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

EN = Path("src/English_Ver/pages")
ZH = Path("src/Chinese_Ver/pages")
CJK = re.compile(r"[\u4e00-\u9fff]")
LINK = re.compile(r"\]\(([^()\s]+)\)")
FOOTER = re.compile(r"<!-- source: .*? \| revision: .*? -->")


def stats(text: str) -> dict:
    lines = text.splitlines()
    return {
        "links": Counter(LINK.findall(text)),
        "fences": sum(1 for ln in lines if ln.strip().startswith("```")),
        "table_rows": sum(1 for ln in lines if ln.lstrip().startswith("|")),
        "headings": sum(1 for ln in lines if re.match(r"^#{1,6} ", ln)),
        "bullets": sum(1 for ln in lines if re.match(r"^\s*(?:[-*]|\d+\.) ", ln)),
        "footer": (FOOTER.search(text).group(0) if FOOTER.search(text) else ""),
        "cjk": len(CJK.findall(text)),
        "letters": len(re.findall(r"[A-Za-z]", text)),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paths", nargs="*", help="only check these files")
    args = ap.parse_args()

    if args.paths:
        targets = []
        for raw in args.paths:
            candidate = Path(raw)
            if not candidate.exists():
                candidate = Path("src/Chinese_Ver") / raw
            targets.append(candidate)
    else:
        targets = sorted(ZH.rglob("*.md"))
    problems: list[str] = []
    checked = 0
    for zh in targets:
        rel = zh.resolve().relative_to(ZH.resolve())
        en = EN / rel
        if not en.exists():
            problems.append(f"no source: {rel}")
            continue
        checked += 1
        a, b = stats(zh.read_text(encoding="utf-8")), stats(en.read_text(encoding="utf-8"))
        for key in ("fences", "table_rows", "headings", "bullets"):
            if a[key] != b[key]:
                problems.append(f"{rel}: {key} {a[key]} != {b[key]}")
        if a["links"] != b["links"]:
            missing = b["links"] - a["links"]
            extra = a["links"] - b["links"]
            problems.append(f"{rel}: links differ (missing {sum(missing.values())}, extra {sum(extra.values())})")
        if a["footer"] != b["footer"]:
            problems.append(f"{rel}: source/revision comment changed")
        if b["letters"] > 120 and a["cjk"] == 0:
            problems.append(f"{rel}: not translated (cjk=0)")

    print(f"checked {checked} files, problems {len(problems)}")
    for p in problems[:60]:
        print("  " + p)
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
