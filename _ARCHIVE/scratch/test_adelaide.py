"""Quick test of Adelaide Uni scraper extraction."""
import os, sys, re, requests
from bs4 import BeautifulSoup

DIR = r'C:\Users\Dewa(Interlace)\Documents\Interlace Code\WebScraping-CourseCricos\The University Of Adelaide'

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def get_page(url):
    r = requests.get(url, headers=HEADERS, timeout=60)
    return r.text, BeautifulSoup(r.text, 'html.parser')

def extract_cricos(html):
    m = re.search(r'cricosCode"\s+content="([^"]+)"', html)
    return m.group(1) if m else ""

def extract_duration(html):
    m = re.search(r'timeRequired"\s+content="([^"]+)"', html)
    return m.group(1) if m else ""

def extract_intake(html):
    m = re.search(r'startMonth"\s+content="([^"]+)"', html)
    return m.group(1) if m else ""

def parse_years_to_weeks(text):
    m = re.search(r"([\d.]+)\s*years?", str(text), re.I)
    if m:
        years = float(m.group(1))
        return str(int(round(years * 52)))
    return ""

def extract_fees(html, soup):
    body = soup.get_text()
    
    # Duration years
    years = 1
    dm = re.search(r'timeRequired"\s+content="([^"]+)"', html)
    if dm:
        ym = re.search(r"([\d.]+)\s*years?", dm.group(1), re.I)
        if ym:
            years = float(ym.group(1))
    
    # Fee
    offshore = "NULL"
    fee_section = soup.find(lambda t: t.name in ('h2','h3','h4','strong') and 'indicative annual' in t.get_text(strip=True).lower())
    if fee_section:
        parent = fee_section.find_parent(['div','section','div'])
        if not parent:
            parent = fee_section.parent
        fee_text = parent.get_text() if parent else fee_section.get_text()
        dm2 = re.search(r'\$([0-9,]+)', fee_text)
        if dm2:
            annual = float(dm2.group(1).replace(',', ''))
            offshore = str(int(round(annual * years)))
    
    if offshore == "NULL":
        for match in re.finditer(r'\$([0-9,]+)', body):
            start = max(0, match.start() - 150)
            ctx = body[start:match.end() + 150].lower()
            if any(kw in ctx for kw in ['international', 'indicative', 'annual', 'fee']):
                annual = float(match.group(1).replace(',', ''))
                offshore = str(int(round(annual * years)))
                break
    
    return offshore

# Test
urls = [
    'https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/',
    'https://adelaide.edu.au/study/degrees/bachelor-of-software-engineering-honours/',
    'https://adelaide.edu.au/study/degrees/bachelor-of-psychology-honours/',
]

for url in urls:
    html, soup = get_page(url)
    cricos = extract_cricos(html)
    duration = extract_duration(html)
    weeks = parse_years_to_weeks(duration)
    intake = extract_intake(html)
    fee = extract_fees(html, soup)
    title = soup.find('title')
    title_t = title.get_text(strip=True) if title else ''
    
    print(f"URL: {url}")
    print(f"  Title: {title_t[:80]}")
    print(f"  CRICOS: {cricos}")
    print(f"  Duration: {duration} -> {weeks} weeks")
    print(f"  Intake: {intake}")
    print(f"  Fee (total): {fee}")
    print()
