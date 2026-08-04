"""
UNSW Sydney — Exploration Script
URL: https://www.unsw.edu.au/ (provider 00098G, 665 CSV courses)

Checks: Cloudflare, sitemap, footer CRICOS, course page SSR, course URLs

Usage:
  cd /c/Users/Dewa(Interlace)/Documents/Interlace Code/WebScraping-CourseCricos
  venv/Scripts/python scratch/unsw_explore.py
"""

import json
import re
import sys
import time

try:
    from curl_cffi import requests
except ImportError:
    print("ERROR: curl_cffi not installed. Run: pip install curl_cffi")
    sys.exit(1)

BASE = "https://www.unsw.edu.au"
OUT_DIR = "scratch"


def check(label, ok, detail=""):
    status = "✅" if ok else "❌"
    print(f"  {status} {label}" + (f" — {detail}" if detail else ""))


def probe_cloudflare():
    print("\n[1] Cloudflare / CDN check")
    try:
        r = requests.get(BASE, impersonate="chrome124", timeout=30)
        server = r.headers.get("Server", "")
        cf_ray = r.headers.get("CF-RAY", "")
        x_cache = r.headers.get("X-Cache", "")
        via = r.headers.get("Via", "")

        is_cf = "cloudflare" in server.lower() or "cloudflare" in via.lower()
        is_cf_fe = "cloudfront" in via.lower() or "CloudFront" in r.headers.get("X-Amz-Cf-Pop", "")

        detail_parts = [f"Server: {server}"]
        if x_cache:
            detail_parts.append(f"X-Cache: {x_cache}")
        if via:
            detail_parts.append(f"Via: {via[:60]}")
        if is_cf_fe:
            detail_parts.append("CloudFront CDN detected")

        check("Cloudflare detected", is_cf, " | ".join(detail_parts))
        check("Has CloudFront/AWS CDN", is_cf_fe, "Uses CloudFront as CDN")
        check("curl_cffi OK", r.status_code == 200, f"HTTP {r.status_code}")
        return r
    except Exception as e:
        check("Cloudflare probe failed", False, str(e))
        return None


def check_sitemap():
    print("\n[2] Sitemap check")
    try:
        r = requests.get(f"{BASE}/sitemap.xml", impersonate="chrome124", timeout=60)
        check("Sitemap reachable", r.status_code == 200, f"HTTP {r.status_code}, {len(r.text):,} chars")

        if "urlset" in r.text:
            # Single large sitemap
            all_urls = re.findall(r'<loc>([^<]+)</loc>', r.text)
            check("URLs in sitemap", len(all_urls) > 0, f"{len(all_urls):,} total URLs")

            # Categorize URLs
            study_urls = [u for u in all_urls if "/study/" in u]
            course_urls = [u for u in all_urls if any(p in u for p in ["/course", "/degree", "/program"])]
            check("Study-related URLs", len(study_urls) > 0, f"{len(study_urls):,} study URLs")
            check("Course/degree/program URLs", len(course_urls) > 0, f"{len(course_urls):,} matched")

            # Look at degree page patterns
            ug_urls = [u for u in all_urls if "/undergraduate/" in u]
            pg_urls = [u for u in all_urls if "/postgraduate/" in u]
            check("Undergraduate degree pages", len(ug_urls) > 0, f"{len(ug_urls):,} pages")
            check("Postgraduate degree pages", len(pg_urls) > 0, f"{len(pg_urls):,} pages")

            if ug_urls:
                print(f"    Sample undergraduate: {ug_urls[0]}")
            if pg_urls:
                print(f"    Sample postgraduate: {pg_urls[0]}")
        else:
            check("Sitemap format", False, r.text[:200])
    except Exception as e:
        check("Sitemap check failed", False, str(e))


def check_footer_cricos():
    print("\n[3] Footer CRICOS check")
    try:
        r = requests.get(BASE, impersonate="chrome124", timeout=30)
        found = "00098G" in r.text

        # Extract the CRICOS line
        matches = re.findall(r'CRICOS[^<]*Provider[^<]*Code[^<]*:?\s*00098G', r.text)
        if not matches:
            matches = re.findall(r'00098G', r.text)

        detail = matches[0] if matches else ""
        check("CRICOS 00098G in footer", found, detail[:120])
    except Exception as e:
        check("Footer check failed", False, str(e))


def check_course_page_ssr():
    print("\n[4] Course page SSR check")
    # Use real course page
    sample_url = f"{BASE}/study/undergraduate/bachelor-of-commerce"
    try:
        r = requests.get(sample_url, impersonate="chrome124", timeout=30,
                         params={"studentType": "International"})
        is_ssr = "Bachelor of Commerce" in r.text
        has_cricos = "CRICOS Code" in r.text or "CRICOS code" in r.text
        has_program_code = "Program code" in r.text.lower() or "Program Code" in r.text
        has_fees = "$" in r.text and ("fee" in r.text.lower() or "Fee" in r.text)
        has_duration = "Year" in r.text or "year" in r.text

        check("Course page SSR (has title)", is_ssr, f"HTTP {r.status_code}")
        check("CRICOS code on page", has_cricos)
        check("Program code present", has_program_code)
        check("Fee information present", has_fees)
        check("Duration present", has_duration)

        # Extract CRICOS code
        cricos_match = re.search(r'CRICOS\s*Code[:\s]*([A-Z0-9]+)', r.text, re.IGNORECASE)
        if cricos_match:
            print(f"    CRICOS Code found: {cricos_match.group(1)}")

        program_match = re.search(r'Program\s*[Cc]ode[:\s]*(\d+)', r.text)
        if program_match:
            print(f"    Program Code found: {program_match.group(1)}")
    except Exception as e:
        check("Course page check failed", False, str(e))


def explore_course_finder():
    print("\n[5] Course finder / API exploration")
    try:
        # Try degree search API
        search_url = f"{BASE}/study/find-a-degree-or-course/degree-search-results"
        r = requests.get(search_url, impersonate="chrome124", timeout=30,
                         params={"study-area": "Business & Commerce"})

        check("Degree search result page reachable", r.status_code == 200, f"HTTP {r.status_code}")

        # Search results are likely rendered client-side (JS)
        # Check for the total count mention in the page source
        if "View all degrees" in r.text or "Results" in r.text:
            total_match = re.search(r'View all degrees\s*\((\d+)\)', r.text)
            if total_match:
                check("Total degrees stated on page", True, f"{total_match.group(1)} degrees")
            else:
                check("Degree search page has result markers", True)
        else:
            check("Degree search results", False, "Likely client-side rendered (JS needed)")

        # Check for hidden JSON data or API config
        json_data = re.findall(r'data-props=\"{[^}]+}\"', r.text) or re.findall(r'window\.__INITIAL_STATE__\s*=', r.text)
        check("Embedded data/props found", len(json_data) > 0, f"{len(json_data)} matches" if json_data else "No embedded state found")

        # Try to find REST endpoint patterns
        api_refs = re.findall(r'(https?://[^"\'\\]*api[^"\'\\]*)', r.text)
        check("API endpoint references in page", len(api_refs) > 0, f"{len(api_refs)} references" if api_refs else "No direct API references")
    except Exception as e:
        check("Course finder check failed", False, str(e))


def enumerate_course_urls():
    print("\n[6] Course URL enumeration (from sitemap)")
    try:
        r = requests.get(f"{BASE}/sitemap.xml", impersonate="chrome124", timeout=60)
        all_urls = re.findall(r'<loc>([^<]+)</loc>', r.text)

        # Filter to actual degree/course pages (not archive, not config, not news)
        course_patterns = [
            "/study/undergraduate/", "/study/postgraduate/",
            "/study/professional-development/", "/study/your-future/"
        ]
        course_urls = []
        for u in all_urls:
            if any(p in u for p in course_patterns):
                # Exclude archive and non-degree pages
                if "/webarchive/" not in u and "/config" not in u:
                    course_urls.append(u)

        check("URLs from sitemap", len(course_urls) > 0,
              f"{len(course_urls):,} course/degree URLs (of {len(all_urls):,} total)")
        if course_urls:
            print(f"    Sample: {course_urls[0]}")
            print(f"    Sample: {course_urls[min(1, len(course_urls)-1)]}")

        # Alternatively, API-based discovery
        print("\n  Alternative: use degree search API if available")
        # Check if total count from search page
        total_match = re.search(r'View all degrees\s*\((\d+)\)', r.text[:50000] if len(r.text) > 50000 else r.text)
        if total_match:
            print(f"    Total degrees stated: {total_match.group(1)}")
    except Exception as e:
        check("URL enumeration failed", False, str(e))


def summary():
    print("\n" + "="*60)
    print("UNSW — EXPLORATION SUMMARY")
    print("="*60)
    findings = {
        "Provider": "00098G",
        "CSV Courses": 665,
        "Base URL": BASE,
        "Cloudflare": "NO — Apache → CloudFront CDN (AWS)",
        "Impersonation needed": "No (standard HTTP works)",
        "Sitemap": "Single massive sitemap.xml (7.8MB) — contains all URLs",
        "Footer CRICOS": "Present — 'UNSW CRICOS Provider Code: 00098G'",
        "Course page SSR": "Full SSR — title, CRICOS code, program code, fees, duration in HTML",
        "Course URL pattern": "https://www.unsw.edu.au/study/{level}/{course-slug}",
        "Degree finder": "/study/find-a-degree-or-course with filters, ~482 degrees",
        "Approach": "Parse sitemap for /study/undergraduate/ and /study/postgraduate/ URLs → scrape SSR. Or use degree search page to collect program codes."
    }
    for k, v in findings.items():
        print(f"  {k:30s}: {v}")


if __name__ == "__main__":
    print("="*60)
    print("UNSW — EXPLORATION")
    print("="*60)

    probe_cloudflare()
    check_sitemap()
    check_footer_cricos()
    check_course_page_ssr()
    explore_course_finder()
    enumerate_course_urls()
    summary()
