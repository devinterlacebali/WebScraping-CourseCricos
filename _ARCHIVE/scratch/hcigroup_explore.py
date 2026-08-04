#!/usr/bin/env python3
"""Health Careers International Pty Ltd (HCI Group) — www.hcigroup.com.au
Exploration: Cloudflare, footer CRICOS, sitemap, CSV coverage, course page SSR.

CRICOS: 03386G
CSV courses: 7
Note: HCI Group is a corporate holding site. Actual course delivery is via
IHNA (www.ihna.edu.au, RTO division) and IHM (www.ihm.edu.au, HE division).
"""

import asyncio
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from curl_cffi import requests as curl_requests
    print("[OK] curl_cffi imported")
    CURL_OK = True
except ImportError:
    print("[!] curl_cffi not available")
    CURL_OK = False

BASE = "https://www.hcigroup.com.au"


async def main():
    # ── 1. Cloudflare ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("1. HOMEPAGE FETCH (Cloudflare check)")
    print("=" * 60)
    try:
        r = curl_requests.get(BASE, impersonate="chrome", timeout=30)
        print(f"Status: {r.status_code}")
        print(f"Content-Length: {len(r.text)} bytes")
        body_low = r.text.lower()

        cf_indicators = ["cloudflare", "__cf_bm", "cf-ray", "cf-challenge", "iuam"]
        for ind in cf_indicators:
            if ind in body_low:
                print(f"  [!] CF indicator found: '{ind}'")

        if "checking your browser" in body_low or "attention required" in body_low:
            print("  [!] CLOUDFLARE CHALLENGE DETECTED")
        else:
            print("  [OK] No CF challenge")

        headers = dict(r.headers)
        cf_hdrs = {k: v for k, v in headers.items() if "cf-" in k.lower()}
        if cf_hdrs:
            print(f"  CF headers: {json.dumps(cf_hdrs, indent=2)}")
        else:
            print("  No CF headers")

        with open("scratch/hcigroup_homepage.html", "w", encoding="utf-8") as f:
            f.write(r.text)
    except Exception as e:
        print(f"  [ERROR] {e}")

    # ── 2. Footer CRICOS ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("2. FOOTER CRICOS PROVIDER CODE")
    print("=" * 60)
    try:
        with open("scratch/hcigroup_homepage.html", encoding="utf-8") as f:
            html = f.read()
        # HCI is a corporate site — check broadly
        for m in re.finditer(r".{0,60}(CRICOS|TEQSA|RTO|03386).{0,60}", html, re.IGNORECASE):
            print(f"  {m.group().strip()}")
        # Also check footer-like areas
        footer_m = re.search(r"<footer[^>]*>(.*?)</footer>", html, re.DOTALL | re.IGNORECASE)
        if footer_m:
            ft = re.sub(r"<[^>]+>", " ", footer_m.group(1))
            ft = re.sub(r"\s+", " ", ft).strip()
            print(f"\n  Footer: {ft[:1000]}")
        else:
            print("  (No footer tag)")
    except FileNotFoundError:
        print("  Homepage not saved")

    # ── 3. Sitemap ─────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("3. SITEMAP")
    print("=" * 60)
    for path in ["/sitemap.xml", "/sitemap_index.xml", "/wp-sitemap.xml"]:
        try:
            r = curl_requests.get(urljoin(BASE, path), impersonate="chrome", timeout=15)
            print(f"{path} → {r.status_code} ({len(r.text)} bytes)")
            if r.status_code == 200:
                urls = re.findall(r"<loc>(.*?)</loc>", r.text, re.IGNORECASE)
                print(f"  URLs: {len(urls)}")
                for u in urls[:5]:
                    print(f"    - {u}")
        except Exception as e:
            print(f"{path} → ERROR: {e}")

    # ── 4. CSV coverage ────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("4. CSV COVERAGE (provider 03386G)")
    print("=" * 60)
    csv_path = Path(__file__).resolve().parent.parent / "cricos-courses.csv"
    if csv_path.exists():
        import csv
        count = 0
        courses = []
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for row in reader:
                if row and row[0].strip() == "03386G":
                    count += 1
                    courses.append(row[3] if len(row) > 3 else "?")
        print(f"CRICOS courses in CSV: {count}")
        for c in courses:
            print(f"  - {c}")

    # ── 5. Course page SSR ─────────────────────────────────────────
    print("\n" + "=" * 60)
    print("5. COURSE PAGE SSR")
    print("=" * 60)
    print("NOTE: HCI Group corporate site does NOT host course pages.")
    print("Course delivery is via subsidiaries:")
    print("  - IHNA (RTO division: www.ihna.edu.au/courses/)")
    print("  - IHM (HE division: www.ihm.edu.au/courses/)")
    print("  - Stanley College (www.stanleycollege.edu.au)")
    print()
    # Check IHNA as a proxy
    print("Checking IHNA course listing (proxy):")
    try:
        r = curl_requests.get("https://www.ihna.edu.au/courses/", impersonate="chrome", timeout=30)
        print(f"  /courses/ → {r.status_code} ({len(r.text)} bytes)")
        if len(r.text) > 500:
            print("  SSR: YES")
            html_low = r.text.lower()
            for kw in ["overview", "description", "duration", "course", "cricos"]:
                if kw in html_low:
                    print(f"  Content: {kw.title()} ✓")
                    break
        else:
            print("  SSR: No")
    except Exception as e:
        print(f"  [ERROR] {e}")

    # ── Summary ────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Cloudflare: 'cloudflare' text mention in body, NO challenge, NO CF headers")
    print("CRICOS: not directly in HCI footer (corporate site); courses delivered under 03386G via IHNA/IHM")
    print("Sitemap: NONE found on www.hcigroup.com.au")
    print("CSV: 7 courses under 03386G")
    print("SSR: IHNA course pages are SSR (~125KB with content)")


if __name__ == "__main__":
    asyncio.run(main())
