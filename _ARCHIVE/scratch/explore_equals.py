import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

urls = [
    'https://equals.edu.au/courses/nursing-health/diploma-of-nursing/',
    'https://equals.edu.au/courses/social-work-and-community/diploma-of-community-services/',
    'https://equals.edu.au/courses/social-work-and-community/bachelor-of-human-services/',
    'https://equals.edu.au/courses/nursing-health/advanced-diploma-of-nursing/',
    'https://equals.edu.au/courses/nursing-health/certificate-iii-in-pathology/',
    'https://equals.edu.au/courses/social-work-and-community/diploma-of-early-childhood-education-and-care/',
]
for url in urls:
    r = curl.get(url, impersonate='chrome120', timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = url.split("/")[-2]
    print(f"\n=== {title} ===")
    
    h2 = soup.find('h2')
    print(f"  Course (h2): {h2.get_text(strip=True) if h2 else 'N/A'}")
    
    li = soup.find('li', class_='international-exclusive')
    if li:
        m = re.search(r'CRICOS.*?:\s*(\d{6}[A-Za-z])', li.get_text())
        print(f"  CRICOS: {m.group(1) if m else li.get_text(strip=True)}")
    
    cinfo = soup.find('div', class_='course-info')
    if cinfo:
        t = cinfo.get_text(strip=True)
        print(f"  Raw course-info: {t[:300]}")
        # Duration
        dm = re.search(r'Duration\s*([\d\s]+?)(?:week|year|month)', t, re.I)
        if dm:
            dur_match = re.search(r'Duration\s*([\d\s]+(?:to\s*[\d\s]+)?)\s*(week|year|month)', t, re.I)
            if dur_match:
                print(f"  Duration: {dur_match.group(1).strip()} {dur_match.group(2)}")
        # Fee 
        fm = re.search(r'\$([\d,]+)', t)
        if fm:
            print(f"  Fee found: ${fm.group(1)}")
        # Intake
        im = re.search(r'Intakes?\s*([\w\s|,]+)', t, re.I)
        if im:
            print(f"  Intake: {im.group(1).strip()}")
    
    # Also check for international fee specifically 
    fee_table = soup.find('table')
    if fee_table:
        rows = fee_table.find_all('tr')
        for row in rows:
            cells = row.find_all(['td','th'])
            text = ' | '.join(c.get_text(strip=True) for c in cells)
            if 'international' in text.lower() or 'tuition' in text.lower():
                print(f"  Table row: {text}")
