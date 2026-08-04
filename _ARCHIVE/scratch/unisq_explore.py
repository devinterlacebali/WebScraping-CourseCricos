"""Explore UniSQ site structure."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

# Sitemap
r = curl.get('https://www.unisq.edu.au/sitemap.xml', impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'xml')
locs = [l.text for l in soup.find_all('loc')]
print(f'Sitemap URLs: {len(locs)}')

# Find course/degree URLs
study_urls = [u for u in locs if '/study/' in u]
print(f'Study URLs: {len(study_urls)}')
for u in study_urls[:20]:
    print(f'  {u}')
print('...')

# Check if sitemap index
sitemaps = [u for u in locs if u.endswith('.xml') or '/sitemap' in u]
print(f'\nSub-sitemaps: {len(sitemaps)}')
for s in sitemaps:
    print(f'  {s}')
    if s.endswith('.xml') and 'sitemap' in s:
        try:
            r2 = curl.get(s, impersonate='chrome120', timeout=15)
            locs2 = re.findall(r'<loc>(.*?)</loc>', r2.text)
            degs = [u for u in locs2 if 'degree' in u.lower() or 'course' in u.lower() or 'program' in u.lower()]
            if degs:
                print(f'    Found {len(degs)} program URLs:')
                for d in degs[:3]: print(f'      {d}')
                for d in degs[-2:]: print(f'      {d}')
        except: pass

# Test a course page
for path in ['/study/degrees/bachelor-of-nursing', '/study/degrees/bachelor-nursing', 
             '/study/courses/bachelor-of-nursing', '/international/degrees/bachelor-of-nursing']:
    u = f'https://www.unisq.edu.au{path}'
    r2 = curl.get(u, impersonate='chrome120', timeout=15)
    print(f'\n{path}: {r2.status_code}, {len(r2.text)}b')
    if r2.status_code == 200 and len(r2.text) > 2000:
        s = BeautifulSoup(r2.text, 'html.parser')
        h1 = s.find('h1')
        print(f'  H1: {h1.get_text(strip=True) if h1 else \"none\"}')
        print(f'  Title: {s.title.string.strip() if s.title else \"none\"}'[:80])
        # Look for CRICOS
        body = s.get_text()
        for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', body, re.I):
            print(f'  CRICOS: {m.group()}')
        for kw in ['fee', 'tuition', 'cricos', 'duration']:
            if kw in body.lower():
                for m in re.finditer(r'.{0,30}' + kw + r'.{0,60}', body, re.I):
                    ctx = m.group().strip()[:120]
                    if 'error' not in ctx.lower() and 'footer' not in ctx.lower():
                        print(f'  [{kw}]: {ctx}')
        break
