"""Debug BSW fee extraction."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for url in [
    'https://www.acknowledgeeducation.edu.au/courses/bachelor-of-social-work',
    'https://www.acknowledgeeducation.edu.au/courses/advanced-diploma-of-hospitality-management',
]:
    print(f'\n=== {url.split("/")[-1]} ===')
    r = requests.get(url, headers=H, timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    bodies = soup.find_all('div', class_='accordion-body')
    for i, b in enumerate(bodies):
        t = b.get_text(strip=True)
        if any(w in t.lower() for w in ['fee', 'tuition', 'international', 'domestic']):
            print(f'  [{i}] {t[:300]}')
    # All dollar amounts in context
    for m in re.finditer(r'\$([0-9,]+)', r.text):
        ctx = r.text[max(0,m.start()-80):m.end()+80]
        print(f'  ${m.group(1)} → {ctx.strip()[:100]}')
