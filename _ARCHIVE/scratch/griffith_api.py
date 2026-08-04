"""Find Griffith program API."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

url = 'https://www.griffith.edu.au/study/degrees/bachelor-of-nursing-2036'
r = curl.get(url, impersonate='chrome120', timeout=30)

# Search for API URLs in all scripts
for s in BeautifulSoup(r.text, 'html.parser').find_all('script'):
    if s.string and len(s.string) > 100:
        # Look for API endpoints
        for m in re.finditer(r'(https?://[^"\'\\s]+(?:api|graphql|program|course)[^"\'\\s]*)', s.string, re.I):
            print(f'  API URL: {m.group()[:120]}')
        # Look for relative API paths
        for m in re.finditer(r'["\'](/api/[^"\']+)["\']', s.string, re.I):
            print(f'  API path: {m.group(1)}')
        # Look for config/service URLs
        for m in re.finditer(r'["\'](.*?/program[^"\']*)["\']', s.string, re.I):
            val = m.group(1)
            if len(val) > 10 and 'http' not in val and '//' not in val:
                print(f'  Program path: {val}')
        # Search for /study/degrees/sitemap or JSON data
        for m in re.finditer(r'/study/degrees/[^"\'\\s]+\.json', s.string):
            print(f'  JSON data: {m.group()}')

# Check for hidden span/data attributes with program data
soup = BeautifulSoup(r.text, 'html.parser')
for el in soup.find_all(['div','span','section'], attrs={'data-program': True}):
    print(f'  Data-program: {el.get("data-program")}')
for el in soup.find_all(attrs={'data-course-code': True}):
    print(f'  Data-course-code: {el.get("data-course-code")}')
for el in soup.find_all(attrs={'data-degree': True}):
    print(f'  Data-degree: {el.get("data-degree")}')

# Try common API endpoints
print('\n=== Trying API endpoints ===')
for path in [
    '/sitemap.xml?type=program',
    '/sitemaps/collections/programs.xml',
    '/api/degrees',
    '/api/programs/search',
    '/study/degrees/programs.json',
    '/sites/default/files/programs.json',
]:
    r2 = curl.get(f'https://www.griffith.edu.au{path}', impersonate='chrome120', timeout=15)
    is_json = 'json' in r2.headers.get('content-type', '')
    print(f'  {path}: {r2.status_code}, {len(r2.text)}b, json={is_json}')

# Check sitemap index sub-sitemaps
print('\n=== Sitemap sub-sitemaps ===')
r3 = curl.get('https://www.griffith.edu.au/sitemap.xml', impersonate='chrome120', timeout=15)
urls = re.findall(r'<loc>(.*?)</loc>', r3.text)
for u in urls:
    if 'program' in u.lower() or 'degree' in u.lower() or 'course' in u.lower():
        r4 = curl.get(u, impersonate='chrome120', timeout=15)
        print(f'  {u.split("/")[-1]}: {r4.status_code}, {len(r4.text)}b')
        prog_urls = re.findall(r'<loc>(.*?)</loc>', r4.text)
        print(f'    URLs: {len(prog_urls)}')
        for pu in prog_urls[:3]:
            print(f'      {pu}')
