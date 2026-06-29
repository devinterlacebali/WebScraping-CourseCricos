"""
monitor_changes.py
------------------
Jalankan satu scraper, baca file .sql hasilnya, normalisasi jadi snapshot JSON
per cricos_course_code, lalu bandingkan dengan snapshot sebelumnya.
Kalau ada perubahan -> kirim notifikasi ke Google Chat (Incoming Webhook).
Snapshot terbaru ditimpa supaya jadi pembanding untuk run berikutnya.

Contoh:
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

# Pastikan emoji/karakter non-ASCII aman di console Windows.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Field yang ditarik dari tiap statement UPDATE di file .sql.
FIELDS = [
    "course_description",
    "total_course_duration",
    "offshore_tuition_fee",
    "entry_requirements",
    "apply_form",
]

# Field pendek -> ditampilkan nilai lama/baru di notifikasi.
# Field panjang (HTML) -> cukup ditandai "berubah" tanpa dump isinya.
SHORT_FIELDS = {"total_course_duration", "offshore_tuition_fee", "apply_form"}


def run_scraper(scraper_path):
    """Jalankan scraper python. Return True kalau sukses."""
    print(f"⚙️  Menjalankan scraper: {scraper_path}")
    try:
        result = subprocess.run(
            [sys.executable, scraper_path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
            env={**os.environ, "SCRAPER_HEADLESS": "True"},
        )
        print(result.stdout[-2000:])  # ekor log saja biar tidak banjir
        return True
    except subprocess.CalledProcessError as e:
        print(f"🔴 Scraper gagal: {e}")
        print((e.stderr or "")[-2000:])
        return False


def parse_sql(sql_path):
    """
    Ubah file .sql (kumpulan statement UPDATE) jadi dict:
        { cricos_code: { field: value, ... }, ... }
    Nilai SQL berupa string ber-quote tunggal dengan escape '' -> dikembalikan ke '.
    """
    if not os.path.exists(sql_path):
        print(f"⚠️  File SQL tidak ditemukan: {sql_path}")
        return {}

    with open(sql_path, "r", encoding="utf-8") as f:
        content = f.read()

    snapshot = {}
    # Pisahkan tiap statement berdasarkan penanda WHERE ... ';'
    blocks = re.split(r";\s*\n", content)
    for block in blocks:
        m_cricos = re.search(r"cricos_course_code\s*=\s*'([^']+)'", block)
        if not m_cricos:
            continue
        cricos = m_cricos.group(1)
        record = {}
        for field in FIELDS:
            m = re.search(rf"{field}\s*=\s*'((?:[^']|'')*)'", block)
            record[field] = m.group(1).replace("''", "'") if m else ""
        snapshot[cricos] = record
    return snapshot


def diff_snapshots(old, new):
    """Bandingkan dua snapshot. Return list perubahan (added/removed/modified)."""
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
    lines = [f"🔔 **Perubahan terdeteksi: {name}**", ""]
    for kind, cricos, fields in changes:
        if kind == "added":
            lines.append(f"➕ Course baru `{cricos}`")
        elif kind == "removed":
            lines.append(f"➖ Course hilang `{cricos}`")
        else:  # modified
            lines.append(f"✏️  `{cricos}` — field berubah:")
            for f in fields:
                if f in SHORT_FIELDS:
                    lines.append(f"   • {f}: `{old[cricos].get(f)}` → `{new[cricos].get(f)}`")
                else:
                    lines.append(f"   • {f} (konten panjang berubah)")
    return "\n".join(lines)


def send_discord(message):
    url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not url:
        print("⚠️  DISCORD_WEBHOOK_URL belum diset. Notifikasi dilewati.")
        print("---- pesan yang akan dikirim ----")
        print(message)
        return
    # Discord membatasi pesan maksimal 2000 karakter.
    if len(message) > 1900:
        message = message[:1900] + "\n… (dipotong)"
    try:
        res = requests.post(url, json={"content": message}, timeout=10)
        if res.ok:
            print("🚀 Notifikasi Discord terkirim.")
        else:
            print(f"❌ Gagal kirim Discord: {res.status_code} {res.text}")
    except Exception as e:
        print(f"❌ Error kirim notifikasi: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Nama institusi (untuk notifikasi)")
    parser.add_argument("--scraper", required=True, help="Path file scraper .py")
    parser.add_argument("--sql", required=True, help="Path file .sql hasil scraper")
    parser.add_argument("--snapshot", required=True, help="Path file snapshot.json")
    parser.add_argument("--skip-run", action="store_true", help="Lewati eksekusi scraper (debug)")
    args = parser.parse_args()

    if not args.skip_run:
        if not run_scraper(args.scraper):
            print("⛔ Berhenti: scraper gagal, snapshot tidak diubah.")
            sys.exit(1)

    new = parse_sql(args.sql)
    if not new:
        print("⛔ Berhenti: hasil scrape kosong, snapshot tidak diubah (hindari false alarm).")
        sys.exit(1)

    if os.path.exists(args.snapshot):
        with open(args.snapshot, "r", encoding="utf-8") as f:
            old = json.load(f)
    else:
        old = None

    if old is None:
        print(f"ℹ️  Belum ada snapshot. Membuat baseline pertama ({len(new)} course).")
    else:
        changes = diff_snapshots(old, new)
        if changes:
            print(f"📣 {len(changes)} perubahan terdeteksi.")
            send_discord(build_message(args.name, old, new, changes))
        else:
            print("✅ Tidak ada perubahan.")

    # Timpa snapshot dengan hasil terbaru -> jadi pembanding run berikutnya.
    with open(args.snapshot, "w", encoding="utf-8") as f:
        json.dump(new, f, ensure_ascii=False, indent=2, sort_keys=True)
    print(f"💾 Snapshot diperbarui: {args.snapshot}")


if __name__ == "__main__":
    main()
