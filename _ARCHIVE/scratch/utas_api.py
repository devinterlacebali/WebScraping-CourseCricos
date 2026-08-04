"""UTas - find the actual course data."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.utas.edu.au'

# Check /courses/ page for JS data
r = curl.get(f'{DOMAIN}/courses/', impersonate='chrome120', timeout=30)
print(f'/courses/: {r.status_code}, {len(r.text)}b')

# Check for __NEXT_DATA__
if '__NEXT_DATA__' in r.text:
    m = re.search(r'__NEXT_DATA__\s*=\s*({.*?});', r.text, re.S)
    if m:
        data = json.loads(m.group(1))
        print('Next.js data found!')
        print(json.dumps(data, indent=2)[:500])

# Check for API calls in JS
for m in re.finditer(r'/api/([^"\'<>]+)', r.text):
    api = m.group(0)
    if 'course' in api.lower() or 'degree' in api or 'search' in api:
        print(f'API: {api}')

# Look for course data in scripts
soup = BeautifulSoup(r.text, 'html.parser')
for sc in soup.find_all('script'):
    if sc.string and any(kw in sc.string for kw in ['"courses"', '"degrees"', '"programs"', 'pageProps']):
        print(f'Script with course data ({len(sc.string)}b)')
        print(sc.string[:500])
        break

# Check if there's a graphql endpoint
for endpoint in ['/graphql', '/api/graphql']:
    try:
        r2 = curl.post(f'{DOMAIN}{endpoint}', impersonate='chrome120', timeout=10,
                      json={"query": "{ __schema { types { name } } }"})
        if r2.status_code == 200 and 'json' in r2.headers.get('content-type', ''):
            print(f'\n{endpoint}: GraphQL available')
            print(r2.text[:200])
    except: pass

# Try /courses/ navigate with Scrapling for JS rendering
from scrapling import Fetcher
ff = Fetcher()
r3 = ff.get(f'{DOMAIN}/courses/')
if r3.status == 200 and len(r3.text) > 1000:
    s3 = BeautifulSoup(r3.text, 'html.parser')
    body = re.sub(r'\s+', ' ', s3.get_text())
    links = [a['href'] for a in s3.find_all('a', href=True)]
    course_links = [l for l in links if any(k in l for k in ['/course/', '/study/'])]
    print(f'\nScrapling /courses/: {len(course_links)} course links')
    for l in course_links[:5]: print(f'  {l}')
