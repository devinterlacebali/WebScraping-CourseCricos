"""Explore Murdoch University website structure."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

url = 'https://www.murdoch.edu.au/study/courses/bachelor-of-nursing'
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
    if content and name and len(content) < 200:
        print(" ", name, ":", content[:100])

# CRICOS - look for meta
print("\n=== CRICOS ===")
for m in re.finditer(r'cricos|CRICOS', html):
    ctx = html[max(0,m.start()-50):m.end()+100]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f"  -> {clean[:150]}")

# Look for spans with CRICOS number
print("\n=== CRICOS NUMBERS ===")
for m in re.finditer(r'\b(\d{6,7}[A-Za-z]?)\b', html):
    ctx = html[max(0,m.start()-30):m.end()+30]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f"  {m.group(1)}: {clean[:100]}")

# Sections
print("\n=== KEY DIVS ===")
for el_id in ['overview', 'entry-requirements', 'fees', 'course-structure', 'admission']:
    el = soup.find(id=el_id) or soup.find('div', id=el_id) or soup.find('section', id=el_id)
    if el:
        print(f"  #{el_id}: FOUND ({len(str(el))} chars)")

# Fee
print("\n=== FEE ===")
body = html
for m in re.finditer(r'\$[0-9,]+', body):
    start = max(0, m.start() - 100)
    ctx = body[start:m.end()+100]
    clean = re.sub(r'\s+', ' ', ctx)
    if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'annual']):
        print(f"  -> {clean[:200]}")

# Sitemap / course listing
print("\n=== SITEMAP ===")
r2 = requests.get('https://www.murdoch.edu.au/sitemap.xml', headers=headers, timeout=60)
if r2.status_code == 200:
    urls = re.findall(r'<loc>(https://www\.murdoch\.edu\.au/study/courses/[^<]+)</loc>', r2.text)
    print(f"  Course URLs found: {len(urls)}")
    for u in urls[:5]:
        print(f"    {u}")
else:
    print(f"  Status: {r2.status_code}")
