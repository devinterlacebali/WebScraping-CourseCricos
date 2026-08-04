"""
ANU — Exploration Script
URL: https://www.anu.edu.au/ (provider 00120C, 420 CSV courses)

Key domains:
  - www.anu.edu.au — main site (Drupal)
  - study.anu.edu.au — study microsite (Drupal)
  - programsandcourses.anu.edu.au — program/course catalogue (.NET app)

Checks: Cloudflare, sitemap, footer CRICOS, course page SSR, course URLs

Usage:
  cd /c/Users/Dewa(Interlace)/Documents/Interlace Code/WebScraping-CourseCricos
  venv/Scripts/python scratch/anu_explore.py
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

BASE = "https://www.anu.edu.au"
STUDY_BASE = "https://study.anu.edu.au"
PC_BASE = "https://programsandcourses.anu.edu.au"


def check(label, ok, detail=""):
    status = "✅" if ok else "❌"
    print(f"  {status} {label}" + (f" — {detail}" if detail else ""))


def probe_cloudflare():
    print("\n[1] Cloudflare / CDN check")
    try:
        r = requests.get(BASE, impersonate="chrome124", timeout=30,
                         allow_redirects=True)
        server = r.headers.get("Server", "")
        cf_ray = r.headers.get("CF-RAY", "")
        cf_bm = "__cf_bm" in str(r.headers.get("set-cookie", ""))

        detail_parts = [f"Server: {server}"]
        if cf_ray:
            detail_parts.append(f"CF-RAY: {cf_ray}")

        is_cf = "cloudflare" in server.lower() or cf_ray or cf_bm
        check("Cloudflare detected", is_cf, " | ".join(detail_parts))

        # Also check programsandcourses subdomain
        r2 = requests.get(PC_BASE, impersonate="chrome124", timeout=30)
        server2 = r2.headers.get("Server", "")
        check(f"    {PC_BASE} Server", True, f"{server2} (HTTP {r2.status_code})")

        # Check study subdomain
        r3 = requests.get(STUDY_BASE, impersonate="chrome124", timeout=30,
                          allow_redirects=True)
        server3 = r3.headers.get("Server", "")
        check(f"    {STUDY_BASE} Server", True, f"{server3} (HTTP {r3.status_code})")

        return r
    except Exception as e:
        check("Cloudflare probe failed", False, str(e))
        return None


def check_sitemap():
    print("\n[2] Sitemap check")
    try:
        r = requests.get(f"{BASE}/sitemap.xml", impersonate="chrome124", timeout=30)
        check("Sitemap index reachable", r.status_code == 200, f"HTTP {r.status_code}")

        if "sitemapindex" in r.text:
            pages = re.findall(r'<sitemap><loc>([^<]+)</loc>', r.text)
            check("Sitemap sub-pages found", len(pages) > 0, f"{len(pages)} sub-sitemaps (pages 1-27+)")

            # Check a few pages for content types
            for pg in [1, 2, 4]:
                try:
                    rp = requests.get(f"{BASE}/sitemap.xml?page={pg}",
                                      impersonate="chrome124", timeout=30)
                    urls = re.findall(r'https://[^<]+', rp.text)
                    study_urls = [u for u in urls if "/study/" in u]
                    if study_urls:
                        check(f"  Sitemap page {pg} study URLs", True, f"{len(study_urls)} URLs")
                        print(f"    Sample: {study_urls[0]}")
                except Exception:
                    pass
        else:
            check("Sitemap format", False, r.text[:200])
    except Exception as e:
        check("Sitemap check failed", False, str(e))


def check_footer_cricos():
    print("\n[3] Footer CRICOS check")
    # Check main ANU site
    try:
        r = requests.get(BASE, impersonate="chrome124", timeout=30,
                         allow_redirects=True)
        found = "00120C" in r.text
        # Look for CRICOS Provider Code pattern
        matches = re.findall(r'CRICOS[^<]*Provider[^<]*Code[^<]*[:=\s]*00120C',
                             r.text, re.IGNORECASE | re.DOTALL)
        detail = matches[0].strip() if matches else ""
        if not detail and found:
            # Find context
            idx = r.text.find("00120C")
            if idx >= 0:
                snippet = r.text[max(0, idx-40):idx+40]
                detail = f"Found: ...{snippet}..."
        check("CRICOS 00120C on www.anu.edu.au", found, detail[:120])
    except Exception as e:
        check(f"CRICOS check on www.anu.edu.au failed", False, str(e))
    
    # Check study subdomain
    try:
        r = requests.get(STUDY_BASE, impersonate="chrome124", timeout=30,
                         allow_redirects=True)
        found = "00120C" in r.text
        matches = re.findall(r'CRICOS[^<]*Provider[^<]*Code[^<]*[:=\s]*00120C',
                             r.text, re.IGNORECASE | re.DOTALL)
        detail = matches[0].strip() if matches else ""
        if not detail and found:
            idx = r.text.find("00120C")
            if idx >= 0:
                snippet = r.text[max(0, idx-40):idx+40]
                detail = f"Found: ...{snippet}..."
        check("CRICOS 00120C on study.anu.edu.au", found, detail[:120])
    except Exception as e:
        check(f"CRICOS check on study.anu.edu.au failed", False, str(e))
    
    # Check programsandcourses subdomain
    try:
        r = requests.get(PC_BASE, impersonate="chrome124", timeout=30,
                         allow_redirects=True)
        found = "00120C" in r.text
        matches = re.findall(r'CRICOS[^<]*Provider[^<]*Code[^<]*[:=\s]*00120C',
                             r.text, re.IGNORECASE | re.DOTALL)
        detail = matches[0].strip() if matches else ""
        if not detail and found:
            idx = r.text.find("00120C")
            if idx >= 0:
                snippet = r.text[max(0, idx-40):idx+40]
                detail = f"Found: ...{snippet}..."
        check("CRICOS 00120C on programsandcourses.anu.edu.au", found, detail[:120])
    except Exception as e:
        check(f"CRICOS check on programsandcourses.anu.edu.au failed", False, str(e))


def check_course_page_ssr():
    print("\n[4] Course page SSR check")
    # Use ANU's program catalogue
    sample_url = f"{PC_BASE}/program/BADAN"
    try:
        r = requests.get(sample_url, impersonate="chrome124", timeout=30)
        is_ssr = "Bachelor of Applied Data Analytics" in r.text
        has_cricos = "CRICOS CODE" in r.text or "CRICOS code" in r.text
        has_length = "LENGTH" in r.text and "year" in r.text
        has_units = "Units" in r.text or "units" in r.text
        has_atar = "ATAR" in r.text
        has_fees_section = "Indicative Fees" in r.text or "Fees" in r.text

        check("Course page SSR (has program title)", is_ssr, f"HTTP {r.status_code}")
        check("CRICOS code on page", has_cricos)
        check("Length/duration present", has_length)
        check("ATAR/entry requirements", has_atar)
        check("Units/study load info", has_units)
        check("Fees section present", has_fees_section)

        # Extract CRICOS
        cricos_match = re.search(r'CRICOS\s*CODE[:\s]*([A-Z0-9]+)', r.text, re.IGNORECASE)
        if cricos_match:
            print(f"    CRICOS Code: {cricos_match.group(1)}")

        # Extract plan code
        plan_match = re.search(r'ACADEMIC\s*PLAN[:\s]*(\w+)', r.text, re.IGNORECASE)
        if plan_match:
            print(f"    Academic Plan: {plan_match.group(1)}")
    except Exception as e:
        check("Course page check failed", False, str(e))


def explore_catalogue_api():
    print("\n[5] Catalogue API exploration")
    try:
        # Check if search page returns JSON
        r = requests.get(f"{PC_BASE}/search", impersonate="chrome124", timeout=30,
                         headers={"Accept": "application/json"})
        is_json = "application/json" in r.headers.get("Content-Type", "")
        check("JSON API from /search", is_json, f"HTTP {r.status_code}")

        # Try degree builder API
        for path in ["/api/programs", "/api/courses", "/api/search"]:
            try:
                ra = requests.get(f"{PC_BASE}{path}", impersonate="chrome124", timeout=15,
                                 headers={"Accept": "application/json"})
                ct = ra.headers.get("Content-Type", "")
                if "json" in ct or ra.status_code in (200, 404):
                    check(f"API endpoint {path}", "json" in ct, f"HTTP {ra.status_code} CT:{ct[:50]}")
                else:
                    check(f"API endpoint {path}", False, f"HTTP {ra.status_code}")
            except Exception:
                check(f"API endpoint {path}", False, "Error")

        # Check if the search page loads with results from query params
        r2 = requests.get(f"{PC_BASE}/search?q=bachelor", impersonate="chrome124", timeout=30)
        has_results = "Bachelor of" in r2.text
        check("Search page with query has results", has_results)

        # Count programs listed - ANU search results are HTML tables
        # Look for the table rows with program data
        code_count = len(re.findall(r'<a\s+href="/program/[^"]+"', r2.text))
        check(f"Program links on search page", code_count > 0, f"~{code_count} program links")
        if code_count == 0:
            # Try looking for the show all link
            show_all = "Show all results" in r2.text
            check("  'Show all results' link present", show_all)

        # Get total counts from the search page
        r3 = requests.get(f"{PC_BASE}/search", impersonate="chrome124", timeout=30)
        total_matches = re.findall(r'(\d+)\s*RESULTS', r3.text, re.IGNORECASE)
        if total_matches:
            print(f"  Total results stated: {total_matches[0]}")

        for career in ["Undergraduate", "Postgraduate", "Research"]:
            count_match = re.search(rf'{career}\s*\((\d+)\)', r3.text)
            if count_match:
                print(f"  {career}: {count_match.group(1)} programs")

        # Try to extract program codes from the HTML
        # Table structure: <td><a href="/program/CODE">CODE</a></td>
        codes = re.findall(r'<a\s+href="/program/([A-Z0-9]+)"', r3.text)
        check("Program codes extracted", len(codes) > 0, f"{len(codes)} codes")
        if codes:
            print(f"  Sample codes: {codes[:5]}")
    except Exception as e:
        check("API exploration failed", False, str(e))


def enumerate_program_urls():
    print("\n[6] Course URL enumeration")
    try:
        print(f"  URL pattern: {PC_BASE}/program/{{CODE}}")
        print(f"  Example: {PC_BASE}/program/BADAN")

        # Try to count total from search page
        r = requests.get(f"{PC_BASE}/search", impersonate="chrome124", timeout=30)
        total_matches = re.findall(r'(\d+)\s*RESULTS', r.text, re.IGNORECASE)
        if total_matches:
            print(f"  Total results stated: {total_matches[0]}")

        # Count by career
        for career in ["Undergraduate", "Postgraduate", "Research"]:
            count_match = re.search(rf'{career}\s*\((\d+)\)', r.text)
            if count_match:
                print(f"  {career}: {count_match.group(1)} programs")

        # Extract program links
        codes = re.findall(r'<a\s+href="/program/([A-Z0-9]+)"', r.text)
        if codes:
            urls = [f"{PC_BASE}/program/{c}" for c in sorted(set(codes))]
            print(f"  Extracted {len(urls)} program URLs from search page")
            for u in urls[:5]:
                print(f"    {u}")

        # The catalogue uses show-all links for each section
        print("\n  Strategy:")
        print("  1. GET /search to get program counts per category")
        print("  2. Either iterate all codes or use degree-builder API")
        print("  3. Scrape each /program/{CODE} page for details")
    except Exception as e:
        check("URL enumeration failed", False, str(e))


def summary():
    print("\n" + "="*60)
    print("ANU — EXPLORATION SUMMARY")
    print("="*60)
    findings = {
        "Provider": "00120C",
        "CSV Courses": 420,
        "Base URL": BASE,
        "Cloudflare": "NO — Bare metal (Apache, ASP.NET)",
        "Impersonation needed": "No (standard HTTP works fine)",
        "Sitemap": "27+ sub-pages — mostly /study/ event/admin pages, NO direct program URLs",
        "Footer CRICOS": "Present on all domains — 'CRICOS Provider Code: 00120C'",
        "Course page SSR": "Full SSR via programsandcourses.anu.edu.au — title, CRICOS code, ATAR, duration in HTML",
        "Course URL pattern": "https://programsandcourses.anu.edu.au/program/{CODE}",
        "Catalogue": ".NET ASP app with search at /search, lists ~394 programs total",
        "Approach": "Scrape program listing from /search (HTML) → get program codes → scrape each /program/{CODE} page. Or call potential JSON API endpoints."
    }
    for k, v in findings.items():
        print(f"  {k:30s}: {v}")


if __name__ == "__main__":
    print("="*60)
    print("ANU — EXPLORATION")
    print("="*60)

    probe_cloudflare()
    check_sitemap()
    check_footer_cricos()
    check_course_page_ssr()
    explore_catalogue_api()
    enumerate_program_urls()
    summary()
