"""
RMIT University course scraper (Scrapling, plain HTTP).

RMIT renders course pages server-side (real pages are ~400-600 KB; guessed URLs return
a 189 KB SPA/404 shell — so URLs MUST come from the sitemap). Each real course page
carries structured `<meta class="elastic">` tags (product_name, description,
s_studenttype, next_intake_international, duration_international, fees_international) and
the course CRICOS code(s) in the campus/fees table under a "CRICOS" column header.

Strategy = register spine + site enrichment (join by CRICOS). The CRICOS register
(00122A, 496 non-expired) is authoritative for code + duration(weeks) + TOTAL tuition, so
every registered course is inserted. Site pages add the course description + intake,
joined to the register by the CRICOS code scraped from the page. Register-only courses
emit a partial UPDATE (no description) so DB text isn't wiped.
"""
import re
import sys
import csv
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
PROVIDER_CODE = "00122A"                          # RMIT University
SLUG = "rmit"
DIR = "Royal Melbourne Institute of Technology"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
REGISTER_CSV = "cricos-courses.csv"
SITEMAP_URL = "https://www.rmit.edu.au/sitemap.xml"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]
CRICOS_RE = re.compile(r"\b(\d{6}[A-Z])\b")

# --- helpers ---------------------------------------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

def num_fee(val):
    v = re.sub(r"[^\d.]", "", str(val or ""))
    if not v:
        return "NULL"
    n = float(v)
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

# --- register --------------------------------------------------------------
def load_register():
    out = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["CRICOS Provider Code"].strip() != PROVIDER_CODE:
                continue
            if r["Expired"].strip().lower() == "yes":
                continue
            out.append({
                "cricos": r["CRICOS Course Code"].strip(),
                "title": r["Course Name"].strip(),
                "weeks": re.sub(r"[^\d]", "", r.get("Duration (Weeks)") or ""),
                "tuition": num_fee(r.get("Tuition Fee")),
                "non_tuition": num_fee(r.get("Non Tuition Fee")),
            })
    return out

# --- sitemap ---------------------------------------------------------------
def course_urls():
    h = str(get_page(SITEMAP_URL).html_content)
    locs = re.findall(r"<loc>([^<]+)</loc>", h)
    return [l for l in locs
            if "/study-with-us/levels-of-study/" in l
            and re.search(r"-[a-z]{1,3}\d{3,4}$", l.rstrip("/"))]

# --- page enrichment -------------------------------------------------------
def scrape_page(url):
    """Return (cricos_codes, {description, intake_months, name}) or (None, None) if the
    course has no international offering."""
    soup = BeautifulSoup(str(get_page(url).html_content), "html.parser")

    def meta(name):
        m = soup.find("meta", class_="elastic", attrs={"name": name})
        return (m.get("content") or "").strip() if m else ""

    if "international" not in meta("s_studenttype").lower():
        return None, None

    codes = []
    for lab in soup.find_all(["div", "th", "span"]):
        if re.sub(r"\s+", " ", lab.get_text(" ", strip=True)) == "CRICOS":
            cont = lab
            for _ in range(6):
                if cont.parent:
                    cont = cont.parent
            for c in CRICOS_RE.findall(cont.get_text(" ")):
                if c not in codes:
                    codes.append(c)
            break

    desc = meta("description")
    data = {
        "name": meta("product_name"),
        "description": clean_html(f"<h4>Course overview</h4><p>{desc}</p>") if desc else "",
        "intake_months": months_in(meta("next_intake_international")),
        "url": url,
    }
    return codes, data

# --- main ------------------------------------------------------------------
def main():
    register = load_register()
    urls = course_urls()
    print(f"Register: {len(register)} courses | sitemap course URLs: {len(urls)}\n")

    site = {}          # cricos -> page data
    all_intake = set()
    for i, u in enumerate(urls, 1):
        try:
            codes, data = scrape_page(u)
            if codes and data:
                all_intake.update(data["intake_months"])
                for c in codes:
                    site.setdefault(c, data)
                tag = "✅"
            else:
                tag = "· "
            print(f"{tag} ({i}/{len(urls)}) {u.split('/')[-1][:50]} → {codes or '—'}")
        except Exception as e:
            print(f"❌ ({i}/{len(urls)}) {u.split('/')[-1][:40]}: {e}")

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_intake)

    results, enriched = [], 0
    for r in register:
        d = {"cricos": r["cricos"], "title": r["title"], "url": "",
             "course_duration_per_week": r["weeks"], "offshore_tuition_fee": r["tuition"],
             "enrolment_fee": r["non_tuition"], "course_description": "",
             "intake_months": [], "source": "register", "note": ""}
        p = site.get(r["cricos"])
        if p:
            d.update(url=p["url"], course_description=p["description"],
                     intake_months=p["intake_months"], source="page")
            enriched += 1
        results.append(d)

    emitted = set()
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if d["cricos"] in emitted:
                continue
            emitted.add(d["cricos"])
            if d["source"] == "page" and d["course_description"]:
                f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    apply_form = '{d["url"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")
            else:
                f.write(f"""-- Register-only (no site match): {d['title']}
UPDATE courses SET
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
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
        "enrolment_fee": cell(d["enrolment_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "source": d["source"], "note": d["note"],
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    print(f"\n✅ {len(emitted)} courses ({enriched} enriched from site, {len(emitted)-enriched} "
          f"register-only). Intake: {intake_date}\nSQL  -> {SQL_PATH}\nxlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
