"""Notre Dame - find where 015324A is in raw HTML."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

url = 'https://www.notredame.edu.au/programs/arts-and-sciences/undergraduate/bachelor-of-arts-major-social-justice'
r = curl.get(url, impersonate='chrome120', timeout=30)
body = r.text

# Find ALL occurrences of 015324A
for m in re.finditer('015324A', body):
    idx = m.start()
    ctx = body[max(0,idx-200):idx+200]
    print(f'Position {idx}:')
    print(re.sub(r'\s+', ' ', ctx))
    print(f'---')
    # Find surrounding tag
    tag_start = body.rfind('<', idx-200, idx)
    tag_end = body.find('>', idx, idx+200)
    if tag_start >= 0 and tag_end >= 0:
        tag = body[tag_start:tag_end+1]
        print(f'Tag: {tag[:300]}')
    print()
