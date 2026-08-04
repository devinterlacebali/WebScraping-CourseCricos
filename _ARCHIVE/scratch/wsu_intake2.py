"""WSU - find intake from website."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Check the /future page which lists courses
r = curl.get(f'{DOMAIN}/future', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')
body = re.sub(r'\s+', ' ', s.get_text())

# Look for intake/session/semester mentions
for kw in ['intake', 'session', 'semester', 'start', 'commencement', 'study period']:
    for m in re.finditer(kw + r'.{0,100}', body, re.I):
        txt = m.group()[:120]
        if any(month in txt for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
            print(f'{kw}: {txt}')
            break

# Check /study page
print('\n=== /study ===')
r2 = curl.get(f'{DOMAIN}/study', impersonate='chrome120', timeout=30)
s2 = BeautifulSoup(r2.text, 'html.parser')
body2 = re.sub(r'\s+', ' ', s2.get_text())
for m in re.finditer(r'(?:intake|session|semester|start).{0,100}', body2, re.I):
    txt = m.group()[:120]
    if any(month in txt for month in ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'March', 'July']):
        print(f'  {txt}')

# Check /international 
print('\n=== /international ===')
r3 = curl.get(f'{DOMAIN}/international', impersonate='chrome120', timeout=30)
s3 = BeautifulSoup(r3.text, 'html.parser')
body3 = re.sub(r'\s+', ' ', s3.get_text())
for m in re.finditer(r'(?:intake|session|semester|start|commence).{0,100}', body3, re.I):
    txt = m.group()[:120]
    if any(month in txt for month in ['Jan', 'Feb', 'Mar', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'March', 'July']):
        print(f'  {txt}')

# Check inherent-requirements for nursing intake
print('\n=== Bachelor of Nursing page ===')
r4 = curl.get(f'{DOMAIN}/inherent-requirements/bachelor-of-nursing-inherent-requirements', impersonate='chrome120', timeout=30)
s4 = BeautifulSoup(r4.text, 'html.parser')
body4 = re.sub(r'\s+', ' ', s4.get_text())
for m in re.finditer(r'(?:intake|session|semester|start|commence).{0,100}', body4, re.I):
    print(f'  {m.group()[:120]}')

# Look for course finder link
print('\n=== Course finder link ===')
for a in s.find_all('a', href=True):
    if 'course' in a.get('href','').lower() and 'find' in a.get_text(strip=True).lower():
        print(f'  {a["href"]} — {a.get_text(strip=True)[:60]}')

# Try hie/degrees 
print('\n=== HIE degrees ===')
r5 = curl.get(f'{DOMAIN}/hie/degrees', impersonate='chrome120', timeout=30)
if r5.status_code == 200:
    s5 = BeautifulSoup(r5.text, 'html.parser')
    body5 = re.sub(r'\s+', ' ', s5.get_text())
    for m in re.finditer(r'(?:intake|session|semester|start).{0,100}', body5, re.I):
        txt = m.group()[:120]
        if any(month in txt for month in ['Jan', 'Mar', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']):
            print(f'  {txt}')
