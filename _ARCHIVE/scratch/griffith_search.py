"""Check Griffith page HTML for course data."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

# Search API / program search
for url in [
    'https://www.griffith.edu.au/study/degrees',
    'https://www.griffith.edu.au/study/courses',
    'https://www.griffith.edu.au/study/degrees/bachelor-of-nursing',
    'https://www.griffith.edu.au/study/degrees/bachelor-of-nursing-2036',
]:
    r = curl.get(url, impersonate='chrome120', timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(f'=== {url} ===')
    print(f'Status: {r.status_code}, Size: {len(r.text)}b')
    
    # Skip listing pages - focus on actual degree pages
    if url == r.url and r.status_code == 200:
        # Check for degree content
        has_degree_data = False
        for kw in ['CRICOS', 'cricos', 'program', 'duration', 'degree name']:
            if kw in r.text:
                has_degree_data = True
                break
        
        h1 = soup.find('h1')
        h1_text = h1.get_text(strip=True) if h1 else 'none'
        
        # Check for link list - search for degree links in HTML
        links = soup.find_all('a', href=True)
        degree_urls = [a['href'] for a in links if '/study/degrees/' in a['href'] and not a['href'].endswith('/study/degrees')]
        degree_urls = sorted(set(degree_urls))
        
        print(f'H1: {h1_text}')
        print(f'Degree links: {len(degree_urls)}')
        if degree_urls:
            for d in degree_urls[:5]:
                print(f'  {d}')
        
        if has_degree_data:
            print('✅ Has degree content')
            # Meta
            for m in soup.find_all('meta'):
                n = m.get('name','') or m.get('property','') or ''
                c = m.get('content','')
                if any(kw in n.lower() for kw in ['cricos','duration','desc','fee']):
                    print(f'  Meta {n}: {c[:150]}')
    
    print()

# Also try to find program search API
for url in [
    'https://www.griffith.edu.au/api/programs',
    'https://www.griffith.edu.au/api/courses',
    'https://www.griffith.edu.au/programs/api/search',
]:
    r = curl.get(url, impersonate='chrome120', timeout=15)
    print(f'API {url}: {r.status_code}, {len(r.text)}b')
    if r.status_code == 200 and 'json' in r.headers.get('content-type', ''):
        try:
            data = r.json()
            if isinstance(data, list):
                print(f'  List of {len(data)} items')
        except: pass
