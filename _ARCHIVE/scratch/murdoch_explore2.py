"""Murdoch - check for JSON data in the page more carefully."""
import requests, re, json, sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

url = 'https://www.murdoch.edu.au/course/Undergraduate/mj-cams'
r = S.get(url, timeout=30)
text = r.text
print(f'Length: {len(text)}')

# Look for ALL script tags that might contain JSON
print('=== ALL script[type=application/json] ===')
for m in re.finditer(r'<script[^>]+type="application/json"[^>]*>(.*?)</script>', text, re.DOTALL):
    print(f'  Found {len(m.group(1))} chars')
    print(f'  Start: {m.group(1)[:300]}')

print('\n=== Look for data-* attributes with course info ===')
# Search for cricos / fee / duration in the raw HTML
for kw in ['cricos', 'fee', 'duration', 'credit', 'international', 'semester']:
    # Only look in the first 20000 chars outside of scripts
    body_start = text.find('<main')
    if body_start == -1:
        body_start = text.find('<body')
    if body_start == -1:
        body_start = 0
    sample = text[body_start:body_start+100000]
    indices = []
    idx = 0
    while True:
        idx = sample.lower().find(kw, idx)
        if idx == -1: break
        indices.append(idx)
        idx += 1
    if indices:
        print(f'\n  "{kw}" found {len(indices)} times in body')
        for i in indices[:5]:
            ctx = sample[max(0,i-50):i+150]
            clean_ctx = re.sub(r'\s+', ' ', ctx)
            print(f'    ...{clean_ctx[:250]}')

# Check if data is in a JSON data attribute  
print('\n=== Look for data properties/attributes ===')
for m in re.finditer(r'data-[a-z-]+="[^"]*cricos[^"]*"', text, re.I):
    print(f'  {m.group(0)[:200]}')
for m in re.finditer(r'data-[a-z-]+="[^"]*[0-9]{6,7}[A-Za-z][^"]*"', text):
    print(f'  DATA ATTR: {m.group(0)[:200]}')
