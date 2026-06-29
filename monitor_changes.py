"""
monitor_changes.py
------------------
Run a scraper, read its .sql output, normalize it into a JSON snapshot keyed by
cricos_course_code, then compare against the previous snapshot.
If something changed -> send a Discord notification (Incoming Webhook) and attach
an SQL file containing only the changed courses. The latest snapshot overwrites
the old one so it becomes the baseline for the next run.

Example:
    python monitor_changes.py \
        --name "Crown Institute of Higher Education" \
        --scraper "Crown Institute of Higher Education/cihe.py" \
        --sql "Crown Institute of Higher Education/cihe_courses_update.sql" \
        --snapshot "Crown Institute of Higher Education/snapshot.json"
"""

import os
import re
import sys
import json
import argparse
import subprocess

import requests

# Reuse the existing helpers from run_all.py so the rules stay consistent.
try:
    from run_all import analyze_logs, determine_cwd_and_args
except Exception:
    analyze_logs = None
    determine_cwd_and_args = None

# Make sure emojis / non-ASCII characters are safe in the Windows console.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# If more than this fraction of courses lose their description, treat the run as a
# broken scrape (page layout likely changed) rather than a real content change.
BROKEN_EMPTY_RATIO = 0.5

# Fields pulled from each UPDATE statement in the .sql file.
FIELDS = [
    "course_description",
    "total_course_duration",
    "offshore_tuition_fee",
    "entry_requirements",
    "apply_form",
]

# Short fields -> show old/new value in the notification.
# Long fields (HTML) -> just flag as "changed" without dumping the content.
SHORT_FIELDS = {"total_course_duration", "offshore_tuition_fee", "apply_form"}


def run_scraper(scraper_path):
    """Run the python scraper. Return (exit_code, log_lines)."""
    print(f"⚙️  Running scraper: {scraper_path}")
    root = os.path.abspath(os.path.dirname(__file__))
    # Run from the same working directory run_all.py would use, so each scraper
    # writes its .sql to the expected location regardless of how it builds paths.
    if determine_cwd_and_args is not None:
        cwd, target = determine_cwd_and_args(os.path.abspath(scraper_path), root)
    else:
        cwd, target = None, scraper_path
    result = subprocess.run(
        [sys.executable, target],
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "SCRAPER_HEADLESS": "True", "PYTHONPATH": root},
    )
    logs = (result.stdout or "").splitlines() + (result.stderr or "").splitlines()
    print("\n".join(logs[-40:]))  # tail of the log only, to avoid flooding
    return result.returncode, logs


def classify_health(logs, exit_code):
    """Wrap run_all.analyze_logs; fall back to a simple exit-code check if unavailable."""
    if analyze_logs is not None:
        return analyze_logs(logs, exit_code)
    if exit_code != 0:
        return "🔴 BROKEN (RUSAK)", [f"Exit code {exit_code}"]
    return "🟢 HEALTHY (SEHAT)", []


def _filled_count(snapshot):
    """How many courses have a non-empty course_description."""
    return sum(1 for rec in snapshot.values() if rec.get("course_description", "").strip())


def looks_broken(old, new):
    """
    Catch silent breakage: the scraper exits cleanly but returns empty data
    (e.g. the page layout changed). Return (is_broken, reason).

    To avoid false positives on scrapers that are legitimately sparse, we only
    flag a *regression*: it had content before and most of it vanished now.
    On the very first baseline (no old snapshot) we accept whatever we got.
    """
    if not new:
        return True, "No courses were parsed from the SQL output."
    if not old:
        return False, ""  # first baseline -> nothing to compare against

    old_filled = _filled_count(old)
    new_filled = _filled_count(new)
    if old_filled >= 3 and new_filled < old_filled * (1 - BROKEN_EMPTY_RATIO):
        return True, (
            f"course_description dropped from {old_filled} to {new_filled} courses — "
            f"the page layout likely changed."
        )
    return False, ""


def parse_sql(sql_path):
    """
    Turn the .sql file (a series of UPDATE statements) into:
        snapshot: { cricos_code: { field: value, ... }, ... }
        raw:      { cricos_code: original SQL statement text }
    SQL values are single-quoted strings with '' escaping -> converted back to '.
    """
    if not os.path.exists(sql_path):
        print(f"⚠️  SQL file not found: {sql_path}")
        return {}, {}

    with open(sql_path, "r", encoding="utf-8") as f:
        content = f.read()

    snapshot = {}
    raw = {}  # cricos -> original SQL statement text (for the changes file)
    # Split each statement on the WHERE ... ';' boundary.
    blocks = re.split(r";\s*\n", content)
    for block in blocks:
        m_cricos = re.search(r"cricos(?:_course)?_code\s*=\s*'([^']+)'", block)
        if not m_cricos:
            continue
        cricos = m_cricos.group(1)
        record = {}
        for field in FIELDS:
            m = re.search(rf"{field}\s*=\s*'((?:[^']|'')*)'", block)
            record[field] = m.group(1).replace("''", "'") if m else ""
        snapshot[cricos] = record
        raw[cricos] = block.strip() + ";"
    return snapshot, raw


def write_changes_sql(sql_path, changes, raw):
    """
    Write a .sql file containing ONLY the UPDATE statements for changed/new courses,
    ready to run directly against the database. Return the file path, or None if empty.
    """
    from datetime import datetime, timezone

    statements = [
        raw[cricos]
        for kind, cricos, _ in changes
        if kind in ("added", "modified") and cricos in raw
    ]
    if not statements:
        return None  # only removed courses -> nothing to UPDATE

    base, ext = os.path.splitext(sql_path)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    out_path = f"{base}_changes_{stamp}{ext}"

    header = (
        f"-- Changes detected {datetime.now(timezone.utc).isoformat()} UTC\n"
        f"-- {len(statements)} course(s) changed. Run directly against the database.\n\n"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + "\n\n".join(statements) + "\n")
    print(f"📄 Changes SQL written: {out_path} ({len(statements)} course(s))")
    return out_path


def diff_snapshots(old, new):
    """Compare two snapshots. Return a list of changes (added/removed/modified)."""
    changes = []

    for cricos in new:
        if cricos not in old:
            changes.append(("added", cricos, None))
        else:
            changed_fields = [f for f in FIELDS if old[cricos].get(f) != new[cricos].get(f)]
            if changed_fields:
                changes.append(("modified", cricos, changed_fields))

    for cricos in old:
        if cricos not in new:
            changes.append(("removed", cricos, None))

    return changes


def build_message(name, old, new, changes):
    lines = [f"🔔 **Changes detected: {name}**", ""]
    for kind, cricos, fields in changes:
        if kind == "added":
            lines.append(f"➕ New course `{cricos}`")
        elif kind == "removed":
            lines.append(f"➖ Course removed `{cricos}`")
        else:  # modified
            lines.append(f"✏️  `{cricos}` — fields changed:")
            for f in fields:
                if f in SHORT_FIELDS:
                    lines.append(f"   • {f}: `{old[cricos].get(f)}` → `{new[cricos].get(f)}`")
                else:
                    lines.append(f"   • {f} (long content changed)")
    return "\n".join(lines)


def send_discord(message, file_path=None):
    url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not url:
        print("⚠️  DISCORD_WEBHOOK_URL is not set. Notification skipped.")
        print("---- message that would be sent ----")
        print(message)
        if file_path:
            print(f"(file that would be attached: {file_path})")
        return
    # Discord caps messages at 2000 characters.
    if len(message) > 1900:
        message = message[:1900] + "\n… (truncated)"
    try:
        if file_path and os.path.exists(file_path):
            # Send message + file attachment via multipart.
            with open(file_path, "rb") as f:
                res = requests.post(
                    url,
                    data={"payload_json": json.dumps({"content": message})},
                    files={"file": (os.path.basename(file_path), f)},
                    timeout=30,
                )
        else:
            res = requests.post(url, json={"content": message}, timeout=10)
        if res.ok:
            print("🚀 Discord notification sent" + (" (with SQL attachment)." if file_path else "."))
        else:
            print(f"❌ Failed to send Discord: {res.status_code} {res.text}")
    except Exception as e:
        print(f"❌ Error sending notification: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Institution name (for the notification)")
    parser.add_argument("--scraper", required=True, help="Path to the scraper .py file")
    parser.add_argument("--sql", required=True, help="Path to the scraper's .sql output")
    parser.add_argument("--snapshot", required=True, help="Path to the snapshot.json file")
    parser.add_argument("--skip-run", action="store_true", help="Skip running the scraper (debug)")
    args = parser.parse_args()

    if not args.skip_run:
        exit_code, logs = run_scraper(args.scraper)
        status, reasons = classify_health(logs, exit_code)
        print(f"Health check: {status}")
        if "BROKEN" in status:
            # Hard failure (crash, error in logs). Alert, and DO NOT touch the snapshot.
            msg = (
                f"🔴 **Scraper BROKEN: {args.name}**\n"
                f"The scraper failed — snapshot left unchanged. Please check it.\n"
                + "\n".join(f"• `{r}`" for r in reasons)
            )
            send_discord(msg)
            print("⛔ Stopping: scraper broken, snapshot left unchanged.")
            sys.exit(1)

    new, raw = parse_sql(args.sql)

    if os.path.exists(args.snapshot):
        with open(args.snapshot, "r", encoding="utf-8") as f:
            old = json.load(f)
    else:
        old = None

    # Content-level guard: catches silent breakage that produced no error log.
    broken, reason = looks_broken(old, new)
    if broken:
        msg = (
            f"🔴 **Scraper likely BROKEN: {args.name}**\n"
            f"Result looks invalid — snapshot left unchanged (no false alarm).\n"
            f"• {reason}"
        )
        send_discord(msg)
        print(f"⛔ Stopping: {reason} Snapshot left unchanged.")
        sys.exit(1)

    if old is None:
        print(f"ℹ️  No snapshot yet. Creating the first baseline ({len(new)} courses).")
    else:
        changes = diff_snapshots(old, new)
        if changes:
            print(f"📣 {len(changes)} change(s) detected.")
            # Write an SQL file with only the changed/new courses, then attach it to Discord.
            changes_sql = write_changes_sql(args.sql, changes, raw)
            send_discord(build_message(args.name, old, new, changes), file_path=changes_sql)
        else:
            print("✅ No changes.")

    # Overwrite the snapshot with the latest result -> baseline for the next run.
    with open(args.snapshot, "w", encoding="utf-8") as f:
        json.dump(new, f, ensure_ascii=False, indent=2, sort_keys=True)
    print(f"💾 Snapshot updated: {args.snapshot}")


if __name__ == "__main__":
    main()
