"""Check ECU footer for provider code."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

r = curl.get('https://www.ecu.edu.au', impersonate='chrome120', timeout=20)
footer = BeautifulSoup(r.text, 'html.parser').find('footer')
if footer:
    ft = footer.get_text()
    for m in re.finditer(r'CRICOS|PRISMS|Provider|002', ft):
        ctx = ft[max(0,m.start()-30):m.end()+40]
        print(f'  {ctx.strip()[:100]}')
else:
    print('no footer found')
    # Search full text
    body = re.sub(r'\s+', ' ', r.text)
    for m in re.finditer(r'CRICOS.{0,50}\d{5,7}[A-Z]', body):
        print(f'  {m.group()[:100]}')
