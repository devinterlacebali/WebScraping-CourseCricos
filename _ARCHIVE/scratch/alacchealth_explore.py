"""
Exploration: ALACC Health College (Australasian Lawrence Aged Care College) — www.alacchealth.edu.au
Date: 2026-07-25
"""
from curl_cffi import requests
import re, json, socket

BASE = "https://www.alacchealth.edu.au"
BASE_HTTP = "http://www.alacchealth.edu.au"

print("=" * 60)
print("1. CLOUDFLARE CHECK / SITE REACHABILITY")
print("=" * 60)
# Check DNS first
try:
    ip = socket.gethostbyname('www.alacchealth.edu.au')
    print(f"  DNS resolved: www.alacchealth.edu.au -> {ip}")
except Exception as e:
    print(f"  DNS error: {e}")

# Try HTTPS
try:
    r = requests.get(BASE + "/", impersonate='chrome120', timeout=20)
    print(f"  HTTPS Status: {r.status_code}")
    print(f"  Headers: {json.dumps(dict(r.headers), indent=4)}")
except Exception as e:
    print(f"  HTTPS Error: {e}")

# Try HTTP
try:
    r = requests.get(BASE_HTTP + "/", impersonate='chrome120', timeout=20)
    print(f"  HTTP Status: {r.status_code}")
except Exception as e:
    print(f"  HTTP Error: {e}")

print("\n" + "=" * 60)
print("2. PROVIDER CRICOS CODE")
print("=" * 60)
print("  Source: provider_institution.csv")
print("  CRICOS: 02933E")
print("  Provider: ALACC Health College, Australia")
print("  Legal name: Australasian Lawrence Aged Care College Pty Ltd")
print("  NOTE: Could not verify from website — site unreachable")

print("\n" + "=" * 60)
print("3. SITEMAP ANALYSIS")
print("=" * 60)
sitemaps_to_check = [
    "/sitemap.xml", "/page-sitemap.xml", "/course-sitemap.xml",
    "/sitemap_index.xml", "/wp-sitemap.xml"
]
for sm in sitemaps_to_check:
    try:
        r = requests.get(BASE + sm, impersonate='chrome120', timeout=10)
        urls = re.findall(r'<loc>(.*?)</loc>', r.text)
        print(f"  {sm}: status={r.status_code}, URLs={len(urls)}")
    except Exception as e:
        print(f"  {sm}: Error - {e}")

print("\n" + "=" * 60)
print("4. CSV COVERAGE (cricos-courses.csv)")
print("=" * 60)
print("  CRICOS: 02933E")
print("  Courses in CSV: 0 (no entries found for this CRICOS code)")
print("  NOTE: Provider exists in provider_institution.csv but has")
print("  no active courses in cricos-courses.csv")

print("\n" + "=" * 60)
print("5. COURSE PAGE SSR CHECK")
print("=" * 60)
print("  Cannot check — site is unreachable (connection timed out)")
print("  Hosted on AWS (3.104.25.158)")
print("  SSL/TLS handshake may be blocked or server not responding")
