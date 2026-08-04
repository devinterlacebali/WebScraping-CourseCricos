"""
UniSQ course scraper — requests + BS4 with ?studentType=international.

UniSQ is a traditional SSR site. Course data is in the summary bar.
International fee/duration/CRICOS/start months are visible when ?studentType=international is appended.
"""
import os
import re
import sys
import csv
import json
import time

sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from bs4 import BeautifulSoup
from curl_cffi import requests as curl_requests
import pandas as pd

PROVIDER_CODE = "00244B"
SLUG = "unisq"
DIR = "University of Southern Queensland"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
DOMAIN = "https://www.unisq.edu.au"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
MONTH_ABBR = {"jan": "January", "feb": "February", "mar": "March", "apr": "April",
              "may": "May", "jun": "June", "jul": "July", "aug": "August",
              "sep": "September", "oct": "October", "nov": "November", "dec": "December",
              "february": "February", "january": "January", "june": "June", "july": "July"}

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5"}

def sanitise(html):
    if not html: return ""
    frag = BeautifulSoup(html, "html.parser")
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href": del t[a]
    for t in frag.find_all("span"): t.unwrap()
    while True:
        d = frag.find("div")
        if d is None: break
        if d.find(["p", "ul", "ol", "li", "div", "table", "h5"]): d.unwrap()
        else: d.name = "p"
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS: t.unwrap()
    for t in frag.find_all(["p", "li"]):
        if not t.get_text(strip=True) and not t.find("br"): t.decompose()
    return str(frag)

def clean_html(html):
    if not html: return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

def get_page(url, tries=3):
    for i in range(tries):
        try:
            r = curl_requests.get(url, impersonate='chrome120', timeout=45)
            if len(r.text) < 2000: return None
            return r
        except Exception as e:
            time.sleep(1.5 * (i + 1))
    return None

def months_in_text(text):
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", str(text)):
        k = tok.lower()
        if k in MONTH_ABBR and MONTH_ABBR[k] not in found:
            found.append(MONTH_ABBR[k])
    return found

# --- CSV lookup ---
def build_cricos_lookup():
    lookup = {}
    try:
        with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                if not row or len(row) < 4: continue
                if row[0].strip() in (PROVIDER_CODE, "02225M"):
                    name = row[3].strip()
                    norm = re.sub(r'[^a-z0-9\s]', ' ', name.lower())
                    norm = re.sub(r'\s+', ' ', norm).strip()
                    lookup[norm] = (row[2].strip(), name)
    except FileNotFoundError:
        pass
    return lookup

def match_cricos(lookup, title):
    if not title: return ""
    norm = re.sub(r'[^a-z0-9\s]', ' ', title.lower())
    norm = re.sub(r'\s+', ' ', norm).strip()
    if norm in lookup: return lookup[norm][0]
    for csv_key, (cc, _) in lookup.items():
        tw = set(norm.split())
        cw = set(csv_key.split())
        if len(tw) >= 2 and len(cw) >= 2:
            if len(tw & cw) / max(len(tw), len(cw)) >= 0.6:
                return cc
    return ""

# --- page-based extraction ---
def extract_course_data(page, full, title, csv_lookup):
    """Extract all fields from a page (BeautifulSoup)."""
    result = {
        "cricos": "", "course_description": "", "course_duration_per_week": "",
        "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL", "materials_fee": "NULL",
        "entry_requirements": "", "intake_months": []
    }

    # --- CRICOS from summary bar ---
    for el in page.find_all(['div', 'li', 'p', 'dd']):
        txt = el.get_text(strip=True)
        m = re.match(r'^CRICOS\s*(\d{6,7}[A-Za-z]?)$', txt, re.I)
        if m:
            result["cricos"] = m.group(1)
            break
    if not result["cricos"]:
        for el in page.find_all(['div', 'dl', 'p'], string=re.compile(r'CRICOS', re.I)):
            txt = el.get_text(strip=True)
            m = re.search(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', txt, re.I)
            if m:
                result["cricos"] = m.group(1)
                break

    # Fallback to CSV if no CRICOS on page
    if not result["cricos"]:
        result["cricos"] = match_cricos(csv_lookup, title)

    # --- Fee ---
    # "International full fee paying" section
    for el in page.find_all(string=re.compile(r'International full fee paying', re.I)):
        parent_maybe = el.find_parent(['div', 'section'])
        if parent_maybe:
            txt_area = parent_maybe.get_text()
        else:
            idx = full.find(el)
            txt_area = full[max(0,idx-500):idx+500] if idx >= 0 else full
        # AUD 34,280 or $34,280
        for m in re.finditer(r'(?:AUD|\$)\s*([0-9,]+)', txt_area):
            val = int(m.group(1).replace(',', ''))
            if val >= 10000:
                dur_years = 1
                dn = result.get("course_duration_per_week", "")
                if dn and str(dn).isdigit():
                    dur_years = max(1, round(int(dn) / 52))
                result["offshore_tuition_fee"] = str(val * dur_years)
                break

    # --- Duration ---
    # Format: "Duration3 years (or part-time equivalent)"
    for m in re.finditer(r'Duration\s*(\d+\.?\d*)\s*(year|month|week)', full, re.I):
        num = float(m.group(1))
        unit = m.group(2).lower()
        if 'year' in unit: result["course_duration_per_week"] = str(int(round(num * 52)))
        elif 'month' in unit: result["course_duration_per_week"] = str(int(round(num * 4.33)))
        else: result["course_duration_per_week"] = str(int(num))
        break

    # --- Intake ---
    start_labels = page.find_all(['div', 'li', 'p'], string=re.compile(r'^Start$', re.I))
    for sl in start_labels:
        parent = sl.find_parent(['div'])
        if parent:
            parent_txt = parent.get_text(strip=True)
            months_found = months_in_text(parent_txt)
            if months_found:
                result["intake_months"] = months_found
                break
    if not result["intake_months"]:
        # Broader search
        for m in re.finditer(r'(?:Start|Intake)(?:[^.:]*)[.:]\s*([A-Za-z, ]+)', full):
            txt = m.group(1)
            months_found = months_in_text(txt)
            if months_found:
                result["intake_months"] = months_found
                break

    # --- Description from Overview ---
    ov = page.find(['h2', 'h3'], string=re.compile(r'^Overview$', re.I))
    if ov:
        parts = []
        for sib in ov.find_all_next():
            if sib.name in ['h2', 'h3'] and 'Overview' not in sib.get_text(strip=True):
                break
            if sib.name == 'p' and sib.get_text(strip=True):
                parts.append(str(sib))
            if len(parts) >= 8: break
        if parts:
            result["course_description"] = clean_html(sanitise(''.join(parts)))

    # --- Entry requirements ---
    er = page.find(['h2', 'h3'], string=re.compile(r'^Entry requirements$', re.I))
    if er:
        parts = []
        for sib in er.find_all_next():
            if sib.name in ['h2', 'h3'] and 'requirements' not in sib.get_text(strip=True).lower():
                break
            if sib.name in ['p', 'ul'] and sib.get_text(strip=True):
                parts.append(str(sib))
            if len(parts) >= 8: break
        if parts:
            result["entry_requirements"] = clean_html(sanitise(''.join(parts)))

    return result

# --- main ---
def main():
    csv_lookup = build_cricos_lookup()
    print(f"CSV lookup: {len(csv_lookup)} courses")

    # Get sitemap URLs
    r = curl_requests.get(f"{DOMAIN}/sitemap.xml", impersonate='chrome120', timeout=30)
    urls = re.findall(r'<loc>(.*?)</loc>', r.text)
    # Filter to potential degree pages under /study/degrees-and-courses/
    deg_urls = sorted(set([u for u in urls if '/study/degrees-and-courses/' in u
                           and not u.endswith('/degrees-and-courses')
                           and len(u.rstrip('/').split('/')) == 6]))

    # Filter out known category pages
    cat_keywords = {'undergraduate-study', 'postgraduate-study', 'research-study', 'online-study',
                    'pathway-programs', 'find-a-degree', 'compare', 'arts-and-communication',
                    'health-and-community', 'business-and-commerce', 'education', 'engineering',
                    'law-and-criminology', 'creative-arts', 'science-and-mathematics',
                    'information-technology', 'aviation', 'biomedical-sciences',
                    'surveying-and-built-environment', 'humanities-and-social-science',
                    'nursing-and-midwifery', 'psychology-and-counselling',
                    'agriculture-and-environment'}
    degree_urls = [u for u in deg_urls if u.rstrip('/').split('/')[-1] not in cat_keywords]
    print(f"Potential degree URLs: {len(degree_urls)}")

    # Build driver
    rows = []
    for i, url in enumerate(degree_urls, 1):
        slug = url.rstrip('/').split('/')[-1]
        title = slug.replace('-', ' ').title()
        # Fetch page with international param
        intl_url = f"{url}?studentType=international"
        rp = get_page(intl_url)
        if rp is None:
            rows.append({'cricos': '', 'title': title, 'url': intl_url})
            print(f"  ⚠️ [{i}/{len(degree_urls)}] {title[:40]}")
            continue
        soup = BeautifulSoup(rp.text, 'html.parser')
        h1 = soup.find('h1')
        real_title = h1.get_text(strip=True) if h1 else title
        full = re.sub(r"\s+", " ", soup.get_text())

        # Quick check: is this a course page with data?
        has_data = bool(re.search(r'International full fee paying.*(?:AUD|\$)\s*[0-9,]{4,}|CRICOS\s*\d{6,7}[A-Za-z]', full))
        if not has_data:
            # Skip category pages
            rows.append({'cricos': '', 'title': real_title, 'url': intl_url, '_skip': True})
            print(f"  🚫 [{i}/{len(degree_urls)}] {real_title[:40]} (no course data)")
            continue

        cricos = ""
        for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', full, re.I):
            cricos = m.group(1)
            break
        if not cricos:
            cricos = match_cricos(csv_lookup, real_title)

        rows.append({'cricos': cricos, 'title': real_title, 'url': intl_url, '_skip': False})
        print(f"  {'✅' if cricos else '⏭️'} [{i}/{len(degree_urls)}] {real_title[:50]}")

    # Filter out non-course pages
    course_rows = [r for r in rows if not r.get('_skip', False)]
    print(f"\nActual course pages: {len(course_rows)}")

    pd.DataFrame(course_rows).drop(columns=['_skip'], errors='ignore').to_excel(EXCEL_PATH, index=False)
    print(f"✅ Driver saved: {len(course_rows)} courses")

    # Scrape each course
    df = pd.read_excel(EXCEL_PATH)
    results = []
    all_intakes = []

    for i, (_, row) in enumerate(df.iterrows(), 1):
        url = str(row['url'])
        title = str(row['title'])
        cricos = str(row.get('cricos', '')).strip()
        if cricos.lower() in ('nan', 'none', 'null', ''): cricos = ""

        # Fetch international page
        rp = get_page(url)
        if rp is None:
            results.append({
                'cricos': cricos, 'title': title, 'url': url,
                'course_description': '', 'course_duration_per_week': '',
                'offshore_tuition_fee': 'NULL', 'onshore_tuition_fee': 'NULL',
                'enrolment_fee': 'NULL', 'materials_fee': 'NULL',
                'entry_requirements': '', 'intake_months': [],
            })
            print(f"  ❌ [{i}/{len(df)}] {title[:40]} (fetch failed)")
            continue

        soup = BeautifulSoup(rp.text, 'html.parser')
        full = re.sub(r"\s+", " ", soup.get_text())

        # Extract
        data = extract_course_data(soup, full, title, csv_lookup)
        data['cricos'] = data['cricos'] or cricos
        data['title'] = title
        data['url'] = url
        if data['intake_months']:
            all_intakes.extend(data['intake_months'])

        results.append(data)

        marker = '✅' if data['cricos'] else '⏭️'
        print(f"  {marker} [{i}/{len(df)}] {title[:50]} | CRICOS={data.get('cricos','')} | Fee={data.get('offshore_tuition_fee','')}")

        if i % 20 == 0: time.sleep(0.3)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_intakes)

    # SQL output
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write(f"UPDATE provider_institution SET intake_date = '{intake_date}', updated_at = NOW() WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d.get("cricos"):
                f.write(f"-- ⏭️ (no CRICOS): {d['title']} | {d['url']}\n\n")
                continue
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    onshore_tuition_fee = {d["onshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    materials_fee = {d["materials_fee"]},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["url"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")

    # Excel output
    def cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]

    pd.DataFrame([{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "enrolment_fee": cell(d["enrolment_fee"]),
        "materials_fee": cell(d["materials_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    with_cricos = sum(1 for d in results if d.get("cricos"))
    with_fee = sum(1 for d in results if d.get("offshore_tuition_fee", "NULL") not in ("NULL", ""))
    with_dur = sum(1 for d in results if d.get("course_duration_per_week"))

    print(f"\n✅ {len(results)} courses.")
    print(f"   CRICOS: {with_cricos}")
    print(f"   Fee: {with_fee}")
    print(f"   Duration: {with_dur}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL -> {SQL_PATH}")
    print(f"   xlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
