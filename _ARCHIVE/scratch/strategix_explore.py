#!/usr/bin/env python3
"""Strategix Training Group Pty Ltd — www.strategix.com.au
Exploration: Cloudflare, footer CRICOS, sitemap, CSV coverage, course page SSR.

CRICOS: 03623M | RTO: 31418
CSV courses: 22
Note: Built on Webflow platform. Course pages at /course/xxx route
return 404 to curl_cffi — likely SPA/CSR routing. No sitemap.xml found.
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

BASE = "https://www.strategix.com.au"


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

        with open("scratch/strategix_homepage.html", "w", encoding="utf-8") as f:
            f.write(r.text)
    except Exception as e:
        print(f"  [ERROR] {e}")

    # ── 2. Footer CRICOS ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("2. FOOTER CRICOS PROVIDER CODE")
    print("=" * 60)
    try:
        with open("scratch/strategix_homepage.html", encoding="utf-8") as f:
            html = f.read()
        for m in re.finditer(r".{0,40}(CRICOS|RTO|03623).{0,40}", html, re.IGNORECASE):
            print(f"  {m.group().strip()}")
        footer_m = re.search(r"<footer[^>]*>(.*?)</footer>", html, re.DOTALL | re.IGNORECASE)
        if footer_m:
            ft = re.sub(r"<[^>]+>", " ", footer_m.group(1))
            ft = re.sub(r"\s+", " ", ft).strip()
            print(f"\n  Footer: {ft[:1000]}")
    except FileNotFoundError:
        print("  Homepage not saved")

    # ── 3. Sitemap ─────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("3. SITEMAP SEARCH")
    print("=" * 60)
    for path in ["/sitemap.xml", "/sitemap_index.xml", "/wp-sitemap.xml",
                 "/sitemap-index.xml", "/robots.txt"]:
        try:
            r = curl_requests.get(urljoin(BASE, path), impersonate="chrome", timeout=15)
            print(f"{path} → {r.status_code} ({len(r.text)} bytes)")
            if r.status_code == 200 and len(r.text) > 50:
                urls = re.findall(r"<loc>(.*?)</loc>", r.text, re.IGNORECASE)
                print(f"  URLs in sitemap: {len(urls)}")
                for u in urls[:5]:
                    print(f"    - {u}")
                print(f"  Content preview: {r.text[:300]}")
        except Exception as e:
            print(f"  {path} → ERROR: {e}")

    # ── 4. CSV coverage ────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("4. CSV COVERAGE (provider 03623M)")
    print("=" * 60)
    csv_path = Path(__file__).resolve().parent.parent / "cricos-courses.csv"
    if csv_path.exists():
        import csv
        count = 0
        courses = []
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for row in reader:
                if row and row[0].strip() == "03623M":
                    count += 1
                    courses.append(row[3] if len(row) > 3 else "?")
        print(f"CRICOS courses in CSV: {count}")
        for c in courses:
            print(f"  - {c}")

    # ── 5. Course page SSR ─────────────────────────────────────────
    print("\n" + "=" * 60)
    print("5. COURSE PAGE SSR")
    print("=" * 60)
    print("NOTE: Strategix is Webflow-based (cdn.prod.website-files.com).")
    print("Course routes (/course/xxx) return 404 to curl_cffi —")
    print("likely client-side routing or Webflow JS rendering needed.")
    print()
    # Try homepage for course links
    try:
        with open("scratch/strategix_homepage.html", encoding="utf-8") as f:
            html = f.read()
        links = re.findall(r'href=[\"\']([^\"\']+)[\"\']', html)
        course_links = set(l for l in links if '/course/' in l.lower() or 'courses' in l.lower() and not l.startswith('#') and 'http' not in l)
        print(f"Course links found on homepage: {len(course_links)}")
        for cl in sorted(course_links)[:15]:
            print(f"  - {cl}")
    except FileNotFoundError:
        print("  Homepage not available")
    # Sample course page fetch
    for slug in ["/courses", "/course/certificate-iii-in-business"]:
        try:
            r = curl_requests.get(urljoin(BASE, slug), impersonate="chrome", timeout=15)
            print(f"{slug} → {r.status_code} ({len(r.text)} bytes)")
            if len(r.text) > 500:
                print("  SSR: YES (via JS/SPA? — content present)")
            else:
                print("  SSR: No (empty/little content)")
        except Exception as e:
            print(f"  {slug} → ERROR: {e}")

    # ── Summary ────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Cloudflare: NO indicators on homepage, BUT CF headers present")
    print("CRICOS: 03623M in footer (RTO 31418)")
    print("Sitemap: NONE found — all paths return 404")
    print("CSV: 22 courses")
    print("SSR: Likely NO — Webflow SPA. /course/xxx routes 404 via curl_cffi")
    print("     Need Playwright/browser to render course pages")


if __name__ == "__main__":
    asyncio.run(main())
