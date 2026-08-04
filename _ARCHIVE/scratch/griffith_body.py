"""Check Griffith - full body extraction."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

url = 'https://www.griffith.edu.au/study/degrees/bachelor-of-nursing-2036'
r = curl.get(url, impersonate='chrome120', timeout=30)

# Strip all HTML tags and see actual content
body = re.sub(r'<script[^>]*>.*?</script>', '', r.text, flags=re.DOTALL)
body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL)
body = re.sub(r'<[^>]+>', '\n', body)
lines = [l.strip() for l in body.split('\n') if l.strip() and len(l.strip()) > 20]
print(f'Content lines: {len(lines)}')
for l in lines[:40]:
    print(f'  {l[:150]}')
print('...')
for l in lines[-10:]:
    print(f'  {l[:150]}')

# Check if this URL always returns the same or has program-specific data
print(f'\nUnique content markers (CRICOS, program, degree):')
for kw in ['CRICOS', 'program name', 'degree name', 'Bachelor of Nursing']:
    for m in re.finditer(r'.{0,60}' + kw + r'.{0,60}', r.text):
        ctx = m.group().strip()
        if len(ctx) > 20:
            print(f'  [{kw}]: {ctx[:120]}')
