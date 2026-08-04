"""Curtin - try handbooks and search API."""
import sys, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://courses.curtin.edu.au'

# Check handbook.curtin.edu.au
print('=== handbook.curtin.edu.au ===')
r = curl.get('https://handbook.curtin.edu.au/', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')
h1 = s.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
has_next = '__NEXT_DATA__' in r.text
has_nuxt = '__NUXT__' in r.text
print(f'Next.js: {has_next}, Nuxt: {has_nuxt}')

# Check for sitemap
for sm in ['/sitemap.xml', '/sitemap-index.xml', '/courses-sitemap.xml']:
    r2 = curl.get(f'https://handbook.curtin.edu.au{sm}', impersonate='chrome120', timeout=15)
    if r2.status_code == 200:
        urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
        print(f'  {sm}: {len(urls)} URLs')
        if urls:
            for u in urls[:3]: print(f'    {u}')
    else:
        print(f'  {sm}: {r2.status_code}')

# Check courses page for __NEXT_DATA__
r3 = curl.get('https://handbook.curtin.edu.au/courses', impersonate='chrome120', timeout=30)
if 'pageProps' in r3.text or '__NEXT_DATA__' in r3.text:
    print(f'\n/courses: Next.js detected!')
    # Try to parse __NEXT_DATA__
    m = re.search(r'__NEXT_DATA__\s*=\s*({.*?});', r3.text, re.S)
    if m:
        try:
            data = json.loads(m.group(1))
            if 'props' in data:
                print(f'  Props keys: {list(data["props"].keys())[:5]}')
        except: pass

# Try search API
print('\n=== Search API ===')
for q in ['nursing', 'bachelor', 'master']:
    for url in [f'{DOMAIN}/wp-json/mimas/v1/search?q={q}',
                f'https://search.curtin.edu.au/s/search.json?collection=curtin~sp-courses&q={q}']:
        try:
            r4 = curl.get(url, impersonate='chrome120', timeout=15)
            ct = r4.headers.get('content-type', '')
            print(f'{url}: {r4.status_code} {ct[:30]}')
            if 'json' in ct and len(r4.text) > 10:
                data = r4.json()
                if isinstance(data, dict):
                    for k, v in list(data.items())[:5]:
                        v_str = str(v)[:100]
                        print(f'  {k}: {v_str}')
        except Exception as e:
            print(f'{url}: {str(e)[:50]}')
