"""Debug UniSQ page text."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
import re

u = 'https://www.unisq.edu.au/study/degrees-and-courses/bachelor-of-nursing?studentType=international'
r = curl.get(u, impersonate='chrome120', timeout=30)
full = re.sub(r'\s+', ' ', r.text)

# Check for the exact patterns
print('=== Searching for International full fee ===')
for m in re.finditer(r'International.{0,100}\$[0-9,]{4,}', full, re.I):
    print(f'  {m.group()[:120]}')

print('\n=== Searching for CRICOS near number ===')
for m in re.finditer(r'CRICOS.{0,20}\d{6,7}', full, re.I):
    print(f'  {m.group()[:80]}')

print('\n=== Raw text around CRICOS ===')
idx = full.lower().find('cricos')
if idx >= 0:
    print(f'  context: {full[max(0,idx-30):idx+80]}')

print('\n=== Raw text around "International full fee" ===')
idx2 = full.lower().find('international full fee')
if idx2 >= 0:
    print(f'  context: {full[max(0,idx2-30):idx2+200]}')
else:
    print('  "International full fee" not found')
    # Search for "International" near "fee"
    for m in re.finditer(r'International.{0,50}fee.{0,200}', full, re.I):
        print(f'  Found: {m.group()[:200]}')
