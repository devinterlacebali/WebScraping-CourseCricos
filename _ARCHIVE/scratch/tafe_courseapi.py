"""TAFE NSW - explore course data from API."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.tafensw.edu.au'

# Get healthcare area
r = curl.get(f'{DOMAIN}/api/course-areas/healthcare', impersonate='chrome120', timeout=30)
data = r.json()
print(f'Keys: {list(data.keys())}')
print(json.dumps(data, indent=2)[:2000])

# Check if courses are embedded
if 'courses' in data:
    courses = data['courses']
    print(f'\nCourses: type {type(courses).__name__}')
    if isinstance(courses, list):
        print(f'  Count: {len(courses)}')
        for c in courses[:3]:
            print(f'  {json.dumps(c)[:300]}')
    elif isinstance(courses, dict):
        print(f'  Keys: {list(courses.keys())[:10]}')
        print(f'  {json.dumps(courses)[:500]}')

# Try to get individual course data
for ep in ['/api/courses/HLT54121-01', '/api/course/HLT54121-01',
           '/api/courses/diploma-of-nursing--HLT54121-01',
           '/api/course-detail/HLT54121-01',
           '/api/course/detail/HLT54121-01']:
    r2 = curl.get(f'{DOMAIN}{ep}', impersonate='chrome120', timeout=10)
    ct = r2.headers.get('content-type', '')
    if r2.status_code == 200 and 'json' in ct:
        print(f'\n{ep}: 200')
        print(r2.text[:500])
        break
