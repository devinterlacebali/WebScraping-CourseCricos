#!/usr/bin/env python3
"""Stanley International College Pty Ltd — www.stanleycollege.edu.au
Exploration: Cloudflare, footer CRICOS, sitemap, CSV coverage, course page SSR.

CRICOS: 03047E | RTO: 51973 | TEQSA: PRV14050
CSV courses: 27
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

BASE = "https://www.stanleycollege.edu.au"


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

        with open("scratch/stanley_homepage.html", "w", encoding="utf-8") as f:
            f.write(r.text)
    except Exception as e:
        print(f"  [ERROR] {e}")

    # ── 2. Footer CRICOS ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("2. FOOTER CRICOS PROVIDER CODE")
    print("=" * 60)
    try:
        with open("scratch/stanley_homepage.html", encoding="utf-8") as f:
            html = f.read()
        footer_m = re.search(r"<footer[^>]*>(.*?)</footer>", html, re.DOTALL | re.IGNORECASE)
        if footer_m:
            ft = re.sub(r"<[^>]+>", " ", footer_m.group(1))
            ft = re.sub(r"\s+", " ", ft).strip()
            print(f"  Footer: {ft[:1000]}")
        else:
            print("  No <footer> tag found — scanning broadly:")
            for m in re.finditer(r".{0,60}(CRICOS|PRV|TEQSA|RTO).{0,60}", html, re.IGNORECASE):
                print(f"    {m.group().strip()}")
    except FileNotFoundError:
        print("  Homepage not saved")

    # ── 3. Sitemap ─────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("3. SITEMAP — /sitemap.xml")
    print("=" * 60)
    try:
        r = curl_requests.get(urljoin(BASE, "/sitemap.xml"), impersonate="chrome", timeout=30)
        print(f"Status: {r.status_code}, Size: {len(r.text)} bytes")
        if r.status_code == 200:
            urls = re.findall(r"<loc>(.*?)</loc>", r.text, re.IGNORECASE)
            print(f"Total URLs: {len(urls)}")
            course_urls = [
                u for u in urls
                if any(kw in u.lower() for kw in ["course", "program", "degree", "diploma", "certificate", "bachelor", "master"])
            ]
            print(f"Course-like URLs: {len(course_urls)}")
            for u in course_urls[:10]:
                print(f"  - {u}")
            with open("scratch/stanley_sitemap.xml", "w", encoding="utf-8") as f:
                f.write(r.text)
        else:
            print("  Not found")
    except Exception as e:
        print(f"  [ERROR] {e}")

    # ── 4. CSV coverage ────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("4. CSV COVERAGE (provider 03047E)")
    print("=" * 60)
    csv_path = Path(__file__).resolve().parent.parent / "cricos-courses.csv"
    if csv_path.exists():
        import csv
        count = 0
        courses = []
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for row in reader:
                if row and row[0].strip() == "03047E":
                    count += 1
                    courses.append(row[3] if len(row) > 3 else "?")
        print(f"CRICOS courses in CSV: {count}")
        for c in courses:
            print(f"  - {c}")
    else:
        print(f"  CSV not found at {csv_path}")

    # ── 5. Course page SSR ─────────────────────────────────────────
    print("\n" + "=" * 60)
    print("5. COURSE PAGE SSR")
    print("=" * 60)
    sample_course = "/courses/diploma-of-nursing/"
    try:
        r = curl_requests.get(urljoin(BASE, sample_course), impersonate="chrome", timeout=30)
        print(f"{sample_course} → {r.status_code} ({len(r.text)} bytes)")
        if r.status_code == 200 and len(r.text) > 500:
            print("  SSR: YES (server-rendered content > 500B)")
            html = r.text.lower()
            for kw in ["overview", "description", "duration", "fee", "entry requirement", "cricos"]:
                if kw in html:
                    print(f"  Content section: {kw.title()} ✓")
                    break
            cricos = re.search(r"cricos[^<]*?(\d{5}[0-9A-Z])", r.text, re.IGNORECASE)
            if cricos:
                print(f"  CRICOS on page: {cricos.group(1)}")
        else:
            print("  SSR: No (small or empty response)")
    except Exception as e:
        print(f"  [ERROR] {e}")

    # ── Summary ────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Cloudflare: indicator in body ('cloudflare' text mention) but NO CF headers, NO challenge")
    print("CRICOS: 03047E (footer)")
    print("Sitemap: /sitemap.xml — 146 total URLs, ~64 course-like (28 course pages)")
    print("CSV: 27 courses")
    print("SSR: YES — course page returns ~146KB with CRICOS + overview content")


if __name__ == "__main__":
    asyncio.run(main())
