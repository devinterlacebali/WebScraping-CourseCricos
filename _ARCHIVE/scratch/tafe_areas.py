"""TAFE NSW - explore course-areas API."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.tafensw.edu.au'

# Get all course areas
r = curl.get(f'{DOMAIN}/api/course-areas', impersonate='chrome120', timeout=30)
data = r.json()
areas = data.get('courseAreas', [])
print(f'Course areas: {len(areas)}')

# Show first 3
for a in areas[:3]:
    print(f'\n  {a["id"]} — {a["name"]}')
    print(f'  Desc: {a["description"][:100]}')
    print(f'  Keys: {list(a.keys())}')
    if 'courses' in a:
        print(f'  Courses: {len(a["courses"])}')
        for c in a['courses'][:3]:
            print(f'    {json.dumps(c)[:200]}')

# Find nursing area
print(f'\n=== Nursing area ===')
for a in areas:
    if 'nurs' in a['id'].lower() or 'health' in a['id'].lower():
        print(f'\n  {a["id"]} — {a["name"]}')
        print(f'  Keys: {list(a.keys())}')
        # Try to get specific area
        r2 = curl.get(f'{DOMAIN}/api/course-areas/{a["id"]}', impersonate='chrome120', timeout=15)
        if r2.status_code == 200:
            d2 = r2.json()
            print(f'  Area detail keys: {list(d2.keys())[:10]}')
            print(f'  Snippet: {json.dumps(d2)[:500]}')
        break

# Check if course-areas/{id}/courses exists
print(f'\n=== Courses per area ===')
for area_id in ['healthcare']:
    for ep in [f'/api/course-areas/{area_id}/courses',
               f'/api/course-areas/{area_id}/course',
               f'/api/courses?area={area_id}',
               f'/api/course-area/{area_id}']:
        r3 = curl.get(f'{DOMAIN}{ep}', impersonate='chrome120', timeout=10)
        ct = r3.headers.get('content-type', '')
        if r3.status_code == 200 and 'json' in ct:
            print(f'{ep}: 200 | {r3.text[:200]}')
        elif r3.status_code != 404:
            print(f'{ep}: {r3.status_code}')
