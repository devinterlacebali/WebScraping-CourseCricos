"""CDU - find fee API endpoint."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = "https://www.cdu.edu.au"
url = "https://www.cdu.edu.au/study/course/bachelor-nursing-wnurs1"
r = curl.get(url, impersonate='chrome120', timeout=20, cookies={"CDU_STUDENT_TYPE": "international"})
soup = BeautifulSoup(r.text, 'html.parser')

# Search for JS that fetches course data
print('=== Scripts with fetch/ajax calls ===')
for sc in soup.find_all('script'):
    if not sc.string: continue
    txt = sc.string
    if any(kw in txt for kw in ['fetch(', '$.ajax', 'axios', 'xhr', 'XMLHttpRequest']):
        print(f'Found {len(txt)}b script with fetch/ajax')
        # Extract URL endpoints
        for m in re.finditer(r'["\'](https?://[^"\']*api[^"\']*)["\']', txt):
            print(f'  API URL: {m.group(1)[:120]}')
        for m in re.finditer(r'["\'](/api/[^"\']*)["\']', txt):
            print(f'  API path: {m.group(1)[:120]}')
        break

# Check for all.js / app.js bundles
for sc in soup.find_all('script', src=True):
    src = sc['src']
    if any(kw in src for kw in ['app', 'main', 'bundle', 'vendor', 'chunk']):
        url2 = src if src.startswith('http') else f'{DOMAIN}{src}'
        try:
            r2 = curl.get(url2, impersonate='chrome120', timeout=10)
            if 'fetch' in r2.text or 'api' in r2.text or 'graphql' in r2.text:
                print(f'\n=== {src} ===')
                for m in re.finditer(r'["\'](https?://[^"\']*(?:api|graphql|fee|course|tuition)[^"\']*)["\']', r2.text):
                    print(f'  Endpoint: {m.group(1)[:120]}')
                for m in re.finditer(r'["\'](/[^"\']*(?:api|graphql|fee|course|tuition)[^"\']*)["\']', r2.text):
                    print(f'  Path: {m.group(1)[:120]}')
        except:
            pass

# Check for course codes in page
print('\n=== Course code patterns ===')
course_codes = re.findall(r'(?:wnurs|w[a-z]{4}\d)', r.text)
print(f'Course codes: {set(course_codes)}')

# Check for data-course element
print('\n=== data attributes ===')
for el in soup.find_all():
    for attr in el.attrs:
        if 'course' in attr.lower():
            val = str(el[attr])[:200]
            print(f'  <{el.name}> {attr}={val}')
