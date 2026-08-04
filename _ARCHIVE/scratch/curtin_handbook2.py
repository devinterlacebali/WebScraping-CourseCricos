"""Curtin handbook - find courses."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
import re

# Get all handbook URLs
r = curl.get('https://handbook.curtin.edu.au/sitemap.xml', impersonate='chrome120', timeout=60)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
print(f'Total URLs: {len(urls)}')

# Filter for courses (not units)
course_urls = [u for u in urls if '/courses/' in u.lower()]
unit_urls = [u for u in urls if '/units/' in u.lower()]
other_urls = [u for u in urls if '/courses/' not in u.lower() and '/units/' not in u.lower()]

print(f'Course URLs: {len(course_urls)}')
print(f'Unit URLs: {len(unit_urls)}')
print(f'Other: {len(other_urls)}')

# Show some course URLs
for u in course_urls[:10]:
    print(f'  {u}')
    
# Also check the search API with correct format
print('\n=== Curtin Funnelback search ===')
# The search.curtin.edu.au returned HTML but the collection might work
for collection in ['curtin~sp-courses', 'curtin~sp-units', 'curtin~web']:
    try:
        r2 = curl.get(f'https://search.curtin.edu.au/s/search.json?collection={collection}&q=nursing',
                      impersonate='chrome120', timeout=15)
        ct = r2.headers.get('content-type', '')
        print(f'{collection}: {r2.status_code} {ct[:30]}')
        if 'json' in ct:
            data = r2.json()
            results = data.get('response', {}).get('resultPacket', {}).get('results', [])
            print(f'  Results: {len(results)}')
            for res in results[:2]:
                print(f'  Title: {res.get("title", "")[:60]}')
    except Exception as e:
        print(f'{collection}: {str(e)[:50]}')
