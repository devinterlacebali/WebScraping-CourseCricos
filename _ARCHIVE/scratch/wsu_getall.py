"""WSU - get all course URLs from listing pages."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Get all links from postgraduate listing
r = curl.get(f'{DOMAIN}/future/study/courses/postgraduate', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')

# Show all links that contain future/study/courses
course_urls = set()
for a in s.find_all('a', href=True):
    h = a['href']
    if 'future/study/courses' in h:
        parts = h.strip('/').split('/')
        # Actual course pages: /future/study/courses/postgraduate/{slug} (5+ parts)
        if len(parts) >= 5 and parts[3] in ('undergraduate', 'postgraduate', 'research'):
            full = h if h.startswith('http') else f'{DOMAIN}{h}'
            course_urls.add(full)

print(f'Course URLs from postgraduate: {len(course_urls)}')
for u in sorted(course_urls)[:10]:
    print(f'  {u}')

# Now scrape a few and check CRICOS extraction
print('\n=== Test extraction ===')
for url in sorted(course_urls)[:3]:
    r2 = curl.get(url, impersonate='chrome120', timeout=30)
    body = r2.text
    # Raw HTML search for CRICOS
    for m in re.finditer(r'\b(\d{6,7}[A-Za-z])\b', body):
        code = m.group(1)
        ctx = body[max(0,m.start()-40):m.end()+40]
        # Check if hex color
        if not re.search(r'[0-9A-Fa-f]{6}', code):
            print(f'{url.split("/")[-1][:30]}: CRICOS={code} | ctx={ctx.strip()[:80]}')
            break
    else:
        print(f'{url.split("/")[-1][:30]}: NO CRICOS found')
