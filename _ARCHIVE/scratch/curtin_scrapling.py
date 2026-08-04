"""Curtin exploration with Scrapling."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from scrapling import Fetcher
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.curtin.edu.au'
f = Fetcher()

r = f.get(DOMAIN)
print(f'Main: {r.status}, {len(r.text)}b')

# Check if Scrapling bypasses CF
body = r.text
print(f'Cloudflare in text: {"cloudflare" in body.lower() or "cf-browser-verification" in body}')
print(f'Response has h1: {bool(re.search(r"<h1", body))}')

# Try course listing with Scrapling
print('\n=== /study/courses ===')
r2 = f.get(f'{DOMAIN}/study/courses')
print(f'Status: {r2.status}, {len(r2.text)}b')
s2 = BeautifulSoup(r2.text, 'html.parser')
h1 = s2.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')

# Try nursing course page
print('\n=== Course page ===')
for slug in ['bachelor-of-science-nursing', 'bachelor-of-science-nursing--b-nursv8']:
    url = f'{DOMAIN}/study/courses/{slug}'
    r3 = f.get(url)
    print(f'{slug}: {r3.status}, {len(r3.text)}b')
    if r3.status == 200 and len(r3.text) > 1000:
        s3 = BeautifulSoup(r3.text, 'html.parser')
        body3 = re.sub(r'\s+', ' ', s3.get_text())
        cricos = bool(re.search(r'CRICOS', body3))
        fee = bool(re.search(r'AUD\s*\$?\s*[0-9,]{4,}', body3))
        dur = bool(re.search(r'Duration', body3))
        print(f'  CRICOS={cricos}, Fee={fee}, Dur={dur}')
        if cricos:
            for m in re.finditer(r'CRICOS.{0,80}', body3):
                print(f'  CRICOS: {m.group()[:100]}')
        if fee:
            for m in re.finditer(r'\$[0-9,]{5,}', body3):
                ctx = body3[max(0,m.start()-40):m.end()+40]
                print(f'  Fee: {ctx.strip()[:120]}')
        break
