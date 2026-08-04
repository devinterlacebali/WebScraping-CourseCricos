"""Debug WSU entry requirements HTML."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'
r = curl.get(f'{DOMAIN}/future/study/courses/undergraduate/bachelor-of-nursing', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')

# Show all h2/h3/h4
print('=== Headings ===')
for h in s.find_all(['h2', 'h3', 'h4']):
    txt = h.get_text(strip=True)
    if any(k in txt.lower() for k in ['entry', 'admission', 'requirement']):
        print(f'  [{h.name}] {txt}')
        # Show surrounding HTML structure
        for sibling in h.find_next_siblings()[:3]:
            print(f'    -> {sibling.name} class={sibling.get("class", [])}')
            if sibling.name in ['div', 'p']:
                print(f'       text={sibling.get_text(strip=True)[:80]}')

# Show entry requirement section
print('\n=== Entry requirement section ===')
for h in s.find_all(['h2', 'h3', 'h4']):
    if 'entry' in h.get_text(strip=True).lower():
        print(f'Heading: {h.get_text(strip=True)}')
        div = h.find_next('div')
        if div and 'wysiwyg' in str(div.get('class', [])):
            print(f'Next div with wysiwyg: {div.get_text(strip=True)[:200]}')
        else:
            print(f'Next: {div.name if div else "None"} class={div.get("class", []) if div else "N/A"}')
        break

# Find all div.wysiwyg  
print('\n=== All wysiwyg divs ===')
for i, div in enumerate(s.find_all('div', class_=lambda c: c and 'wysiwyg' in str(c))):
    # Find preceding heading
    prev_h2 = div.find_previous(['h2', 'h3', 'h4'])
    prev_txt = prev_h2.get_text(strip=True) if prev_h2 else 'NONE'
    txt = div.get_text(strip=True)[:100]
    print(f'  Div {i}: prev heading="{prev_txt}" | text="{txt}"')
