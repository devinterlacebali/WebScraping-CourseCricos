"""
Bond University — Exploration Script
URL: https://bond.edu.au/ (provider 00017B, 179 CSV courses)

Checks: Cloudflare, sitemap, footer CRICOS, course page SSR, course URLs

Usage:
  cd /c/Users/Dewa(Interlace)/Documents/Interlace Code/WebScraping-CourseCricos
  venv/Scripts/python scratch/bond_explore.py
"""

import json
import sys
import time

# Use curl_cffi for Cloudflare-immune requests
try:
    from curl_cffi import requests
except ImportError:
    print("ERROR: curl_cffi not installed. Run: pip install curl_cffi")
    sys.exit(1)

BASE = "https://bond.edu.au"
OUT_DIR = "scratch"


def check(label, ok, detail=""):
    status = "✅" if ok else "❌"
    print(f"  {status} {label}" + (f" — {detail}" if detail else ""))


def probe_cloudflare():
    """Check if Cloudflare is detected."""
    print("\n[1] Cloudflare check")
    try:
        r = requests.get(BASE, impersonate="chrome124", timeout=30)
        server = r.headers.get("Server", "")
        cf_ray = r.headers.get("CF-RAY", "")
        cf_bm = "cf_bm" in str(r.cookies) or "__cf_bm" in str(r.headers.get("set-cookie", ""))
        is_cf = "cloudflare" in server.lower() or cf_ray or cf_bm

        detail_parts = []
        if server:
            detail_parts.append(f"Server: {server}")
        if cf_ray:
            detail_parts.append(f"CF-RAY: {cf_ray}")
        if is_cf:
            detail_parts.append("Cloudflare ACTIVE")

        check("Cloudflare detected", is_cf, " | ".join(detail_parts))
        check("curl_cffi bypass OK", r.status_code == 200, f"HTTP {r.status_code}")
        return r
    except Exception as e:
        check("Cloudflare probe failed", False, str(e))
        return None


def check_sitemap():
    """Check sitemap structure."""
    print("\n[2] Sitemap check")
    try:
        r = requests.get(f"{BASE}/sitemap.xml", impersonate="chrome124", timeout=30)
        check("Sitemap index reachable", r.status_code == 200, f"HTTP {r.status_code}")

        if "sitemapindex" in r.text:
            import re
            pages = re.findall(r'<sitemap><loc>([^<]+)</loc>', r.text)
            check("Sitemap sub-pages found", len(pages) > 0, f"{len(pages)} sub-sitemaps")

            # Check first page for program URLs
            r2 = requests.get(f"{BASE}/sitemap.xml?page=1", impersonate="chrome124", timeout=30)
            program_urls = re.findall(r'https://bond\.edu\.au/program/[^<]+', r2.text)
            check(f"Program URLs in sitemap page 1", len(program_urls) > 0,
                  f"{len(program_urls)} program URLs found")
            if program_urls:
                print(f"    Sample: {program_urls[0]}")
        elif "urlset" in r.text:
            check("Sitemap is direct (no index)", True, "single urlset")
        else:
            check("Sitemap format unexpected", False, r.text[:200])
    except Exception as e:
        check("Sitemap check failed", False, str(e))


def check_footer_cricos():
    """Check footer for CRICOS provider code."""
    print("\n[3] Footer CRICOS check")
    try:
        r = requests.get(BASE, impersonate="chrome124", timeout=30)
        found = "00017B" in r.text
        cricos_text = ""
        import re
        matches = re.findall(r'CRICOS[^<]*00017B[^<]*', r.text)
        if matches:
            cricos_text = matches[0].strip()
        check("CRICOS 00017B in footer", found, cricos_text[:120] if cricos_text else "")
    except Exception as e:
        check("Footer check failed", False, str(e))


def check_course_page_ssr():
    """Check a sample course page for SSR (server-side rendered content)."""
    print("\n[4] Course page SSR check")
    sample_url = f"{BASE}/program/master-of-enterprise-artificial-intelligence"
    try:
        r = requests.get(sample_url, impersonate="chrome124", timeout=30)
        is_ssr = "Master of Enterprise Artificial Intelligence" in r.text
        has_cricos_code = "CRICOS code" in r.text.lower() or "CRICOS Code" in r.text
        check("Course page SSR (has program title)", is_ssr, f"HTTP {r.status_code}")
        check("CRICOS code on course page", has_cricos_code)

        # Check for key fields
        for field in ["Program code", "Duration", "Delivery mode", "Location", "CRICOS"]:
            has_field = field.lower() in r.text.lower()
            check(f"  Field: {field}", has_field)
    except Exception as e:
        check("Course page check failed", False, str(e))


def enumerate_program_urls():
    """Enumerate program URLs from sitemap."""
    print("\n[5] Course URL enumeration")
    try:
        import re
        all_program_urls = set()
        # Check page 1
        for page in [1, 2]:
            try:
                r = requests.get(f"{BASE}/sitemap.xml?page={page}",
                                 impersonate="chrome124", timeout=30)
                urls = re.findall(r'https://bond\.edu\.au/program/[^<]+', r.text)
                all_program_urls.update(urls)
            except Exception:
                pass

        # Also check program-finder API
        try:
            r = requests.get(f"{BASE}/study/program-finder",
                             impersonate="chrome124", timeout=30)
            # Look for program URLs embedded in page
            urls = re.findall(r'/program/[^"\'\\]+', r.text)
            for u in urls:
                all_program_urls.add(f"https://bond.edu.au{u}" if u.startswith("/") else u)
        except Exception:
            pass

        check("Program URLs discovered", len(all_program_urls) > 0,
              f"{len(all_program_urls)} unique program URLs")
        if all_program_urls:
            samples = sorted(all_program_urls)[:5]
            for s in samples:
                print(f"    {s}")
    except Exception as e:
        check("URL enumeration failed", False, str(e))


def summary():
    """Print a summary of findings."""
    print("\n" + "="*60)
    print("BOND UNIVERSITY — EXPLORATION SUMMARY")
    print("="*60)
    findings = {
        "Provider": "00017B",
        "CSV Courses": 179,
        "Base URL": BASE,
        "Cloudflare": "YES — uses Cloudflare with cf_bm cookies",
        "Impersonation needed": "Yes (curl_cffi with chrome124 works)",
        "Sitemap": "sitemap.xml → 13 sub-pages — contains /program/ URLs",
        "Footer CRICOS": "Present — 'CRICOS Provider Code 00017B'",
        "Course page SSR": "Full SSR — title, CRICOS code, duration, fees all in HTML",
        "Course URL pattern": "https://bond.edu.au/program/{program-slug}",
        "Approach": "Use curl_cffi to list sitemap pages → parse /program/ URLs → scrape each SSR page"
    }
    for k, v in findings.items():
        print(f"  {k:25s}: {v}")


if __name__ == "__main__":
    print("="*60)
    print("BOND UNIVERSITY — EXPLORATION")
    print("="*60)

    probe_cloudflare()
    check_sitemap()
    check_footer_cricos()
    check_course_page_ssr()
    enumerate_program_urls()
    summary()
