"""CDU - search for fee in JS bundles."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.cdu.edu.au'
url = 'https://www.cdu.edu.au/study/course/bachelor-nursing-wnurs1'
r = curl.get(url, impersonate='chrome120', timeout=20, cookies={"CDU_STUDENT_TYPE": "international"})
soup = BeautifulSoup(r.text, 'html.parser')

# Find all external JS files
print('=== JS bundles ===')
for sc in soup.find_all('script', src=True):
    src = sc['src']
    if any(kw in src for kw in ['app', 'main', 'runtime', 'chunk', 'vendor']):
        print(f'  {src.split("/")[-1] if "/" in src else src}')

# Download and scan the main app bundle for API endpoints
print('\n=== Searching app bundle for fee API ===')
for sc in soup.find_all('script', src=True):
    src = sc['src']
    if 'app.' in src or 'main.' in src or 'runtime' in src:
        url2 = src if src.startswith('http') else f'{DOMAIN}{src}'
        try:
            r2 = curl.get(url2, impersonate='chrome120', timeout=15)
            text = r2.text
            for m in re.finditer(r'["\'](https?://[^"\']*(?:api|fee|intl|tuition)[^"\']*)["\']', text):
                print(f'  API URL: {m.group(1)[:120]}')
            for m in re.finditer(r'["\'](/[^"\']*(?:api|fee|intl|tuition)[^"\']*)["\']', text):
                print(f'  Path: {m.group(1)[:120]}')
            # Search for 'international' or 'domestic' in the bundle
            if 'international' in text and 'fee' in text:
                # Find the relevant section
                idx = text.find('international')
                print(f'\n  Bundle context around "international": {text[max(0,idx-50):idx+200][:300]}')
        except:
            pass
        
# Check for __NEXT_DATA__ or SSR data
print('\n=== Checking for embedded JSON data ===')
for sc in soup.find_all('script', type='application/json'):
    if sc.string:
        print(f'  JSON script ({len(sc.string)}b): {sc.string[:200]}')

# Try gql endpoint  
for path in ['/graphql', '/api/graphql']:
    try:
        r3 = curl.post(f'{DOMAIN}{path}', impersonate='chrome120', timeout=10,
                      json={"query": "{ courses { id name fee international } }"})
        print(f'{path}: {r3.status_code}')
        if r3.status_code == 200:
            print(f'  {r3.text[:200]}')
    except:
        pass
