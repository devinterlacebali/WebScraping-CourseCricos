import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

urls = [
    'https://www.stanleycollege.edu.au/courses/bachelor-of-business/',
    'https://www.stanleycollege.edu.au/courses/bachelor-of-community-services/',
    'https://www.stanleycollege.edu.au/courses/bachelor-of-business-with-a-major-in-management/',
    'https://www.stanleycollege.edu.au/courses/bachelor-of-business-with-a-major-in-accounting/',
    'https://www.stanleycollege.edu.au/courses/bachelor-of-business-with-a-major-in-digital-marketing/',
    'https://www.stanleycollege.edu.au/courses/bachelor-of-business-with-a-major-in-hospitality-and-events-management/',
    'https://www.stanleycollege.edu.au/courses/bachelor-of-information-and-communications-technology/',
    'https://www.stanleycollege.edu.au/courses/106012D-certificate-iii-in-business/',
    'https://www.stanleycollege.edu.au/courses/sit30821-certificate-iii-in-commercial-cookery/',
]
for url in urls:
    r = curl.get(url, impersonate='chrome120', timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = url.split("/")[-2]
    print(f"\n=== {title} ===")
    h1 = soup.find('h1')
    print(f"  H1: {h1.get_text(strip=True) if h1 else 'N/A'}")
    
    # check for listdiv classes
    for cls in ['cricos', 'fees', 'duration', 'intake']:
        div = soup.find('div', class_=cls)
        if div:
            print(f"  {cls}: {div.get_text(strip=True)[:200]}")
        else:
            print(f"  {cls}: NOT FOUND")
            # Maybe in a table?
            for table in soup.find_all('table'):
                t = table.get_text(strip=True)
                if cls.lower() in t.lower():
                    print(f"    Found in table: {t[:200]}")
    
    # Check for CRICOS in body
    cricos = re.findall(r'\b(\d{6}[A-Za-z])\b', soup.get_text())
    if cricos:
        print(f"  CRICOS in body: {list(set(cricos))}")
