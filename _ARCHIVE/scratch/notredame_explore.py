"""Notre Dame - quick exploration."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.notredame.edu.au'

# Check Cloudflare + sitemap
r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
print(f'Homepage: {r.status_code} ({len(r.text)} bytes)')
print(f'CF-Ray: {r.headers.get("cf-ray", "none")}')

# Sitemap
for sp in ['/sitemap.xml', '/sitemap_index.xml', '/sitemap-index.xml']:
    r2 = curl.get(f'{DOMAIN}{sp}', impersonate='chrome120', timeout=15)
    print(f'{sp}: {r2.status_code} ({len(r2.text)} bytes)')
    if r2.status_code == 200 and len(r2.text) > 100:
        urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
        course_urls = [u for u in urls if any(k in u.lower() for k in ['course', 'degree', 'program', 'study'])]
        print(f'  Total URLs: {len(urls)}, Course-related: {len(course_urls)}')
        if course_urls: print(f'  e.g. {course_urls[0]}')

# Check CSV coverage
import csv
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    codes = {}
    for row in reader:
        if not row or len(row) < 3: continue
        if 'notre dame' in row[3].lower():
            codes.setdefault(row[0].strip(), 0)
            codes[row[0].strip()] += 1
    print(f'CSV matches: {codes}')
