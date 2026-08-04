"""Curtin courses subdomain deep."""
import sys, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://courses.curtin.edu.au'

# Check if there's a REST API
endpoints = [
    '/wp-json/wp/v2/pages?per_page=100',
    '/wp-json/wp/v2/courses',
    '/wp-json/',
    '/wp-json/wp/v2/types',
    '/wp-json/mimas/v1/courses',
    '/wp-json/mimas/v1/search',
    '/api/courses',
    '/graphql',
]

for ep in endpoints:
    try:
        r = curl.get(f'{DOMAIN}{ep}', impersonate='chrome120', timeout=15)
        ct = r.headers.get('content-type', '')
        if 'json' in ct and r.status_code == 200 and len(r.text) > 20:
            data = r.json()
            if isinstance(data, list):
                print(f'{ep}: {len(data)} items')
                if data and isinstance(data[0], dict):
                    print(f'  Keys: {list(data[0].keys())[:8]}')
            elif isinstance(data, dict):
                print(f'{ep}: dict with keys={list(data.keys())[:10]}')
                if 'routes' in data:
                    print(f'  Routes: {list(data["routes"].keys())[:10]}')
        else:
            print(f'{ep}: {r.status_code} {ct[:30]}')
    except Exception as e:
        print(f'{ep}: {str(e)[:50]}')

# Check the app.js for API endpoints
print('\n--- app.js API scan ---')
r2 = curl.get('https://s30991.pcdn.co/wp-content/themes/mimas/dist/js/app.js?ver=0981140f4c2f42ba8ae293709f2b3064', 
              impersonate='chrome120', timeout=15)
text = r2.text
for m in re.finditer(r'["\'](https?://[^"\']*(?:api|graphql|course|search)[^"\']*)["\']', text):
    print(f'  API: {m.group(1)[:120]}')
for m in re.finditer(r'["\'](/[^"\']*(?:api|graphql|course|search)[^"\']*)["\']', text):
    print(f'  Path: {m.group(1)[:120]}')
    
# The theme is 'mimas' - check if there's an offerings listing
print('\n--- Offerings / Courses search ---')
for path in ['/courses', '/study', '/search', '/offerings', '/programs']:
    try:
        r3 = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=15)
        if r3.status_code == 200:
            s3 = BeautifulSoup(r3.text, 'html.parser')
            h1 = s3.find('h1')
            hm = h1.get_text(strip=True)[:60] if h1 else 'none'
            # Count links
            links = len(s3.find_all('a', href=re.compile(r'course|degree|program')))
            print(f'{path}: {r3.status_code} H1={hm} links={links}')
            # Check for JSON in script
            for sc in s3.find_all('script'):
                if sc.string and ('wp.data' in sc.string or 'wp.api' in sc.string or 'courses' in sc.string):
                    print(f'  Script: {sc.string[:200]}')
                    break
    except Exception as e:
        print(f'{path}: {str(e)[:50]}')
