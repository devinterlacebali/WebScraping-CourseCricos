"""
Astral Skills Institute of Australia (ASIA) scraper (Scrapling).

Site: https://asia.edu.au — Elementor, free-form <h3> section headings each
followed by a text-editor widget (no tabs/accordion). CRICOS course codes appear
inline in the description, e.g. "(111552M)". Tuition fees and specific intake
months are NOT published on the site or brochure, so those fields are left NULL /
blank (flagged for manual entry).

Output: asia_courses_update.sql  +  enriched asia.xlsx
"""
import os
import re
import sys
import pandas as pd
from bs4 import BeautifulSoup            # only to sanitise small HTML fragments
from scrapling.fetchers import Fetcher

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROVIDER_CODE = "03858C"
EXCEL_PATH = "Astral Skills Institute of Australia/asia.xlsx"
SQL_PATH = "Astral Skills Institute of Australia/asia_courses_update.sql"

# Section headings (matched case-insensitively by prefix) -> destination field
DESCRIPTION_SECTIONS = [
    "course description", "what you will achieve", "study mode", "delivery method",
    "assessment methods", "course structure", "possible career outcomes",
    "academic pathways", "credit transfer", "recognition", "additional information",
]
REQUIREMENT_SECTIONS = [
    "pre-requisites", "rto requirements for international students",
]

# ---------- helpers ----------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

def sanitise(html: str) -> str:
    frag = BeautifulSoup(html, "html.parser")
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    return str(frag)

def txt(el):
    return re.sub(r"\s+", " ", el.get_all_text()).strip()

def classes(el):
    return el.attrib.get("class") or ""

# ---------- section extraction (Elementor free-form heading bucketing) ----------
def get_sections(page):
    """Return {normalised_heading: (original_title, html)} in document order."""
    widgets = page.xpath(
        "//div[contains(@class,'elementor-widget-heading') "
        "or contains(@class,'elementor-widget-text-editor')]",
        adaptive=True,
    )
    sections = {}
    current_key = current_title = None
    parts = []

    def flush():
        if current_key and parts:
            sections.setdefault(current_key, (current_title, "".join(parts)))

    for w in widgets:
        if "elementor-widget-heading" in classes(w):
            flush()
            current_title = txt(w)
            current_key = current_title.lower()
            parts = []
        else:
            if current_key:
                parts.append(w.html_content)
    flush()
    return sections

def _collect(sections, wanted):
    out = ""
    for w in wanted:
        for key, (title, html) in sections.items():
            if key.startswith(w) and BeautifulSoup(html, "html.parser").get_text(strip=True):
                out += f"<h4>{title}</h4>{sanitise(html)}"
                break
    return out

def extract_course_description(page):
    return clean_html(_collect(get_sections(page), DESCRIPTION_SECTIONS))

def extract_entry_requirements(page):
    body = _collect(get_sections(page), REQUIREMENT_SECTIONS)
    return clean_html(body)

def extract_duration(full_text):
    m = re.search(r"Duration\s*[:\-–]?\s*(\d+\s*weeks?)", full_text, re.IGNORECASE)
    return re.sub(r"\s+", " ", m.group(1)).lower() if m else ""

def extract_cricos(full_text):
    m = re.search(r"\b([01]\d{5}[A-Z])\b", full_text)
    return m.group(1) if m else ""

# ---------- per course ----------
def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    if cricos.lower() in ("nan", "none", "null"):
        cricos = ""
    m = re.search(r"[0-9A-Z]{5,8}", cricos)
    cricos = m.group(0) if m else ""
    title = str(row["title"]).strip()

    d = {"cricos": cricos, "title": title, "url": url, "course_description": "",
         "total_course_duration": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url}
    try:
        page = Fetcher.get(url, stealthy_headers=True)
        full = re.sub(r"\s+", " ", page.get_all_text())
        d["course_description"] = extract_course_description(page)
        d["entry_requirements"] = extract_entry_requirements(page)
        d["total_course_duration"] = extract_duration(full)
        if not d["cricos"]:
            d["cricos"] = extract_cricos(full)   # inline "(111552M)" fallback
        print(f"✅ {url}")
    except Exception as e:
        print(f"❌ {url}: {e}")
    return d

# ---------- main ----------
def main():
    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Excel not found: {EXCEL_PATH}")
        return
    df = pd.read_excel(EXCEL_PATH)
    results = [scrape_course(r) for _, r in df.iterrows()]

    # Intake months are not published by ASIA ("Various intake and start dates").
    intake_date = ""

    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped (no CRICOS course code on page): {d['title']} | {d['url']}\n\n")
                continue
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["total_course_duration"]}',
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    onshore_tuition_fee = {d["onshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    materials_fee = {d["materials_fee"]},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")

    def cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]
    pd.DataFrame([{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "total_course_duration": d["total_course_duration"],
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "enrolment_fee": cell(d["enrolment_fee"]),
        "materials_fee": cell(d["materials_fee"]),
        "intake": "",
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    print(f"\n✅ {len(results)} courses. SQL -> {SQL_PATH}\nxlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
