"""
Reach Community College scraper (Scrapling).

Site: https://reachcollege.edu.au — Elementor, free-form <h3> section headings.
Course pages expose everything cleanly: CRICOS Code, Duration, Offshore/Onshore
tuition fee, a $200 Non-Tuition (handling) fee, and prose sections. Intakes are
"Rolling" (no specific months), so intake_date is left blank.

Section bucketing note: QR/"view on mobile" widgets inject junk <h3> headings
inside real sections, so we only START a new bucket on a KNOWN section heading,
END it on a STOP heading, and treat every other heading as junk (absorbed).

Output: reach_courses_update.sql  +  enriched reach.xlsx
"""
import os
import re
import sys
import pandas as pd
from bs4 import BeautifulSoup
from scrapling.fetchers import Fetcher

# Shared AI formatter (repo root) — optional, opt-in via OPENROUTER_API_KEY
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
try:
    import ai_formatter
except Exception:
    ai_formatter = None

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROVIDER_CODE = "03904B"
EXCEL_PATH = "Reach Community College/reach.xlsx"
SQL_PATH = "Reach Community College/reach_courses_update.sql"

# Known section headings (normalised prefix -> display label)
# course_description = the "Course Overview" section only.
DESCRIPTION_SECTIONS = {
    "course overview": "Course Overview",
}
REQUIREMENT_SECTIONS = {"entry requirements": "Entry Requirements"}
KNOWN = {**DESCRIPTION_SECTIONS, **REQUIREMENT_SECTIONS}

# Headings that terminate the current section (content must not overrun into these)
STOP_HEADINGS = (
    "course pricing", "offshore fee", "onshore fee", "rolling intakes",
    "course format", "non-tuition fees", "student equipment required", "overview",
    "we're here to help", "give us a call", "number of units", "cricos code",
    "duration", "mode of delivery", "locations", "weeks", "units",
    "tuition fee", "tuition course fees",
)
# Junk content to drop within a kept section
JUNK_TEXT_PREFIXES = ("view on mobile", "select an intake", "scan the code")

# ---------- helpers ----------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

def clean_numeric_fee(val) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5", "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html: str) -> str:
    """Flatten wrapper divs/spans into clean, minimal semantic HTML."""
    frag = BeautifulSoup(html, "html.parser")
    # Drop non-content tags outright
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
    # Strip every attribute except href
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    # Unwrap inline wrappers
    for t in frag.find_all("span"):
        t.unwrap()
    # Normalise <div>: wrapper (has block children) -> unwrap; text-only -> <p>
    while True:
        div = frag.find("div")
        if div is None:
            break
        if div.find(["p", "ul", "ol", "li", "div", "table", "h5"]):
            div.unwrap()
        else:
            div.name = "p"
    # Bold short label paragraphs ending in ':' (e.g. "Academic requirement:")
    for p in frag.find_all("p"):
        s = p.get_text(strip=True)
        if s.endswith(":") and len(s) < 60 and not p.find(["strong", "b", "a"]):
            p.string = ""
            strong = frag.new_tag("strong")
            strong.string = s
            p.append(strong)
    # Drop leftover unknown tags (keep their text) and empty elements
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def txt(el):
    return re.sub(r"\s+", " ", el.get_all_text()).strip()

def classes(el):
    return el.attrib.get("class") or ""

# ---------- section bucketing ----------
def get_sections(page):
    widgets = page.xpath(
        "//div[contains(@class,'elementor-widget-heading') "
        "or contains(@class,'elementor-widget-text-editor') "
        "or contains(@class,'elementor-widget-icon-list')]",
        adaptive=True,
    )
    sections = {}
    current = None
    parts = []

    def flush():
        if current and parts:
            sections.setdefault(current, "".join(parts))

    for w in widgets:
        if "elementor-widget-heading" in classes(w):
            n = txt(w).lower()
            start = next((k for k in KNOWN if n.startswith(k)), None)
            if start:
                flush()
                current, parts = start, []
            elif n.startswith(STOP_HEADINGS):
                flush()
                current, parts = None, []
            # else: junk heading -> keep current, ignore heading text
            continue
        if current is None:
            continue
        t = txt(w)
        if not t or t.lower().startswith(JUNK_TEXT_PREFIXES):
            continue
        parts.append(w.html_content)
    flush()
    return sections

def extract_course_description(sections):
    out = ""
    for key, label in DESCRIPTION_SECTIONS.items():
        html = sections.get(key)
        if html and BeautifulSoup(html, "html.parser").get_text(strip=True):
            out += f"<h4>{label}</h4>{sanitise(html)}"
    return clean_html(out)

def extract_entry_requirements(sections):
    html = sections.get("entry requirements")
    if not (html and BeautifulSoup(html, "html.parser").get_text(strip=True)):
        return ""
    # Preferred: AI-formatted categorised table (opt-in via OPENROUTER_API_KEY)
    if ai_formatter is not None and ai_formatter.enabled():
        plain = re.sub(r"\s+", " ", BeautifulSoup(html, "html.parser").get_text(" ", strip=True))
        plain = re.sub(r"^\s*Entry Requirements\s*", "", plain, flags=re.IGNORECASE)
        table = ai_formatter.format_requirements(plain)
        if table:
            return clean_html(f"<h4>Entry Requirements</h4>{table}")
    # Fallback: flattened source HTML
    body = sanitise(html)
    body = re.sub(r"^\s*<p>\s*Entry Requirements\s*</p>", "", body, flags=re.IGNORECASE)
    return clean_html(f"<h4>Entry Requirements</h4>{body}")

# ---------- header fields ----------
def extract_duration(full_text):
    # course_duration_per_week is a NUMBER (weeks), not a string
    m = re.search(r"(\d+)\s*Weeks Course Duration", full_text, re.IGNORECASE) \
        or re.search(r"Duration\s*(\d+)\s*Weeks", full_text, re.IGNORECASE)
    return m.group(1) if m else ""

def extract_fees(full_text):
    def grab(p):
        m = re.search(p, full_text, re.IGNORECASE)
        return clean_numeric_fee(m.group(1)) if m else "NULL"
    offshore = grab(r"Offshore Fee\s*\$?\s*([\d,]+)")
    onshore = grab(r"Onshore Fee\s*\$?\s*([\d,]+)")
    enrolment = grab(r"Non-Tuition Fees\s*\$?\s*([\d,]+)")
    return offshore, onshore, enrolment

def extract_cricos(full_text):
    m = re.search(r"CRICOS Code:\s*([0-9A-Z]{5,8})", full_text)
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
         "course_duration_per_week": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url}
    try:
        page = Fetcher.get(url, stealthy_headers=True)
        full = re.sub(r"\s+", " ", page.get_all_text())
        sections = get_sections(page)
        d["course_description"] = extract_course_description(sections)
        d["entry_requirements"] = extract_entry_requirements(sections)
        d["course_duration_per_week"] = extract_duration(full)
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], d["enrolment_fee"] = extract_fees(full)
        if not d["cricos"]:
            d["cricos"] = extract_cricos(full)
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

    # Reach uses rolling intakes with dates scheduled across all 12 months.
    intake_date = "January, February, March, April, May, June, July, August, September, October, November, December"

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
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
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
        "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
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
