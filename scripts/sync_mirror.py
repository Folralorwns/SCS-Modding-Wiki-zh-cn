#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scheduled sync: refresh English_Ver and queue changed pages for translation.

Behaviour
---------
1. Ask the wiki for the current revision of every page (≈35 small API calls) and
   compare it with src/English_Ver/manifest.json → added / changed / removed.
2. If something changed, rebuild the English mirror:
       rebuild_mirror.py --force  →  share_images.py --root src
3. Copy every new/changed English page into the translation queue:

       src/Chinese_Ver/Waiting_For_Trans/<pages-relative-path>.md

   The queue mirrors `pages/` (e.g. Waiting_For_Trans/articles/Documentation/Tools.md),
   so the image links (`../../../images/…`) keep working exactly as in English.

   - pages already translated (footer revision >= wiki revision) are removed from
     the queue automatically
   - pages deleted upstream are removed from the queue
   - src/Chinese_Ver/pages/ is never touched

Scheduling (Windows, daily 03:00)
---------------------------------
    schtasks /Create /SC DAILY /ST 03:00 /TN "scs-wiki-sync" ^
             /TR "E:\\SCS-Modding-Wiki-zh-cn\\scripts\\sync_mirror.cmd"

Scheduling (Linux/macOS)
------------------------
    0 3 * * * cd /path/to/repo && python scripts/sync_mirror.py --log

Usage
-----
    python scripts/sync_mirror.py --check        # only ask the wiki, write report
    python scripts/sync_mirror.py                # sync + queue
    python scripts/sync_mirror.py --skip-rebuild # queue only (no network rebuild)
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
SRC = PROJECT / "src"
EN = SRC / "English_Ver"
ZH = SRC / "Chinese_Ver"
QUEUE = ZH / "Waiting_For_Trans"
STATE = SRC / ".sync_state.json"
REPORT = ZH / "SYNC_REPORT.md"
API = "https://modding.scssoft.com/api.php"
UA = "SCS-Modding-Wiki-zh-cn/1.0 (scheduled sync)"
REV_RE = re.compile(r"\| revision: (\d+)")

log_lines: list[str] = []


def log(message: str) -> None:
    print(message, flush=True)
    log_lines.append(message)


def parse_rev(path: Path) -> int:
    if not path.exists():
        return 0
    m = REV_RE.search(path.read_text(encoding="utf-8"))
    return int(m.group(1)) if m else 0


def api(session: requests.Session, **params) -> dict:
    params.setdefault("format", "json")
    params.setdefault("formatversion", "2")
    for attempt in range(4):
        try:
            r = session.post(API, data=params, timeout=90)
            if r.status_code == 200:
                return r.json()
            if r.status_code == 429:
                time.sleep(3 * (attempt + 1))
                continue
        except requests.RequestException:
            pass
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"API failed: {params.get('list') or params.get('prop')}")


def fetch_page_titles(session: requests.Session) -> list[str]:
    titles: list[str] = []
    for ns in range(16):
        cont: dict = {}
        while True:
            data = api(session, action="query", list="allpages", apnamespace=ns,
                       aplimit="max", **cont)
            titles += [p["title"] for p in data.get("query", {}).get("allpages", [])]
            cont = data.get("continue") or {}
            if not cont:
                break
    return titles


def fetch_revids(session: requests.Session, titles: list[str]) -> dict[str, int]:
    revids: dict[str, int] = {}
    chunks = [titles[i:i + 50] for i in range(0, len(titles), 50)]
    for n, chunk in enumerate(chunks, 1):
        data = api(session, action="query", prop="revisions", rvprop="ids",
                   titles="|".join(chunk))
        for page in data.get("query", {}).get("pages", []):
            revids[page["title"]] = int((page.get("revisions") or [{"revid": 0}])[0]["revid"])
        if n % 8 == 0:
            log(f"  revision batch {n}/{len(chunks)}")
        time.sleep(0.12)
    return revids



def fetch_recent_changes(session: requests.Session, since: datetime) -> list[dict]:
    """Special:RecentChanges equivalent (list=recentchanges)."""
    entries: list[dict] = []
    cont: dict = {}
    start = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = since.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    while True:
        data = api(session, action="query", list="recentchanges",
                   rcprop="title|revid|timestamp|type|loginfo", rclimit="max",
                   rcstart=start, rcend=end, **cont)
        entries += data.get("query", {}).get("recentchanges", [])
        cont = data.get("continue") or {}
        if not cont:
            break
        time.sleep(0.12)
    return entries


def resolve_titles(session: requests.Session, titles: list[str]) -> dict[str, int]:
    """Current revid per title; 0 means the page no longer exists."""
    out: dict[str, int] = {}
    chunks = [titles[i:i + 50] for i in range(0, len(titles), 50)]
    for chunk in chunks:
        data = api(session, action="query", prop="revisions", rvprop="ids",
                   titles="|".join(chunk))
        for page in data.get("query", {}).get("pages", []):
            if page.get("missing") or not page.get("revisions"):
                out[page["title"]] = 0
            else:
                out[page["title"]] = int(page["revisions"][0]["revid"])
    return out


def rebuild() -> None:
    for script, extra in (("rebuild_mirror.py", ["--force"]),
                          ("share_images.py", ["--root", "src"])):
        cmd = [sys.executable, str(HERE / script), *extra]
        log("+ " + " ".join(cmd))
        subprocess.run(cmd, cwd=PROJECT, check=True)



def retarget_links(text: str, dest: Path, en_page: Path) -> str:
    """Point page-to-page links at Chinese_Ver/pages, so they work in the queue
    and after the file is moved into pages/ (both live at the same depth)."""
    import os
    from urllib.parse import quote, unquote

    pages_en = EN / "pages"
    pages_zh = ZH / "pages"

    def rel(target: Path, from_file: Path) -> str:
        relp = os.path.relpath(target, from_file.parent).replace(os.sep, "/")
        return quote(relp, safe="/:@$&*+,;=~-._")

    out = []
    last = 0
    for m in re.finditer(r"\]\(([^()\s]+)\)", text):
        href = m.group(1)
        if re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I) or href.startswith("#"):
            continue
        base, _, frag = href.partition("#")
        if not base.lower().endswith(".md"):
            continue
        target = (en_page.parent / unquote(base)).resolve()
        try:
            rel_path = target.relative_to(pages_en.resolve())
        except ValueError:
            continue
        new = rel(pages_zh / rel_path, dest) + (("#" + frag) if frag else "")
        out.append((m.start(1), m.end(1), new))
    for start, end, new in reversed(out):
        text = text[:start] + new + text[end:]
    return text

def queue_changes(manifest: dict, changed: set[str], removed: set[str]) -> dict[str, list[str]]:
    """Copy changed pages into Waiting_For_Trans; drop ones already translated."""
    result = {"queued": [], "cleared": [], "removed": []}
    pages = {p["title"]: p for p in manifest["pages"]}

    for title in sorted(changed):
        page = pages.get(title)
        if page is None:
            continue
        rel = page["md"]                       # pages/<group>/<path>.md
        en = EN / rel
        zh = ZH / rel                          # translated page, may not exist
        dest = QUEUE / rel[len("pages/"):]     # queue mirrors pages/
        if zh.exists() and parse_rev(zh) >= int(page.get("revid") or 0):
            if dest.exists():
                dest.unlink()
                result["cleared"].append(title)
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(en, dest)
        text = dest.read_text(encoding="utf-8")
        fixed = retarget_links(text, dest, en)
        if fixed != text:
            dest.write_text(fixed, encoding="utf-8", newline="\n")
        result["queued"].append(title)

    for title in sorted(removed):
        page = pages.get(title)
        if page is None:
            continue
        dest = QUEUE / page["md"][len("pages/"):]
        if dest.exists():
            dest.unlink()
        result["removed"].append(title)

    # sweep: drop queue entries that are already translated or gone upstream
    by_md = {p["md"]: p for p in manifest["pages"]}
    for dest in sorted(QUEUE.rglob("*.md")):
        rel = "pages/" + dest.relative_to(QUEUE).as_posix()
        page = by_md.get(rel)
        if page is None:
            dest.unlink()
            continue
        zh = ZH / rel
        if zh.exists() and parse_rev(zh) >= int(page.get("revid") or 0):
            dest.unlink()
            if page["title"] not in result["cleared"]:
                result["cleared"].append(page["title"])
    return result


def write_report(diff: dict, queued: dict | None, timestamp: str) -> None:
    lines = [f"# 同步报告 — {timestamp}", "",
             f"上游：新增 {len(diff['added'])} · 修改 {len(diff['changed'])} · 删除 {len(diff['removed'])}", ""]
    for label, key in (("新增页面", "added"), ("上游已修改", "changed"), ("上游已删除", "removed")):
        if diff[key]:
            lines.append(f"## {label}（{len(diff[key])}）")
            lines += [f"- `{t}`" for t in diff[key][:300]]
            lines.append("")
    if queued is not None:
        lines += [
            "## 待翻译队列（Chinese_Ver/Waiting_For_Trans）",
            f"- 新增待译：{len(queued['queued'])}",
            f"- 已译完并移出队列：{len(queued['cleared'])}",
            f"- 上游删除并移出队列：{len(queued['removed'])}",
        ]
        if queued["queued"]:
            lines += ["", "### 队列内容"] + [f"- [ ] `{t}`" for t in queued["queued"]]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    log(f"report: {REPORT.relative_to(PROJECT)}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Scheduled sync of the SCS wiki mirror")
    ap.add_argument("--check", action="store_true", help="only query upstream, write report")
    ap.add_argument("--skip-rebuild", action="store_true", help="queue only, no rebuild")
    ap.add_argument("--force", action="store_true", help="rebuild even without changes")
    ap.add_argument("--no-queue", action="store_true", help="update English_Ver only")
    ap.add_argument("--log", action="store_true", help="append to src/sync.log")
    ap.add_argument("--days", type=int, default=30, help="look back N days when no state (default 30)")
    ap.add_argument("--full", action="store_true", help="scan every page instead of RecentChanges")
    args = ap.parse_args()

    started = time.time()
    manifest_path = EN / "manifest.json"
    if not manifest_path.exists():
        print("src/English_Ver/manifest.json missing — run rebuild_mirror.py once")
        return 1
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    known = {p["title"]: int(p.get("revid") or 0) for p in manifest["pages"]}
    session = requests.Session()
    session.headers.update({"User-Agent": UA})
    log(f"[{datetime.now().astimezone():%Y-%m-%d %H:%M}] checking upstream")
    if args.full:
        current = fetch_page_titles(session)
        revids = fetch_revids(session, current)
        log(f"  full scan: {len(current)} pages")
        diff = {
            "added": sorted(set(current) - set(known)),
            "removed": sorted(set(known) - set(current)),
            "changed": sorted(t for t in current if t in known and revids.get(t) != known[t]),
        }
    else:
        state_path = SRC / ".sync_state.json"
        state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
        last = state.get("last_sync")
        since = (datetime.fromisoformat(last) if last
                 else datetime.now(timezone.utc) - timedelta(days=args.days))
        log(f"  RecentChanges since {since:%Y-%m-%d %H:%M}")
        entries = fetch_recent_changes(session, since)
        touched = {e["title"] for e in entries
                   if e.get("type") in ("edit", "new") or e.get("logtype") in ("delete", "move")}
        log(f"  {len(entries)} changes, {len(touched)} pages touched")
        revids = resolve_titles(session, sorted(touched)) if touched else {}
        diff = {
            "added": sorted(t for t, rev in revids.items() if rev and t not in known),
            "removed": sorted(t for t, rev in revids.items() if not rev and t in known),
            "changed": sorted(t for t, rev in revids.items()
                              if rev and t in known and rev != known[t]),
        }
    log(f"  added={len(diff['added'])} changed={len(diff['changed'])} removed={len(diff['removed'])}")

    if args.check:
        write_report(diff, None, f"{datetime.now().astimezone():%Y-%m-%d %H:%M:%S}")
        return 0

    if any(diff.values()) or args.force:
        if args.skip_rebuild:
            log("  --skip-rebuild: using current English_Ver")
        else:
            rebuild()
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        log("  nothing to do upstream")

    if args.no_queue:
        write_report(diff, None, f"{datetime.now().astimezone():%Y-%m-%d %H:%M:%S}")
        return 0

    queued = queue_changes(manifest, set(diff["added"]) | set(diff["changed"]), set(diff["removed"]))
    log("queue: queued={} cleared={} removed={}".format(
        len(queued["queued"]), len(queued["cleared"]), len(queued["removed"])))
    write_report(diff, queued, f"{datetime.now().astimezone():%Y-%m-%d %H:%M:%S}")
    (SRC / ".sync_state.json").write_text(
        json.dumps({"last_sync": datetime.now(timezone.utc).isoformat(timespec="seconds")},
                   ensure_ascii=False, indent=1),
        encoding="utf-8", newline="\n")
    log(f"done in {(time.time() - started) / 60:.1f} min")

    if args.log:
        with open(SRC / "sync.log", "a", encoding="utf-8") as fh:
            fh.write("\n".join(log_lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
