"""Test the ACTUAL fee logic from the updated scraper."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = 'https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/'
r = requests.get(url, headers=headers, timeout=60)
soup = BeautifulSoup(r.text, 'html.parser')

# Updated scraper logic:
years = 4  # simplified for test
offshore = "NULL"

for sub in soup.select('div.degree-details-content-section-subtitle'):
    txt = sub.get_text()
    print(f"Checking subtitle: '{txt.strip()[:50]}'")
    if '$' in txt:
        print(f"  ✅ FOUND fee: '{txt.strip()}'")
        fee_subtitle = sub
        dm = re.search(r'\$([0-9,]+)', fee_subtitle.get_text())
        if dm:
            annual = float(dm.group(1).replace(',', ''))
            offshore = str(int(round(annual * years)))
        break

print(f"\nResult: offshore = {offshore}")
