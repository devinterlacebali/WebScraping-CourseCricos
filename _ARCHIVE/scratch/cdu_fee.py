"""CDU fee format deep check."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

url = 'https://www.cdu.edu.au/study/course/bachelor-nursing-wnurs1'
r = curl.get(url, impersonate='chrome120', timeout=20, cookies={"CDU_STUDENT_TYPE": "international"})
soup = BeautifulSoup(r.text, 'html.parser')

# Check script tags for JSON data
for i, sc in enumerate(soup.find_all('script')):
    if sc.string and any(kw in sc.string.lower() for kw in ['fee', 'tuition', 'cricos', 'aud']):
        print(f'=== Script {i} ({len(sc.string)}b) ===')
        print(sc.string[:600])
        print('...')
        break

# Search for dollar amounts in raw HTML
print('\nDollar amounts > 1000:')
for m in re.finditer(r'\$\s*[0-9,]{4,}', r.text):
    ctx = r.text[max(0,m.start()-40):m.end()+40]
    print(f'  {m.group()} in: {ctx.strip()[:120]}')

# CRICOS in raw HTML
print(f'\nCRICOS in raw HTML: {bool(re.search(r"CRICOS", r.text))}')

# Check fee section
fee_sec = soup.find(string=re.compile(r'International tuition', re.I))
if fee_sec:
    parent = fee_sec.parent
    print(f'\nFee section parent: {parent.get_text()[:200]}')
else:
    print('\nNo International tuition text found')
    print(f'  International: {"International" in r.text}')
    print(f'  tuition: {"tuition" in r.text}')
    print(f'  Fees: {"Fees" in r.text}')
    
# Check if the international data is loaded via JS
print('\n--- Looking for course data in window.__INITIAL_STATE__ or similar ---')
for sc in soup.find_all('script'):
    if sc.string and '__INITIAL' in sc.string:
        print(f'Found __INITIAL in script: {sc.string[:200]}')
    if sc.string and 'window.__' in sc.string:
        print(f'Found window config: {sc.string[:200]}')

# Check if there's an API endpoint in the page for fetching fee data
api_patterns = re.findall(r'https?://[^"\'<>]*(?:api|graphql|rest)[^"\'<>]*', r.text)
print(f'\nAPI endpoints found: {len(api_patterns)}')
for api in api_patterns[:3]:
    print(f'  {api}')
