"""Debug what actually exists in page for fees."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = 'https://www.acknowledgeeducation.edu.au/courses/diploma-of-nursing-draft'
r = requests.get(url, headers=headers, timeout=60)
html = r.text

# Find all dollar amounts in raw HTML
print("=== All $ in raw HTML ===")
for m in re.finditer(r'\$[0-9,]+', html):
    start = max(0, m.start() - 100)
    ctx = html[start:m.end()+100]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f"  -> {clean[:200]}")
    print()

# Also check for any "Tuition fee" text
print("=== 'Tuition fee' in HTML ===")
for m in re.finditer(r'[Tt]uition\s*[Ff]ee', html):
    start = max(0, m.start() - 100)
    ctx = html[start:m.end()+100]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f"  -> {clean[:200]}")
