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
    'https://equals.edu.au/courses/social-work-and-community/master-of-social-work-qualifying/',
    'https://equals.edu.au/courses/nursing-health/diploma-of-ayurvedic-lifestyle-consultation/',
]
for url in urls:
    r = curl.get(url, impersonate='chrome120', timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = url.split("/")[-2]
    print(f"\n=== {title} ===")
    
    h2 = soup.find('h2')
    print(f"  Course (h2): {h2.get_text(strip=True) if h2 else 'N/A'}")
    
    # ALL CRICOS-like patterns on the page
    body_text = soup.get_text()
    # Find all 6-digit + letter patterns
    cricos_matches = re.findall(r'\b(\d{6}[A-Za-z])\b', body_text)
    # Filter out known false positives
    cricos_matches = [c for c in cricos_matches if not re.match(r'^\d{6}[Mm]$', c)]
    if cricos_matches:
        # Deduplicate preserving order
        seen = set()
        unique = []
        for c in cricos_matches:
            if c not in seen:
                seen.add(c)
                unique.append(c)
        print(f"  CRICOS candidates (unique): {unique}")
    
    # Also look for the CRICOS text specifically
    for el in soup.find_all(string=re.compile(r'CRICOS Course Code|CRICOS code|cricos course', re.I)):
        p = el.parent
        print(f"  CRICOS element: {p.get_text(strip=True)[:150]}")
    
    # Check if there's a hidden span or small text with CRICOS code
    print(f"  Page has 'CRICOS Course Code': {'CRICOS Course Code' in body_text}")
    print(f"  Page has 'CRICOS': {'CRICOS' in body_text}")
