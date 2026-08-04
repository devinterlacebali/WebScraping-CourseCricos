"""Notre Dame - verify course pages."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'

# Get all program pages from sitemap
r = curl.get(DOMAIN + '/sitemap.xml', impersonate='chrome120', timeout=30)
all_urls = re.findall(r'<loc>(.*?)</loc>', r.text)

# Filter for course detail pages
pat = r'/programs/[^/]+/(undergraduate|postgraduate|vet|research|microcredential|online)/[a-z]'
course_urls = [u for u in all_urls if re.search(pat, u)]
print(f'Course URLs from sitemap: {len(course_urls)}')
for u in course_urls[:3]:
    print(f'  {u}')

# Check one for data
if course_urls:
    u = course_urls[0]
    r2 = curl.get(u, impersonate='chrome120', timeout=15)
    body = r2.text
    s2 = BeautifulSoup(body, 'html.parser')
    
    h1 = s2.find('h1')
    print(f'\n=== {h1.get_text(strip=True) if h1 else "?"} ===')
    
    for m in re.finditer(r'CRICOS.{0,80}', body, re.I):
        txt = re.sub(r'\s+', ' ', m.group())[:100]
        print(f'  {txt}')
    
    for m in re.finditer(r'\$[\s,0-9]+', body):
        ctx = re.sub(r'\s+', ' ', body[max(0,m.start()-40):m.end()+40])[:100]
        if re.search(r'\d{4,}', m.group()):
            print(f'  Fee: {ctx}')
            break
    
    nurs = [u for u in course_urls if 'nurs' in u.lower()]
    print(f'\nNursing URLs: {len(nurs)}')
    for u in nurs[:3]:
        print(f'  {u}')
