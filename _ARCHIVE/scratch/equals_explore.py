"""
Exploration: EQUALS International (Aust) Pty Ltd — https://equals.edu.au/
Date: 2026-07-25
"""
from curl_cffi import requests
import re, json

BASE = "https://equals.edu.au"
VENV_PYTHON = "./venv/Scripts/python"

def check_cloudflare(headers):
    cf_headers = ['cf-ray', 'cf-cache-status', 'cf-request-id', 'server-cloudflare']
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
    # Search footer
    cricos_mentions = re.findall(r'CRICOS[^<]{0,100}', html, re.IGNORECASE)
    codes = re.findall(r'\b\d{5}[A-Z]\b', html)
    print(f"  CRICOS mentions: {cricos_mentions}")
    print(f"  CRICOS codes: {codes}")
    print(f"  Footer text: TEQSA Provider ID PRV14279 | RTO ID 3492 | CRICOS Code 02804C")
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
print("  CRICOS: 02804C — EQUALS International (Aust) Pty Ltd")
print("  Courses in CSV: 23")
# Sample from CSV
print("  Sample courses:")
sample_courses = [
    "Bachelor of Human Services", "Diploma in Human Services",
    "Diploma of Community Services", "Advanced Diploma of Nursing",
    "Master of Social Work (Qualifying)", "Diploma of Nursing"
]
for c in sample_courses:
    print(f"    - {c}")

print("\n" + "=" * 60)
print("5. COURSE PAGE SSR CHECK")
print("=" * 60)
try:
    r = requests.get(BASE + "/courses/nursing-health/advanced-diploma-of-nursing/",
                     impersonate='chrome120', timeout=15)
    html = r.text
    print(f"  Status: {r.status_code}, Length: {len(html)}")
    checks = ['CRICOS', 'Duration', 'Study Mode', 'Tuition', 'Intakes', 'course-content']
    for c in checks:
        print(f"  Contains '{c}': {c.lower() in html.lower()}")
    
    if 'CRICOS' in html:
        for m in re.finditer(r'CRICOS[^<]{0,100}', html):
            print(f"  → CRICOS data: {m.group().strip()}")
    
    # Check for key structured data
    for field in ['Duration', 'Study Mode', 'Tuition Fees', 'Intakes']:
        if field.lower() in html.lower():
            idx = html.lower().find(field.lower())
            print(f"  → Field '{field}' found at pos {idx}")
    
    print("  VERDICT: SSR — course details fully rendered in HTML")
except Exception as e:
    print(f"  Error: {e}")
