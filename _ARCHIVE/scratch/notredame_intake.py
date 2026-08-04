"""Notre Dame - fix intake detection."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

url = 'https://www.notredame.edu.au/programs/school-of-nursing/undergraduate/bachelor-of-nursing'
r = curl.get(url, impersonate='chrome120', timeout=30)
body = r.text
s = BeautifulSoup(body, 'html.parser')

# Check all meta tags related to intake/start/commencement/semester
for m in s.find_all('meta'):
    name = m.get('name','')
    content = m.get('content','')
    if any(k in (name or '').lower() for k in ['commence', 'semester', 'session', 'intake', 'start_date', 'program.start']):
        print(f'Meta [{name}] = [{content}]')

# Also check <meta name="programs.commencement">
meta_com = s.find('meta', attrs={'name': lambda x: x and 'commence' in (x or '').lower()})
if meta_com:
    print(f'Found: {meta_com["name"]} = {meta_com["content"]}')
    # months
    text = meta_com['content']
    months = ['January','February','March','April','May','June',
              'July','August','September','October','November','December']
    for m in months:
        if re.search(rf'\b{m}\b', text, re.I):
            print(f'  Month: {m}')
    # semester
    if re.search(r'Semester\s+1', text):
        print(f'  Semester 1 -> Jan/Feb')
    if re.search(r'Semester\s+2', text):
        print(f'  Semester 2 -> July')

# Also check visible page text
txt = s.get_text(' ', strip=True)
for m in re.finditer(r'(commence|start date|intake).{0,40}', txt, re.I):
    t = m.group()[:60]
    if any(k in t.lower() for k in ['semester', 'feb', 'jul', 'jan', 'mar']):
        print(f'Text: {t}')
