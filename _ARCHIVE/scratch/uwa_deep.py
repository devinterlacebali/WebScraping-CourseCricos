"""Deep dive UWA course page structure for scraper design."""
import requests, re, json
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = 'https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours'
r = requests.get(url, headers=headers, timeout=30)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

print("=== H2 HEADINGS ===")
for h in soup.find_all('h2'):
    txt = h.get_text(strip=True)
    if txt:
        print(" ", txt)

print("\n=== H3 HEADINGS ===")
for h in soup.find_all('h3'):
    txt = h.get_text(strip=True)[:80]
    if txt:
        print(" ", txt)

# JSON-LD
print("\n=== JSON-LD ===")
for script in soup.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(script.string)
        print(json.dumps(data, indent=2)[:2000])
    except:
        pass

# Framework data
print("\n=== FRAMEWORK DATA ===")
for script in soup.find_all('script'):
    txt = script.string or ''
    if '__NEXT_DATA__' in txt or '__NUXT__' in txt or 'window.__' in txt:
        print("Found framework script, len=", len(txt))
        print(txt[:500])
        break
    if 'DigitalDataLayer' in txt or 'digitalData' in txt or 'Sitecore' in txt:
        print("Found Sitecore data, len=", len(txt))
        print(txt[:500])
        break

# Look for course data in data attributes
print("\n=== DATA ATTRIBUTES ===")
for el in soup.find_all(attrs={"data-course-id": True}):
    print(" data-course-id:", el.get("data-course-id"))

for el in soup.find_all(attrs={"data-cricos": True}):
    print(" data-cricos:", el.get("data-cricos"))

# Check for hidden span with CRICOS
print("\n=== CRICOS SEARCH ===")
for m in re.finditer(r'\b(\d{6,7}[A-Za-z]?)\b', html):
    start = max(0, m.start() - 40)
    ctx = html[start:m.end() + 40]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f"  {m.group(1)}: {clean[:120]}")

# Fee
print("\n=== FEE SEARCH ===")
for m in re.finditer(r'\$[0-9,]+', html):
    start = max(0, m.start() - 80)
    ctx = html[start:m.end() + 80]
    clean = re.sub(r'\s+', ' ', ctx)
    if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'indicative', 'annual']):
        print(" ", clean[:250])

# Duration
print("\n=== DURATION ===")
for m in re.finditer(r'(\d+\.?\d*)\s*(year|month|week)', html, re.I):
    start = max(0, m.start() - 40)
    ctx = html[start:m.end() + 40]
    clean = re.sub(r'\s+', ' ', ctx)
    print(" ", clean[:150])
