"""Explore Victoria University website structure."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

url = 'https://www.vu.edu.au/courses/bachelor-of-laws-graduate-entry-blge/international'
r = requests.get(url, headers=headers, timeout=60)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

print("Status:", r.status_code)
print("Title:", soup.find('title').get_text(strip=True) if soup.find('title') else '')
print()

# Check for meta tags
print("=== META TAGS ===")
for meta in soup.find_all('meta'):
    name = meta.get('name', '') or meta.get('property', '') or meta.get('itemprop', '')
    content = meta.get('content', '')
    if content and name:
        print(" ", name, ":", content[:100])

# Check CRICOS
print("\n=== CRICOS SEARCH ===")
for span in soup.find_all('span'):
    text = span.get_text(strip=True)
    if re.match(r'^[0-9]{6,7}[A-Za-z]?$', text):
        print("  CRICOS span:", text)

# Check for key divs
print("\n=== SECTIONS ===")
for div_id in ['overview', 'entry-requirements', 'course-structure', 'fees', 'how-to-apply']:
    el = soup.find(id=div_id) or soup.find('div', id=div_id) or soup.find('section', id=div_id)
    if el:
        print("  #" + div_id + ": FOUND")

# Fee info 
print("\n=== FEE SEARCH ===")
body = soup.get_text()
# Search for dollar amounts with context
for m in re.finditer(r'\$[0-9,]+', body):
    start = max(0, m.start() - 80)
    ctx = body[start:m.end() + 80].strip()
    ctx_clean = re.sub(r'\s+', ' ', ctx)
    if any(kw in ctx_clean.lower() for kw in ['fee', 'tuition', 'cost', 'international', 'total', 'annual', 'year']):
        print("  ->", ctx_clean[:250])

# Check what's in the driver xlsx links
print("\n=== DUMP ALL COURSE PAGE STRUCTURE ===")
# Check overview div
overview = soup.select_one('div#overview')
if overview:
    print("Overview HTML (first 500):", str(overview)[:500])
else:
    # Look for main content
    for cls in ['content', 'main', 'article', 'body']:
        el = soup.find('div', class_=lambda x: x and cls in x)
        if el:
            print("Found div with class containing " + cls)
            break
