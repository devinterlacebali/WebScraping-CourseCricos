"""UWA - debug entry requirements extraction."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(H)

url = 'https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours'
r = S.get(url, timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
full = re.sub(r'\s+', ' ', soup.get_text())

print('=== Entry Requirements search ===')
# Check if text has entry req
if 'entry requirements' in full.lower():
    idx = full.lower().find('entry requirements')
    print(f'Found at idx {idx}: {full[idx:idx+300]}')
else:
    print('NOT FOUND in body text')

# Look for tabpanel
tabpanels = soup.find_all('div', {'role': 'tabpanel'})
print(f'\nTabpanels found: {len(tabpanels)}')
for tp in tabpanels:
    txt = tp.get_text(strip=True)[:100]
    print(f'  Tabpanel: {txt}...')

# Look for the entry tabpanel
entry_tab = soup.find(lambda t: t.name in ['div', 'section'] and 
                       t.get('role') == 'tabpanel' and 
                       ('entry' in t.get_text(strip=True).lower() or 'admission' in t.get_text(strip=True).lower()))
if entry_tab:
    print(f'\nFound entry tabpanel!')
    print(entry_tab.get_text(strip=True)[:500])
else:
    # Check for h2 exactly "Entry requirements"
    h2s = soup.find_all('h2')
    for h in h2s:
        t = h.get_text(strip=True)
        if 'entry' in t.lower():
            print(f'\nFound h2: "{t}"')
            # Get content after
            el = h.find_next_sibling()
            count = 0
            while el and count < 10:
                if el.name in ['h2', 'h3', 'h4']:
                    break
                if el.get_text(strip=True):
                    print(f'  Content: {el.get_text(strip=True)[:200]}')
                    count += 1
                el = el.find_next_sibling()

print('\n=== All h2 headings ===')
for h in soup.find_all(['h2','h3']):
    print(f'  <{h.name}>: {h.get_text(strip=True)[:80]}')
