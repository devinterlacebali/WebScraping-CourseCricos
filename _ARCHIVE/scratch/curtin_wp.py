"""Curtin - WP REST API."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

DOMAIN = 'https://www.curtin.edu.au'

# WordPress REST API endpoints
endpoints = [
    '/wp-json/wp/v2/pages',
    '/wp-json/wp/v2/courses',
    '/wp-json/wp/v2/degrees',
    '/wp-json/wp/v2/programs',
    '/wp-json/wp/v2/study',
    '/wp-json/wp/v2/posts?categories=courses',
    '/wp-json/wp/v2/pages?slug=study/courses',
    '/wp-json/',  # root discovery
]

for ep in endpoints:
    try:
        r = curl.get(f'{DOMAIN}{ep}', impersonate='chrome120', timeout=15)
        if 'json' in r.headers.get('content-type', '') and r.status_code == 200:
            data = r.json()
            if isinstance(data, list):
                print(f'{ep}: {len(data)} items')
                if data:
                    keys = list(data[0].keys()) if isinstance(data[0], dict) else []
                    print(f'  Keys: {[k for k in keys if not k.startswith("_")][:8]}')
                    if 'slug' in data[0]:
                        for item in data[:3]:
                            print(f'  slug={item.get("slug","")}, title={item.get("title",{}).get("rendered","")}')
            elif isinstance(data, dict):
                print(f'{ep}: dict with keys={list(data.keys())[:8]}')
    except Exception as e:
        ep_clean = ep.split('/')[-1]
        print(f'{ep}: {str(e)[:50]}')

# Also check if there is a custom post type for courses
# Try common patterns
r2 = curl.get(f'{DOMAIN}/wp-json/wp/v2/types', impersonate='chrome120', timeout=15)
if r2.status_code == 200:
    types = r2.json()
    print(f'\nPost types: {list(types.keys())[:15]}')
    for t, info in types.items():
        if any(kw in t.lower() for kw in ['course', 'degree', 'program', 'study']):
            print(f'  {t}: {info.get("name","")} - {info.get("rest_base","")}')
            
# Check for course listing via JavaScript
r3 = curl.get(f'{DOMAIN}/study/courses/', impersonate='chrome120', timeout=30)
s3 = BeautifulSoup(r3.text, 'html.parser')
print(f'\n--- /study/courses/ (with trailing slash) ---')
print(f'H1: {s3.find("h1").get_text(strip=True)[:60] if s3.find("h1") else "none"}')
# Check if there's search/filter elements
els = s3.find_all(string=re.compile(r'courses|filter|search', re.I))
print(f'Mentions courses/filter/search: {len(els)}')
for el in els[:3]:
    print(f'  {el[:100]}')
