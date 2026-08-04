"""Check which ECU course URLs are valid."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.ecu.edu.au'

r = curl.get(DOMAIN + '/sitemap.courses.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
N = min(len(urls), 250)

valid = 0
invalid = 0
seen_slugs = set()
for i, url in enumerate(urls, 1):
    slug = url.rstrip('/').split('/')[-1]
    if slug in seen_slugs:
        invalid += 1
        continue
    seen_slugs.add(slug)
    
    try:
        rp = curl.get(url, impersonate='chrome120', timeout=15)
        sp = BeautifulSoup(rp.text, 'html.parser')
        h1 = sp.find('h1')
        title = h1.get_text(strip=True)[:50] if h1 else 'none'
        body = re.sub(r"\s+", " ", sp.get_text())
        has_cricos = bool(re.search(r'CRICOS[^\d]*\d{6,7}', body))
        has_fee = bool(re.search(r'AUD\s*\$?\s*[0-9,]{4,}', body))
        has_dur = bool(re.search(r'\d+\s*(year|month)\s', body))
        has_about = 'About this Course' in body
        
        if ('Supplemental' in title or not has_cricos) and not has_about:
            invalid += 1
            if i <= 10:
                print(f'  ❌ [{i}] {title[:40]} | {slug[:40]}')
        else:
            valid += 1
            if i <= 15 or valid <= 5:
                print(f'  ✅ [{i}] {title[:40]} | CRICOS={has_cricos} Fee={has_fee} Dur={has_dur}')
    except Exception as e:
        invalid += 1
        if i <= 10:
            print(f'  ⚠️ [{i}] {slug[:40]} | {str(e)[:50]}')

print(f'\n✅ Valid: {valid}, ❌ Invalid: {invalid}, Total: {len(seen_slugs)}')
