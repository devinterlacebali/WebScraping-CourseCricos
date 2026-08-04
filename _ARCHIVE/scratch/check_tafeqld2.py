"""Check TAFE QLD - working courses only"""
from curl_cffi import requests as curl_requests
from bs4 import BeautifulSoup
import re

# Check a diploma course that should exist - Diploma of Nursing
resp = curl_requests.get('https://tafeqld.edu.au/course/36/36286/diploma-of-nursing', impersonate='chrome120', timeout=30)
html = resp.text
print(f'Status: {resp.status_code}, Len: {len(html)}')

if resp.status_code != 200:
    print(f'404 page. First 200 chars: {html[:200]}')
else:
    soup = BeautifulSoup(html, 'html.parser')
    text = re.sub(r'\s+', ' ', soup.get_text(' ', strip=True))
    
    print('First 800 chars:', text[:800])
    print()
    for m in re.finditer(r'\$[\d,]+', text):
        start = max(0, m.start()-80)
        end = min(len(text), m.end()+80)
        chunk = text[start:end]
        print(f'  ${m.group()}: ...{chunk.strip()}...')
