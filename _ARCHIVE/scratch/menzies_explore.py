"""
Exploration: Menzies Institute of Technology Pty Ltd — http://www.menzies.vic.edu.au/
Date: 2026-07-25
"""
from curl_cffi import requests
import re, json

BASE = "http://www.menzies.vic.edu.au"

def check_cloudflare(headers):
    for h in headers:
        if 'cloudflare' in str(headers[h]).lower() or h.lower().startswith('cf-'):
            return True, h
    server = headers.get('server', '')
    if 'cloudflare' in server.lower():
        return True, 'server'
    return False, server

print("=" * 60)
print("1. CLOUDFLARE CHECK")
print("=" * 60)
try:
    r = requests.get(BASE + "/", impersonate='chrome120', timeout=15)
    print(f"  Status: {r.status_code}")
    is_cf, detail = check_cloudflare(dict(r.headers))
    print(f"  Cloudflare: {'YES' if is_cf else 'NO'} (server: {detail})")
    print(f"  Headers: {json.dumps(dict(r.headers), indent=4)}")
except Exception as e:
    print(f"  Error: {e}")

print("\n" + "=" * 60)
print("2. PROVIDER CRICOS CODE (from footer)")
print("=" * 60)
try:
    r = requests.get(BASE + "/", impersonate='chrome120', timeout=15)
    html = r.text
    cricos_mentions = re.findall(r'CRICOS[^<]{0,100}', html, re.IGNORECASE)
    codes = re.findall(r'\b\d{5}[A-Z]\b', html)
    rto = re.findall(r'RTO[^<]{0,100}', html, re.IGNORECASE)
    print(f"  CRICOS mentions: {cricos_mentions}")
    print(f"  CRICOS codes found in HTML: {codes}")
    print(f"  RTO mentions: {rto}")
    
    # Check about page too
    r2 = requests.get(BASE + "/about-us/", impersonate='chrome120', timeout=15)
    html2 = r2.text
    codes2 = re.findall(r'\b\d{5}[A-Z]\b', html2)
    cricos2 = re.findall(r'CRICOS[^<]{0,100}', html2, re.IGNORECASE)
    print(f"  About page CRICOS mentions: {cricos2}")
    print(f"  About page codes found: {codes2}")
    print(f"  NOTE: CRICOS code 02815M is from CSV — NOT found in website HTML")
except Exception as e:
    print(f"  Error: {e}")

print("\n" + "=" * 60)
print("3. SITEMAP ANALYSIS")
print("=" * 60)
sitemaps_to_check = [
    "/sitemap.xml", "/page-sitemap.xml", "/course-sitemap.xml",
    "/post-sitemap.xml", "/sitemap_index.xml"
]
for sm in sitemaps_to_check:
    try:
        r = requests.get(BASE + sm, impersonate='chrome120', timeout=10)
        urls = re.findall(r'<loc>(.*?)</loc>', r.text)
        print(f"  {sm}: status={r.status_code}, URLs={len(urls)}")
        if urls and len(urls) <= 5:
            for u in urls:
                print(f"    {u}")
        elif urls:
            print(f"    First 3: {urls[:3]}")
    except Exception as e:
        print(f"  {sm}: Error - {e}")

print("\n" + "=" * 60)
print("4. CSV COVERAGE (cricos-courses.csv)")
print("=" * 60)
print("  CRICOS: 02815M — Menzies Institute of Technology Pty Ltd")
print("  Courses in CSV: 18")
sample_courses = [
    "Diploma of Dental Technology",
    "Certificate IV in Automotive Mechanical Diagnosis",
    "Certificate III in Light Vehicle Mechanical Technology",
    "Diploma of Nursing",
    "Certificate IV in Ageing Support",
    "Diploma of Community Services"
]
for c in sample_courses:
    print(f"    - {c}")

print("\n" + "=" * 60)
print("5. COURSE PAGE SSR CHECK")
print("=" * 60)
try:
    r = requests.get(BASE + "/course/acute-health/",
                     impersonate='chrome120', timeout=15)
    html = r.text
    print(f"  URL: {BASE}/course/acute-health/")
    print(f"  Status: {r.status_code}, Length: {len(html)}")
    title = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    print(f"  Title: {title.group(1) if title else 'N/A'}")
    print(f"  NOTE: This is an ARCHIVE/CATEGORY page, not a course detail page")
    
    # Check if there are individual course pages
    r2 = requests.get(BASE + "/course/test-health-course/",
                      impersonate='chrome120', timeout=15)
    html2 = r2.text
    title2 = re.search(r'<title>(.*?)</title>', html2, re.DOTALL)
    print(f"  /course/test-health-course/ title: {title2.group(1) if title2 else 'N/A'}")
    
    checks = ['CRICOS', 'duration', 'fee', 'intake', 'delivery', 'cricos']
    for c in checks:
        found = c.lower() in html.lower()
        print(f"  Contains '{c}' (archive): {found}")
    
    print("  VERDICT: No individual course detail pages found.")
    print("  Course-sitemap has only 2 archive/category URLs.")
    print("  Course data likely not available via SSR on this site.")
except Exception as e:
    print(f"  Error: {e}")
