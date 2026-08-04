"""Test VU scraper extraction on 2 courses."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def test_scrape(url, duration_text):
    r = requests.get(url, headers=headers, timeout=60)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.get_text()
    
    # CRICOS
    cricos = ""
    for span in soup.find_all('span'):
        text = span.get_text(strip=True)
        if re.match(r'^[0-9]{6,7}[A-Za-z]?$', text):
            cricos = text
            break
    
    # Duration parse
    ym = re.search(r'([\d.]+)\s*year', duration_text, re.I)
    years = float(ym.group(1)) if ym else 1
    weeks = str(int(round(years * 52)))
    
    # Fee: look for "$X per semester" near international context
    offshore = ""
    for m in re.finditer(r'\$([0-9,]+)', body):
        start = max(0, m.start() - 80)
        ctx = body[start:m.end() + 100].strip()
        ctx_clean = re.sub(r'\s+', ' ', ctx)
        if 'semester' in ctx_clean.lower() and any(kw in ctx_clean.lower() for kw in ['international', 'tuition']):
            per_sem = float(m.group(1).replace(',', ''))
            total = int(round(per_sem * 2 * years))
            offshore = str(total)
            break
    
    # Enrolment fee
    enrolment = ""
    for m in re.finditer(r'\$([0-9,]+)', body):
        start = max(0, m.start() - 40)
        ctx = body[start:m.end() + 40].strip()
        ctx = re.sub(r'\s+', ' ', ctx)
        if 'application' in ctx.lower():
            enrolment = str(int(float(m.group(1).replace(',', ''))))
            break
    
    # Intake
    intake = ""
    for m in re.finditer(r'\b(February|July|March|January|August|October|April|May|June|September|November|December)\b', body):
        if intake:
            intake += "|"
        intake += m.group(1)
    
    # Description - overview
    desc = ""
    overview = soup.select_one('#overview')
    if overview:
        desc = str(overview)[:1000]
    
    # Entry
    entry = ""
    entry_el = soup.select_one('#entry-requirements')
    if entry_el:
        entry = str(entry_el)[:1000]
    
    title_m = re.search(r'<title>(.*?)</title>', html)
    title = title_m.group(1) if title_m else ""
    title = re.sub(r'\s*[|]\s*Victoria University.*$', '', title).strip()
    
    return {
        'title': title,
        'cricos': cricos,
        'duration': duration_text,
        'weeks': weeks,
        'offshore': offshore,
        'enrolment': enrolment,
        'intake': intake,
        'desc_len': len(desc),
        'entry_len': len(entry),
    }

# Test 2 courses from the driver
tests = [
    ('https://www.vu.edu.au/courses/bachelor-of-laws-graduate-entry-blge/international', '3 years full time or longer for part time'),
    ('https://www.vu.edu.au/courses/diploma-of-building-and-construction-building-cpc50220/international', '2 years full time or longer for part time'),
]

for url, dur in tests:
    result = test_scrape(url, dur)
    print(f"\n✅ {result['title']}")
    print(f"   CRICOS: {result['cricos']}")
    print(f"   Duration: {result['duration']} -> {result['weeks']} weeks")
    print(f"   Offshore Fee: ${result['offshore']}")
    print(f"   Enrolment Fee: ${result['enrolment']}")
    print(f"   Intake: {result['intake']}")
    print(f"   Description chars: {result['desc_len']}")
    print(f"   Entry chars: {result['entry_len']}")
