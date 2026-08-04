"""Deep dive VU fee and entry requirements."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Test both /international and non-international
urls = [
    ('https://www.vu.edu.au/courses/bachelor-of-laws-graduate-entry-blge/international', 'International'),
    ('https://www.vu.edu.au/courses/bachelor-of-laws-graduate-entry-blge', 'Domestic'),
]

for url, label in urls:
    print(f"\n{'='*60}")
    print(f"{label}: {url}")
    print('='*60)
    
    r = requests.get(url, headers=headers, timeout=60)
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.get_text()
    
    # Fee section - find the block with fee info
    fee_heading = soup.find('h2', string=re.compile(r'[Ff]ee'))
    if not fee_heading:
        fee_heading = soup.find(['h2','h3'], string=re.compile(r'[Ff]ees and'))
    if fee_heading:
        print(f"\n  Fee heading: '{fee_heading.get_text(strip=True)}'")
        # Get content after it
        parent = fee_heading.find_parent('section') or fee_heading.find_parent('[class*="fee"]')
        if not parent:
            parent = fee_heading.parent
        parent_text = parent.get_text()
        for m in re.finditer(r'\$[0-9,]+', parent_text):
            start = max(0, m.start() - 50)
            ctx = parent_text[start:m.end()+80].strip()
            ctx = re.sub(r'\s+', ' ', ctx)
            print(f"    -> {ctx[:200]}")
    
    # Also just dump generic fee context
    print(f"\n  All fee-related text:")
    for m in re.finditer(r'\$[0-9,]+', body):
        start = max(0, m.start() - 60)
        ctx = body[start:m.end()+60].strip()
        ctx = re.sub(r'\s+', ' ', ctx)
        if any(kw in ctx.lower() for kw in ['fee', 'tuition', 'semester', 'annual', 'total', 'international', 'cost']):
            print(f"    -> {ctx[:200]}")
    
    # Duration
    print(f"\n  Duration text:")
    for m in re.finditer(r'(\d+\.?\d*)\s*(year|semester|month|week)', body, re.I):
        start = max(0, m.start() - 40)
        ctx = body[start:m.end()+60].strip()
        ctx = re.sub(r'\s+', ' ', ctx)
        print(f"    -> {ctx[:200]}")
    
    # Entry requirements
    entry = soup.select_one('#entry-requirements')
    if entry:
        texts = entry.get_text(strip=True)[:200]
        print(f"\n  Entry requirements (first 200): {texts}")
    else:
        print("\n  #entry-requirements: NOT FOUND")
