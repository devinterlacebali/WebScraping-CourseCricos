"""UTas - find course API and page structure."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.utas.edu.au'

# Check /courses/ for structure
r = curl.get(f'{DOMAIN}/courses/', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')

# Check all script tags for JSON data
print('=== Scripts with course data ===')
for i, sc in enumerate(s.find_all('script')):
    if sc.string and ('course' in sc.string.lower() or 'degree' in sc.string.lower()):
        txt = sc.string[:300]
        print(f'Script {i}: {txt[:200]}')
        break

# Check for data attributes
print('\n=== Data attributes ===')
for el in s.find_all(attrs={'data-course': True})[:3]:
    print(f'  data-course: {el["data-course"][:200]}')

for el in s.find_all(attrs={'data-search': True})[:3]:
    print(f'  data-search: {el["data-search"][:200]}')

# Check headings
print('\n=== Headings ===')
for h in s.find_all(['h1','h2','h3'])[:5]:
    t = h.get_text(strip=True)
    if len(t) > 3: print(f'  [{h.name}] {t[:60]}')

# Check all links for course pattern
print('\n=== Link patterns ===')
course_links = set()
for a in s.find_all('a', href=True):
    h = a['href']
    if 'course' in h.lower() or '/degree/' in h.lower():
        course_links.add(h)
        if len(course_links) > 10: break
if course_links: 
    for l in course_links: print(f'  {l}')
else:
    # Show some sample links
    all_links = list(set(a['href'] for a in s.find_all('a', href=True)))
    print(f'Total links: {len(all_links)}')
    for l in all_links[:5]: print(f'  {l}')

# Check for API endpoint in HTML
print('\n=== API endpoints ===')
for m in re.finditer(r'https?://[^"\'<>]*(?:api|graphql|rest|course|degree)[^"\'<>]*', r.text):
    url = m.group()[:120]
    if any(kw in url for kw in ['api', 'search', 'course', 'graphql']):
        print(f'  {url}')

# Try direct course slug patterns
print('\n=== Course page checks ===')
for path in ['/courses/degree/bachelor-of-nursing', '/study/courses/bachelor-of-nursing',
             '/study/degree/bachelor-of-nursing', '/course/bachelor-of-nursing']:
    try:
        r2 = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=15)
        if r2.status_code == 200 and len(r2.text) > 1000:
            s2 = BeautifulSoup(r2.text, 'html.parser')
            h1 = s2.find('h1')
            body = re.sub(r'\s+', ' ', s2.get_text())
            cricos = bool(re.search(r'CRICOS', body))
            print(f'{path}: 200 | H1={h1.get_text(strip=True)[:40] if h1 else "?"} | CRICOS={cricos}')
            if cricos:
                for m in re.finditer(r'CRICOS.{0,80}', body):
                    print(f'  {m.group()[:100]}')
        else:
            print(f'{path}: {r2.status_code}')
    except: pass
