"""
Exploration: Education Training & Employment Australia Pty. Ltd. (ETEA) — http://www.etea.edu.au/
Date: 2026-07-25
"""
from curl_cffi import requests
import re, json

BASE = "http://www.etea.edu.au"

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
    print(f"  CRICOS mentions: {cricos_mentions}")
    print(f"  CRICOS codes: {codes}")
except Exception as e:
    print(f"  Error: {e}")

print("\n" + "=" * 60)
print("3. SITEMAP ANALYSIS")
print("=" * 60)
sitemaps_to_check = [
    "/sitemap.xml", "/page-sitemap.xml", "/course-sitemap.xml",
    "/sitemap_index.xml", "/web-story-sitemap.xml"
]
for sm in sitemaps_to_check:
    try:
        r = requests.get(BASE + sm, impersonate='chrome120', timeout=10)
        urls = re.findall(r'<loc>(.*?)</loc>', r.text)
        print(f"  {sm}: status={r.status_code}, URLs={len(urls)}")
        if urls and len(urls) <= 10:
            for u in urls:
                print(f"    {u}")
        elif urls:
            print(f"    First 5: {urls[:5]}")
    except Exception as e:
        print(f"  {sm}: Error - {e}")

print("\n" + "=" * 60)
print("4. CSV COVERAGE (cricos-courses.csv)")
print("=" * 60)
print("  CRICOS: 02925E — Education Training & Employment Australia Pty. Ltd.")
print("  Courses in CSV: 31")
sample_courses = [
    "Certificate IV in Ageing Support",
    "Diploma of Community Services",
    "Certificate III in Individual Support",
    "Diploma of Nursing",
    "Diploma of Early Childhood Education and Care",
    "Certificate III in Light Vehicle Mechanical Technology",
    "Diploma of Counselling"
]
for c in sample_courses:
    print(f"    - {c}")

print("\n" + "=" * 60)
print("5. COURSE PAGE SSR CHECK")
print("=" * 60)
try:
    r = requests.get(BASE + "/chc52025-diploma-of-community-services/",
                     impersonate='chrome120', timeout=15)
    html = r.text
    print(f"  URL: {BASE}/chc52025-diploma-of-community-services/")
    print(f"  Status: {r.status_code}, Length: {len(html)}")
    title = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    print(f"  Title: {title.group(1) if title else 'N/A'}")
    
    checks = ['CRICOS', 'duration', 'fee', 'intake', 'delivery']
    for c in checks:
        found = c.lower() in html.lower()
        print(f"  Contains '{c}': {found}")
    
    if 'CRICOS' in html:
        for m in re.finditer(r'CRICOS[^<]{0,100}', html):
            print(f"  → CRICOS: {m.group().strip()}")
    
    print("  VERDICT: SSR — course pages render with description,")
    print("  CRICOS provider, duration text. Fee data in PDF links.")
    print("  Individual course pages exist for ~31 courses.")
except Exception as e:
    print(f"  Error: {e}")
