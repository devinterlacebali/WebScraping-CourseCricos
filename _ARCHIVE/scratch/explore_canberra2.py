"""Deep dive UC Canberra course page."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = 'https://www.canberra.edu.au/course/bachelor-of-nursing'
r = requests.get(url, headers=headers, timeout=60)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

print("Status:", r.status_code)
print("Title:", soup.find('title').get_text(strip=True) if soup.find('title') else '')

# Meta
print("\n=== META ===")
for meta in soup.find_all('meta'):
    name = meta.get('name','') or meta.get('property','')
    content = meta.get('content','')
    if content and name and len(content) < 300:
        if any(kw in name.lower() for kw in ['cricos', 'description', 'title']):
            print(" ", name, ":", content[:150])

# CRICOS
print("\n=== CRICOS ===")
for m in re.finditer(r'CRICOS|cricos|00212K', html):
    start = max(0, m.start() - 50)
    ctx = html[start:m.end() + 80]
    print(" ", re.sub(r'\s+', ' ', ctx)[:150])

# Fee
print("\n=== FEE ===")
for m in re.finditer(r'\$[0-9,]+', html):
    start = max(0, m.start() - 80)
    ctx = html[start:m.end() + 80]
    clean = re.sub(r'\s+', ' ', ctx)
    if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'indicative', 'annual']):
        print(" ", clean[:250])

# Duration
print("\n=== DURATION ===")
for m in re.finditer(r'(\d+)\s*(year|month|week)', html, re.I):
    start = max(0, m.start() - 30)
    ctx = html[start:m.end() + 30]
    print(" ", re.sub(r'\s+', ' ', ctx)[:150])

# Sections
print("\n=== SECTIONS ===")
for h in soup.find_all(['h2', 'h3', 'h4']):
    txt = h.get_text(strip=True)
    if txt and len(txt) > 5 and len(txt) < 100:
        print(" ", h.name, ":", txt[:80])

# Intake
print("\n=== INTAKE ===")
for m in re.finditer(r'(February|July|Semester|Intake|March)', html):
    start = max(0, m.start() - 30)
    ctx = html[start:m.end() + 30]
    print(" ", re.sub(r'\s+', ' ', ctx)[:150])

# Main
print("\n=== MAIN ===")
main = soup.find('main') or soup.find('div', class_=re.compile(r'content|main|course'))
if main:
    print(" First 500:", main.text[:500])
