"""
QUT course scraper — uses curl_cffi to bypass Cloudflare.

QUT sitemap at https://www.qut.edu.au/sitemaps/collections/courses.xml (413 courses).
Course pages are SSR with JSON-LD (Course schema) containing courseCode + description.
Fee, duration, CRICOS, entry requirements in static HTML.
"""
import os
import re
import sys
import csv
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

# --- constants ---------------------------------------------------------------
PROVIDER_CODE = "00213J"          # QUT
SLUG = "qut"
DIR = "Queensland University of Technology"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
TIMEOUT = 60

# QUT publishes two fee years side by side. The later year is frequently still
# "Fee available from October", so pin the current year and fall back to whatever
# year actually carries figures.
FEE_YEAR = "2026"

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December", "january": "January",
    "february": "February", "march": "March", "april": "April", "june": "June",
    "july": "July", "august": "August", "september": "September",
    "october": "October", "november": "November", "december": "December",
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- shared helpers ----------------------------------------------------------
ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html: str) -> str:
    if not html:
        return ""
    frag = BeautifulSoup(html, "html.parser")
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
    for p in frag.find_all("p"):
        s = p.get_text(strip=True)
        if s.endswith(":") and len(s) < 60 and not p.find(["strong", "b", "a"]):
            p.string = ""
            strong = frag.new_tag("strong")
            strong.string = s
            p.append(strong)
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

def months_in(text):
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", str(text)):
        k = tok.lower()
        if k in MONTHS and MONTHS[k] not in found:
            found.append(MONTHS[k])
    return found

def get_page(url, tries=3):
    last = RuntimeError("unreachable")
    for i in range(tries):
        try:
            return curl_requests.get(url, impersonate='chrome120', timeout=TIMEOUT)
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last

# --- CSV lookup --------------------------------------------------------------
def build_cricos_lookup():
    lookup = {}
    try:
        with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                if not row or len(row) < 4:
                    continue
                if row[0].strip() == PROVIDER_CODE:
                    name = row[3].strip()
                    norm = re.sub(r'[^a-z0-9\s]', ' ', name.lower())
                    norm = re.sub(r'\s+', ' ', norm).strip()
                    lookup[norm] = (row[2].strip(), name)
    except FileNotFoundError:
        pass
    return lookup

def build_register():
    """{cricos: weeks} for this provider, non-expired. Used as a duration fallback
    when the page doesn't state one — without it the annual fee can't be annualised."""
    reg = {}
    try:
        with open('cricos-courses.csv', 'r', encoding='utf-8-sig') as f:
            for r in csv.DictReader(f):
                if r['CRICOS Provider Code'].strip() != PROVIDER_CODE:
                    continue
                if r['Expired'].strip().lower() == 'yes':
                    continue
                reg[r['CRICOS Course Code'].strip()] = re.sub(
                    r'[^\d]', '', r.get('Duration (Weeks)') or '')
    except FileNotFoundError:
        pass
    return reg

REGISTER_WEEKS = {}


def match_cricos(lookup, title):
    norm = re.sub(r'[^a-z0-9\s]', ' ', title.lower())
    norm = re.sub(r'\s+', ' ', norm).strip()
    if norm in lookup:
        return lookup[norm][0]
    for csv_key, (cc, _) in lookup.items():
        tw = set(norm.split())
        cw = set(csv_key.split())
        if len(tw) >= 2 and len(cw) >= 2:
            if len(tw & cw) / max(len(tw), len(cw)) >= 0.6:
                return cc
    return ""

# --- extraction functions (template format) ----------------------------------

def extract_course_description(page):
    """page = BeautifulSoup. JSON-LD has description, or first h2 section."""
    # JSON-LD description
    ld = page.find('script', type='application/ld+json')
    if ld:
        try:
            import json
            data = json.loads(ld.string)
            if isinstance(data, dict) and data.get('@type') == 'Course':
                desc = data.get('description', '')
                if desc:
                    return clean_html(f"<h4>About this course</h4><p>{desc}</p>")
        except:
            pass
    # Fallback: first h2 section text
    h2 = page.find('h2')
    if h2:
        parts = []
        for sib in h2.find_all_next():
            if sib.name in ['h2', 'h3', 'h4']:
                break
            if sib.name == 'p' and sib.get_text(strip=True):
                parts.append(str(sib))
                if len(parts) >= 3:
                    break
        if parts:
            return clean_html(sanitise(''.join(parts)))
    return ""

def extract_entry_requirements(page):
    """page = BeautifulSoup. QUT has 'Requirements' section."""
    req = page.find('h2', string=re.compile(r'Requirements', re.I))
    if not req:
        req = page.find('h3', string=re.compile(r'Requirements', re.I))
    if req:
        parts = []
        for sib in req.find_all_next():
            if sib.name in ['h2', 'h3'] and 'Requirement' not in sib.get_text(strip=True):
                break
            if sib.name == 'p' and sib.get_text(strip=True):
                parts.append(str(sib))
        if parts:
            return clean_html(sanitise(''.join(parts)))
    return ""

def extract_duration(full_text):
    """full_text = page text. QUT: 'X years full-time'."""
    m = re.search(r'(\d+\.?\d*)\s*(year|month|week)s?\s*(full|part)', full_text, re.I)
    if m:
        num = float(m.group(1))
        unit = m.group(2).lower()
        if 'year' in unit:
            return str(int(round(num * 52)))
        elif 'month' in unit:
            return str(int(round(num * 4.33)))
        else:
            return str(int(num))
    return ""

def parse_fee_boxes(page):
    """
    QUT's fee panel is a grid of `.box-wrap` boxes, each headed 'YYYY fees'.
    Within one year the boxes are ordered [domestic, international] — verified
    across a 40-page sample, where the CSP (domestic-only) marker never once
    appeared outside the first box of a group.

    Returns {year: {"domestic": text, "international": text}}.
    """
    panel = page.find(class_=lambda c: c and "course_tab_content__fees" in c)
    if not panel:
        return {}
    groups = {}
    for box in panel.select(".box-wrap"):
        h = box.find(["h2", "h3", "h4", "h5"])
        m = re.search(r"(\d{4})\s*fees", h.get_text(" ", strip=True), re.I) if h else None
        if not m:
            continue
        groups.setdefault(m.group(1), []).append(
            re.sub(r"\s+", " ", box.get_text(" ", strip=True)))
    return {yr: {"domestic": b[0], "international": b[1] if len(b) > 1 else ""}
            for yr, b in groups.items() if b}


def fee_from_box(text, years):
    """
    One fee box -> TOTAL course fee (repo convention, see uq.py).

    '$N per year ...'   -> N * years
    '$N per course ...' -> N, already a whole-of-course figure — must NOT be multiplied
    '$A - $B ...'       -> A; the upper bound only applies if you exceed the max RTP time
    """
    if not text:
        return "NULL"
    amounts = [int(a.replace(",", "")) for a in re.findall(r"\$([\d,]+)", text)]
    if not amounts:
        return "NULL"
    val = amounts[0]
    if re.search(r"per\s*course", text, re.I):
        return str(val)
    if re.search(r"per\s*year", text, re.I) and years:
        return str(round(val * years))
    return str(val)


def extract_fees(page, full_text, duration_weeks):
    """
    QUT quotes an indicative annual (or whole-of-course) fee, split into a domestic
    and an international box per year. Stored as total course fee.

    The old implementation regex-scanned the whole page for the first '$N per year',
    which picked up the *domestic* box whenever it came first in the DOM — e.g.
    Doctor of Education took $43,700 (domestic RTP upper bound) instead of $37,600.
    """
    # Fractional, not rounded: round() turned a 26-week course into a full year and
    # so doubled its fee, and 78 weeks (1.5 years) into 2. Affected 48 of 203 courses.
    years = 0.0
    if duration_weeks and str(duration_weeks).isdigit():
        years = int(duration_weeks) / 52

    boxes = parse_fee_boxes(page)
    for yr in [FEE_YEAR] + sorted(boxes, reverse=True):
        if yr not in boxes:
            continue
        offshore = fee_from_box(boxes[yr]["international"], years)
        onshore = fee_from_box(boxes[yr]["domestic"], years)
        if offshore != "NULL" or onshore != "NULL":
            return offshore, onshore, "NULL", "NULL"
    return "NULL", "NULL", "NULL", "NULL"

def extract_intake_months(page, full_text):
    """QUT mentions semesters / months."""
    found = months_in(full_text)
    return found

def extract_cricos(page):
    """QUT has CRICOS in dt/dd pairs on the page."""
    # Look for dt containing CRICOS
    dt = page.find('dt', string=re.compile(r'CRICOS', re.I))
    if dt:
        dd = dt.find_next('dd')
        if dd:
            code = dd.get_text(strip=True)
            m = re.match(r'(\d{6,7}[A-Za-z]?)', code)
            if m:
                return m.group(1)
    # fallback: dt in other locations or p/b tags
    for el in page.find_all(['p', 'b', 'strong', 'dd', 'span', 'abbr']):
        m = re.match(r'(\d{6,7}[A-Za-z]?)', el.get_text(strip=True))
        if m:
            code = m.group(1)
            ctx = el.get_text(strip=True)
            if 'CRICOS' in ctx or any(c in ctx for c in ['00213', '098']):
                return code
    return ""

# --- per course --------------------------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row.get("cricos", "")).strip()
    if cricos.lower() in ("nan", "none", "null", ""):
        cricos = ""
    cricos = re.sub(r'[^0-9A-Za-z]', '', cricos)
    title = str(row.get("title", "")).strip()
    if title.lower() in ('nan', '', 'none'):
        title = ''

    d = {"cricos": cricos, "title": title, "url": url,
         "course_description": "", "course_duration_per_week": "",
         "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
         "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": []}

    try:
        r = get_page(url)
        soup = BeautifulSoup(r.text, "html.parser")
        full = re.sub(r"\s+", " ", soup.get_text())

        # Title
        if not d["title"]:
            h1 = soup.find('h1')
            if h1:
                d["title"] = h1.get_text(strip=True)

        d["course_description"] = clean_html(extract_course_description(soup))
        d["entry_requirements"] = clean_html(extract_entry_requirements(soup))

        # CRICOS must be resolved before fees: the register supplies the duration
        # fallback, and without a duration an annual fee can't be turned into a total.
        if not d["cricos"]:
            d["cricos"] = extract_cricos(soup)

        d["course_duration_per_week"] = extract_duration(full)
        if not d["course_duration_per_week"]:
            d["course_duration_per_week"] = REGISTER_WEEKS.get(d["cricos"], "")

        d["offshore_tuition_fee"], d["onshore_tuition_fee"], \
            d["enrolment_fee"], d["materials_fee"] = extract_fees(soup, full, d["course_duration_per_week"])

        d["intake_months"] = extract_intake_months(soup, full)

        print(f"  ✅ {d['title'][:55] if d['title'] else url[:55]}")
    except Exception as e:
        print(f"  ❌ {url[:60]}: {e}")

    return d

# --- merge -------------------------------------------------------------------
def merge_by_cricos(results):
    """
    Several QUT course pages can share one CRICOS code (major variants, and the
    parent page that carries no fee at all): 410 pages map to 203 codes. Emitting
    one UPDATE per page meant they overwrote each other and the last page silently
    won — for 0101552 that left $2,500 out of values ranging to $26,300.

    Merge each group into a single record: first non-empty wins for text, highest
    wins for fees, and any disagreement is recorded so the SQL stays auditable.
    """
    groups = {}
    for d in results:
        if d["cricos"]:
            groups.setdefault(d["cricos"], []).append(d)

    merged = []
    for cricos, rows in groups.items():
        best = dict(rows[0])
        best["_pages"] = len(rows)
        best["_conflicts"] = {}

        for key in ("course_description", "entry_requirements", "title"):
            best[key] = next((r[key] for r in rows if r.get(key)), "")

        # Fee and duration must come from ONE page. Taking the max fee but the first
        # duration mixed a 3-year fee with a 2-year duration on 0101676 (Paramedic
        # Science: the graduate-entry and standard pages share a CRICOS).
        priced = [r for r in rows if str(r["offshore_tuition_fee"]).isdigit()]
        primary = max(
            priced or rows,
            key=lambda r: (int(r["offshore_tuition_fee"]) if str(r["offshore_tuition_fee"]).isdigit() else -1,
                           int(r["course_duration_per_week"]) if str(r["course_duration_per_week"]).isdigit() else -1),
        )
        for key in ("offshore_tuition_fee", "onshore_tuition_fee",
                    "enrolment_fee", "materials_fee", "course_duration_per_week"):
            best[key] = primary[key]

        for key in ("offshore_tuition_fee", "onshore_tuition_fee"):
            vals = sorted({int(r[key]) for r in rows if str(r[key]).isdigit()})
            if len(vals) > 1:
                best["_conflicts"][key] = vals

        if not str(best["course_duration_per_week"]).isdigit():
            best["course_duration_per_week"] = next(
                (r["course_duration_per_week"] for r in rows if r.get("course_duration_per_week")), "")

        best["intake_months"] = sorted({m for r in rows for m in r["intake_months"]},
                                       key=MONTH_ORDER.index)
        best["url"] = best["apply_form"] = primary["url"]

        merged.append(best)
    return merged


# --- main --------------------------------------------------------------------
def main():
    global REGISTER_WEEKS
    REGISTER_WEEKS = build_register()
    print(f"📋 Register: {len(REGISTER_WEEKS)} non-expired courses for {PROVIDER_CODE}")

    if not os.path.exists(EXCEL_PATH):
        print("Building driver from sitemap...")
        r = get_page('https://www.qut.edu.au/sitemaps/collections/courses.xml')
        urls = re.findall(r'<loc>(.*?)</loc>', r.text)
        print(f"Found {len(urls)} course URLs")

        csv_lookup = build_cricos_lookup()
        print(f"CSV lookup: {len(csv_lookup)} courses")

        rows = []
        for i, url in enumerate(urls, 1):
            try:
                rp = get_page(url)
                if rp.status_code != 200:
                    print(f"  ⏭️ [{i}] {url.split('/')[-1]} -> {rp.status_code}")
                    continue
                soup = BeautifulSoup(rp.text, 'html.parser')
                h1 = soup.find('h1')
                title = h1.get_text(strip=True) if h1 else url.split('/')[-1]

                # CRICOS from page
                page_cricos = extract_cricos(soup)
                if not page_cricos:
                    page_cricos = match_cricos(csv_lookup, title)

                rows.append({'cricos': page_cricos, 'title': title, 'url': url})
                print(f"  {'✅' if page_cricos else '⏭️'} [{i}/{len(urls)}] {title[:55]}")
                time.sleep(0.3)
            except Exception as e:
                print(f"  ❌ [{i}] {url}: {e}")

        pd.DataFrame(rows).to_excel(EXCEL_PATH, index=False)
        print(f"\n✅ Driver saved: {len(rows)} courses")

    df = pd.read_excel(EXCEL_PATH)
    total = len(df)
    print(f"\n📊 Found {total} courses")

    results = []
    for i, (_, row) in enumerate(df.iterrows(), 1):
        d = scrape_course(row)
        results.append(d)
        if i % 15 == 0:
            time.sleep(1)

    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)

    merged = merge_by_cricos(results)

    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- UPDATE provider institution\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⏭️ Skipped (no CRICOS): {d['title']} | {d['url']}\n")
        f.write("\n")

        for d in merged:
            if d["_pages"] > 1:
                f.write(f"-- {d['_pages']} course pages share CRICOS {d['cricos']}\n")
            for col, vals in d["_conflicts"].items():
                f.write(f"--   conflicting {col}: {vals} -> kept {d[col]}\n")

            # Only emit columns we actually have. Writing NULL would wipe good data
            # already in the DB for the 67 courses whose fee never parsed.
            sets = []
            if d["course_description"]:
                sets.append(f"    course_description = '{d['course_description']}'")
            if d["course_duration_per_week"]:
                sets.append(f"    course_duration_per_week = {d['course_duration_per_week']}")
            for col in ("offshore_tuition_fee", "onshore_tuition_fee",
                        "enrolment_fee", "materials_fee"):
                if str(d[col]).isdigit():
                    sets.append(f"    {col} = {d[col]}")
            if d["entry_requirements"]:
                sets.append(f"    entry_requirements = '{d['entry_requirements']}'")
            sets.append(f"    apply_form = '{d['apply_form']}'")
            sets.append("    updated_at = NOW()")

            f.write("UPDATE courses SET\n" + ",\n".join(sets) +
                    f"\nWHERE cricos_course_code = '{d['cricos']}';\n")

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

    no_cricos = sum(1 for d in results if not d["cricos"])
    with_fee = sum(1 for d in merged if str(d["offshore_tuition_fee"]).isdigit())
    with_onshore = sum(1 for d in merged if str(d["onshore_tuition_fee"]).isdigit())
    with_desc = sum(1 for d in merged if d["course_description"])
    with_entry = sum(1 for d in merged if d["entry_requirements"])
    with_dur = sum(1 for d in merged if d["course_duration_per_week"])
    conflicts = sum(1 for d in merged if d["_conflicts"])
    in_register = sum(1 for d in merged if d["cricos"] in REGISTER_WEEKS)

    print(f"\n✅ {len(results)} pages -> {len(merged)} courses ({no_cricos} pages had no CRICOS).")
    print(f"   With offshore fee: {with_fee}/{len(merged)}")
    print(f"   With onshore fee : {with_onshore}/{len(merged)}")
    print(f"   With description : {with_desc}/{len(merged)}")
    print(f"   With entry reqs  : {with_entry}/{len(merged)}")
    print(f"   With duration    : {with_dur}/{len(merged)}")
    print(f"   Fee conflicts merged: {conflicts} (listed as comments in the SQL)")
    print(f"   In CRICOS register  : {in_register}/{len(REGISTER_WEEKS)}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL   -> {SQL_PATH}")
    print(f"   xlsx  -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
