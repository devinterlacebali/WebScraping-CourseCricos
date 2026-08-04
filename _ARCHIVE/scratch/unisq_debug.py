"""Debug the exact text processing."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

u = 'https://www.unisq.edu.au/study/degrees-and-courses/bachelor-of-nursing?studentType=international'
r = curl.get(u, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
full = re.sub(r'\s+', ' ', soup.get_text())

print(f'Full text length: {len(full)}')
print(f'\n=== First 500 chars of stripped text ===')
print(full[:500])

print(f'\n=== Searching for "International full fee" ===')
idx = full.lower().find('international full fee')
if idx >= 0:
    print(f'  Found at {idx}: "{full[idx:idx+200]}"')
else:
    print('  NOT FOUND')
    # Try without 'full'
    idx2 = full.lower().find('international fee')
    if idx2 >= 0:
        print(f'  "international fee" at {idx2}: "{full[idx2:idx2+200]}"')
    # Try just "International"
    idx3 = full.lower().find('international')
    if idx3 >= 0:
        print(f'  "international" at {idx3}: "{full[idx3:idx3+200]}"')

print(f'\n=== Searching for CRICOS ===')
idx4 = full.lower().find('cricos')
if idx4 >= 0:
    print(f'  Found at {idx4}: "{full[idx4:idx4+200]}"')
else:
    print('  NOT FOUND')

# Try the actual regex
pat1 = re.compile(r'International full fee paying.*(?:AUD|\$)\s*[0-9,]{4,}')
m1 = pat1.search(full)
print(f'\nRegex "International full fee paying...AUD": {m1.group()[:100] if m1 else "NO MATCH"}')

pat2 = re.compile(r'CRICOS\s*\d{6,7}[A-Za-z]')
m2 = pat2.search(full)
print(f'Regex "CRICOS": {m2.group()[:50] if m2 else "NO MATCH"}')
