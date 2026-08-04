"""Notre Dame - find where CRICOS is actually stored."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

url = 'https://www.notredame.edu.au/programs/school-of-nursing/undergraduate/bachelor-of-nursing'
r = curl.get(url, impersonate='chrome120', timeout=30)
body = r.text

# Search raw HTML for 015324A
for m in re.finditer('015324A', body):
    ctx = body[max(0,m.start()-100):m.end()+100]
    print('015324A ctx:')
    print(re.sub(r'\s+', ' ', ctx))
    print()

# Find all meta tags
for m in re.finditer(r'<meta[^>]*>', body, re.I):
    tag = m.group()
    if 'CRICOS' in tag.upper() or '015324A' in tag or '01032F' in tag:
        print('Meta:', re.sub(r'\s+', ' ', tag)[:200])
        print()

# Search for the CRICOS number near provider code 01032F
pat = r'01032F.{0,500}015324A'
m = re.search(pat, body, re.I | re.S)
if m:
    print('Provider + CRICOS:')
    print(re.sub(r'\s+', ' ', m.group())[:300])
