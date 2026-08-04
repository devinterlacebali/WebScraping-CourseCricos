"""
James Cook University course scraper (Scrapling, plain HTTP — no browser).

Rewritten from the old Playwright version: JCU course pages embed a schema.org
`Course` JSON-LD block with everything we need — CRICOS (`identifier`), description,
and `offers` (Domestic CSP + International tuition, both indicative *annual* fees).
Duration / intake / entry come from the `.course-fast-facts` tiles in the raw HTML.
No tab-clicking needed (the old scraper drove Playwright to open the International tab).

Fees are annual -> stored as the TOTAL over the course (annual x years), matching the
repo convention. The CRICOS register (00117J) backfills any registered course whose
page we didn't scrape, so every registered JCU course is covered.
"""
import re
import sys
import csv
import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from scrapling.fetchers import Fetcher

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- constants -------------------------------------------------------------
PROVIDER_CODE = "00117J"                          # James Cook University
SLUG = "jcu"
DIR = "James Cook University"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
REGISTER_CSV = "cricos-courses.csv"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- helpers ---------------------------------------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5"}

def sanitise(node) -> str:
    if node is None:
        return ""
    frag = BeautifulSoup(str(node), "html.parser")
    for t in frag.find_all(["script", "style", "svg", "img", "button", "iframe"]):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    for t in frag.find_all("span"):
        t.unwrap()
    for t in frag.find_all(["h1", "h2", "h3", "h4", "h6"]):
        t.name = "h5"
    while True:
        div = frag.find("div")
        if div is None:
            break
        if div.find(["p", "ul", "ol", "li", "div", "h5"]):
            div.unwrap()
        else:
            div.name = "p"
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i", "h5"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def txt(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)) if el else ""

def num_fee(val):
    v = re.sub(r"[^\d.]", "", str(val or ""))
    if not v:
        return "NULL"
    n = float(v)
    # < $100 is a nominal placeholder (e.g. the $1 Exchange Program), not a real fee
    return str(int(n)) if n >= 100 else "NULL"

def get_page(url, tries=3):
    last = RuntimeError("unreachable")
    for i in range(tries):
        try:
            return Fetcher.get(url, stealthy_headers=True)
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last

def months_in(text):
    return [m for m in MONTH_ORDER if re.search(rf"\b{m}\b", text or "")]

# --- JSON-LD + tile extraction ---------------------------------------------
def course_ldjson(soup):
    for sc in soup.select("script[type='application/ld+json']"):
        try:
            d = json.loads(sc.string or "{}")
        except Exception:
            continue
        if isinstance(d, dict) and d.get("@type") == "Course":
            return d
    return {}

def offer_annual(course, category):
    for o in course.get("offers", []) or []:
        if category.lower() in (o.get("category") or "").lower():
            price = (o.get("priceSpecification") or {}).get("price")
            if price:
                return float(price)
    return None

def tile(soup, cls):
    return soup.select_one(f"[class*='fast-facts-{cls}']")

def extract_years(soup):
    d = tile(soup, "duration")
    m = re.search(r"([\d.]+)\s*year", txt(d), re.I)
    if m:
        return float(m.group(1))
    m = re.search(r"([\d.]+)\s*month", txt(d), re.I)
    return float(m.group(1)) / 12 if m else None

# --- per course ------------------------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    title = str(row.get("title", "")).strip()
    d = {"cricos": "", "title": title, "url": url, "course_description": "",
         "course_duration_per_week": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL",
         "materials_fee": "NULL", "entry_requirements": "", "apply_form": url,
         "intake_months": [], "source": "page", "note": ""}
    try:
        soup = BeautifulSoup(str(get_page(url).html_content), "html.parser")
        course = course_ldjson(soup)
        d["cricos"] = (course.get("identifier") or "").strip()
        d["title"] = course.get("name") or title

        desc = (course.get("description") or "").strip()
        if desc:
            d["course_description"] = clean_html(f"<h4>Course overview</h4><p>{desc}</p>")

        years = extract_years(soup)
        if years:
            d["course_duration_per_week"] = str(int(round(years * 52)))
        yr = years or 1
        intl = offer_annual(course, "International")
        dom = offer_annual(course, "Domestic")
        if intl:
            d["offshore_tuition_fee"] = str(int(round(intl * yr)))
        if dom:
            d["onshore_tuition_fee"] = str(int(round(dom * yr)))

        com = tile(soup, "commencing")
        d["intake_months"] = months_in(txt(com))

        er = tile(soup, "entry-requ")
        if er:
            for h in er.select("[class*='__header']"):
                h.decompose()
            d["entry_requirements"] = clean_html("<h4>Entry Requirements</h4>" + sanitise(er))

        if not d["cricos"]:
            d["note"] = "no CRICOS in JSON-LD"
        print(f"{'✅' if d['cricos'] else '⚠️ '} {d['title'][:44]:44} → {d['cricos'] or '—'} | "
              f"off {d['offshore_tuition_fee']} on {d['onshore_tuition_fee']} "
              f"| {d['course_duration_per_week'] or '?'}w")
    except Exception as e:
        d["note"] = f"error: {e}"
        print(f"❌ {url}: {e}")
    return d

# --- register backfill -----------------------------------------------------
def load_register():
    reg = {}
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["CRICOS Provider Code"].strip() != PROVIDER_CODE:
                continue
            if r["Expired"].strip().lower() == "yes":
                continue
            reg[r["CRICOS Course Code"].strip()] = r
    return reg

def register_rows(scraped_codes):
    """Partial records for registered courses the site scrape didn't cover."""
    extra = []
    for code, r in load_register().items():
        if code in scraped_codes:
            continue
        weeks = re.sub(r"[^\d]", "", r.get("Duration (Weeks)") or "")
        extra.append({
            "cricos": code, "title": r["Course Name"].strip(),
            "url": "", "course_description": "", "course_duration_per_week": weeks,
            "offshore_tuition_fee": num_fee(r.get("Tuition Fee")),
            "onshore_tuition_fee": "NULL", "enrolment_fee": num_fee(r.get("Non Tuition Fee")),
            "materials_fee": "NULL", "entry_requirements": "", "apply_form": "",
            "intake_months": [], "source": "register",
            "note": "not on site scrape; from CRICOS register",
        })
    return extra

# --- main ------------------------------------------------------------------
def main():
    df = pd.read_excel(EXCEL_PATH)
    # The xlsx doubles as our enriched output, so on re-runs it also contains the
    # register-only rows (blank url). Only scrape rows with a real course URL;
    # register rows are re-derived from the CSV below.
    driver = [r for _, r in df.iterrows() if str(r.get("url", "")).strip().startswith("http")]
    results = [scrape_course(r) for r in driver]
    scraped_codes = {d["cricos"] for d in results if d["cricos"]}
    results += register_rows(scraped_codes)

    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)

    enriched = sum(1 for d in results if d["source"] == "page" and d["cricos"])
    emitted = set()
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped ({d['note'] or 'no CRICOS'}): {d['title']} | {d['url']}\n\n")
                continue
            if d["cricos"] in emitted:
                f.write(f"-- ⚠️ Skipped (CRICOS {d['cricos']} already emitted): {d['title']}\n\n")
                continue
            emitted.add(d["cricos"])
            if d["source"] == "register":
                f.write(f"""-- Register-only (not on site scrape): {d['title']}
UPDATE courses SET
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")
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
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
        "source": d["source"], "note": d["note"],
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    print(f"\n✅ {len(emitted)} courses ({enriched} from site, {len(emitted)-enriched} register-only). "
          f"Intake: {intake_date}\nSQL  -> {SQL_PATH}\nxlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
