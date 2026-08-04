"""Explore Griffith University website structure."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Test course page
url = 'https://www.griffith.edu.au/study/degrees/bachelor-of-nursing'
r = requests.get(url, headers=headers, timeout=60)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

print("Status:", r.status_code)
print("Title:", soup.find('title').get_text(strip=True) if soup.find('title') else '')
print("Length:", len(html))

if r.status_code == 200 and len(html) > 100:
    # Meta
    print("\n=== META ===")
    for meta in soup.find_all('meta'):
        name = meta.get('name','') or meta.get('property','')
        content = meta.get('content','')
        if content and name:
            if any(kw in name.lower() for kw in ['cricos', 'description']):
                print(" ", name, ":", content[:150])

    # CRICOS
    print("\n=== CRICOS ===")
    for m in re.finditer(r'CRICOS|cricos|00233E', html):
        start = max(0, m.start()-50)
        ctx = html[start:m.end()+80]
        print(" ", re.sub(r'\s+',' ',ctx)[:150])

    # Fee
    print("\n=== FEE ===")
    for m in re.finditer(r'\$[0-9,]+', html):
        start = max(0, m.start()-80)
        ctx = html[start:m.end()+80]
        clean = re.sub(r'\s+',' ',ctx)
        if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'indicative', 'annual']):
            print(" ", clean[:250])

    # Duration
    print("\n=== DURATION ===")
    for m in re.finditer(r'(\d+\.?\d*)\s*(year|month|week)', html, re.I):
        start = max(0, m.start()-30)
        ctx = html[start:m.end()+30]
        print(" ", re.sub(r'\s+',' ',ctx)[:150])

    # Sections
    print("\n=== SECTIONS ===")
    for h in soup.find_all(['h2','h3']):
        txt = h.get_text(strip=True)
        if txt and len(txt) > 3 and len(txt) < 80:
            print(" ", h.name, ":", txt)

    # Intake
    print("\n=== INTAKE ===")
    for m in re.finditer(r'(Trimester|Semester|Intake|February|July|March|October)', html):
        start = max(0, m.start()-30)
        ctx = html[start:m.end()+30]
        print(" ", re.sub(r'\s+',' ',ctx)[:150])

    # JSON-LD
    print("\n=== JSON-LD ===")
    for script in soup.find_all('script', type='application/ld+json'):
        import json
        try:
            data = json.loads(script.string)
            d = json.dumps(data, indent=2)[:1500]
            if 'course' in d.lower():
                print(d)
        except:
            pass

    # Check for data attributes with course info
    print("\n=== COURSE DATA ===")
    for el in soup.find_all(attrs={"data-course-id": True})[:3]:
        print(f"  data-course-id: {el.get('data-course-id')}")

    # Check for __NEXT_DATA__
    for script in soup.find_all('script'):
        txt = script.string or ''
        if '__NEXT_DATA__' in txt or '__NUXT__' in txt:
            print(f"  Framework data: {txt[:300]}")
            break
else:
    print("No content / client-side?")

# Sitemap
print("\n=== SITEMAP ===")
for sm in ['sitemap.xml', 'study/sitemap.xml', 'sitemap_index.xml']:
    r2 = requests.get(f'https://www.griffith.edu.au/{sm}', headers=headers, timeout=30)
    if r2.status_code == 200:
        u = re.findall(r'<loc>([^<]+)</loc>', r2.text)
        print(f"  {sm}: {len(u)} URLs")
        cu = [x for x in u if '/study/degrees/' in x.lower()]
        print(f"  Course URLs: {len(cu)}")
        for x in cu[:3]:
            print(f"    {x}")
        if not cu:
            # Check what paths exist
            paths = set()
            for x in u:
                p = x.replace('https://www.griffith.edu.au', '').split('/')
                if len(p) > 2:
                    paths.add(f"/{p[1]}/{p[2]}")
            print("  Sample paths:", sorted(paths)[:10])
        break
    else:
        print(f"  {sm}: {r2.status_code}")
