"""Curtin - process sitemaps."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
import re

DOMAIN = 'https://www.curtin.edu.au'

# Get study sitemaps
for sm in ['/study/page-sitemap1.xml', '/study/pd-sitemap1.xml', '/study/extras-sitemap1.xml']:
    r = curl.get(f'{DOMAIN}{sm}', impersonate='chrome120', timeout=30)
    urls = re.findall(r'<loc>(.*?)</loc>', r.text)
    print(f'{sm}: {len(urls)} URLs')
    course_urls = [u for u in urls if any(kw in u.lower() for kw in 
                   ['course', 'degree', 'program', 'bachelor', 'master', 'graduate', 'diploma'])]
    print(f'  Course-related: {len(course_urls)}')
    for u in course_urls[:5]: print(f'  {u}')
    if not course_urls and urls:
        for u in urls[:3]: print(f'  {u}')

# Check courses.curtin.edu.au sitemap
print('\n--- courses.curtin.edu.au ---')
try:
    r2 = curl.get('https://courses.curtin.edu.au/sitemap.xml', impersonate='chrome120', timeout=30)
    print(f'Sitemap: {r2.status_code}, {len(r2.text)}b')
    if r2.status_code == 200:
        urls2 = re.findall(r'<loc>(.*?)</loc>', r2.text)
        print(f'URLs: {len(urls2)}')
        for u in urls2[:5]: print(f'  {u}')
except Exception as e:
    print(f'Sitemap error: {e}')

# Check courses.curtin.edu.au main page for JS route
print('\n--- courses.curtin.edu.au explore ---')
r3 = curl.get('https://courses.curtin.edu.au/', impersonate='chrome120', timeout=30)
print(f'Status: {r3.status_code}, {len(r3.text)}b')
s3 = __import__('bs4').BeautifulSoup(r3.text, 'html.parser')
h1 = s3.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
has_next = '__NEXT_DATA__' in r3.text
has_nuxt = '__NUXT__' in r3.text
print(f'Next.js: {has_next}, Nuxt: {has_nuxt}')
for sc in s3.find_all('script', src=True):
    src = sc['src']
    if any(kw in src for kw in ['app', 'main', 'vendor', 'bundle']):
        print(f'  Bundle: {src}')
links = set()
for a in s3.find_all('a', href=True):
    h = a['href']
    if '/course/' in h.lower() or '/degree/' in h.lower():
        links.add(h)
print(f'Course links: {len(links)}')
for l in sorted(list(links))[:5]: print(f'  {l}')
