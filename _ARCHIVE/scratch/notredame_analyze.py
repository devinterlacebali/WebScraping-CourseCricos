"""Notre Dame - full page analysis."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

url = 'https://www.notredame.edu.au/programs/school-of-nursing/undergraduate/bachelor-of-nursing'
r = curl.get(url, impersonate='chrome120', timeout=30)
body = r.text
s = BeautifulSoup(body, 'html.parser')

# All meta tags
for m in s.find_all('meta'):
    name = m.get('name','')
    content = m.get('content','')
    if name or content:
        print(f'Meta [name={name}][content={content[:120]}]')

# Check JSON-LD @graph
for sc in s.select('script[type="application/ld+json"]'):
    try:
        d = json.loads(sc.string or '{}')
        if '@graph' in d:
            for item in d['@graph']:
                if isinstance(item, dict) and item.get('@type') in ('WebPage', 'Course'):
                    print(f'Graph @type: {item.get("@type")}: {list(item.keys())[:10]}')
                    if 'identifier' in item:
                        print(f'  identifier: {item["identifier"]}')
                    if 'offers' in item:
                        print(f'  offers: {item["offers"]}')
        else:
            print(f'JSON-LD keys: {list(d.keys())[:10]}')
    except: pass

# Check div/program-detail sections
for el in s.find_all(class_=lambda c: c and ('program' in c.lower() or 'course' in c.lower() or 'detail' in c.lower())):
    cls = ' '.join(el.get('class',[]))
    txt = el.get_text(strip=True)[:100]
    if len(txt) > 20:
        print(f'Section [.{cls}]: {txt[:80]}')

# Check fee in text
for m in re.finditer(r'(?:fee|cost|tuition|price|international)\s*.*?\$[\s,0-9]+', body, re.I):
    txt = re.sub(r'\s+', ' ', m.group())[:100]
    if not re.search(r'background|margin|padding|font', txt, re.I):
        print(f'Fee text: {txt}')
