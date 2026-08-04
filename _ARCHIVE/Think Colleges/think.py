"""
Think: Colleges Pty Ltd scraper (www.think.edu.au) — template format.

Traditional SSR site, no Cloudflare. 7 courses, 3 with CRICOS.
CRICOS/CSV matching for provider 00246M.
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
PROVIDER_CODE = "00246M"
SLUG = "think"
DIR = "Think Colleges"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
DOMAIN = "https://www.think.edu.au"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
TIMEOUT = 30

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
    """Fetch page via curl_cffi (no Cloudflare needed but curl_cffi is faster)."""
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
    """Return sorted list of month names found in text."""
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
            if len(tw & cw) / max(len(tw), len(cw)) >= 0.5:
                return cc
    return ""


def _csv_fee(lookup, title):
    """Return fee from CSV for matching title."""
    for csv_key, (_, csv_fee, csv_name) in lookup.items():
        if csv_name.lower() in title.lower() or title.lower() in csv_name.lower():
            if csv_fee:
                try:
                    val_str = csv_fee.replace("$", "").replace(",", "").strip()
                    return str(int(float(val_str))) if val_str else "NULL"
                except ValueError:
                    pass
        # fuzzy match
        tw = set(re.sub(r"[^a-z0-9\s]", " ", title.lower()).split())
        cw = set(csv_key.split())
        if len(tw) >= 2 and len(cw) >= 2 and len(tw & cw) / max(len(tw), len(cw)) >= 0.5:
            if csv_fee:
                try:
                    val_str = csv_fee.replace("$", "").replace(",", "").strip()
                    return str(int(float(val_str))) if val_str else "NULL"
                except ValueError:
                    pass
    return "NULL"


# --- 6 x extract_* functions ------------------------------------------------
def extract_course_title(page):
    h1 = page.find("h1")
    return h1.get_text(strip=True) if h1 else ""


def extract_course_description(page):
    heading = page.find(["h2", "h3", "h4"], string=re.compile(r"^(What is|About|Overview)", re.I))
    if not heading:
        return ""
    parts = []
    for sib in heading.find_all_next(["p", "ul", "ol"], limit=8):
        if sib.name in ["h2", "h3", "h4"] and sib.get_text(strip=True):
            break
        if sib.name in ["p", "ul", "ol"] and sib.get_text(strip=True):
            parts.append(str(sib))
    if not parts:
        return ""
    return clean_html(sanitise("".join(parts)))


def extract_cricos(page, full_text, csv_lookup, title):
    # From page — only from main content, not related courses sidebar
    for el in page.find_all(string=re.compile(r"CRICOS[^\d]*\d{6,7}[A-Za-z]?")):
        parent = el.find_parent()
        if parent and "item-ref" in parent.get("class", []):
            continue  # skip related-course badges
        # Also skip footer/provider sections
        if parent and parent.find_parent("footer"):
            continue
        # Check if it's in the entry-details section or accordion
        m = re.search(r"CRICOS[^\d]*(\d{6,7}[A-Za-z]?)", el)
        if m:
            return m.group(1)
    # Fallback to CSV
    return _match_cricos(csv_lookup, title)


def extract_fee(page, full_text, csv_lookup, title):
    # From page — look for tuition amount (not salary data)
    for m in re.finditer(r"(?:course fees?|tuition|VET|domestic)[^$]{0,20}\$?\s*([0-9,]+)", full_text, re.I):
        g = m.group(1).strip().replace(",", "")
        if not g:
            continue
        val = int(g)
        if 10000 < val < 200000:
            return str(val)
    # Fallback to CSV
    return _csv_fee(csv_lookup, title)


def extract_entry_requirements(page):
    er_section = page.find(["h2", "h3", "h4"], string=re.compile(r"^Entry details|Admission criteria|Entry requirements", re.I))
    if not er_section:
        return ""
    parts = []
    # Prefer "Admission criteria" sub-heading
    admission = page.find(["h4"], string=re.compile(r"^Admission criteria", re.I))
    if admission:
        for sib in admission.find_all_next(["p", "ul", "ol", "li"], limit=15):
            if sib.name in ["h2", "h3", "h4"] and "Admission" not in sib.get_text(strip=True):
                break
            if sib.name in ["p", "ul", "li"] and sib.get_text(strip=True):
                parts.append(str(sib))
    else:
        for sib in er_section.find_all_next(["p", "ul", "ol"], limit=8):
            if sib.name in ["h2", "h3", "h4"]:
                break
            if sib.name in ["p", "ul", "ol"] and sib.get_text(strip=True):
                parts.append(str(sib))
    if not parts:
        return ""
    return clean_html(sanitise("".join(parts)))


def extract_duration(full_text):
    for m in re.finditer(r"(\d+\.?\d*)\s*(year|month|week)\s", full_text, re.I):
        num = float(m.group(1))
        unit = m.group(2).lower()
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
def scrape_course(row):
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
    full_text = re.sub(r"\s+", " ", page.get_text())

    csv_lookup = _build_cricos_lookup()
    title = extract_course_title(page) or row["title"]
    cricos = extract_cricos(page, full_text, csv_lookup, title)

    return {
        "cricos": cricos,
        "title": title,
        "url": url,
        "course_description": extract_course_description(page),
        "course_duration_per_week": extract_duration(full_text),
        "offshore_tuition_fee": extract_fee(page, full_text, csv_lookup, title),
        "onshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL",
        "materials_fee": "NULL",
        "entry_requirements": extract_entry_requirements(page),
        "intake": extract_intake_months(full_text),
    }


# --- discovery: build driver ------------------------------------------------
def build_driver():
    """Discover all course URLs from /courses listing page, dedup, return DataFrame."""
    r = curl_requests.get(f"{DOMAIN}/courses", impersonate="chrome120", timeout=TIMEOUT)
    soup = BeautifulSoup(r.text, "html.parser")

    all_urls = set()
    for a in soup.find_all("a", href=True):
        h = a["href"]
        if "/courses/" in h and "course-guides" not in h:
            all_urls.add((f"{DOMAIN}{h}" if not h.startswith("http") else h).rstrip("/"))

    # Deduplicate by slug, prefer shallow path
    deduped = {}
    for u in sorted(all_urls):
        slug = u.rstrip("/").split("/")[-1].split("?")[0].lower()
        depth = len(u.rstrip("/").split("/"))
        if slug not in deduped or depth < len(deduped[slug].rstrip("/").split("/")):
            deduped[slug] = u

    rows = []
    for u in sorted(deduped.values()):
        slug = u.rstrip("/").split("/")[-1]
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
    df = build_driver()
    print(f"Driver: {len(df)} courses")

    results = []
    all_intakes = []

    for i, (_, row) in enumerate(df.iterrows(), 1):
        d = scrape_course(row.to_dict())
        results.append(d)
        if d.get("intake"):
            for m in d["intake"].split(", "):
                all_intakes.append(m)
        marker = "✅" if d.get("cricos") else "⏭️"
        print(f"  {marker} [{i}/{len(df)}] {d['title'][:50]} | CRICOS={d.get('cricos','')} | Fee={d.get('offshore_tuition_fee','NULL')}")

    # Deduplicate
    seen = set()
    uniq = []
    for d in results:
        key = (d["title"].lower().strip(), d.get("cricos", ""))
        if key not in seen:
            seen.add(key)
            uniq.append(d)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_intakes)
    save_output(uniq, intake_date)

    with_cricos = sum(1 for d in uniq if d.get("cricos"))
    with_fee = sum(1 for d in uniq if d.get("offshore_tuition_fee", "NULL") not in ("NULL", ""))
    with_dur = sum(1 for d in uniq if d.get("course_duration_per_week"))

    print(f"\n✅ {len(uniq)} courses.")
    print(f"   CRICOS: {with_cricos}")
    print(f"   Fee: {with_fee}")
    print(f"   Duration: {with_dur}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL -> {SQL_PATH}")
    print(f"   xlsx -> {EXCEL_PATH}")


if __name__ == "__main__":
    main()
