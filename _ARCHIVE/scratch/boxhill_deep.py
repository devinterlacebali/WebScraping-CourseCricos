"""Box Hill - find course pages and structure."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.boxhill.edu.au'

# Robots.txt
r = curl.get(DOMAIN + '/robots.txt', impersonate='chrome120', timeout=15)
print('robots.txt:', r.status_code, len(r.text), 'bytes')
if len(r.text) > 10:
    for line in r.text.splitlines():
        if 'sitemap' in line.lower():
            print('  ', line.strip())

# Check study/courses pages
paths = [
    '/courses',
    '/study',
    '/international',
    '/study/courses',
    '/courses/international',
    '/future-students/international',
    '/course-search',
]

for p in paths:
    r2 = curl.get(DOMAIN + p, impersonate='chrome120', timeout=15)
    print(f'{p}: {r2.status_code} ({len(r2.text)} bytes)')
    if r2.status_code == 200 and len(r2.text) > 1000:
        s = BeautifulSoup(r2.text, 'html.parser')
        links = []
        for a in s.find_all('a', href=True):
            h = a['href']
            txt = a.get_text(strip=True)[:40]
            if 'course' in h.lower() or '/international/' in h.lower() or '/study/' in h.lower():
                if not h.startswith('http'): h = DOMAIN + h if h.startswith('/') else h
                links.append((txt, h))
        print(f'  Links: {len(links)}')
        if links:
            for t, h in links[:5]:
                print(f'    [{t[:30]}] -> {h[:70]}')

# Check JSON-LD on homepage
r3 = curl.get(DOMAIN, impersonate='chrome120', timeout=15)
body = r3.text
for m in re.finditer(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', body, re.I | re.S):
    print(f'\nJSON-LD: {m.group(1)[:300]}')
