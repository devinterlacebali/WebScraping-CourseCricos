"""Check ECU duration format."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

url = 'https://www.ecu.edu.au/degrees/courses/bachelor-of-science-nursing'
r = curl.get(url, impersonate='chrome120', timeout=20)
soup = BeautifulSoup(r.text, 'html.parser')
body = re.sub(r'\s+', ' ', soup.get_text())

# Look for duration context
print('=== Duration mentions ===')
for m in re.finditer(r'.{30}(?:\d+\s*(?:year|month|week)).{30}', body, re.I):
    print(f'  {m.group().strip()[:100]}')
    print()

print('\n=== "Duration" headings ===')
for h in soup.find_all(['h2','h3','h4'], string=re.compile(r'[Dd]uration')):
    print(f'  [{h.name}] {h.get_text(strip=True)[:60]}')
    parent = h.find_parent(['div','section'])
    if parent:
        print(f'  Parent text: {parent.get_text()[:200]}')
