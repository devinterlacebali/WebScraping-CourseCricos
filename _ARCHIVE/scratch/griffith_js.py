"""Find Griffith Vue app API by examining JS bundles."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

url = 'https://www.griffith.edu.au/study/degrees/bachelor-of-nursing-2036'
r = curl.get(url, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')

# Find all JS script src
js_urls = []
for s in soup.find_all('script'):
    src = s.get('src', '')
    if src:
        if not src.startswith('http'):
            src = 'https://www.griffith.edu.au' + src if src.startswith('/') else 'https://www.griffith.edu.au/' + src
        js_urls.append(src)
    elif s.string and len(s.string) > 500:
        # Inline scripts - look for API base URL or fetch calls
        for m in re.finditer(r'["\'`](https?://[^"\'`]+(?:api|graphql|service|program|degree)[^"\'`]*)["\'`]', s.string, re.I):
            print(f'  Inline API: {m.group(1)}')
        for m in re.finditer(r'fetch\(["\'`]([^"\'`]+)["\'`\)]', s.string):
            print(f'  fetch(): {m.group(1)}')
        for m in re.finditer(r'axios\.(?:get|post)\(["\'`]([^"\'`]+)["\'`\)]', s.string):
            print(f'  axios: {m.group(1)}')
        for m in re.finditer(r'baseURL[:=]\s*["\'`]([^"\'`]+)["\'`]', s.string):
            print(f'  baseURL: {m.group(1)}')

print(f'\nJS bundles loaded: {len(js_urls)}')
# Fetch a few key JS bundles and search for API paths
fetched = set()
for js in js_urls[:10]:
    if js in fetched or '.js' not in js: continue
    fetched.add(js)
    try:
        r2 = curl.get(js, impersonate='chrome120', timeout=15)
        if r2.status_code == 200 and len(r2.text) > 1000:
            # Search for API routes
            for m in re.finditer(r'["\'`](/api/[^"\'`]+)["\'`]', r2.text):
                api_path = m.group(1)
                if 'search' in api_path.lower() or 'program' in api_path.lower() or 'degree' in api_path.lower() or 'course' in api_path.lower():
                    print(f'  [{js.split("/")[-1][:30]}]: {api_path}')
            # Search for URL patterns
            for m in re.finditer(r'["\'`](https?://programs?[^"\'`]+)["\'`]', r2.text):
                print(f'  [{js.split("/")[-1][:30]}]: program URL: {m.group(1)[:100]}')
    except:
        pass

# Also check if there's a nuxt.config / vue config
for path in ['/nuxt.config.js', '/vue.config.js', '/config.js', '/app.config.js']:
    r3 = curl.get(f'https://www.griffith.edu.au{path}', impersonate='chrome120', timeout=10)
    if r3.status_code == 200:
        print(f'\nFound config: {path}')

# Check if there's a JSON file with courses in the HTML
for s in soup.find_all('script', type=re.compile(r'json', re.I)):
    if s.string:
        print(f'\nJSON script ({len(s.string)}b): {s.string[:200]}')
