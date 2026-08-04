"""Curtin handbook - find API."""
import sys, json, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

url = 'https://handbook.curtin.edu.au/courses/course-ug-bachelor-of-science-nursing--b-nursv8'
r = curl.get(url, impersonate='chrome120', timeout=30)

# Check for Next.js data
if '__NEXT_DATA__' in r.text:
    m = re.search(r'__NEXT_DATA__\s*=\s*({.*?});', r.text, re.S | re.I)
    if m:
        data = json.loads(m.group(1))
        print('Next.js data found!')
        props = data.get('props', {}).get('pageProps', {})
        print(f'PageProps keys: {list(props.keys())[:15]}')
        if 'course' in props:
            print(json.dumps(props['course'], indent=2)[:1000])
        if 'program' in props:
            print(json.dumps(props['program'], indent=2)[:1000])
        print('\nFull props (first 2000 chars):')
        print(json.dumps(props, indent=2)[:2000])

# Also check for fetch calls to API
print('\n=== API endpoints in page ===')
for m in re.finditer(r'https?://[^"\'<>]*(?:api|graphql|v1|v2|course)[^"\'<>]*', r.text):
    print(f'  {m.group()[:120]}')

# Check for graphql endpoint
print('\n=== GraphQL check ===')
r2 = curl.post('https://handbook.curtin.edu.au/api/graphql', 
               impersonate='chrome120', timeout=15,
               json={"query": "{ courses { nodes { id title } } }"})
print(f'graphql: {r2.status_code}, {r2.text[:200]}')

# Try known Curtin API pattern
print('\n=== Known API patterns ===')
for path in ['/api/course/b-nursv8', '/api/courses/b-nursv8', '/api/program/b-nursv8',
             '/api/v1/courses/b-nursv8']:
    try:
        r3 = curl.get(f'https://handbook.curtin.edu.au{path}', impersonate='chrome120', timeout=10,
                      headers={'Accept': 'application/json'})
        ct = r3.headers.get('content-type', '')
        if 'json' in ct or r3.status_code == 200:
            print(f'{path}: {r3.status_code} {r3.text[:200]}')
    except: pass
