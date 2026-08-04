"""CDU check if CRICOS/fee are SSR or CSR."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.cdu.edu.au'

# Fetch a nursing course
url = f'{DOMAIN}/study/course/bachelor-nursing-wnurs1'
r = curl.get(url, impersonate='chrome120', timeout=20)
soup = BeautifulSoup(r.text, 'html.parser')
body = re.sub(r'\s+', ' ', soup.get_text())

print(f'CRICOS mentions:')
for m in re.finditer(r'CRICOS.{0,60}\d{6,7}[A-Za-z]?', body):
    print(f'  {m.group()[:80]}')

print(f'\nInternational fee mentions:')
for m in re.finditer(r'International.{0,100}\$[0-9,]{4,}', body):
    print(f'  {m.group()[:120]}')

print(f'\nAll dollar amounts > $1000:')
for m in re.finditer(r'\$[0-9,]{4,}', body):
    ctx = body[max(0,m.start()-30):m.end()+30]
    print(f'  {m.group()}: {ctx.strip()[:80]}')

# Duration
print(f'\nDuration:')
for m in re.finditer(r'(\d+\.?\d*)\s*(year|month|week)', body, re.I):
    ctx = body[max(0,m.start()-30):m.end()+30]
    print(f'  {m.group()}: {ctx.strip()[:80]}')

# Check if international data is in hidden/JSON data
for sc in soup.find_all('script'):
    if sc.string and ('intl' in sc.string.lower() or 'international' in sc.string.lower()):
        print(f'\nScript with intl data: {sc.string[:200]}')
        break

# Check the toggle buttons
print(f'\nToggle buttons:')
for btn in soup.find_all(['button','a','label'], string=re.compile(r'Domestic|International', re.I)):
    print(f'  {btn.get_text(strip=True)[:30]} href={btn.get("href","")[:60]}')
