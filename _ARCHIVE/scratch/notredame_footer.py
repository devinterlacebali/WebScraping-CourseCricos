"""Notre Dame - check footer + course pages."""
import sys, re, csv
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'

# Get footer
for path in ['/', '/study/our-programs']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    # Search for CRICOS patterns
    body = r.text
    for m in re.finditer(r'(\d{6,7}[A-Za-z])', body):
        code = m.group(1)
        ctx = body[max(0,m.start()-20):m.end()+20].strip()
        # Skip hex/color codes
        if re.search(r'#[0-9a-fA-F]|background|color:|opacity|margin|padding|width|height', ctx, re.I):
            continue
        print(f'{path}: CRICOS-like: {code} | ctx: {ctx[:60]}')
        break
    
    # Also search for provider code after specific keywords
    for m in re.finditer(r'(?:Provider|CRICOS|TEQSA|PRV).{0,30}', body, re.I):
        txt = re.sub(r'\s+', ' ', m.group())
        print(f'{path}: Found: {txt[:80]}')

# Try sitemap for actual course pages
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r2.text)

# Look for course detail pages
detail = [u for u in urls if re.match(r'.*/programs?/[a-z]', u) or re.match(r'.*/course/[a-z]', u)]
print(f'\nDetail course URLs: {len(detail)}')
for u in detail[:5]:
    print(f'  {u}')

# Try to find program pages
program = [u for u in urls if '/program/' in u.lower() or '/programs/' in u.lower()]
print(f'\nProgram URLs: {len(program)}')
for u in program[:5]:
    print(f'  {u}')
