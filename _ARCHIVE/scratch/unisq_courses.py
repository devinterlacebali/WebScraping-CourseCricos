"""Find course URLs and check data on UniSQ."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

# Sitemap - find degree-and-courses URLs
r = curl.get('https://www.unisq.edu.au/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
deg_urls = [u for u in urls if '/degrees-and-courses/' in u and not u.endswith('/degrees-and-courses')]
deg_urls = sorted(set(deg_urls))
print(f'Degree-and-courses URLs: {len(deg_urls)}')
for d in deg_urls[:5]: print(f'  {d}')
print(f'  ...')
for d in deg_urls[-3:]: print(f'  {d}')

# Test the correct course URL
u = 'https://www.unisq.edu.au/study/degrees-and-courses/bachelor-of-nursing'
r2 = curl.get(u, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r2.text, 'html.parser')
body = soup.get_text()
print(f'\nCourse: {r2.status_code}, {len(r2.text)}b')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True) if h1 else "none"}')

# JSON-LD
print('\n=== JSON-LD ===')
for s in soup.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(s.string.strip())
        items = data if isinstance(data, list) else [data]
        for item in items:
            if isinstance(item, dict) and 'Course' in item.get('@type', ''):
                for k, v in item.items():
                    if isinstance(v, (str, int, float, bool)):
                        print(f'  {k}: {v}')
                    elif isinstance(v, list) and len(v) < 10:
                        print(f'  {k}: {json.dumps(v)[:200]}')
    except: pass

# CRICOS
print('\n=== CRICOS ===')
for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', body, re.I):
    print(f'  {m.group()[:80]}')

# Fee
print('\n=== FEES ===')
for m in re.finditer(r'\$([0-9,]+)\s*per\s*year', body, re.I):
    ctx = body[max(0,m.start()-40):m.end()+40]
    print(f'  {m.group()} | ctx: {ctx.strip()[:100]}')
for m in re.finditer(r'(?:International|Tuition)[^$]*\$([0-9,]+)', body, re.I):
    print(f'  Intl fee: ${m.group(1)}')

# Duration
print('\n=== DURATION ===')  
for m in re.finditer(r'(?:Duration|Program length)[^:]*:\s*(\d+\s*(?:year|month|week))', body, re.I):
    print(f'  {m.group()}')

# Intake
print('\n=== INTAKE ===')
for m in re.finditer(r'(?:Start|Intake)[^:]*:\s*([A-Za-z ,]+)', body, re.I):
    txt = m.group(1)[:60]
    if '2025' not in txt and '2026' not in txt:
        print(f'  {m.group()[:80]}')

# Check for API/data in page
print('\n=== SCRIPT DATA ===')
for s in soup.find_all('script'):
    if s.string and len(s.string) > 2000:
        for kw in ['cricos', 'fee', 'duration', 'program', 'courseData']:
            if kw in s.string.lower():
                for m in re.finditer(r'["\']cricos["\']\s*:\s*["\']([^"\']+)["\']', s.string, re.I):
                    print(f'  CRICOS in script: {m.group(1)}')
                for m in re.finditer(r'["\'](?:fee|tuition)["\']\s*:\s*["\']?(\$?[0-9,]+)["\']?', s.string, re.I):
                    ctx = s.string[max(0,m.start()-30):m.end()+30]
                    if 'international' in ctx.lower() or 'intl' in ctx.lower():
                        print(f'  Fee in script: {m.group(1)} | ctx: {ctx.strip()[:80]}')
                break

# Degree structure - data tables
print('\n=== SUMMARY SECTION ===')
for m in re.finditer(r'ATAR.*?QTAC.*?Duration.*?Start', body, re.I):
    print(f'  {m.group()[:150]}')

# Intro section
for el in soup.find_all(['section', 'div'], class_=lambda c: c and ('intro' in c.lower() or 'summary' in c.lower() or 'header' in c.lower())):
    txt = el.get_text(strip=True)[:200]
    if len(txt) > 30 and 'menu' not in txt.lower():
        print(f'  Section: {txt[:150]}')
