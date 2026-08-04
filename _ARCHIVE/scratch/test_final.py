"""Quick test of updated scraper fee extraction."""
import os, sys, re, requests
from bs4 import BeautifulSoup

# Simulate the updated fee logic
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def parse_years_to_weeks(text):
    m = re.search(r"([\d.]+)\s*years?", str(text), re.I)
    if m:
        return str(int(round(float(m.group(1)) * 52)))
    return ""

urls = [
    'https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/',
    'https://adelaide.edu.au/study/degrees/bachelor-of-software-engineering-honours/',
    'https://adelaide.edu.au/study/degrees/bachelor-of-psychology-honours/',
    'https://adelaide.edu.au/study/degrees/master-of-nursing-science/',
]

for url in urls:
    r = requests.get(url, headers=headers, timeout=60)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # Title
    title_m = re.search(r'<title>(.*?)</title>', html)
    title = re.sub(r'\s*[|]\s*Adelaide University.*$', '', title_m.group(1)) if title_m else ''
    title = re.sub(r'^Study\s+', '', title).strip()
    
    # CRICOS
    cricos_m = re.search(r'cricosCode"\s+content="([^"]+)"', html)
    cricos = cricos_m.group(1) if cricos_m else 'N/A'
    
    # Duration
    dur_m = re.search(r'timeRequired"\s+content="([^"]+)"', html)
    dur_text = dur_m.group(1) if dur_m else 'N/A'
    weeks = parse_years_to_weeks(dur_text)
    
    # Years
    years = 1
    ym = re.search(r"([\d.]+)\s*years?", dur_text, re.I)
    if ym:
        years = float(ym.group(1))
    
    # Fee
    fee_subtitle = soup.select_one('div.degree-details-content-section-subtitle span')
    if fee_subtitle:
        dm = re.search(r'\$([0-9,]+)', fee_subtitle.get_text())
        if dm:
            annual = float(dm.group(1).replace(',', ''))
            total = int(round(annual * years))
            print(f"\n✅ {title[:60]}")
            print(f"   CRICOS: {cricos}")
            print(f"   Duration: {dur_text} -> {weeks} weeks")
            print(f"   Found fee span: ${annual:,} annual x {years}yr = ${total:,} total")
        else:
            print(f"\n❌ {title[:60]} - fee span found but no $ match")
    else:
        print(f"\n❌ {title[:60]} - NO fee span found")
        # Debug
        detal = soup.select_one('.degree-details-content-section-subtitle')
        if detal:
            print(f"   Found div but no span? {detal}")
        else:
            print(f"   degree-details-content-section-subtitle NOT FOUND")
