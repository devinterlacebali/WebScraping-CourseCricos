"""Explore Think.edu.au."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

base = 'https://www.think.edu.au'

# Check main page + sitemap
for url in [base, f'{base}/sitemap.xml', f'{base}/courses']:
    try:
        r = curl.get(url, impersonate='chrome120', timeout=30)
        print(f'{url}: status={r.status_code}, size={len(r.text)}b')
        if 'text/html' in r.headers.get('content-type',''):
            soup = BeautifulSoup(r.text, 'html.parser')
            h1 = soup.find('h1')
            print(f'  H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
        if r.status_code == 200:
            # Just show first 300 chars as text
            text = re.sub(r'\s+', ' ', soup.get_text())[:300] if 'html' in r.headers.get('content-type','') else r.text[:300]
            print(f'  Text: {text[:200]}')
    except Exception as e:
        print(f'{url}: ERROR {e}')
    print()
