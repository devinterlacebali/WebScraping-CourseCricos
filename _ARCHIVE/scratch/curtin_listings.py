"""Curtin - deeper sitemap + course listing."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.curtin.edu.au'

# Get the actual sitemaps
for sm in ['page-sitemap1.xml', 'extras-sitemap1.xml']:
    r = curl.get(f'{DOMAIN}/{sm}', impersonate='chrome120', timeout=30)
    if r.status_code == 200:
        urls = re.findall(r'<loc>(.*?)</loc>', r.text)
        print(f'{sm}: {len(urls)} URLs')
        course_urls = [u for u in urls if any(kw in u.lower() for kw in ['course', 'study', 'degree', 'program'])]
        print(f'  Course-related: {len(course_urls)}')
        for u in course_urls[:5]: print(f'  {u}')
        if not course_urls:
            # Show some sample URLs
            for u in urls[:5]: print(f'  {u}')
    else:
        print(f'{sm}: {r.status_code}')

# Check /study/courses listing
print('\n--- /study/courses ---')
r2 = curl.get(f'{DOMAIN}/study/courses', impersonate='chrome120', timeout=30)
s2 = BeautifulSoup(r2.text, 'html.parser')
print(f'Status: {r2.status_code}, {len(r2.text)}b')
h1 = s2.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')

# Check for course links
links = set()
for a in s2.find_all('a', href=True):
    h = a['href']
    if '/course/' in h.lower() and h not in links:
        links.add(h)
print(f'Unique /course/ links: {len(list(links))}')
for l in sorted(list(links))[:10]: print(f'  {l}')

# Check if it's a search page with query params
for form in s2.find_all('form'):
    print(f'Form action: {form.get("action", "none")}')
    for inp in form.find_all('input'):
        print(f'  Input: {inp.get("name", "")} = {inp.get("value", "")}')
        
# Check if there's JSON data in scripts
for sc in s2.find_all('script'):
    if sc.string and ('courses' in sc.string or 'pageProps' in sc.string):
        txt = sc.string[:300]
        if 'pageProps' in txt or '__NEXT' in txt:
            print(f'\nFramework found: {txt[:200]}')
            
# Check for API endpoints in JS
for m in re.finditer(r'https?://[^"\'<>]*(?:api|rest|graphql)[^"\'<>]*', r2.text):
    print(f'API: {m.group()[:120]}')
