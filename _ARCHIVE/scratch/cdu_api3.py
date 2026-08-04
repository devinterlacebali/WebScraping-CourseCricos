"""CDU API discovery."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.cdu.edu.au'
headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
cookies = {"CDU_STUDENT_TYPE": "international"}

# Get all courses from API
r = curl.get(f'{DOMAIN}/api/courses', impersonate='chrome120', timeout=30, headers=headers)
data = r.json()
results = data.get('results', [])
print(f'Total API results: {len(results)}')

# Check first entry structure
if results:
    print(f'\nFirst entry keys: {list(results[0].keys())}')
    print(f'First entry: {json.dumps(results[0], indent=2)[:500]}')

# Find nursing courses
nursing = [c for c in results if 'nurs' in c.get('courseName', '').lower() or 'nurs' in c.get('courseCode', '').lower()]
print(f'\nNursing courses: {len(nursing)}')
for c in nursing[:3]:
    print(json.dumps(c, indent=2))
    
# Check for international fee fields
print('\n=== Looking for international/fee fields ===')
for c in results[:100]:
    for k, v in c.items():
        ks = k.lower()
        if any(kw in ks for kw in ['fee', 'cost', 'tuition', 'intl', 'international', 'price']):
            print(f'  {k}: {v} (in course {c.get("id","")})')

# Check for CRICOS field
print('\n=== Looking for CRICOS field ===')
for c in results[:100]:
    for k, v in c.items():
        if 'cricos' in k.lower():
            print(f'  {k}: {v} (in course {c.get("id","")})')

# Check nursing course details via API
print('\n=== Course detail API check ===')
for slug in ['wnurs1', 'wnurs', 'bachelor-nursing-wnurs1']:
    try:
        r2 = curl.get(f'{DOMAIN}/api/course/{slug}', impersonate='chrome120', timeout=10, headers=headers)
        if r2.json():
            data2 = r2.json()
            print(f'/api/course/{slug}: {len(data2)} entries')
            if len(data2) > 0:
                print(json.dumps(data2[0], indent=2)[:600])
    except:
        pass
