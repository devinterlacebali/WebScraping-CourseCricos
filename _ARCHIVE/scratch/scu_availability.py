"""Explore the Availability & Fees tables on course pages with JavaScript year selector."""
from curl_cffi import requests
from bs4 import BeautifulSoup
import json, re

# Test both 2026 and 2027 URLs
urls = [
    'https://www.scu.edu.au/study/courses/diploma-of-business-2127279/2026/',
    'https://www.scu.edu.au/study/courses/diploma-of-business-2127279/',
]

for url in urls:
    print(f'\n{"="*60}')
    print(f'URL: {url}')
    r = requests.get(url, impersonate='chrome124')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Look for Availability and fees table
    print('\n--- Availability/Fees tables ---')
    tables = soup.find_all('table')
    print(f'Total tables: {len(tables)}')
    for i, table in enumerate(tables):
        caption = table.find('caption')
        caption_text = caption.get_text(strip=True) if caption else ''
        if 'fee' in caption_text.lower() or 'avail' in caption_text.lower() or 'cricos' in caption_text.lower():
            print(f'\nTable {i}: {caption_text}')
            # Print header row
            thead = table.find('thead')
            if thead:
                headers = [th.get_text(strip=True) for th in thead.find_all('th')]
                print(f'  Headers: {headers}')
            tbody = table.find('tbody')
            if tbody:
                rows = tbody.find_all('tr')
                for row in rows[:10]:
                    cells = [td.get_text(strip=True) for td in row.find_all('td')]
                    print(f'  Row: {cells}')
    
    # Look for the course-snapshot section more carefully
    print('\n--- Course Snapshot ---')
    snapshot = soup.find('div', class_='course-snapshot')
    if snapshot:
        print(snapshot.get_text(strip=True)[:500])
    
    # Check for the dom_snapshot_fee element
    fee_elem = soup.find(id='dom_snapshot_fee')
    if fee_elem:
        print(f'\nDomestic fee: {fee_elem.get_text(strip=True)}')
    
    # Look for int snapshot
    int_snapshot = soup.find(string=re.compile(r'International snapshot'))
    if int_snapshot:
        parent = int_snapshot.find_parent('div')
        if parent:
            print(f'\nInternational snapshot: {parent.get_text(strip=True)[:300]}')
    
    # Check the accordion sections
    print('\n--- Accordion: Overview sections ---')
    accordion = soup.find_all('div', class_='accordion-item')
    for item in accordion:
        header = item.find(['h2', 'h3'])
        header_text = header.get_text(strip=True)[:80] if header else ''
        body = item.find('div', class_='accordion-body')
        body_text = body.get_text(strip=True)[:200] if body else ''
        if any(x in (header_text+body_text).lower() for x in ['location', 'teaching', 'term', 'fee', 'cricos']):
            print(f'\n  Accordion: {header_text}')
            print(f'  Body: {body_text}')

    # Find the Availability and fees content via JS selector
    print('\n--- Location/Teaching Period tables ---')
    for div in soup.find_all('div', class_='js-course-selector-content'):
        header_text = ''
        prev = div.find_previous(['h2', 'h3', 'h4'])
        if prev:
            header_text = prev.get_text(strip=True)
        content = div.get_text(strip=True)[:300]
        if any(x in content.lower() for x in ['location', 'brisbane', 'gold', 'coffs', 'lismore', 'term', 'fee', 'cricos']):
            print(f'\n  Section: {header_text}')
            print(f'  Content: {content}')
