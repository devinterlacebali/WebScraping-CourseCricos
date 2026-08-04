"""
ECU (Edith Cowan University) course scraper — template format.

Traditional SSR site, no Cloudflare. 250 courses in sitemap.
Tabbed domestic/international on course pages.
Provider: 00251G
"""
import os
import re
import sys
import csv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

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
PROVIDER_CODE = "00279B"
SLUG = "ecu"
DIR = "Edith Cowan University"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
DOMAIN = "https://www.ecu.edu.au"
SITEMAP_URL = f"{DOMAIN}/sitemap.courses.xml"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
TIMEOUT = 60

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

# --- shared helpers (from template) ------------------------------------------
ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5"}

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
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)


def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()


def get_page(url: str, tries: int = 3):
    for i in range(tries):
        try:
            r = curl_requests.get(url, impersonate='chrome120', timeout=TIMEOUT)
            if len(r.text) < 1000:
                return None
            return r
        except Exception:
            time.sleep(1.5 * (i + 1))
    return None


def _months_in_text(text: str):
    found = set()
    for tok in re.findall(r"[A-Za-z]{3,9}", str(text)):
        key = tok.lower().capitalize()
        if key in MONTH_ORDER:
            found.add(key)
    return [m for m in MONTH_ORDER if m in found]


# --- CRICOS CSV lookup ------------------------------------------------------
def _build_cricos_lookup():
    lookup = {}
    try:
        with open("cricos-courses.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)
            for row in reader:
                if not row or len(row) < 4:
                    continue
                if row[0].strip() == PROVIDER_CODE:
                    name = row[3].strip()
                    norm = re.sub(r"[^a-z0-9\s]", " ", name.lower())
                    norm = re.sub(r"\s+", " ", norm).strip()
                    lookup[norm] = (row[2].strip(), row[20].strip() if len(row) > 20 else "", name)
    except FileNotFoundError:
        pass
    return lookup


def _match_cricos(lookup, title):
    if not title:
        return ""
    norm = re.sub(r"[^a-z0-9\s]", " ", title.lower())
    norm = re.sub(r"\s+", " ", norm).strip()
    if norm in lookup:
        return lookup[norm][0]
    for csv_key, (cc, _, _) in lookup.items():
        tw = set(norm.split())
        cw = set(csv_key.split())
        if len(tw) >= 2 and len(cw) >= 2:
            if len(tw & cw) / max(len(tw), len(cw)) >= 0.6:
                return cc
    return ""


# --- 6 x extract_* functions ------------------------------------------------
def extract_course_title(page):
    h1 = page.find("h1")
    if h1:
        return h1.get_text(strip=True)
    return ""


def extract_course_description(page):
    heading = page.find(["h2"], string=re.compile(r"About this Course", re.I))
    if not heading:
        return ""
    parts = []
    for sib in heading.find_all_next(["p", "ul", "ol"], limit=8):
        if sib.name in ["h2"] and sib.get_text(strip=True):
            break
        if sib.name in ["p", "ul", "ol"] and sib.get_text(strip=True):
            parts.append(str(sib))
    if not parts:
        return ""
    return clean_html(sanitise("".join(parts)))


def extract_cricos(page, full_text, csv_lookup, title):
    # From page — look for "CRICOS code" section heading
    cr_heading = page.find(["h3"], string=re.compile(r"CRICOS code", re.I))
    if cr_heading:
        # Text is in the same parent div or next sibling
        parent = cr_heading.find_parent(["div", "section"])
        if parent:
            txt = parent.get_text()
            m = re.search(r"CRICOS\s*code[^\d]*(\d{6,7}[A-Za-z]?)", txt, re.I)
            if m:
                return m.group(1)
        # Try next sibling
        sib = cr_heading.find_next_sibling()
        if sib:
            m = re.search(r"(\d{6,7}[A-Za-z]?)", sib.get_text())
            if m:
                return m.group(1)
    # Broader search (full text)
    m = re.search(r"CRICOS\s*code[^\d]*(\d{6,7}[A-Za-z]?)", full_text, re.I)
    if m:
        return m.group(1)
    # Fallback to CSV
    return _match_cricos(csv_lookup, title)


def extract_fee(page, full_text, csv_lookup, title, duration_weeks):
    # Look for "International students" section then extract AUD amount
    # Fee text: "International students - estimated 1st year indicative fee AUD $44,000"
    m = re.search(r"International students[^$]*AUD\s*\$?\s*([0-9,]+)", full_text, re.I)
    if m:
        val = int(m.group(1).replace(",", ""))
        if val > 1000:
            # Multiply by duration years if available
            if duration_weeks and str(duration_weeks).isdigit():
                years = max(1, round(int(duration_weeks) / 52))
                return str(val * years)
            return str(val)
    # Try CSV fallback
    for csv_key, (_, csv_fee, csv_name) in csv_lookup.items():
        if csv_name.lower() in title.lower() or title.lower() in csv_name.lower():
            if csv_fee:
                try:
                    v = csv_fee.replace("$", "").replace(",", "").strip()
                    return str(int(float(v))) if v else "NULL"
                except ValueError:
                    pass
    return "NULL"


def extract_entry_requirements(page):
    # Look for "Course Entry" section that contains admission requirements
    entry_heading = page.find(["h2"], string=re.compile(r"^Course Entry$", re.I))
    if not entry_heading:
        # Try "Entry requirements" subheading
        entry_heading = page.find(["h2", "h3"], string=re.compile(r"Entry requirements", re.I))
    if not entry_heading:
        return ""
    parts = []
    for sib in entry_heading.find_all_next(["p", "ul", "ol"], limit=12):
        if sib.name in ["h2", "h3"] and sib.get_text(strip=True):
            # Stop if we hit a major heading (like "Fees", "Duration")
            txt = sib.get_text(strip=True).lower()
            if any(kw in txt for kw in ["fees", "duration", "about this", "career", "how to apply"]):
                break
        if sib.name in ["p", "ul", "ol"] and sib.get_text(strip=True):
            parts.append(str(sib))
    if not parts:
        return ""
    return clean_html(sanitise("".join(parts)))


def extract_duration(full_text):
    # ECU format: "Duration 3 years full-time" (no colon)
    m = re.search(r"Duration\s*(\d+\.?\d*)\s*(year|month|week)", full_text, re.I)
    if m:
        num = float(m.group(1))
        unit = m.group(2).lower()
        if num > 20 and 'year' in unit:
            return ""
        if "year" in unit:
            return str(int(round(num * 52)))
        elif "month" in unit:
            return str(int(round(num * 4.33)))
        else:
            return str(int(num))
    # Fallback: "X years full-time"
    m = re.search(r"(\d+\.?\d*)\s*(year|month|week)\s*(?:full-time|part-time)", full_text, re.I)
    if m:
        num = float(m.group(1))
        unit = m.group(2).lower()
        if num > 20 and 'year' in unit:
            return ""
        if "year" in unit:
            return str(int(round(num * 52)))
        elif "month" in unit:
            return str(int(round(num * 4.33)))
        else:
            return str(int(num))
    return ""


def extract_intake_months(full_text):
    return ", ".join(_months_in_text(full_text))


# --- scrape_course(row) -----------------------------------------------------
def scrape_course(row, csv_lookup):
    """Scrape one course from a driver row. Row: dict with keys:
       title (from URL slug), url.
    Returns dict with all 11 enriched columns + intake.
    """
    url = row["url"]
    rp = get_page(url)
    if rp is None:
        return {
            "cricos": "", "title": row["title"], "url": url,
            "course_description": "", "course_duration_per_week": "",
            "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
            "enrolment_fee": "NULL", "materials_fee": "NULL",
            "entry_requirements": "", "intake": "",
        }

    page = BeautifulSoup(rp.text, "html.parser")

    # Quick validity check
    h1 = page.find("h1")
    title = h1.get_text(strip=True) if h1 else ""
    if "Supplemental" in title or not title:
        return {
            "cricos": "", "title": title or row["title"], "url": url,
            "course_description": "", "course_duration_per_week": "",
            "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
            "enrolment_fee": "NULL", "materials_fee": "NULL",
            "entry_requirements": "", "intake": "",
        }

    full_text = re.sub(r"\s+", " ", page.get_text())

    title = extract_course_title(page) or row["title"]
    cricos = extract_cricos(page, full_text, csv_lookup, title)
    dur = extract_duration(full_text)
    fee = extract_fee(page, full_text, csv_lookup, title, dur)

    return {
        "cricos": cricos,
        "title": title,
        "url": url,
        "course_description": extract_course_description(page),
        "course_duration_per_week": dur,
        "offshore_tuition_fee": fee,
        "onshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL",
        "materials_fee": "NULL",
        "entry_requirements": extract_entry_requirements(page),
        "intake": extract_intake_months(full_text),
    }


# --- discovery: build driver ------------------------------------------------
def build_driver():
    """Get all course URLs from sitemap.courses.xml, deduplicate."""
    r = curl_requests.get(SITEMAP_URL, impersonate="chrome120", timeout=TIMEOUT)
    urls = re.findall(r"<loc>(.*?)</loc>", r.text)

    # Deduplicate by slug
    deduped = {}
    for u in urls:
        slug = u.rstrip("/").split("/")[-1].lower()
        if slug not in deduped:
            deduped[slug] = u

    rows = []
    for slug, u in sorted(deduped.items()):
        title = slug.replace("-", " ").title()
        rows.append({"title": title, "url": u})

    return pd.DataFrame(rows)


# --- pandas IO + SQL --------------------------------------------------------
def save_output(results, intake_date):
    """Write XLSX + SQL files."""
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write(f"UPDATE provider_institution SET intake_date = '{intake_date}', "
                f"updated_at = NOW() WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
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

    def cell(v):
        return (v or "").replace("''", "'")[:32000] if v not in (None, "NULL") else ""

    pd.DataFrame([{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "enrolment_fee": cell(d["enrolment_fee"]),
        "materials_fee": cell(d["materials_fee"]),
        "intake": d.get("intake", ""),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)


# --- main -------------------------------------------------------------------
def main():
    csv_lookup = _build_cricos_lookup()
    print(f"CSV lookup: {len(csv_lookup)} courses")

    df = build_driver()
    print(f"Driver: {len(df)} courses")

    results = []
    all_intakes = []

    for i, (_, row) in enumerate(df.iterrows(), 1):
        d = scrape_course(row.to_dict(), csv_lookup)
        results.append(d)
        if d.get("intake"):
            for m in d["intake"].split(", "):
                all_intakes.append(m)
        marker = "✅" if d.get("cricos") else "⏭️"
        print(f"  {marker} [{i}/{len(df)}] {d['title'][:50]} | CRICOS={d.get('cricos','')} | Fee={d.get('offshore_tuition_fee','NULL')[:7]}")

    # Filter out invalids (no title, Supplemental)
    valid_results = [d for d in results if d["title"] and "Supplemental" not in d["title"]]
    invalid_count = len(results) - len(valid_results)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_intakes)
    save_output(valid_results, intake_date)

    with_cricos = sum(1 for d in valid_results if d.get("cricos"))
    with_fee = sum(1 for d in valid_results if d.get("offshore_tuition_fee", "NULL") not in ("NULL", ""))
    with_dur = sum(1 for d in valid_results if d.get("course_duration_per_week"))

    print(f"\n✅ {len(valid_results)} courses ({invalid_count} invalid/supplemental skipped).")
    print(f"   CRICOS: {with_cricos}")
    print(f"   Fee: {with_fee}")
    print(f"   Duration: {with_dur}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL -> {SQL_PATH}")
    print(f"   xlsx -> {EXCEL_PATH}")


if __name__ == "__main__":
    main()
