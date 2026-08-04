"""Curtin - check study subdomain."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://study.curtin.edu.au'

r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')
print(f'Status: {r.status_code}, {len(r.text)}b')
h1 = s.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
has_next = '__NEXT_DATA__' in r.text
print(f'Next.js: {has_next}')

r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
if r2.status_code == 200:
    urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
    print(f'Sitemap URL count: {len(urls)}')
    categories = {}
    for u in urls:
        parts = u.replace(DOMAIN, '').strip('/').split('/')
        cat = parts[0] if parts else 'root'
        categories[cat] = categories.get(cat, 0) + 1
    for cat, cnt in sorted(categories.items())[:15]:
        print(f'  /{cat}/: {cnt} URLs')
    course_like = [u for u in urls if any(kw in u for kw in ['/course/', '/offering/', '/degree/', '/program/'])]
    print(f'\nCourse-like URLs: {len(course_like)}')
    for u in course_like[:5]: print(f'  {u}')
    if not course_like:
        # Show some sample URL paths
        for u in urls[:5]: print(f'  {u}')
