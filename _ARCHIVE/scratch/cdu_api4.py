"""CDU API - get all courses + detail."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.cdu.edu.au'
headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}

# Get all pages
all_results = []
for page in [1,2,3,4,5]:
    try:
        r = curl.get(f'{DOMAIN}/api/courses?page={page}', impersonate='chrome120', timeout=30, headers=headers)
        data = r.json()
        results = data.get('results', [])
        if not results: break
        all_results.extend(results)
        print(f'Page {page}: {len(results)} results')
    except:
        break

print(f'\nTotal: {len(all_results)} results')

# Check for nursing
nursing = [c for c in all_results if 'nurs' in c.get('courseName', '').lower() or 'nurs' in c.get('courseCode', '').lower()]
print(f'Nursing in results: {len(nursing)}')
for c in nursing:
    print(f'  {c}')

# Get all unique international course codes
intl_codes = set()
for c in all_results:
    for ic in c.get('internationalCodes', []):
        code = ic.get('courseCode', '')
        if code: intl_codes.add(code)
print(f'\nUnique international course codes: {len(intl_codes)}')
print(f'Sample: {list(intl_codes)[:10]}')

# Check if there's a program/fee API using internal codes
print('\n=== Fee API by internal code ===')
for code in list(intl_codes)[:5]:
    for path in [f'/api/course-fees/{code}', f'/api/fees/{code}', f'/api/program/{code}',
                 f'/api/course/{code}', f'/api/v2/courses/{code}']:
        try:
            r2 = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=10, headers=headers)
            ct = r2.headers.get('content-type', '')
            if r2.status_code == 200 and 'json' in ct:
                data2 = r2.json()
                if data2 and len(str(data2)) > 50:
                    print(f'  {path}: {str(data2)[:200]}')
        except:
            pass

# Check for single program detail
print('\n=== Try /api/courses with full detail ===')
r3 = curl.get(f'{DOMAIN}/api/courses?year=2026&full=true', impersonate='chrome120', timeout=30, headers=headers)
print(f'Full: {r3.status_code}, {r3.text[:300]}')
