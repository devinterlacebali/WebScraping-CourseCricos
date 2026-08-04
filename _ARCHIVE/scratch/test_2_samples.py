"""Test Adelaide Uni scraper on 2 courses and show the SQL output."""
import os, sys, re, requests
from bs4 import BeautifulSoup

DIR = r'C:\Users\Dewa(Interlace)\Documents\Interlace Code\WebScraping-CourseCricos\The University Of Adelaide'

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
    from bs4 import BeautifulSoup as BS
    frag = BS(html, "html.parser")
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
    
    # Fee
    body = soup.get_text()
    offshore = "NULL"
    fee_section = soup.find(lambda t: t.name in ('h2','h3','h4','strong') and 'indicative annual' in t.get_text(strip=True).lower())
    if fee_section:
        parent = fee_section.find_parent(['div','section'])
        if not parent:
            parent = fee_section.parent
        fee_text = parent.get_text() if parent else fee_section.get_text()
        dm = re.search(r'\$([0-9,]+)', fee_text)
        if dm:
            annual = float(dm.group(1).replace(',', ''))
            offshore = str(int(round(annual * years)))
    
    # Enrolment fee
    enrolment = "NULL"
    if 'application fee' in body.lower():
        ma = re.search(r'\$([0-9,]+)', body)
        if ma:
            enrolment = str(int(float(ma.group(1).replace(',', ''))))
    
    return {
        'title': title,
        'cricos': cricos,
        'url': url,
        'duration': weeks,
        'offshore': offshore,
        'enrolment': enrolment,
        'intake': intake_raw,
        'description': clean_html(desc),
        'entry': clean_html(entry),
    }

# Test 2 courses
urls = [
    'https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/',
    'https://adelaide.edu.au/study/degrees/master-of-nursing-science/',
]

for url in urls:
    print(f"\n{'='*80}")
    print(f"PAGE: {url}")
    print('='*80)
    
    d = scrape_course(url)
    
    print(f"\n📋 COURSE: {d['title']}")
    print(f"   CRICOS: {d['cricos']}")
    print(f"   Duration: {d['duration']} weeks")
    print(f"   Intake: {d['intake']}")
    print(f"   Offshore Fee (total): {d['offshore']}")
    print(f"   Enrolment Fee: {d['enrolment']}")
    print(f"\n   Description (first 300 chars):")
    print(f"   {d['description'][:300]}...")
    print(f"\n   Entry Requirements (first 300 chars):")
    print(f"   {d['entry'][:300]}...")
    
    # Simulate SQL
    print(f"\n📝 SQL OUTPUT:")
    print(f"-- Course: {d['title']} ({d['cricos']})")
    print(f"UPDATE courses SET")
    print(f"    course_description = '{d['description'][:200]}...',")
    print(f"    course_duration_per_week = {d['duration'] or 'NULL'},")
    print(f"    offshore_tuition_fee = {d['offshore']},")
    print(f"    onshore_tuition_fee = NULL,")
    print(f"    enrolment_fee = {d['enrolment']},")
    print(f"    materials_fee = NULL,")
    print(f"    entry_requirements = '{d['entry'][:200]}...',")
    print(f"    apply_form = '{d['url']}',")
    print(f"    updated_at = NOW()")
    print(f"WHERE cricos_course_code = '{d['cricos']}';")
