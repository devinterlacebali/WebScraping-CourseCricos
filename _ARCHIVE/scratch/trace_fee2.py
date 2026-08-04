"""Debug: find exact path to fee amount $54,900 in the HTML."""
import requests, re, json
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
r = requests.get('https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/', headers=headers, timeout=60)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

# Find by exact text in raw HTML
print("=== All span elements containing '$' ===")
for span in soup.find_all('span'):
    if '$' in span.get_text():
        text = span.get_text(strip=True)
        print(f"  span tekst: '{text[:100]}'")
        print(f"    parents: {[p.name for p in span.parents][:5]}")
        print(f"    classes: {span.get('class', [])}")
        print()

# Try selectors
print("=== Try CSS selectors ===")
for sel in ['.degree-details', '.fee', '.price', '[class*="fee"]', '[class*="price"]', '[class*="details"]', '.cmp-text']:
    els = soup.select(sel)
    if els:
        print(f"'{sel}': {len(els)} elements")
        for el in els[:3]:
            t = el.get_text(strip=True)[:100]
            if '$' in t or 'fee' in t.lower() or 'Fee' in t:
                print(f"  -> {t}")

# Find all "$" in rendered text
print("\n=== All $ amounts in rendered text ===")
body = soup.get_text()
for m in re.finditer(r'\$[0-9,]+', body):
    start = max(0, m.start()-80)
    ctx = body[start:m.end()+80].strip()
    ctx = re.sub(r'\s+', ' ', ctx)
    print(f"  ...{ctx}...")
