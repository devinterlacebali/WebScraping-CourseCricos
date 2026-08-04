"""Explore ECU using Scrapling-style approach (curl_cffi)."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.ecu.edu.au'

# Check robots.txt first
r = curl.get(f'{DOMAIN}/robots.txt', impersonate='chrome120', timeout=20)
print(f'robots.txt: {len(r.text)}b')
lines = r.text.split('\n')[:30]
for l in lines:
    if 'sitemap' in l.lower() or 'disallow' in l.lower():
        print(f'  {l.strip()}')

# Common sitemap
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=20)
print(f'\nsitemap.xml: status={r2.status_code}')
if 'login' in r2.text.lower()[:200]:
    print('  → Requires login (CMS auth)')

# Try future-students courses listing
print('\n=== /future-students/courses/ ===')
r3 = curl.get(f'{DOMAIN}/future-students/courses/', impersonate='chrome120', timeout=20)
s3 = BeautifulSoup(r3.text, 'html.parser')
h1 = s3.find('h1')
print(f'H1: {h1.get_text(strip=True) if h1 else "none"}')
# Find course links
links = set()
for a in s3.find_all('a', href=True):
    h = a['href']
    if '/courses/' in h and 'course' in h.lower():
        full = h if h.startswith('http') else f'{DOMAIN}{h}'
        links.add(full.rstrip('/'))
print(f'Course links found: {len(links)}')
for l in sorted(list(links)[:10]):
    print(f'  {l}')

# Also check study pages
print('\n=== future-studies ===')
r4 = curl.get(f'{DOMAIN}/future-students/study-areas/', impersonate='chrome120', timeout=20)
s4 = BeautifulSoup(r4.text, 'html.parser')
links2 = set()
for a in s4.find_all('a', href=True):
    h = a['href']
    if 'course' in h.lower():
        full = h if h.startswith('http') else f'{DOMAIN}{h}'
        links2.add(full.rstrip('/'))
print(f'Course links: {len(links2)}')
for l in sorted(list(links2)[:5]):
    print(f'  {l}')
