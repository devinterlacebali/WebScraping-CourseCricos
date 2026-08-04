"""Notre Dame - debug raw HTML for CRICOS."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

url = 'https://www.notredame.edu.au/programs/school-of-nursing/undergraduate/bachelor-of-nursing'
r = curl.get(url, impersonate='chrome120', timeout=30)
body = r.text
print(f'Status: {r.status_code}, Size: {len(body)}')

# Search for ANY 6-digit + letter pattern
codes = re.findall(r'\b\d{6,7}[A-Za-z]\b', body)
# Filter out hex colors (6 char hex + potentially alpha)
real_codes = []
for c in codes:
    # Check context
    idx = body.index(c)
    ctx = body[max(0,idx-30):idx+30]
    if not re.search(r'#[0-9a-fA-F]|color:|opacity|margin|padding', ctx, re.I):
        real_codes.append(c)

print(f'All potential CRICOS codes: {codes[:20]}')
print(f'Real CRICOS candidates: {real_codes[:20]}')

# Also search for "CRICOS Code:" pattern
for m in re.finditer(r'CRICOS.{0,60}', body, re.I):
    txt = re.sub(r'\s+', ' ', body[m.start():m.end()])
    print(f'CRICOS text: [{txt.strip()}]')
    if m.end() - m.start() > len(txt):
        print('  (truncated)')
