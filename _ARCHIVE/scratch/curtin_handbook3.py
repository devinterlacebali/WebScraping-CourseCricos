"""Curtin handbook - check data format."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

url = 'https://handbook.curtin.edu.au/courses/course-ug-bachelor-of-science-nursing--b-nursv8'
r = curl.get(url, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
body = re.sub(r'\s+', ' ', soup.get_text())

print(f'Status: {r.status_code}, {len(r.text)}b')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True)[:80] if h1 else "none"}')

# Search for important data
print('\n=== CRICOS ===')
for m in re.finditer(r'CRICOS.{0,80}', body):
    print(f'  {m.group()[:120]}')
    
print('\n=== Fee/Duration ===')
for kw in ['duration', 'fee', 'tuition', 'year', 'semester']:
    for m in re.finditer(rf'.{{0,30}}{kw}.{{0,50}}', body, re.I):
        ctx = m.group().strip()
        if any(c.isdigit() for c in ctx) and len(ctx) > 10:
            print(f'  {ctx[:120]}')

print('\n=== Dollar amounts ===')
for m in re.finditer(r'\$[0-9,.]{5,}', body):
    ctx = body[max(0,m.start()-30):m.end()+30]
    print(f'  {ctx.strip()[:120]}')
    
print('\n=== Intake months ===')
for m in re.finditer(r'[A-Z][a-z]{2,9}\s+\d{4}', body):
    print(f'  {m.group()}')
    
# Check for CRICOS in specific elements
print('\n=== Elements with CRICOS ===')
for el in soup.find_all(string=re.compile(r'CRICOS')):
    parent = el.parent
    if parent:
        print(f'  Tag: <{parent.name}> Text: {parent.get_text(strip=True)[:100]}')
        print(f'  Parent HTML: {str(parent)[:200]}')
