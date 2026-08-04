import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

urls = [
    'https://www.stanleycollege.edu.au/courses/diploma-of-nursing/',
    'https://www.stanleycollege.edu.au/courses/bachelor-of-business/',
    'https://www.stanleycollege.edu.au/courses/chc52025-diploma-of-community-services/',
    'https://www.stanleycollege.edu.au/courses/chc50125-diploma-of-early-childhood-education-and-care/',
    'https://www.stanleycollege.edu.au/courses/ict50220-diploma-of-information-technology/',
    'https://www.stanleycollege.edu.au/courses/bachelor-of-community-services/',
]
for url in urls:
    r = curl.get(url, impersonate='chrome120', timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = url.split("/")[-2]
    print(f"\n=== {title} ===")
    
    h1 = soup.find('h1')
    print(f"  Course (h1): {h1.get_text(strip=True) if h1 else 'N/A'}")
    
    # CRICOS
    cricos_div = soup.find('div', class_='cricos')
    if cricos_div:
        m = re.search(r'CRICOS.*?(\d{6}[A-Za-z])', cricos_div.get_text(), re.I)
        print(f"  CRICOS: {m.group(1) if m else cricos_div.get_text(strip=True)}")
    
    # Fee
    fee_div = soup.find('div', class_='fees')
    if fee_div:
        t = fee_div.get_text(strip=True)[:200]
        # Get international fee
        m = re.search(r'International.*?\$([\d,]+)', t, re.I | re.DOTALL)
        if not m:
            m = re.search(r'\$([\d,]+)', t)
        print(f"  Fee: ${m.group(1) if m else t}")
    
    # Duration
    dur_div = soup.find('div', class_='duration')
    if dur_div:
        t = dur_div.get_text(strip=True)
        m = re.search(r'Duration.*?(\d+[\d\s]*(?:to\s*\d+)?\s*weeks?)', t, re.I)
        if m:
            print(f"  Duration: {m.group(1)}")
        else:
            print(f"  Duration raw: {t[:150]}")
    
    # Intake
    intake_div = soup.find('div', class_='intake')
    if intake_div:
        t = intake_div.get_text(strip=True)
        m = re.search(r'Intake.*?(\d{4}.*)', t, re.I | re.DOTALL)
        print(f"  Intake: {m.group(1).strip() if m else t[:150]}")
