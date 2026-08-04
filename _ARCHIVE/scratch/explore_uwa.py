"""Explore UWA website structure."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Try UWA course page
url = 'https://www.uwa.edu.au/study/courses/bachelor-of-nursing'
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

# CRICOS
print("\n=== CRICOS ===")
for m in re.finditer(r'cricos|CRICOS|00126G', html):
    ctx = html[max(0,m.start()-60):m.end()+80]
    print("  ", re.sub(r'\s+', ' ', ctx)[:150])

# All numbers that could be CRICOS
for m in re.finditer(r'\b(\d{6,7}[A-Za-z]?)\b', html):
    ctx = html[max(0,m.start()-30):m.end()+30]
    print("  NUM:", m.group(1), ":", re.sub(r'\s+', ' ', ctx)[:100])

# Fee
print("\n=== FEE ===")
for m in re.finditer(r'\$[0-9,]+', html):
    start = max(0, m.start() - 80)
    ctx = html[start:m.end()+80]
    clean = re.sub(r'\s+', ' ', ctx)
    if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'annual', 'total']):
        print("  ->", clean[:250])

# Duration
print("\n=== DURATION ===")
for m in re.finditer(r'(\d+\.?\d*)\s*(years?|months?|weeks?)', html, re.I):
    start = max(0, m.start()-30)
    ctx = html[start:m.end()+60]
    print("  ->", re.sub(r'\s+', ' ', ctx)[:200])

# Sitemap
print("\n=== SITEMAP ===")
r2 = requests.get('https://www.uwa.edu.au/sitemap.xml', headers=headers, timeout=30)
if r2.status_code == 200:
    urls = re.findall(r'<loc>(https://www\.uwa\.edu\.au/study/courses/[^<]+)</loc>', r2.text)
    print("  Course URLs:", len(urls))
    for u in urls[:5]:
        print("   ", u)
else:
    print("  Status:", r2.status_code)
