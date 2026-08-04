"""WSU - check course detail page for intake & CRICOS."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Check a specific course page
for path in ['/future/study/courses/postgraduate/graduate-certificate-in-accounting',
             '/future/study/courses/undergraduate/bachelor-of-nursing']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    print(f'{path}: {r.status_code}, {len(r.text)}b')
    if r.status_code == 200 and len(r.text) > 1000:
        s = BeautifulSoup(r.text, 'html.parser')
        h1 = s.find('h1')
        body = re.sub(r'\s+', ' ', s.get_text())
        print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "?"}')
        
        # CRICOS
        for m in re.finditer(r'CRICOS.{0,80}', body):
            print(f'  CRICOS: {m.group()[:100]}')
        # CRICOS code
        for m in re.finditer(r'\b\d{6,7}[A-Za-z]\b', body):
            code = m.group()
            if len(code) >= 7:
                ctx = body[max(0,m.start()-40):m.end()+40]
                print(f'  Code: {code} | ...{ctx.strip()[:80]}...')
        
        # Intake
        for kw in ['intake', 'session', 'semester', 'start date', 'commencement', 'study period']:
            for m in re.finditer(kw + r'.{0,100}', body, re.I):
                txt = m.group()[:120]
                if any(month in txt for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'March', 'July']):
                    print(f'  Intake: {txt}')
                    break
        
        # Fee 
        for m in re.finditer(r'(?:fee|cost|tuition).{0,100}(?:\$|AUD)', body, re.I):
            print(f'  Fee: {m.group()[:120]}')
        for m in re.finditer(r'AUD\s*\$?\s*[0-9,]{4,}', body):
            ctx = body[max(0,m.start()-60):m.end()+60]
            print(f'  Fee: {ctx.strip()[:120]}')
        
        # Duration
        for m in re.finditer(r'duration.{0,60}(?:\d+\s*year|\d+\s*month|\d+\s*week)', body, re.I):
            print(f'  Duration: {m.group()[:80]}')
        
        break
