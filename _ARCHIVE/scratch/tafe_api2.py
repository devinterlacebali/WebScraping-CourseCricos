"""TAFE NSW - explore API."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

API = 'https://api.tafensw.edu.au'
DOMAIN = 'https://www.tafensw.edu.au'

# Check API root
r = curl.get(API, impersonate='chrome120', timeout=15)
print(f'API root: {r.status_code}, {r.headers.get("content-type","")[:30]}')

# Try course endpoint
for path in ['/api/courses', '/api/v1/courses', '/api/course', '/api/search',
             '/api/course-areas']:
    r2 = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=15)
    ct = r2.headers.get('content-type', '')
    print(f'{path}: {r2.status_code} {ct[:30]} | {len(r2.text)}b')
    if 'json' in ct:
        data = r2.json()
        if isinstance(data, list):
            print(f'  List of {len(data)} items')
            if data: print(f'  Keys: {list(data[0].keys())[:10]}')
        elif isinstance(data, dict):
            print(f'  Keys: {list(data.keys())[:10]}')
        print(f'  {json.dumps(data)[:300]}')

# Try the API domain directly
print('\n=== api.tafensw.edu.au ===')
for path in ['/api/courses', '/api/search', '/api/course-areas', '/api/sitemap']:
    try:
        r3 = curl.get(f'{API}{path}', impersonate='chrome120', timeout=15)
        ct = r3.headers.get('content-type', '')
        print(f'{path}: {r3.status_code} {ct[:30]} | {len(r3.text)}b')
        if 'json' in ct and len(r3.text) < 50000:
            data = r3.json()
            if isinstance(data, list):
                print(f'  {len(data)} items')
                if data and isinstance(data[0], dict):
                    print(f'  keys: {list(data[0].keys())[:10]}')
                print(f'  Snippet: {json.dumps(data)[:300]}')
            elif isinstance(data, dict):
                print(f'  keys: {list(data.keys())[:10]}')
                print(f'  Snippet: {json.dumps(data)[:300]}')
    except Exception as e:
        print(f'{path}: ERROR {str(e)[:40]}')

# Check if course data is searchable
print('\n=== Search nursing courses ===')
for q in ['nursing', 'diploma of nursing']:
    for ep in [f'{API}/api/search?q={q}', f'{API}/api/courses?q={q}',
               f'{DOMAIN}/api/search?q={q}']:
        try:
            r4 = curl.get(ep, impersonate='chrome120', timeout=15)
            if r4.status_code == 200 and len(r4.text) > 10:
                print(f'{ep}: {r4.status_code} | {r4.text[:200]}')
        except: pass
