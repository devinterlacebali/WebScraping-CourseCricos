"""Find Griffith API by examining Vue app JS bundles."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

# Get page and extract JS bundle URLs
r = curl.get('https://www.griffith.edu.au/study/degrees/bachelor-of-nursing-2036', impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')

js_urls = [s.get('src') for s in soup.find_all('script') if s.get('src')]
print(f'JS bundles: {len(js_urls)}')

# Fetch all JS bundles and search for API patterns
api_patterns_found = set()
for js_src in js_urls:
    if not js_src.startswith('http'):
        js_src = 'https://www.griffith.edu.au' + js_src
    try:
        r2 = curl.get(js_src, impersonate='chrome120', timeout=15)
        if r2.status_code != 200: continue
        # Search for API URL patterns
        for m in re.finditer(r'["\']([^"\']*api[^"\']*program[^"\']*)["\']', r2.text, re.I):
            api_patterns_found.add(m.group(1))
        for m in re.finditer(r'["\']([^"\']*program[^"\']*search[^"\']*)["\']', r2.text, re.I):
            api_patterns_found.add(m.group(1))
        for m in re.finditer(r'["\'](https?://[^"\']*griffith[^"\']*(?:api|service|graphql|v1|v2)[^"\']*)["\']', r2.text, re.I):
            api_patterns_found.add(m.group(1))
        for m in re.finditer(r'axios\s*[=:].*?baseURL["\']?\s*[:=]\s*["\']([^"\']+)["\']', r2.text, re.I):
            api_patterns_found.add(m.group(1))
        for m in re.finditer(r'baseUrl\s*[=:]\s*["\']([^"\']+)["\']', r2.text, re.I):
            api_patterns_found.add(m.group(1))
        for m in re.finditer(r'fetch\(["\']([^"\']+(?:api|program|degree|course)[^"\']+)["\']', r2.text, re.I):
            api_patterns_found.add(m.group(1))
    except: pass

print(f'\nAPI patterns found: {len(api_patterns_found)}')
for p in sorted(api_patterns_found):
    print(f'  {p}')

# Try some common API patterns
print('\n=== Trying APIs ===')
api_tests = [
    '/__data/assets/json/programs.json',
    '/study/degrees/_jcr_content.json',
    '/study/degrees/_jcr_content/programs.json',
    '/api/programs',
    '/programs/api/programs',
    '/api/v1/programs',
    '/api/v1/degrees',
    '/api/v1/courses',
    '/griffith-api/programs',
    '/griffith-api/degrees',
    '/__data/assets/json/degrees.json',
    '/api/programs/search?keywords=bachelor',
]
for path in api_tests:
    u = f'https://www.griffith.edu.au{path}'
    r2 = curl.get(u, impersonate='chrome120', timeout=10)
    ct = r2.headers.get('content-type', '')
    print(f'  {path}: {r2.status_code}, {len(r2.text)}b, {ct[:30]}')
    if r2.status_code == 200 and 'json' in ct and len(r2.text) > 100:
        try:
            data = json.loads(r2.text)
            if isinstance(data, list) and len(data) > 0:
                print(f'    List of {len(data)} items')
                if isinstance(data[0], dict):
                    print(f'    First keys: {list(data[0].keys())[:10]}')
        except: pass
