from curl_cffi import requests
import re
from bs4 import BeautifulSoup

# Deep dive on one course page to find structured data elements
url = 'https://www.scu.edu.au/study/courses/diploma-of-business-2127279/'
r = requests.get(url, impersonate='chrome124')
soup = BeautifulSoup(r.text, 'html.parser')

print('=== Page Title ===')
print(soup.title.string if soup.title else 'N/A')

print('\n=== Meta description ===')
meta = soup.find('meta', attrs={'name': 'description'})
if meta:
    print(meta.get('content', ''))

print('\n=== Script tags (types) ===')
for s in soup.find_all('script'):
    if s.get('type') and s.get('type') != 'text/javascript':
        print(f'  type={s.get("type")}, len={len(s.string or "")}')

# Find any data attributes on key sections
print('\n=== Key course info sections ===')
for div in soup.find_all('div', class_=True):
    classes = ' '.join(div.get('class', []))
    text = div.get_text(strip=True)[:80]
    if any(x in text.lower() for x in ['cricos', 'duration', 'intake', 'start date', 'fee', 'location', 'delivery']):
        print(f'  class="{classes}" → {text}')

# Find structured tables or dl
print('\n=== Definition lists (key-value) ===')
for dl in soup.find_all('dl'):
    for dt, dd in zip(dl.find_all('dt'), dl.find_all('dd')):
        print(f'  {dt.get_text(strip=True)}: {dd.get_text(strip=True)[:100]}')

print('\n=== Tables ===')
for table in soup.find_all('table'):
    caption = table.find('caption')
    if caption:
        print(f'  Table: {caption.get_text(strip=True)[:80]}')

# Check for breadcrumb 
print('\n=== Breadcrumb ===')
nav = soup.find('nav', class_=lambda c: c and 'breadcrumb' in c.lower()) if soup else None
if nav:
    for li in nav.find_all('li'):
        print(f'  {li.get_text(strip=True)}')

# Check for JSON structured data
print('\n=== All JSON-LD ===')
for script in soup.find_all('script', type='application/ld+json'):
    if script.string:
        print(script.string[:500])
        print('...')

# Look for specific course detail sections
print('\n=== Course detail IDs ===')
for tag in soup.find_all(id=True):
    tid = tag.get('id')
    if any(x in tid.lower() for x in ['course', 'fee', 'duration', 'intake', 'cricos', 'detail', 'info', 'overview', 'about']):
        print(f'  #{tid} ({tag.name})')

# Check for International/Fees page sections
print('\n=== Domestic/International fee sections ===')
for div in soup.find_all('div', id=True):
    if 'Domestic' in div.get('id', '') or 'International' in div.get('id', '') or 'Fee' in div.get('id', ''):
        print(f'  #{div.get("id")}: {div.get_text(strip=True)[:120]}')

print('\n=== Course code / CRICOS section ===')
for tag in soup.find_all(string=re.compile(r'(?i)cricos')):
    parent = tag.parent
    print(f'  Context: {parent.get_text(strip=True)[:150]}')

print('\n=== Duration info ===')
for tag in soup.find_all(string=re.compile(r'(?i)duration')):
    parent = tag.parent
    parent_text = parent.get_text(strip=True)[:150]
    print(f'  Context: {parent_text}')
