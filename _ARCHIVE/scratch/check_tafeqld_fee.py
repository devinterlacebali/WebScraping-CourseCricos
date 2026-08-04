"""Check TAFE QLD fee structure"""
from curl_cffi import requests as curl_requests
from bs4 import BeautifulSoup
import re

# Check a bachelor course (likely international-relevant)
resp = curl_requests.get('https://tafeqld.edu.au/course/49/49275/bachelor-of-dental-prosthetics', impersonate='chrome120', timeout=30)
html = resp.text
soup = BeautifulSoup(html, 'html.parser')
text = re.sub(r'\s+', ' ', soup.get_text(' ', strip=True))

print("=== Bachelor of Dental Prosthetics ===")
# Find fee info
for m in re.finditer(r'\$[\d,]+', text):
    start = max(0, m.start()-80)
    end = min(len(text), m.end()+80)
    chunk = text[start:end]
    print(f'  ${m.group()}: ...{chunk.strip()}...')
    print()

# Check any bachelor/degree page
print("=== Another check - all dollar amounts ===")
for m in re.finditer(r'\$[\d,]+', text):
    start = max(0, m.start()-40)
    end = min(len(text), m.end()+40)
    print(f'  ${m.group()}: ...{text[start:end].strip()}...')
