"""
Gordon Institute of TAFE (The Gordon) — international course scraper.

Provider CRICOS code: 00011G.

The Gordon publishes its international offering as 9 program-area pages under
`/international/programs/<area>`, each linking to individual course pages at
`/international/international-courses/<slug>`. Each course page exposes clean
H2-anchored sections: Intakes (table), Duration, CRICOS code, Fee, Course
description, Entrance requirements, and a Fees breakdown (tuition + non-tuition).

Fees are stored as **total course fee** (the site's "Total tuition fee" is the
whole-course amount, verified: Diploma of Nursing = $43,000 over 2 years):
  * offshore_tuition_fee = international "Total tuition fee".
  * materials_fee        = "Total approx. non tuition fees".
  * onshore_tuition_fee / enrolment_fee = NULL (these are international-only pages).
"""
import re
import sys
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

PROVIDER_CODE = "00011G"
DIR = "Gordon Institute of TAFE"
SLUG = "gordon"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
BASE = "https://www.thegordon.edu.au"
PROGRAMS = ["aged-care", "beauty-therapy", "building-construction-trades",
            "community-services", "cookery", "early-childhood-education",
            "hospitality", "laboratory-technology", "nursing"]

MONTHS = {m.lower(): m for m in
          ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"]}
MONTH_ORDER = list(MONTHS.values())

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}


# ---------- helpers ----------
def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()


def sanitise(html: str) -> str:
    """Flatten wrapper divs/spans into clean, minimal semantic HTML."""
    frag = BeautifulSoup(html or "", "html.parser")
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


def num(text):
    m = re.search(r"\$?\s*([\d,]{3,})", str(text or ""))
    return m.group(1).replace(",", "") if m else None


def sql_num(v):
    return v if v else "NULL"


def get(url):
    return Fetcher.get(url, stealthy_headers=True)


# ---------- course list ----------
def collect_courses():
    """Return {course_url: title} across all program-area pages."""
    courses = {}
    for area in PROGRAMS:
        soup = BeautifulSoup(get(f"{BASE}/international/programs/{area}").html_content, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a["href"].split("?")[0]
            if "/international/international-courses/" in href:
                url = href if href.startswith("http") else BASE + href
                title = re.sub(r"\s*-\s*International\s*$", "", a.get_text(" ", strip=True)).strip()
                courses.setdefault(url, title)
    return courses


# ---------- per-course extraction ----------
def section_html(soup, name):
    """Sanitised HTML of the section whose <h2> title == name (content = the h2's siblings)."""
    h = soup.find("h2", string=re.compile(r"^\s*" + re.escape(name) + r"\s*$", re.I))
    if not h:
        return ""
    parts = [str(s) for s in h.next_siblings if getattr(s, "name", None)]
    frag = BeautifulSoup("".join(parts), "html.parser")
    for sub in frag.find_all(["h3", "h4", "h6"]):
        sub.name = "h5"          # keep sub-labels (Academic/English/…) as sub-headings
    return sanitise(str(frag))


def h2_value(soup, name):
    """Plain-text value that follows a facts <h2> (e.g. Duration).

    The Gordon renders the value as a bare text node inside the h2's parent block
    (`<div class="intake-data"><h2>Duration</h2>Full-time: 12 Months</div>`), so read
    the whole block's text and strip the label.
    """
    h = soup.find("h2", string=re.compile(r"^\s*" + re.escape(name) + r"\s*$", re.I))
    if not h:
        return ""
    txt = re.sub(r"\s+", " ", h.parent.get_text(" ", strip=True))
    return re.sub(r"^\s*" + re.escape(name) + r"\s*", "", txt, flags=re.I).strip()


def scrape_course(url, title):
    d = {"cricos": "", "title": title, "url": url, "course_description": "",
         "total_course_duration": "", "offshore_tuition_fee": None,
         "onshore_tuition_fee": None, "enrolment_fee": None, "materials_fee": None,
         "entry_requirements": "", "apply_form": url, "intake": "", "months": []}

    r = get(url)
    if r.status != 200:
        print(f"⚠️  {title}: {r.status}")
        return d
    soup = BeautifulSoup(r.html_content, "html.parser")
    text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))

    m = re.search(r"CRICOS code\s*([0-9]{6}[A-Z])", text)
    d["cricos"] = m.group(1) if m else ""

    d["total_course_duration"] = clean_html(h2_value(soup, "Duration"))

    tuition = re.search(r"Total tuition fee:?\s*\$([\d,]+)", text, re.I)
    d["offshore_tuition_fee"] = tuition.group(1).replace(",", "") if tuition else None
    nontui = re.search(r"non[- ]?tuition fees?:?\s*\$([\d,]+)", text, re.I)
    d["materials_fee"] = nontui.group(1).replace(",", "") if nontui else None

    desc = section_html(soup, "Course description")
    if desc:
        d["course_description"] = clean_html(f"<h4>Course Description</h4>{desc}")
    entry = section_html(soup, "Entrance requirements")
    if entry:
        d["entry_requirements"] = clean_html(f"<h4>Entry Requirements</h4>{entry}")

    # Intake months come only from year-prefixed intake rows ("2027 February"). This
    # avoids the placement/units tables (Community Services renders a "Duration &
    # Structure" table right after the Intakes heading) and stray words like "may".
    months = []
    for mm in re.findall(r"20\d{2}\s+([A-Z][a-z]+)", text):
        mon = MONTHS.get(mm.lower())
        if mon and mon not in months:
            months.append(mon)
    d["months"] = months
    d["intake"] = ", ".join(m for m in MONTH_ORDER if m in months)

    return d


# ---------- main ----------
def main():
    courses = collect_courses()
    print(f"📋 {len(courses)} international courses\n")

    results = []
    all_months = set()
    for i, (url, title) in enumerate(sorted(courses.items()), 1):
        try:
            d = scrape_course(url, title)
        except Exception as e:
            print(f"❌ [{i}/{len(courses)}] {title}: {e}")
            continue
        all_months.update(d["months"])
        results.append(d)
        flag = f"CRICOS {d['cricos']}" if d["cricos"] else "no CRICOS"
        print(f"✅ [{i}/{len(courses)}] {title[:44]} | {flag} | ${d['offshore_tuition_fee'] or '-'} "
              f"| {d['total_course_duration'][:22]}")
        time.sleep(0.4)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)

    # ---- SQL ----
    print(f"\n💾 SQL -> {SQL_PATH}")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        written = 0
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped (no CRICOS course code): {d['title']} | {d['url']}\n\n")
                continue
            written += 1
            f.write(
                "UPDATE courses SET\n"
                f"    course_description = '{d['course_description']}',\n"
                f"    total_course_duration = '{d['total_course_duration']}',\n"
                f"    offshore_tuition_fee = {sql_num(d['offshore_tuition_fee'])},\n"
                f"    onshore_tuition_fee = {sql_num(d['onshore_tuition_fee'])},\n"
                f"    enrolment_fee = {sql_num(d['enrolment_fee'])},\n"
                f"    materials_fee = {sql_num(d['materials_fee'])},\n"
                f"    entry_requirements = '{d['entry_requirements']}',\n"
                f"    apply_form = '{d['apply_form']}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_course_code = '{d['cricos']}';\n\n"
            )

    # ---- xlsx ----
    print(f"💾 xlsx -> {EXCEL_PATH}")

    def cell(v):
        return ("" if v in (None, "NULL") else str(v).replace("''", "'"))[:32000]

    pd.DataFrame([{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "total_course_duration": cell(d["total_course_duration"]),
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "materials_fee": cell(d["materials_fee"]),
        "intake": cell(d["intake"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    skipped = sum(1 for d in results if not d["cricos"])
    print(f"\n🏁 Done. {written} course UPDATEs, {skipped} skipped. Provider intake: {intake_date}")


if __name__ == "__main__":
    main()
