"""Dig deeper into Adelaide Uni course page."""
import requests, re, json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
r = requests.get('https://adelaideuni.edu.au/study/degrees/bachelor-of-laws-honours/', headers=headers, timeout=60)
html = r.text

# Find fee section explicitly
print("=== Searching for 'International' in the page ===")
# Find all divs that might contain fee data
for m in re.finditer(r'(?:International)[^<>]{0,500}(?:\$[0-9,]+)[^<>]{0,500}', html):
    ctx = html[max(0,m.start()-200):m.end()+200]
    clean = re.sub(r'<[^>]+>', '\n', ctx)
    clean = re.sub(r'\n+', '\n', clean)
    print(clean[:500])
    print("===")
