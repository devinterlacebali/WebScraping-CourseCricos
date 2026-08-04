"""Check TasTAFE fee structure"""
from curl_cffi import requests as curl_requests
from bs4 import BeautifulSoup
import re

resp = curl_requests.get('https://www.tastafe.tas.edu.au/courses/course/hlt54121?tab=international', impersonate='chrome120', timeout=30)
html = resp.text
soup = BeautifulSoup(html, 'html.parser')
text = re.sub(r'\s+', ' ', soup.get_text(' ', strip=True))

# Find Tuition Fees International section
idx = text.find('Tuition Fees')
if idx >= 0:
    section = text[idx:idx+1000]
    print("=== Tuition Fees section ===")
    print(section[:800])
    
print("\n=== All $ amounts with context ===")
for m in re.finditer(r'\$[\d,]+', text):
    start = max(0, m.start()-80)
    end = min(len(text), m.end()+80)
    chunk = text[start:end]
    if 'International' in chunk or 'Tuition' in chunk or 'Fee' in chunk.lower():
        print(f'  ${m.group()}: ...{chunk.strip()}...')
        print()

# Check for specific sections
print("\n=== Looking at the page structure ===")
for heading in soup.find_all(['h3', 'h4', 'h5']):
    htxt = heading.get_text(strip=True)
    if 'Fee' in htxt or 'Intake' in htxt or 'Duration' in htxt or 'Tuition' in htxt:
        parent = heading.parent
        print(f'{htxt}:')
        print(f'  {parent.get_text(" ", strip=True)[:300]}')
        print()
