"""Debug UC description extraction - better approach."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 ...'}
url = 'https://www.canberra.edu.au/course/364JA/2/2027'
r = requests.get(url, headers=H, timeout=20)
soup = BeautifulSoup(r.text, 'html.parser')

# Find the content-wrapper area
cw = soup.find('div', class_='content-wrapper')
if cw:
    print('=== CONTENT WRAPPER FULL ===')
    print(cw.get_text(strip=True)[:500])
    print()

# Find course-details sections
cds = soup.find_all('div', class_=re.compile(r'course-details'))
print(f'Course-details sections: {len(cds)}')
for i, c in enumerate(cds):
    # Check if it's inside an accordion
    parent_acc = c.find_parent('div', class_=re.compile(r'accordion|bs-accordion'))
    if parent_acc:
        acc_label = parent_acc.find(['h3', 'h4'])
        acc_name = acc_label.get_text(strip=True) if acc_label else '?'
        print(f'  [{i}] ACCORDION: {acc_name}')
    else:
        print(f'  [{i}] STANDALONE: {c.get_text(strip=True)[:200]}')

# Find the first standalone content section
print('\n=== FIRST STANDALONE SECTION ===')
# Look for the tab-content div that isn't in an accordion
tabs = soup.find_all('div', class_='tab-content')
for tab in tabs:
    parent = tab.find_parent('div', class_=re.compile(r'accordion', re.I))
    if not parent:
        txt = tab.get_text(strip=True)[:300]
        print(f'  Standalone tab-content: {txt}')

# Get plain-text description from the first area
print('\n=== FIRST INTRO PARAGRAPHS ===')
first_p = soup.find('div', class_='content-wrapper')
if first_p:
    ps = first_p.find_all('p')
    for p in ps[:5]:
        print(f'  {p.get_text(strip=True)[:150]}')
