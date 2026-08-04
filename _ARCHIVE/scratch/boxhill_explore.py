"""Box Hill Institute - quick exploration."""
import sys, re, csv
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.boxhill.edu.au'

r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
print('Homepage:', r.status_code, len(r.text), 'bytes')
print('CF-Ray:', r.headers.get('cf-ray', 'none'))

# CRICOS in page
body = r.text
for m in re.finditer(r'CRICOS.{0,60}', body, re.I):
    ctx = re.sub(r'\s+', ' ', m.group())[:80]
    print('CRICOS:', ctx)

for m in re.finditer(r'(\d{6}[A-Z])', body):
    idx = m.start()
    ctx = body[max(0,idx-30):idx+30]
    if not re.search(r'#[0-9a-fA-F]|background|color:', ctx, re.I):
        print('Code:', m.group(1), '|', re.sub(r'\s+', ' ', ctx).strip()[:60])

# Sitemap
for sp in ['/sitemap.xml', '/page-sitemap.xml']:
    r2 = curl.get(DOMAIN + sp, impersonate='chrome120', timeout=15)
    print(sp + ':', r2.status_code, len(r2.text), 'bytes')
    if r2.status_code == 200 and len(r2.text) > 100:
        urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
        cu = [u for u in urls if 'course' in u.lower()]
        print('  URLs:', len(urls), 'Course:', len(cu))
        if cu: print('  e.g.', cu[0])

# CSV
with open('cricos-courses.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    seen = {}
    for row in reader:
        inst = row['Institution Name'].strip()
        if 'box hill' in inst.lower() or 'boxhill' in inst.lower():
            code = row['CRICOS Provider Code'].strip()
            if code not in seen:
                seen[code] = 0
            seen[code] += 1
    for code, cnt in seen.items():
        print(f'CSV: {code} -> {cnt} courses')
