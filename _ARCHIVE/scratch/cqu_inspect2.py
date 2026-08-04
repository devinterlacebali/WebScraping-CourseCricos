"""CQU course page inspection."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

# Test specific course pages
for url in [
    'https://www.cqu.edu.au/courses/cu58/bachelor-of-nursing',
    'https://www.cqu.edu.au/courses/cl73/bachelor-of-arts',
    'https://www.cqu.edu.au/courses/cq48/master-of-business-administration',
]:
    r = curl.get(url, impersonate='chrome120', timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.get_text()

    print(f'=== {url.split("/")[-1]} ===')
    print(f'Status: {r.status_code}, Size: {len(r.text)}b')
    print(f'Title: {soup.title.string.strip() if soup.title else "none"}')
    
    # Find course data in scripts
    for s in soup.find_all('script'):
        if s.string and ('course' in s.string.lower() or 'jss' in s.string.lower() or 'routing' in s.string.lower()):
            # Look for __NEXT_DATA__ or jss data
            if '"cricos"' in s.string.lower() or 'cricoscode' in s.string.lower():
                print(f'  FOUND CRICOS in script')
                for m in re.finditer(r'cricos[\w]*["\']:\s*["\'](\d{6,7}[A-Za-z]?)["\']', s.string, re.I):
                    print(f'    CRICOS: {m.group(1)}')
    
    # Check __NEXT_DATA__ specifically
    nd_match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', r.text, re.DOTALL)
    if nd_match:
        nd = json.loads(nd_match.group(1))
        props = nd.get('props', {}).get('pageProps', {})
        component_props = props.get('componentProps', {})
        # Search for cricos in all string values
        def find_cricos(obj, path=''):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, str) and re.match(r'^\d{6,7}[A-Za-z]?$', v):
                        print(f'  CRICOS candidate at {path}.{k}: {v}')
                    find_cricos(v, f'{path}.{k}')
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    find_cricos(v, f'{path}[{i}]')
        find_cricos(props)
    
    # Meta tags for CRICOS
    for m in soup.find_all('meta'):
        if 'cricos' in m.get('name', '').lower() or 'cricos' in m.get('property', '').lower():
            print(f'  Meta CRICOS: {m.get("content")}')
    
    # Duration/fee/intake from body
    for pat in ['Duration', 'Fee', 'Intake', 'Start', 'CRICOS', 'Tuition', 'cricos', 'semester']:
        for m in re.finditer(r'.{0,40}' + pat + r'.{0,60}', body, re.I):
            val = m.group().strip()
            if any(bad in val.lower() for bad in ['error', 'menu', 'footer', 'nav', 'search']):
                continue
            if 15 < len(val) < 200:
                print(f'  [{pat}]: {val[:120]}')
    
    # Headings
    print(f'  H1: {soup.find("h1").get_text(strip=True) if soup.find("h1") else "none"}')
    for h in soup.find_all(['h2','h3'])[:6]:
        t = h.get_text(strip=True)[:60]
        if t:
            print(f'  {h.name}: {t}')
    print()
