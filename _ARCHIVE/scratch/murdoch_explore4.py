"""Murdoch - check API endpoints and data loading."""
import requests, re, json, sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

# Check the /study/courses page
url = 'https://www.murdoch.edu.au/study/courses'
r = S.get(url, timeout=30, allow_redirects=True)
text = r.text
print(f'/study/courses: {r.status_code}, {len(text)} bytes')

# Find course links  
print('\n=== Course links on /study/courses ===')
for m in re.finditer(r'href=["\'](/course/[^"\']+)["\']', text):
    print(f'  {m.group(1)}')

# Check for JSON data blocks
print('\n=== JSON data blocks ===')
for m in re.finditer(r'<script[^>]+type="application/json"[^>]*>(.*?)</script>', text, re.DOTALL):
    c = m.group(1).strip()
    if len(c) > 50:
        print(f'  Found {len(c)} chars: {c[:200]}...')

# Check the explore REST API
print('\n=== REST API endpoints ===')
api_urls = [
    'https://www.murdoch.edu.au/api/courses',
    'https://www.murdoch.edu.au/api/course/find',
    'https://www.murdoch.edu.au/restapi/courses',
    'https://www.murdoch.edu.au/sitefinity/public/demo/courses',
]
for api_url in api_urls:
    try:
        r2 = S.get(api_url, timeout=15)
        print(f'{api_url}: {r2.status_code} ({len(r2.text)} bytes) {r2.text[:200]}')
    except Exception as e:
        print(f'{api_url}: ERROR {e}')

# Try a course detail page and see if there's hidden API data
print('\n=== Check for Sitefinity REST API pattern ===')
test_url = 'https://www.murdoch.edu.au/course/Undergraduate/mj-cams'
r3 = S.get(test_url, timeout=30)
# Look for REST API calls in the page
for m in re.finditer(r'(/api/[a-zA-Z0-9/_-]+)', r3.text):
    print(f'  API call: {m.group(1)}')

# Look for fetch/ajax calls
for m in re.finditer(r'["\']/(?:api|rest|odata)/[^"\']+["\']', r3.text):
    print(f'  AJAX: {m.group(0)}')

# Look for Sitefinity service URLs
for m in re.finditer(r'Sitefinity[^"\']*["\']?:\s*["\']([^"\']+)["\']', r3.text):
    print(f'  SF: {m.group(1)}')
