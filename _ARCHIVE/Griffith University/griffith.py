"""
Griffith program scraper via internal API — degrees.griffith.edu.au.

Griffith's Vue.js SPA loads program data from a REST API.
API base: https://degrees.griffith.edu.au/rest-api/v3/
- /programs?pageSize=500 — all programs (348 total)
- /program/{code} — individual program details (CRICOS, fee, duration, intake, etc.)
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

from curl_cffi import requests as curl_requests
import pandas as pd

PROVIDER_CODE = "00233E"
SLUG = "griffith"
DIR = "Griffith University"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
API_BASE = "https://degrees.griffith.edu.au/rest-api/v3"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

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

def parse_duration_weeks(prog):
    """Extract duration in weeks from program data."""
    dur = prog.get('durationInWeeks') or prog.get('duration', '')
    if dur and str(dur).isdigit():
        return str(int(dur))
    dur_text = str(prog.get('durationText', ''))
    m = re.search(r'(\d+\.?\d*)\s*(year|month|week)', dur_text, re.I)
    if m:
        num = float(m.group(1))
        unit = m.group(2).lower()
        if 'year' in unit: return str(int(round(num * 52)))
        elif 'month' in unit: return str(int(round(num * 4.33)))
        else: return str(int(num))
    return ""

def extract_fees(prog, duration_weeks):
    """Extract fees from program data."""
    offshore = "NULL"
    onshore = "NULL"
    enrolment = "NULL"
    materials = "NULL"
    fee_info = prog.get('feeInfo', {}) or {}
    # Try various fee fields
    for field in ['internationalFee', 'offshoreFee', 'tuitionFee', 'fee', 'totalFee']:
        val = fee_info.get(field, prog.get(field, ''))
        if val and str(val).isdigit():
            offshore = str(int(val))
            break
    # If fee is annual, multiply by years
    if fee_info.get('feeType') == 'Annual' and duration_weeks and duration_weeks.isdigit():
        years = max(1, round(int(duration_weeks) / 52))
        if offshore != "NULL":
            offshore = str(int(int(offshore) * years))
    return offshore, onshore, enrolment, materials

def extract_intake(prog):
    """Extract intake periods."""
    periods = prog.get('intakePeriods', []) or []
    months = []
    for p in periods:
        term = p.get('term', '') or p.get('intakeTerm', '') or ''
        for m_name in MONTH_ORDER:
            if m_name in term and m_name not in months:
                months.append(m_name)
    return months

def map_student_type(st):
    if not st: return "Domestic"
    st = str(st).lower()
    if 'international' in st: return "International"
    return "Domestic"

# --- CSV lookup ---
def build_cricos_lookup():
    lookup = {}
    try:
        with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                if not row or len(row) < 4: continue
                if row[0].strip() == PROVIDER_CODE:
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

# --- main ---
def main():
    csv_lookup = build_cricos_lookup()
    print(f"CSV lookup: {len(csv_lookup)} courses")

    # Fetch all programs via pagination
    all_programs = []
    page = 1
    while True:
        url = f"{API_BASE}/programs?pageSize=100&pageNumber={page}"
        r = curl_requests.get(url, impersonate='chrome120', timeout=30)
        if r.status_code != 200: break
        data = r.json()
        records = data.get('records', [])
        if not records: break
        all_programs.extend(records)
        page += 1
        if page > data.get('pagination', {}).get('totalNumberOfPages', 1): break

    print(f"Total programs from API: {len(all_programs)}")

    # Build driver xlsx
    rows = []
    for prog in all_programs:
        code = prog.get('code', '')
        name = prog.get('name', '')
        st = map_student_type(prog.get('studentType', ''))
        # Build URL
        slug = re.sub(r'[^a-z0-9-]', '-', name.lower()).strip('-')
        url = f"https://www.griffith.edu.au/study/degrees/{slug}-{code}"
        cricos = prog.get('cricos', '') or ''
        if not cricos:
            cricos = match_cricos(csv_lookup, name)
        rows.append({'cricos': cricos, 'title': name, 'url': url,
                     'code': code, 'studentType': st})

    pd.DataFrame(rows).to_excel(EXCEL_PATH, index=False)
    print(f"✅ Driver saved: {len(rows)} programs")

    # --- Scrape each program for details ---
    df = pd.read_excel(EXCEL_PATH)
    results = []
    all_intakes = []

    for i, (_, row) in enumerate(df.iterrows(), 1):
        code = str(row.get('code', '')).strip()
        title = str(row.get('title', '')).strip()
        cricos = str(row.get('cricos', '')).strip()
        if cricos.lower() in ('nan', 'none', 'null', ''): cricos = ""

        # Fetch program details
        detail_url = f"{API_BASE}/program/{code}"
        desc = ""
        dur_weeks = ""
        offshore = "NULL"
        onshore = "NULL"
        enrolment_fee = "NULL"
        materials_fee = "NULL"
        intake = []
        entry_reqs = ""
        cricos_api = cricos

        try:
            r = curl_requests.get(detail_url, impersonate='chrome120', timeout=30)
            if r.status_code == 200:
                prog = r.json()
                if not isinstance(prog, dict):
                    raise ValueError("non-dict response")
                code_api = prog.get('code', code)

                # Description from content[ABOUT]
                for c in prog.get('content', []):
                    if c.get('code') == 'ABOUT' and c.get('studentType') == 'International' and c.get('content'):
                        desc = clean_html(c['content'])
                        break
                if not desc:
                    for c in prog.get('content', []):
                        if c.get('code') == 'ABOUT' and c.get('content'):
                            desc = clean_html(c['content'])
                            break

                # Entry reqs from content[ADM_RQMNT]
                for c in prog.get('content', []):
                    if c.get('code') == 'ADM_RQMNT' and c.get('studentType') == 'International' and c.get('content'):
                        entry_reqs = clean_html(c['content'])
                        break
                if not entry_reqs:
                    for c in prog.get('content', []):
                        if c.get('code') == 'ADM_RQMNT' and c.get('content'):
                            entry_reqs = clean_html(c['content'])
                            break

                # Duration from duration[0].fullTime in years
                dur_list = prog.get('duration', [])
                if dur_list:
                    for d_item in dur_list:
                        if d_item.get('studentType') == 'International' and d_item.get('fullTime'):
                            dur_years = float(d_item['fullTime'])
                            dur_weeks = str(int(round(dur_years * 52)))
                            break
                    if not dur_weeks:
                        for d_item in dur_list:
                            if d_item.get('fullTime'):
                                dur_years = float(d_item['fullTime'])
                                dur_weeks = str(int(round(dur_years * 52)))
                                break

                # Fee from knownFees — find INTL band
                for kf in prog.get('knownFees', []):
                    for fee in kf.get('fees', []):
                        band = fee.get('band', {})
                        cat = band.get('category', '')
                        if 'INT' in cat.upper() and 'UGRD' in cat.upper() and 'DOM' not in cat.upper():
                            annual = fee.get('amount', 0)
                            if annual and annual > 0:
                                if dur_weeks and dur_weeks.isdigit():
                                    years_fee = max(1, round(int(dur_weeks) / 52))
                                    offshore = str(int(round(annual * years_fee)))
                                else:
                                    offshore = str(int(round(annual)))
                            break
                    if offshore != "NULL":
                        break

                # Intake
                intake = []
                for i_item in prog.get('intakes', []):
                    name = i_item.get('name', '')
                    # Map Griffith trimester names to months
                    trimester_months = {'Trimester 1': 'January', 'Trimester 2': 'May', 'Trimester 3': 'September'}
                    for tri, m_name in trimester_months.items():
                        if tri.lower() in name.lower() and m_name not in intake:
                            intake.append(m_name)
                    # Also check for semester/intake names containing month names directly
                    if not intake:
                        for m_name in MONTH_ORDER:
                            if m_name.lower() in name.lower() and m_name not in intake:
                                intake.append(m_name)

                # CRICOS from API
                api_cricos = prog.get('cricos', '') or ''
                if api_cricos and re.match(r'^\d{6,7}[A-Za-z]?$', api_cricos):
                    cricos_api = api_cricos

                print(f"  ✅ [{i}/{len(df)}] {title[:50]}")
            else:
                print(f"  ⚠️ [{i}/{len(df)}] {title[:50]} (API error {r.status_code})")
        except Exception as e:
            print(f"  ❌ [{i}/{len(df)}] {title[:50]}: {e}")

        all_intakes.extend(intake)
        results.append({
            'cricos': cricos_api,
            'title': title,
            'url': row.get('url', ''),
            'course_description': desc,
            'course_duration_per_week': dur_weeks,
            'offshore_tuition_fee': offshore,
            'onshore_tuition_fee': onshore,
            'enrolment_fee': enrolment_fee,
            'materials_fee': materials_fee,
            'entry_requirements': entry_reqs,
            'intake_months': intake,
        })

        if i % 20 == 0: time.sleep(0.3)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_intakes)

    # SQL output
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- UPDATE provider institution\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d["cricos"]:
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

    with_cricos = sum(1 for d in results if d["cricos"])
    with_fee = sum(1 for d in results if d["offshore_tuition_fee"] not in ("NULL", ""))
    with_dur = sum(1 for d in results if d["course_duration_per_week"])

    print(f"\n✅ {len(results)} courses.")
    print(f"   CRICOS: {with_cricos}")
    print(f"   Fee: {with_fee}")
    print(f"   Duration: {with_dur}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL -> {SQL_PATH}")
    print(f"   xlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    from bs4 import BeautifulSoup
    main()
