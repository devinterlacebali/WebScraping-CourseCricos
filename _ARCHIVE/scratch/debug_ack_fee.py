"""Debug Acknowledge fee extraction."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = 'https://www.acknowledgeeducation.edu.au/courses/diploma-of-nursing-draft'
r = requests.get(url, headers=headers, timeout=60)
soup = BeautifulSoup(r.text, 'html.parser')
body = soup.get_text()

# Check what body actually looks like around 'international'
print("=== BODY AROUND 'International' ===")
idx = body.lower().find('international student')
if idx >= 0:
    block = body[idx:idx+600]
    print(repr(block))
else:
    print("'International Student' NOT FOUND in body!")
    # Find any fee-like structures
    for m in re.finditer(r'Tuition fee|tuition fee', body, re.I):
        start = max(0, m.start() - 50)
        block = body[start:m.end()+200]
        print(f"\nBlock: {repr(block)}")
