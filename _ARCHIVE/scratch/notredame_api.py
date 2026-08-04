"""Notre Dame - find API for fee data."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

# Check if there's an API endpoint
apis = [
    '/api/programs/3009',
    '/api/course/3009',
    '/__data/assets/json/3009',
    '/api/program/3009',
    '/program/3009.json',
    '/programs/school-of-nursing/undergraduate/bachelor-of-nursing.json',
]

for api in apis:
    r = curl.get(f'https://www.notredame.edu.au{api}', impersonate='chrome120', timeout=15)
    print(f'{api}: {r.status_code} ({len(r.text)}b)')
    if r.status_code == 200 and len(r.text) > 50:
        if 'application/json' in r.headers.get('content-type', ''):
            print(f'  JSON: {r.text[:300]}')

# Check page for embedded JSON
url = 'https://www.notredame.edu.au/programs/school-of-nursing/undergraduate/bachelor-of-nursing'
r = curl.get(url, impersonate='chrome120', timeout=30)
body = r.text

# Find all script tags and look for JSON
for m in re.finditer(r'<script[^>]*>(.*?)</script>', body, re.I | re.S):
    content = m.group(1).strip()
    if len(content) > 100 and ('{' in content or 'data' in content.lower()):
        print(f'Script tag ({len(content)}b): first 100 chars: {content[:100]}')
        # Check if it's JSON
        if content.strip().startswith('{') or content.strip().startswith('['):
            try:
                d = json.loads(content.strip())
                print(f'  Valid JSON! Keys: {list(d.keys())[:10] if isinstance(d, dict) else "array"}')
                if isinstance(d, dict) and ('fee' in str(d).lower() or 'price' in str(d).lower()):
                    print(f'  Fee-related JSON: {json.dumps(d)[:500]}')
            except: pass
