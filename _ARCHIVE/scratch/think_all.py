"""Check Think fee structure and all course URLs."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, csv

base = 'https://www.think.edu.au'

# Check /courses for all course cards/links
r = curl.get(f'{base}/courses', impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')

# All links from courses page
all_links = set()
for a in soup.find_all('a', href=True):
    h = a['href']
    if h.startswith('/courses/') and h.count('/') >= 2:
        all_links.add(f'{base}{h}')

print('All course links:')
for u in sorted(all_links):
    print(f'  {u}')

# Check Courses dropdown in navigation for sub-categories
nav_cats = set()
for a in soup.find_all('a', href=True):
    h = a['href']
    if '/courses/' in h:
        nav_cats.add(h)

print(f'\nNavigation/sub-categories with /courses/: {nav_cats}')

# Check each course page for CRICOS, fee, etc.
print(f'\n=== Scraping all courses ===')
results = []
for url in sorted(all_links):
    slug = url.rstrip('/').split('/')[-1]
    if slug in ('course-guides',): continue
    
    rp = curl.get(url, impersonate='chrome120', timeout=15)
    sp = BeautifulSoup(rp.text, 'html.parser')
    body = re.sub(r'\s+', ' ', sp.get_text())
    
    h1 = sp.find('h1')
    title = h1.get_text(strip=True) if h1 else slug
    
    # CRICOS
    cricos = ''
    for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', body):
        cricos = m.group(1)
        break
    
    # Fee - look for actual tuition amount, not salary data
    fee = 'NULL'
    for m in re.finditer(r'(?:course fees?|tuition)[^$]{0,20}\$?\s*([0-9,]+)', body, re.I):
        val = int(m.group(1).replace(',',''))
        if 10000 < val < 200000:
            fee = str(val)
            break
    
    # Duration
    dur = ''
    for m in re.finditer(r'(\d+\.?\d*)\s*(year|month|week)\s', body, re.I):
        dur = m.group().strip()
        break
    
    # Intake months
    intake = []
    for m_name in ['January','February','March','April','May','June','July','August','September','October','November','December']:
        if m_name in body:
            intake.append(m_name)
    
    results.append({'title': title, 'cricos': cricos, 'fee': fee, 'duration': dur, 'intake': ', '.join(intake[:3]) if intake else ''})
    print(f'  {title[:45]} | CRICOS={cricos} | Fee={fee} | Dur={dur[:10]} | Intake={", ".join(intake[:3])}')

# CSV lookup
with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    csv_cricos = {}
    for row in reader:
        if row[0].strip() == '00246M' and len(row) >= 4:
            csv_cricos[row[3].strip()] = row[2].strip()

print(f'\nCRICOS CSV courses for Think: {csv_cricos}')
