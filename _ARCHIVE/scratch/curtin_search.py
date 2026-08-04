"""Curtin - find all course pages."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.curtin.edu.au'

# Check if there's a sitemap with course URLs on different sitemap index
# Also check /study/ sub-sitemaps
for prefix in ['study', 'courses', 'degrees']:
    for f in ['sitemap.xml', 'sitemap_index.xml', 'sitemap1.xml']:
        url = f'{DOMAIN}/{prefix}/{f}'
        try:
            r = curl.get(url, impersonate='chrome120', timeout=15)
            if r.status_code == 200:
                urls = re.findall(r'<loc>(.*?)</loc>', r.text)
                print(f'{url}: {len(urls)} URLs')
                if urls:
                    for u in urls[:3]: print(f'  {u}')
        except: pass

# Check if there's a course search API
print('\n--- Course search ---')
search_url = f'{DOMAIN}/study/search/'
r2 = curl.get(search_url, impersonate='chrome120', timeout=30)
if r2.status_code == 200:
    s2 = BeautifulSoup(r2.text, 'html.parser')
    h1 = s2.find('h1')
    print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
    links = set()
    for a in s2.find_all('a', href=True):
        h = a['href']
        if '/study/course/' in h.lower() or '/course/' in h.lower():
            links.add(h)
    print(f'Course links: {len(links)}')
    for l in sorted(list(links))[:10]: print(f'  {l}')
else:
    print(f'{search_url}: {r2.status_code}')

# Try course search API
print('\n--- Search API ---')
for q in ['?search=nursing&type=course', '?s=nursing&post_type=course', '?search=nursing',
          '?q=nursing&type=course']:
    url = f'{DOMAIN}/study/search{q}'
    try:
        r3 = curl.get(url, impersonate='chrome120', timeout=15)
        print(f'{q}: {r3.status_code}')
        if 'json' in r3.headers.get('content-type', ''):
            print(f'  JSON: {r3.text[:200]}')
    except: pass
    
# Try Curtin's alt domain: courses.curtin.edu.au
print('\n--- courses.curtin.edu.au ---')
for sub in ['courses.curtin.edu.au', 'study.curtin.edu.au', 'handbook.curtin.edu.au']:
    try:
        r4 = curl.get(f'https://{sub}', impersonate='chrome120', timeout=15)
        print(f'{sub}: {r4.status_code}, {len(r4.text)}b')
        h1 = BeautifulSoup(r4.text, 'html.parser').find('h1')
        print(f'  H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
    except Exception as e:
        print(f'{sub}: {str(e)[:50]}')
