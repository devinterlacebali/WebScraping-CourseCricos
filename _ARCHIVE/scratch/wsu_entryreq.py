"""WSU - check entry requirements on course page."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

for path in ['/future/study/courses/undergraduate/bachelor-of-nursing',
             '/future/study/courses/postgraduate/master-of-nursing',
             '/future/study/courses/undergraduate/bachelor-of-arts']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    s = BeautifulSoup(r.text, 'html.parser')
    body = r.text
    body_text = re.sub(r'\s+', ' ', s.get_text())
    h1 = s.find('h1')
    title = h1.get_text(strip=True) if h1 else '?'
    print(f'\n=== {title} ===')
    
    # Look for entry requirements sections
    for kw in ['entry requirement', 'admission requirement', 'academic requirement',
               'entry criteria', 'selection criteria', 'how to apply', 'english requirement']:
        for m in re.finditer(kw + r'.{0,200}', body, re.I | re.S):
            txt = re.sub(r'\s+', ' ', m.group()).strip()
            print(f'  [{kw}]: {txt[:200]}')
            break
    
    # Check data-tab="admissions"
    for el in s.find_all(attrs={'data-tab': 'admissions'}) or s.find_all(attrs={'data-tab': 'Admissions'}):
        txt = el.get_text(strip=True)[:500]
        print(f'  [data-tab=admissions]: {txt[:200]}')
    
    # Check for "Admissions" section via aria-labels or IDs
    for sel in ['#admissions', '.admissions', '[id*="admission"]', '[class*="admission"]',
                '#entry', '.entry-requirements']:
        el = s.select_one(sel) if '.' in sel or '#' in sel else None
        if el:
            txt = re.sub(r'\s+', ' ', el.get_text())[:300]
            print(f'  [{sel}]: {txt[:200]}')
    
    # Look for tab buttons/links with admissions
    for a in s.find_all('a', href=True):
        if 'admission' in a.get('href', '').lower() or 'entry' in a.get('href', '').lower():
            print(f'  [link]: {a["href"]}')
    
    # Check content after "Entry Requirements" heading
    for h in s.find_all(['h2', 'h3', 'h4']):
        txt = h.get_text(strip=True).lower()
        if any(k in txt for k in ['entry', 'admission', 'admission requirement']):
            # Get following content
            next_content = []
            for sibling in h.find_next_siblings():
                if sibling.name in ['h2', 'h3', 'h4']: break
                next_content.append(sibling.get_text(strip=True))
            full = ' '.join(next_content)[:500]
            print(f'  [heading "{txt[:30]}"]: {full[:200]}')
            break
