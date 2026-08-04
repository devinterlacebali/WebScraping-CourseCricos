"""Explore Griffith degree listing."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

# Study degrees page - find course urls
r = curl.get('https://www.griffith.edu.au/study/degrees', impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')

# Find all links that look like degree pages
links = soup.find_all('a', href=True)
degree_links = []
for a in links:
    h = a['href']
    if '/study/degrees/' in h and not h.endswith('/study/degrees') and not h.endswith('#') and len(h) > 20:
        degree_links.append(h)

# Deduplicate
degree_links = sorted(set(degree_links))
print(f'Degree links on page: {len(degree_links)}')
for dl in degree_links[:10]:
    print(f'  {dl}')
print(f'  ...')
for dl in degree_links[-3:]:
    print(f'  {dl}')

# Check if there's pagination
next_btn = soup.find('a', string=re.compile(r'Next|Show more', re.I))
print(f'\nNext/pagination: {next_btn.get("href") if next_btn else "none"}')

# Check scripts for API data
for s in soup.find_all('script'):
    if s.string and ('course' in s.string.lower() or 'degree' in s.string.lower()):
        # Search for URL patterns
        for m in re.finditer(r'/study/degrees/[^"\'\\s]+', s.string):
            pass  # already found from links

# Try the first degree page
if degree_links:
    u = degree_links[0]
    if not u.startswith('http'):
        u = 'https://www.griffith.edu.au' + u
    r2 = curl.get(u, impersonate='chrome120', timeout=30)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    body = re.sub(r'\s+', ' ', soup2.get_text())
    print(f'\n=== First degree: {u} ===')
    print(f'Status: {r2.status_code}, Size: {len(r2.text)}b')
    h1 = soup2.find('h1')
    print(f'H1: {h1.get_text(strip=True) if h1 else "none"}')
    
    # Meta
    for m in soup2.find_all('meta'):
        n = m.get('name','') or m.get('property','') or ''
        c = m.get('content','')
        if any(kw in n.lower() for kw in ['cricos','duration','desc','fee','startmonth','description']):
            print(f'  Meta {n}: {c[:150]}')
    
    # JSON-LD
    for s in soup2.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(s.string)
            if isinstance(data, dict):
                print(f'  JSON-LD @type: {data.get("@type", "?")}')
                if data.get('@type') == 'Course':
                    for k in ['name','description','courseCode','cricos','duration','offers']:
                        if k in data:
                            print(f'    {k}: {json.dumps(data[k], indent=2)[:200]}')
        except: pass
    
    # CRICOS, fee, duration
    for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', body, re.I):
        print(f'  CRICOS: {m.group(0)}')
    for m in re.finditer(r'\$([0-9,]+)\s*per\s*year', body, re.I):
        ctx = body[max(0,m.start()-20):m.end()+20]
        print(f'  Fee: {m.group()} | ctx: {ctx.strip()}')
    for m in re.finditer(r'(?:Duration)[^:]*:\s*(\d+\s*(?:year|month|week))', body, re.I):
        print(f'  Dur: {m.group()}')
    for m in re.finditer(r'(?:Program length)[^:]*:\s*(\d+\s*(?:year|month|week))', body, re.I):
        print(f'  PrLen: {m.group()}')
    
    # Headings
    print('\nHeadings:')
    for h in soup2.find_all(['h1','h2','h3'])[:8]:
        t = h.get_text(strip=True)[:60]
        if t: print(f'  {h.name}: {t}')
