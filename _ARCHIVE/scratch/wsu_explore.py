"""WSU - quick exploration."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.westernsydney.edu.au'

r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
print(f'Main: {r.status_code}, {len(r.text)}b')
body = r.text
print(f'Cloudflare: {"cloudflare" in body.lower() or "cf-browser" in body}')
soup = BeautifulSoup(body, 'html.parser')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
has_next = '__NEXT_DATA__' in body
has_nuxt = '__NUXT__' in body
print(f'Next.js: {has_next}, Nuxt: {has_nuxt}')

# Sitemap
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
print(f'\nSitemap: {r2.status_code}, {len(r2.text)}b')
if r2.status_code == 200 and len(r2.text) > 100:
    urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
    print(f'URLs: {len(urls)}')
    # Check if index
    subs = re.findall(r'<sitemap>', r2.text)
    print(f'Index format: {len(subs)}')
    if subs:
        sub_urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
        for su in sub_urls[:8]:
            r3 = curl.get(su, impersonate='chrome120', timeout=15)
            su2 = re.findall(r'<loc>(.*?)</loc>', r3.text)
            course_like = [u for u in su2 if any(k in u.lower() for k in ['course','degree','program','bachelor','master'])]
            print(f'  {su.split("/")[2][:30]}: {len(su2)} URLs, {len(course_like)} course-like')
    else:
        cats = {}
        for u in urls:
            p = u.replace(DOMAIN, '').strip('/').split('/')
            cat = p[0] if p else 'root'
            cats[cat] = cats.get(cat, 0) + 1
        for c, n in sorted(cats.items(), key=lambda x: -x[1])[:10]:
            print(f'  /{c}/: {n}')

# Check CSV
print('\n--- CSV ---')
import csv
codes = {}
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and len(row) > 3 and 'western sydney' in row[3].lower():
            codes[row[0].strip()] = codes.get(row[0].strip(), 0) + 1
print(f'WSU provider codes: {codes}')
