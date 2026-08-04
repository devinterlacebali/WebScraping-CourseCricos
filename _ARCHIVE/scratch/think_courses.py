"""Get all course URLs from Think /courses listing page and individual pages."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

base = 'https://www.think.edu.au'

# Check /courses listing for course cards
r = curl.get(f'{base}/courses', impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
text = soup.get_text()

# Find all links
links = set()
for a in soup.find_all('a', href=True):
    h = a['href']
    if '/courses/' in h and h not in links:
        links.add(h)

# Also check sitemap
r2 = curl.get(f'{base}/sitemap.xml', impersonate='chrome120', timeout=30)
sitemap_urls = set(re.findall(r'<loc>(.*?)</loc>', r2.text))
sitemap_course = set(u for u in sitemap_urls if '/courses/' in u and u.count('/') > 4)

# Also look in JSON/CMS data
scripts = soup.find_all('script')
for sc in scripts:
    if sc.string and ('course' in sc.string.lower() or 'program' in sc.string.lower()):
        if 'window.__NUXT__' in sc.string or '__NEXT_DATA__' in sc.string or 'courses' in sc.string.lower():
            print(f'FOUND script: {sc.string[:200]}')

print(f'Sitemap course URLs: {sitemap_course}')
print(f'\nAll unique course links from page:')
full_urls = set()
for l in links:
    if l.startswith('http'):
        full_urls.add(l.rstrip('/'))
    else:
        full_urls.add(f'{base}{l}'.rstrip('/'))
for u in sorted(full_urls):
    print(f'  {u}')

# Fetch each and check data
print(f'\n=== Fetching each course page ===')
for i, url in enumerate(sorted(full_urls), 1):
    try:
        rp = curl.get(url, impersonate='chrome120', timeout=15)
        sp = BeautifulSoup(rp.text, 'html.parser')
        h1 = sp.find('h1')
        title = h1.get_text(strip=True) if h1 else 'none'
        # Check for data
        body = re.sub(r'\s+', ' ', sp.get_text())
        has_cricos = bool(re.search(r'CRICOS\s*\d{6,7}[A-Za-z]?', body))
        has_fee = bool(re.search(r'\$\s*[0-9,]{4,}', body))
        has_dur = bool(re.search(r'\d+\s*(year|month|week)', body))
        has_intake = bool(re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', body))
        print(f'  [{i}] {title[:45]}: cricos={has_cricos}, fee={has_fee}, dur={has_dur}, intake={has_intake}')
    except Exception as e:
        print(f'  [{i}] ERROR: {e}')
