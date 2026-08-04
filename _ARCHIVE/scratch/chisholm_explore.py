"""Chisholm Institute - quick exploration."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.chisholm.edu.au'

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
if r2.status_code == 200:
    urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
    print(f'URLs: {len(urls)}')
    cats = {}
    for u in urls:
        p = u.replace(DOMAIN, '').strip('/').split('/')
        cat = p[0] if p else 'root'
        cats[cat] = cats.get(cat, 0) + 1
    for c, n in sorted(cats.items(), key=lambda x: -x[1])[:15]:
        print(f'  /{c}/: {n}')

# International page
r3 = curl.get(f'{DOMAIN}/international-students', impersonate='chrome120', timeout=30)
print(f'\n/international-students: {r3.status_code}, {len(r3.text)}b')
if r3.status_code == 200:
    s3 = BeautifulSoup(r3.text, 'html.parser')
    h1_3 = s3.find('h1')
    print(f'H1: {h1_3.get_text(strip=True)[:80] if h1_3 else "none"}')
    links = [a['href'] for a in s3.find_all('a', href=True) if 'course' in a.get('href','').lower()]
    print(f'Course links: {len(links)}')
    for l in links[:5]: print(f'  {l}')

# Check course page
print('\n--- Try course page ---')
for slug in ['diploma-of-nursing', 'bachelor-of-nursing', 'nursing']:
    for pat in ['/courses/{s}', '/course/{s}', '/study/{s}']:
        try:
            r4 = curl.get(f'{DOMAIN}{pat.format(s=slug)}', impersonate='chrome120', timeout=10)
            if r4.status_code == 200 and len(r4.text) > 1000:
                s4 = BeautifulSoup(r4.text, 'html.parser')
                h1_4 = s4.find('h1')
                body4 = re.sub(r'\s+', ' ', s4.get_text())
                cricos = bool(re.search(r'CRICOS', body4))
                fee = bool(re.search(r'AUD|international fee', body4, re.I))
                print(f'{pat.format(s=slug)}: 200 | H1={h1_4.get_text(strip=True)[:40] if h1_4 else "?"} | CRICOS={cricos} | Fee={fee}')
                break
        except: pass
    else:
        continue
    break

# Check CSV
print('\n--- CSV for Chisholm ---')
import csv
codes = set()
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and ('chisholm' in row[3].lower() if len(row) > 3 else False):
            codes.add(row[0].strip())
print(f'Chisholm provider codes: {codes}')
for c in sorted(codes):
    count = sum(1 for row in csv.reader(open('cricos-courses.csv', encoding='utf-8')) if row and row[0].strip() == c)
    print(f'  {c}: {count} courses')
