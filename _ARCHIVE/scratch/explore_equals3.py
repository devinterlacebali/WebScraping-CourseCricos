import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

# EQUALS - extract fees more carefully
urls = [
    'https://equals.edu.au/courses/nursing-health/diploma-of-nursing/',
    'https://equals.edu.au/courses/social-work-and-community/diploma-of-community-services/',
    'https://equals.edu.au/courses/social-work-and-community/bachelor-of-human-services/',
    'https://equals.edu.au/courses/nursing-health/advanced-diploma-of-nursing/',
    'https://equals.edu.au/courses/nursing-health/certificate-iii-in-pathology/',
    'https://equals.edu.au/courses/social-work-and-community/diploma-of-early-childhood-education-and-care/',
    'https://equals.edu.au/courses/social-work-and-community/master-of-social-work-qualifying/',
    'https://equals.edu.au/courses/social-work-and-community/diploma-of-mental-health/',
    'https://equals.edu.au/courses/business-and-leadership/diploma-of-leadership-and-management/',
    'https://equals.edu.au/courses/nursing-health/certificate-iii-in-individual-support-ageing-and-disability/',
]
for url in urls:
    r = curl.get(url, impersonate='chrome120', timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = url.split("/")[-2]
    print(f"\n=== {title} ===")
    
    h2 = soup.find('h2')
    print(f"  Course: {h2.get_text(strip=True) if h2 else 'N/A'}")
    
    # Get international fee from tables
    tables = soup.find_all('table')
    for i, table in enumerate(tables):
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['td','th'])
            text = ' | '.join(c.get_text(strip=True) for c in cells)
            if 'international' in text.lower() or 'non-subsidised' in text.lower() or 'full fee' in text.lower():
                print(f"  Table {i}: {text}")
            # Any row with $ and international context
            if '$' in text and ('international' in text.lower() or 'non' in text.lower()):
                print(f"  Table {i} fee: {text}")
    
    # Also check for fee in course-info-row 2nd dollar amount (international)
    cinfo = soup.find('div', class_='course-info')
    if cinfo:
        t = cinfo.get_text(strip=True)
        dollars = re.findall(r'\$([\d,]+)', t)
        print(f"  Dollar amounts in course-info: {dollars}")
        # Usually the LAST dollar amount is the international fee
        # or the one with commas
    
    # Find "International" section for fees
    for div in soup.find_all('div'):
        t = div.get_text(strip=True)
        if 'International' in t and '$' in t and len(t) < 500:
            print(f"  International fee div: {t[:300]}")
    
    # Find the fee section content
    fee_section = soup.find(id='fees-and-funding-options')
    if fee_section:
        t = fee_section.get_text(strip=True)[:500]
        dollars = re.findall(r'\$([\d,]+)', t)
        print(f"  Fee section dollars: {dollars}")
    
    print(f"  Page length: {len(r.text)}")
