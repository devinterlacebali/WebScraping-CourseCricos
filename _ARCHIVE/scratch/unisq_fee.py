"""Find international fee on UniSQ."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

u = 'https://www.unisq.edu.au/study/degrees-and-courses/bachelor-of-nursing'
r = curl.get(u, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
raw = r.text

# Check the Fees accordion for international content
idx = raw.lower().find('international student')
print(f'International student index: {idx}')
if idx >= 0:
    block = raw[idx:idx+5000]
    print('Block around International student:')
    print(block[:2000])

# Also check for the btn-group Domestic/International toggle  
print('\n=== DOMESTIC/INTERNATIONAL TOGGLE ===')
for div in soup.find_all('div', class_=lambda c: c and 'btn-group' in str(c)):
    print(f'  Found btn-group: {div.get_text(strip=True)[:100]}')
    btns = div.find_all(['button', 'a', 'label'])
    for btn in btns:
        txt = btn.get_text(strip=True)
        target = btn.get('data-bs-target', btn.get('href', ''))
        print(f'    {txt}: target={target}')

# Search for any input[type=radio] that controls tabs
for inp in soup.find_all('input'):
    if inp.get('type') == 'radio':
        name = inp.get('name', '')
        idd = inp.get('id', '')
        val = inp.get('value', '')
        print(f'  Input radio: id={idd}, name={name}, value={val}')
        # Check label for this input
        label = soup.find('label', attrs={'for': idd}) or soup.find('label', string=re.compile(inp.get('id','').replace('-','\-')))
        if label:
            print(f'    Label: {label.get_text(strip=True)[:30]}')
