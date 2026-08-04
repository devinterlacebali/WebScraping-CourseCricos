"""WSU - find course finder and intake."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Look for the course finder URL in the page
r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')

# Find all links with "course" in them
for a in s.find_all('a', href=True):
    txt = a.get_text(strip=True).lower()
    href = a['href']
    if any(k in txt for k in ['course', 'find', 'program', 'degree', 'search', 'study']) and 'course' in href:
        if not href.startswith('http'): href = DOMAIN + href
        print(f'  {href[:120]} | {txt[:40]}')

# Check /future#courses which might load courses via JS
print('\n=== /future#courses ===')
r2 = curl.get(f'{DOMAIN}/future', impersonate='chrome120', timeout=30)
s2 = BeautifulSoup(r2.text, 'html.parser')
# Look for any iframe, embed, or data attributes
for el in s2.find_all(['iframe', 'embed', 'object']):
    src = el.get('src', '') or el.get('data', '')
    if 'course' in src.lower() or 'find' in src.lower():
        print(f'  Found iframe: {src[:120]}')

# Check for embedded course finder link
for a in s2.find_all('a', href=True):
    if 'course' in a['href'].lower() and 'find' in a.get_text(strip=True).lower():
        print(f'  Course finder: {DOMAIN}{a["href"]}')

# Search for intake on international page with more context
print('\n=== International full text search ===')
r3 = curl.get(f'{DOMAIN}/international', impersonate='chrome120', timeout=30)
body = r3.text.lower()
# Check for semester months pattern
intake_patterns = [
    r'march intake|july intake|february intake',
    r'semester one.*march|semester two.*july',
    r'autumn.*session|spring.*session',
    r'start.*(?:march|july|february|january)',
]
for pat in intake_patterns:
    if re.search(pat, body):
        print(f'  Found: {re.search(pat, body).group()[:80]}')

# Also show any "intake" paragraph
for m in re.finditer(r'[^.]*?intake[^.]*\.', body):
    print(f'  Intake mention: {m.group()[:120]}')
