"""Murdoch - test course page extraction for Bachelor of Nursing."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

url = 'https://www.murdoch.edu.au/course/Undergraduate/b1417'
r = S.get(url, timeout=30)
text = r.text

print('=== CRICOS ===')
for m in re.finditer(r'CRICOS[^<]*?([0-9]{6,7}[A-Za-z])', text):
    print(f'  {m.group(0)}')

print()
print('=== Meta Tags ===')
for m in re.finditer(r'<meta[^>]*name="([^"]+)"[^>]*content="([^"]+)"', text, re.I):
    print(f'  {m.group(1)}: {m.group(2)[:80]}')

print()
print('=== Fee section ===')
for tab in ['domestic', 'international']:
    if 'is-' + tab in text:
        print(f'{tab.upper()} section found')
        # Find the details list for this tab
        start = text.find('is-' + tab)
        if start >= 0:
            block = text[start:start+5000]
            for dm in re.finditer(r'\$[0-9,]+', block):
                ctx = block[max(0,dm.start()-60):dm.end()+80]
                clean = re.sub(r'\s+', ' ', ctx)
                print(f'  $ {dm.group(0)} ... {clean[:200]}')

print()
print('=== Duration ===')
dur = re.search(r'(\d+)\s*(year|semester|month)[s]?', text, re.I)
if dur:
    print(f'  {dur.group(0)}')

print()
print('=== Intake/Start dates ===')
seen = set()
for m in re.finditer(r'Semester\s+\d[^<]*', text):
    s = m.group(0).strip()
    if s not in seen:
        seen.add(s)
        print(f'  {s}')

print()
print('=== Course Description (first 300 chars) ===')
body = re.search(r'<body[^>]*>(.*)</body>', text, re.DOTALL)
if body:
    clean = re.sub(r'<script[^>]*>.*?</script>', '', body.group(1), flags=re.DOTALL)
    clean = re.sub(r'<style[^>]*>.*?</style>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'&nbsp;', ' ', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    idx = clean.lower().find('course overview')
    if idx >= 0:
        print(f'  {clean[idx:idx+500]}')

print()
print('=== Entry Requirements (first 300 chars) ===')
idx = clean.lower().find('admission requirements')
if idx >= 0:
    print(f'  {clean[idx:idx+500]}')
