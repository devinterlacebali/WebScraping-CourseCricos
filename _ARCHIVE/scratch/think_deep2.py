"""Deep explore Think page for all course data."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

base = 'https://www.think.edu.au'

# Check 3 sample courses
urls = [
    f'{base}/courses/diploma-of-nursing',
    f'{base}/courses/bachelor-of-health-science-clinical-myotherapy',
    f'{base}/courses/diploma-of-counselling-and-communication-skills',
]

for url in urls:
    print(f'\n{"="*60}')
    print(f'URL: {url}')
    r = curl.get(url, impersonate='chrome120', timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    body = re.sub(r'\s+', ' ', soup.get_text())
    
    h1 = soup.find('h1')
    print(f'Title: {h1.get_text(strip=True) if h1 else "none"}')
    
    # Show all sections/headings structure
    for h in soup.find_all(['h1','h2','h3','h4']):
        txt = h.get_text(strip=True)
        if len(txt) > 3:
            print(f'  [{h.name}] {txt[:60]}')
    
    # CRICOS
    for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', body):
        print(f'\nCRICOS: {m.group(1)}')
    
    # Fee near "course fee" or "international"
    for m in re.finditer(r'(?:course fee|international|tuition|AUD).{0,30}\$\s*([0-9,]+)', body, re.I):
        val = int(m.group(1).replace(',',''))
        if val > 1000:
            print(f'Fee ({m.group()[:60]}): ${val:,}')
    
    # Duration
    for m in re.finditer(r'(\d+\.?\d*)\s*(year|month|week)\s', body, re.I):
        print(f'Duration: {m.group()}')
        break
    
    # Intake
    for m in re.finditer(r'(intake|commencement|start date|study period)[^.:]*[.:]\s*([A-Za-z,\s]+)', body, re.I):
        txt = m.group(2)[:60]
        print(f'Intake: {txt}')
    
    # Description section
    desc_section = soup.find(['h2','h3','h4'], string=re.compile(r'Overview|About', re.I))
    if desc_section:
        desc_text = ''
        for sib in desc_section.find_all_next(['p','ul','ol'], limit=5):
            if sib.name in ['p','li'] and sib.get_text(strip=True):
                desc_text += sib.get_text(strip=True)[:100] + ' '
        print(f'Description: {desc_text[:150]}')
        
    # Entry requirements
    er_section = soup.find(['h2','h3','h4'], string=re.compile(r'Entry requirements|Admission', re.I))
    if er_section:
        er_text = ''
        for sib in er_section.find_all_next(['p','ul','ol'], limit=5):
            if sib.name in ['p','li'] and sib.get_text(strip=True):
                er_text += sib.get_text(strip=True)[:100] + ' '
        print(f'Entry reqs: {er_text[:150]}')
