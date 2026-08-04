"""CDU - try common API patterns."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.cdu.edu.au'
headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
cookies = {"CDU_STUDENT_TYPE": "international"}

# Try common API patterns
paths = [
    '/api/courses',
    '/api/v1/courses',
    '/api/course/wnurs1',
    '/api/fees/wnurs1',
    '/api/course-fees/wnurs1',
    '/api/course/bachelor-nursing-wnurs1',
    '/api/study/course/bachelor-nursing-wnurs1',
    '/data/courses/wnurs1.json',
]

for path in paths:
    try:
        r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=10, headers=headers)
        ct = r.headers.get('content-type', '')
        print(f'{path}: {r.status_code} {ct[:30]} | {r.text[:100]}')
    except Exception as e:
        print(f'{path}: ERROR {str(e)[:50]}')

print('\n--- Try alternative: check if international page has different CSS class data ---')
r = curl.get(f'{DOMAIN}/study/course/bachelor-nursing-wnurs1', impersonate='chrome120', timeout=20, cookies=cookies)
# Check for JSON in script with ID
import re
for m in re.finditer(r'__NUXT__|window\.__DATA__|window\.initialState|window\.config', r.text):
    print(f'  Found: {m.group()[:50]}')
