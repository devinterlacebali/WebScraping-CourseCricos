"""Explore Acknowledge Education website structure."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = 'https://www.acknowledgeeducation.edu.au/courses/diploma-of-nursing-draft'
r = requests.get(url, headers=headers, timeout=60)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

print("Status:", r.status_code)
print("Title:", soup.find('title').get_text(strip=True) if soup.find('title') else '')
print()

# Meta tags
print("=== META TAGS ===")
for meta in soup.find_all('meta'):
    name = meta.get('name', '') or meta.get('property', '') or meta.get('itemprop', '')
    content = meta.get('content', '')
    if content and name:
        print(" ", name, ":", content[:100])

# CRICOS
print("\n=== CRICOS ===")
for m in re.finditer(r'\b([0-9]{6,7}[A-Za-z]?)\b', html):
    ctx = html[max(0,m.start()-60):m.end()+60]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f"  {m.group(1)}: {clean[:120]}")

# Sections
print("\n=== SECTIONS ===")
for cls in ['course-summary-item', 'accordion', 'overview', 'entry']:
    els = soup.find_all(class_=lambda x: x and cls in x.lower())
    if els:
        print(f"  class containing '{cls}': {len(els)} found")

# Fee 
print("\n=== FEE ===")
body = soup.get_text()
for m in re.finditer(r'\$[0-9,]+', body):
    start = max(0, m.start() - 60)
    ctx = body[start:m.end()+60].strip()
    ctx = re.sub(r'\s+', ' ', ctx)
    if any(kw in ctx.lower() for kw in ['fee', 'tuition', 'total', 'international']):
        print(f"  -> {ctx[:200]}")

# Duration
print("\n=== DURATION ===")
for m in re.finditer(r'(\d+)\s*(year|month|week)', body, re.I):
    start = max(0, m.start() - 40)
    ctx = body[start:m.end()+60].strip()
    ctx = re.sub(r'\s+', ' ', ctx)
    print(f"  -> {ctx[:150]}")
