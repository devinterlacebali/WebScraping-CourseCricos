"""CDU - check course detail API formats."""
import sys, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.cdu.edu.au'
headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}

# Try program/course detail with different ID formats
# Bachelor of Nursing internal code is likely: BNSG, BSCN, WNURS, etc.
ids = ['wnurs1', 'WNURS1', 'BNSG', 'BNSING', 'BSCNURS', 'BHSCNURS', 'BNURSE']
for cid in ids:
    for ep in ['/api/course/', '/api/program/']:
        try:
            r = curl.get(f'{DOMAIN}{ep}{cid}', impersonate='chrome120', timeout=10, headers=headers)
            if len(r.text) > 10 and r.status_code == 200:
                data = r.json()
                print(f'{ep}{cid}: {len(str(data))}b')
                if data:
                    print(f'  {json.dumps(data[0] if isinstance(data,list) else data, indent=2)[:500]}')
        except: pass

# Check the sitemap course codes - extract from URL slugs
# Bachelor of Nursing = bachelor-nursing-wnurs1 -> code = wnurs1
print('\n--- Checking course API with course code from sitemap ---')
r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
import re
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
course_urls = [u for u in urls if '/study/course/' in u.lower()]
for u in course_urls[:3]:
    slug = u.rstrip('/').split('/')[-1]
    parts = slug.rsplit('-', 1)
    code = parts[-1] if len(parts) > 1 else slug
    print(f'URL: {slug} -> code: {code}')
    try:
        r2 = curl.get(f'{DOMAIN}/api/course/{code}', impersonate='chrome120', timeout=10, headers=headers)
        print(f'  /api/course/{code}: {r2.status_code}, {r2.text[:200]}')
    except Exception as e:
        print(f'  Error: {e}')
