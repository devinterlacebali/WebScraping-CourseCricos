"""Deep inspect UniSQ degree page HTML structure for fee/duration/CRICOS."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

u = 'https://www.unisq.edu.au/study/degrees-and-courses/bachelor-of-nursing'
r = curl.get(u, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')

# Find fee, duration, start, cricos in the page
# Look for key-value pair containers
print("=== Looking for data containers ===")
# Check all elements with text containing these keywords
for el in soup.find_all(['li', 'span', 'div', 'p', 'dt', 'dd', 'td', 'th']):
    txt = el.get_text(strip=True)
    low = txt.lower()
    if any(kw in low for kw in ['fees', 'international', 'tuition', 'cricos', 'duration', 'start:', 'intake:', 'qtac code:', 'degree code:', 'program code:']):
        if len(txt) > 5 and len(txt) < 200:
            print(f'  [{el.name}.{el.get("class", "")}]: {txt[:150]}')

# Check the top summary/hero section  
print("\n=== Hero/summary area ===")
for el in soup.find_all(['div', 'section'], class_=lambda c: c and any(x in str(c).lower() for x in ['hero', 'summary', 'intro', 'banner', 'header', 'degree'])):
    txt = el.get_text(strip=True)[:300]
    if len(txt) > 20:
        print(f'  {txt[:200]}')

# Check all dl/dt/dd lists
print("\n=== Definition lists ===")
for dl in soup.find_all('dl'):
    txt = dl.get_text(strip=True)[:200]
    if any(kw in txt.lower() for kw in ['fee', 'cricos', 'duration', 'start', 'qtac']):
        print(f'  {txt[:200]}')

# Check tables
print("\n=== Tables ===")
for table in soup.find_all('table'):
    txt = table.get_text(strip=True)[:200]
    if any(kw in txt.lower() for kw in ['fee', 'cricos', 'duration', 'qtac']):
        print(f'  {txt[:200]}')

# Look for fee accordion
print("\n=== Fee accordion ===")
for el in soup.find_all(string=re.compile(r'Fees and scholarships', re.I)):
    parent = el.find_parent(['h2','h3','h4','div','section'])
    if parent:
        # Get siblings for next ~5 elements
        sib = parent.find_next_siblings(['p','div','section','ul','table'])
        for s in sib[:10]:
            t = s.get_text(strip=True)[:200]
            if t:
                print(f'  {t}')
                if 'International' in t and '$' in t:
                    for m in re.finditer(r'\$([0-9,]+)', t):
                        print(f'    fee: ${m.group(1)}')

# Look for placeholder or JSON data in head
print("\n=== Head scripts ===")
for s in soup.find_all('script'):
    if s.get('type') == 'application/json' or 'data' in s.get('id', '').lower():
        if s.string:
            try:
                data = json.loads(s.string)
                print(f'  JSON data keys: {list(data.keys())[:10] if isinstance(data, dict) else type(data).__name__}')
                if isinstance(data, dict):
                    for k in data:
                        if any(x in k.lower() for x in ['cricos','fee','program','course','degree']):
                            print(f'    {k}: {str(data[k])[:200]}')
            except: pass

# Extract fee info from accordion-like sections
print("\n=== Fee info extraction ===")
# Find the fees section
fees_heading = soup.find(['h2','h3'], string=re.compile(r'Fees and scholarships', re.I))
if fees_heading:
    fee_section = fees_heading.find_parent(['div','section'])
    if not fee_section:
        fee_section = fees_heading.parent
    fee_text = fee_section.get_text() if fee_section else ''
    # Look for international fee
    for part in re.split(r'(?=International)', fee_text):
        if 'International' in part:
            for m in re.finditer(r'\$([0-9,]+)', part):
                ctx = part[max(0,m.start()-20):m.end()+40]
                print(f'    ${m.group(1)} | ctx: {ctx.strip()[:100]}')

# Look specifically for the fee amount display
print("\n=== Raw fee area ===")
for m in re.finditer(r'(?:AU\$|\$)[0-9,]+', soup.get_text()):
    ctx = soup.get_text()[max(0,m.start()-30):m.end()+30]
    print(f'  {m.group()} | {ctx.strip()[:100]}')
