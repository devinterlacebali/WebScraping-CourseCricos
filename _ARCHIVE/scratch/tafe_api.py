"""TAFE NSW - find API endpoint used by Nuxt."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.tafensw.edu.au'

# Get course page and look for API calls in JS
r = curl.get(f'{DOMAIN}/course-areas/healthcare/courses/diploma-of-nursing--HLT54121-01', impersonate='chrome120', timeout=30)

# Look for API patterns in the page HTML
api_patterns = re.findall(r'(https?://[^"\'<>]*?(?:api|graphql|course|search|nuxt|_nuxt|__data|content|v1|v2|rest)[^"\'<>]*)', r.text)
print(f'API-like URLs in page: {len(set(api_patterns))}')
for u in sorted(set(api_patterns))[:15]:
    print(f'  {u}')

# Check the JS files for API calls
js_patterns = re.findall(r'(/_nuxt/[^"\'<>]*)', r.text)
print(f'\nNuxt JS files: {len(js_patterns)}')
for j in sorted(set(js_patterns))[:5]:
    print(f'  {j}')
    # Fetch JS file and look for API endpoints
    r2 = curl.get(f'{DOMAIN}{j}', impersonate='chrome120', timeout=15)
    endpoints = re.findall(r'(https?://[^"\'<>\\\\]*?(?:api|course|graphql|search|content)[^"\'<>\\\\]*)', r2.text)
    for ep in endpoints[:10]:
        print(f'    Endpoint: {ep[:130]}')

# Try common Nuxt API patterns
print('\n=== Common API checks ===')
for path in ['/api/course/diploma-of-nursing--HLT54121-01',
             '/api/v1/courses/HLT54121-01',
             '/api/courses/HLT54121-01',
             '/api/course-areas/healthcare']:
    r3 = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=10)
    ct = r3.headers.get('content-type', '')
    if r3.status_code == 200 or 'json' in ct:
        print(f'{path}: {r3.status_code} {ct[:30]}')
        print(f'  {r3.text[:200]}')
