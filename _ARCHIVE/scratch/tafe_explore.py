"""TAFE NSW - quick exploration."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.tafensw.edu.au'

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

# International page
r2 = curl.get(f'{DOMAIN}/international', impersonate='chrome120', timeout=30)
print(f'\n/international: {r2.status_code}, {len(r2.text)}b')
s2 = BeautifulSoup(r2.text, 'html.parser')
h1_2 = s2.find('h1')
print(f'H1: {h1_2.get_text(strip=True)[:80] if h1_2 else "none"}')

# Sitemap
r3 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
print(f'\nSitemap: {r3.status_code}, {len(r3.text)}b')
if r3.status_code == 200:
    urls = re.findall(r'<loc>(.*?)</loc>', r3.text)
    print(f'URLs: {len(urls)}')
    # Categories
    cats = {}
    for u in urls:
        p = u.replace(DOMAIN, '').strip('/').split('/')
        cat = p[0] if p else 'root'
        cats[cat] = cats.get(cat, 0) + 1
    for c, n in sorted(cats.items(), key=lambda x: -x[1])[:15]:
        print(f'  /{c}/: {n}')
    course_urls = [u for u in urls if 'course' in u.lower() or 'international' in u.lower()]
    print(f'\nCourse/Intl URLs: {len(course_urls)}')
    for u in course_urls[:5]: print(f'  {u}')
