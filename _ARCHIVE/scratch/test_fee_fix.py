"""Test Adelaide Uni scraper - FIXED fee extraction."""
import os, sys, re, requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def get_page(url):
    r = requests.get(url, headers=HEADERS, timeout=60)
    return r.text, BeautifulSoup(r.text, 'html.parser')

def clean_html(html):
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

def sanitise(html):
    if not html:
        return ""
    frag = BeautifulSoup(html, "html.parser")
    ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5", "table", "thead", "tbody", "tr", "td", "th"}
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    for t in frag.find_all("span"):
        t.unwrap()
    while True:
        div = frag.find("div")
        if div is None:
            break
        if div.find(["p", "ul", "ol", "li", "div", "table", "h5"]):
            div.unwrap()
        else:
            div.name = "p"
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def parse_years_to_weeks(text):
    m = re.search(r"([\d.]+)\s*years?", str(text), re.I)
    if m:
        return str(int(round(float(m.group(1)) * 52)))
    return ""

def scrape_course(url):
    html, soup = get_page(url)
    
    # Title
    title_m = re.search(r'<title>(.*?)</title>', html)
    title = title_m.group(1) if title_m else ''
    title = re.sub(r'\s*[|]\s*Adelaide University.*$', '', title)
    title = re.sub(r'^Study\s+', '', title).strip()
    
    # CRICOS
    cricos_m = re.search(r'cricosCode"\s+content="([^"]+)"', html)
    cricos = cricos_m.group(1) if cricos_m else ''
    
    # Duration
    dur_m = re.search(r'timeRequired"\s+content="([^"]+)"', html)
    dur_text = dur_m.group(1) if dur_m else ''
    weeks = parse_years_to_weeks(dur_text)
    
    # Years multiplier
    years = 1
    ym = re.search(r"([\d.]+)\s*years?", dur_text, re.I)
    if ym:
        years = float(ym.group(1))
    
    # Intake
    intake_m = re.search(r'startMonth"\s+content="([^"]+)"', html)
    intake_raw = intake_m.group(1) if intake_m else ''
    
    # Description
    desc = ''
    overview_heading = soup.find(lambda t: t.name in ('h2','h3','h4','strong') and 'overview' in t.get_text(strip=True).lower())
    if overview_heading:
        parts = []
        for tag in overview_heading.find_all_next():
            if tag.name in ('h2','h3','h4') and tag != overview_heading and 'overview' not in tag.get_text(strip=True).lower():
                break
            parts.append(str(tag))
        if parts:
            desc = f"<h4>Overview</h4>{sanitise(''.join(parts))}"
    
    # Entry requirements
    entry = ''
    for section_name in ['Entry requirements', 'Admission criteria', 'English language requirements', 'International admissions by country']:
        heading = soup.find(lambda t: t.name in ('h2','h3','h4','strong') and section_name.lower() in t.get_text(strip=True).lower())
        if heading:
            content = []
            for tag in heading.find_all_next():
                if tag.name in ('h2','h3','h4') and tag != heading:
                    break
                if tag.name in ('p','ul','ol','li','div','table','h5'):
                    content.append(str(tag))
            if content:
                entry += f"<h4>{section_name}</h4>{sanitise(''.join(content))}"
    
    # --- FEE FIX ---
    body_text = soup.get_text()
    
    # 1. Find international fee from the degree-details component
    offshore = "NULL"
    # Look in the degree-details section for the fee amount
    fee_subtitle = soup.select_one('.degree-details-content-section-subtitle span')
    if fee_subtitle:
        fee_match = re.search(r'\$([0-9,]+)', fee_subtitle.get_text())
        if fee_match:
            annual = float(fee_match.group(1).replace(',', ''))
            offshore = str(int(round(annual * years)))
    
    # 2. Application fee ($150)
    enrolment = "NULL"
    app_fee_match = re.search(r'application fee (?:of )?AUD?\$([0-9,]+)', body_text, re.I)
    if app_fee_match:
        enrolment = str(int(float(app_fee_match.group(1).replace(',', ''))))
    
    # 3. Detail each dollar amount found for debugging
    print(f"  🔍 All dollar amounts found:")
    for m in re.finditer(r'AUD?\$?([0-9,]+(?:\.\d{2})?)', body_text):
        val = m.group(1).replace(',', '')
        start = max(0, m.start() - 60)
        ctx = body_text[start:m.end() + 60].strip()
        ctx = re.sub(r'\s+', ' ', ctx)
        print(f"     ${val} -> ...{ctx}...")
    
    return {
        'title': title,
        'cricos': cricos,
        'url': url,
        'duration': weeks,
        'offshore': offshore,
        'enrolment': enrolment,
        'intake': intake_raw,
        'description': clean_html(desc)[:300],
        'entry': clean_html(entry)[:300],
    }

# Test
urls = [
    'https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/',
    'https://adelaide.edu.au/study/degrees/bachelor-of-software-engineering-honours/',
]

for url in urls:
    print(f"\n{'='*80}")
    print(f"PAGE: {url}")
    print('='*80)
    d = scrape_course(url)
    print(f"\n✅ RESULTS:")
    print(f"   Title: {d['title']}")
    print(f"   CRICOS: {d['cricos']}")
    print(f"   Duration: {d['duration']} weeks")
    print(f"   Intake: {d['intake']}")
    print(f"   Offshore Tuition Fee (total): ${d['offshore']}")  
    print(f"   Enrolment Fee: ${d['enrolment']}")
