"""Explore Griffith site."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

# Sitemap
r = curl.get('https://www.griffith.edu.au/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
print(f'Sitemap total: {len(urls)}')
course_urls = [u for u in urls if '/study/degrees/' in u]
print(f'Course URLs: {len(course_urls)}')
for u in course_urls[:5]:
    print(f'  {u}')
for u in course_urls[-3:]:
    print(f'  {u}')

# Test one course
u = course_urls[0]
r2 = curl.get(u, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r2.text, 'html.parser')
body = r2.text
full = soup.get_text()
print(f'\nCourse page: {r2.status_code}, {len(r2.text)}b')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True) if h1 else "none"}')
print(f'Title: {soup.title.string.strip() if soup.title else "none"}')

import urllib.parse
parsed = urllib.parse.urlparse(u)
print(f'Path: {parsed.path}')

# Meta
for m in soup.find_all('meta'):
    n = m.get('name','') or m.get('property','') or ''
    c = m.get('content','')
    if any(kw in n.lower() for kw in ['cricos','duration','desc','fee','startmonth']):
        print(f'  Meta {n}: {c[:150]}')

# JSON-LD
for s in soup.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(s.string)
        if isinstance(data, dict):
            print(f'  JSON-LD @type: {data.get("@type", "?")}')
            if data.get('@type') == 'Course':
                for k in data:
                    v = str(data[k])[:120]
                    print(f'    {k}: {v}')
            elif data.get('@type') == 'WebPage':
                for k in ['name','description','courseCode','cricos']:
                    if k in data:
                        print(f'    {k}: {data[k]}')
    except: pass

# Body data
print('\n--- CRICOS ---')
for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', full, re.I):
    print(f'  {m.group()}')
print('--- FEE ---')
for m in re.finditer(r'\$([0-9,]+)\s*per\s*year', full, re.I):
    print(f'  {m.group()}')
print('--- DURATION ---')
for m in re.finditer(r'(?:Duration|Program length)[^:]*:\s*(\d+\s*(?:year|month|week))', full, re.I):
    print(f'  {m.group()}')
print('--- INTAKE ---')
for m in re.finditer(r'(?:Intake|Start|Trimester|Semester)\w*\s*(?:months?|dates?)?[:]\s*([A-Za-z ,]+)', full, re.I):
    val = m.group(1)[:80]
    print(f'  {val}')

# Headings
print('\nHeadings:')
for h in soup.find_all(['h1','h2','h3'])[:8]:
    t = h.get_text(strip=True)[:60]
    if t: print(f'  {h.name}: {t}')
