"""
University of Wollongong (UOW) — course scraper.

Provider CRICOS code: 00102E.

The course finder at uow.edu.au/study/courses/ paginates server-side (`?page=1..62`,
~5 courses/page). Each course page is server-rendered with the fields we need:
  * CRICOS course code ("CRICOS: 000612E").
  * An "International Course fees table" whose **Course fee** column is the TOTAL course
    fee (UOW also lists a per-session fee) -> offshore_tuition_fee (no multiplication).
    The domestic table is loaded client-side only, so onshore is left NULL.
  * Duration, "Starts" sessions (Autumn -> February, Spring -> July intake).
  * Sections are <h2 class="uw-subhead">: Overview (-> description), Admissions
    information (-> entry requirements; fee/profile tables stripped out).

Programs without a CRICOS code are not open to international students -> skipped.
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

PROVIDER_CODE = "00102E"
DIR = "University of Wollongong (UoW)"
SLUG = "uow"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
BASE = "https://www.uow.edu.au"
LIST_URL = BASE + "/study/courses/"
MAX_PAGES = 70

# UOW session -> intake month (2026 session start months).
SESSION_MONTH = {"autumn": "February", "spring": "July", "summer": "December",
                 "winter": "June", "trimester 1": "January", "trimester 2": "May",
                 "trimester 3": "September"}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}


# ---------- helpers ----------
def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()


def sanitise(html: str) -> str:
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
    for t in frag.find_all(["h1", "h2", "h3", "h4", "h6"]):
        t.name = "h5"
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)


def get(url):
    return Fetcher.get(url, stealthy_headers=True)


# ---------- course list ----------
def collect_courses():
    urls = []
    seen = set()
    empty_streak = 0
    for page in range(1, MAX_PAGES + 1):
        html = get(f"{LIST_URL}?page={page}").html_content
        found = re.findall(r'href="(/study/courses/[a-z0-9-]+/)"', html)
        new = 0
        for h in found:
            slug = h.rstrip("/").split("/")[-1]
            if slug in ("courses", "favourites"):
                continue
            u = BASE + h
            if u not in seen:
                seen.add(u)
                urls.append(u)
                new += 1
        empty_streak = empty_streak + 1 if new == 0 else 0
        if empty_streak >= 3:
            break
    return urls


# ---------- per-course extraction ----------
def section_container(soup, name):
    """A wrapper holding the <h2 class="uw-subhead"> section's content (siblings until
    the next uw-subhead heading), or None."""
    h = soup.find("h2", class_="uw-subhead", string=re.compile(r"^\s*" + re.escape(name) + r"\s*$", re.I))
    if not h:
        return None
    wrap = BeautifulSoup("<div></div>", "html.parser")
    div = wrap.div
    for sib in h.find_all_next():
        if sib.name == "h2" and "uw-subhead" in (sib.get("class") or []):
            break
        if sib.parent is not None and sib.find_parent("h2"):
            continue
        if sib.name in ("p", "ul", "ol", "table", "h3", "h4", "dl", "dd", "dt"):
            div.append(BeautifulSoup(str(sib), "html.parser"))
    return div


def offshore_fee(soup):
    """Total international course fee = max $ in the International Course fees table."""
    for tbl in soup.find_all("table"):
        cap = tbl.find("caption")
        if cap and "international" in cap.get_text(strip=True).lower() and "fee" in cap.get_text(strip=True).lower():
            amounts = [int(x.replace(",", "")) for x in re.findall(r"\$\s*([\d,]{4,})", tbl.get_text(" ", strip=True))]
            if amounts:
                return str(max(amounts))
    return None


def scrape_course(url):
    d = {"cricos": "", "title": "", "url": url, "course_description": "",
         "total_course_duration": "", "offshore_tuition_fee": None,
         "onshore_tuition_fee": None, "enrolment_fee": None, "materials_fee": None,
         "entry_requirements": "", "apply_form": url, "intake": "", "months": []}
    r = get(url)
    if r.status != 200:
        return d
    soup = BeautifulSoup(r.html_content, "html.parser")
    text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))

    h1 = soup.find("h1")
    d["title"] = h1.get_text(" ", strip=True) if h1 else ""

    m = re.search(r"CRICOS\s*:?\s*([0-9]{6}[A-Z])", text)
    d["cricos"] = m.group(1) if m else ""

    md = re.search(r"Duration\s*\??\s*(\d+(?:\.\d+)?\s*years?[^.]*?(?:equivalent|full-time)?)", text, re.I)
    d["total_course_duration"] = clean_html(md.group(1).strip()[:80]) if md else ""

    d["offshore_tuition_fee"] = offshore_fee(soup)

    ms = re.search(r"Starts\s*([A-Za-z0-9 ,]{0,60})", text)
    months = []
    if ms:
        for sess, mon in SESSION_MONTH.items():
            if re.search(r"\b" + re.escape(sess) + r"\b", ms.group(1), re.I) and mon not in months:
                months.append(mon)
    d["months"] = months
    d["intake"] = ", ".join(m for m in MONTH_ORDER if m in months)

    overview = section_container(soup, "Overview")
    if overview:
        body = sanitise(str(overview))
        if BeautifulSoup(body, "html.parser").get_text(strip=True):
            d["course_description"] = clean_html(f"<h4>Overview</h4>{body}")[:32000]

    adm = section_container(soup, "Admissions information")
    if adm:
        for tbl in adm.find_all("table"):     # drop the fees table; keep ATAR/profile tables
            cap = tbl.find("caption")
            if cap and "fee" in cap.get_text(strip=True).lower():
                tbl.decompose()
        body = sanitise(str(adm))
        if BeautifulSoup(body, "html.parser").get_text(strip=True):
            d["entry_requirements"] = clean_html(f"<h4>Entry Requirements</h4>{body}")[:32000]

    return d


# ---------- main ----------
def main():
    courses = collect_courses()
    print(f"📋 {len(courses)} courses discovered\n")

    results = []
    all_months = set()
    for i, url in enumerate(courses, 1):
        try:
            d = scrape_course(url)
        except Exception as e:
            print(f"❌ [{i}/{len(courses)}] {url}: {e}")
            continue
        if d["cricos"]:
            all_months.update(d["months"])
        results.append(d)
        tag = f"CRICOS {d['cricos']}" if d["cricos"] else "no CRICOS (skip)"
        print(f"✅ [{i}/{len(courses)}] {d['title'][:40]:42} | {tag} | off ${d['offshore_tuition_fee'] or '-'}")
        time.sleep(0.25)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)

    def sql_num(v):
        return v if v else "NULL"

    print(f"\n💾 SQL -> {SQL_PATH}")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        written = 0
        seen = set()
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped (no CRICOS course code): {d['title']} | {d['url']}\n\n")
                continue
            if d["cricos"] in seen:
                f.write(f"-- Shared CRICOS {d['cricos']} (already updated above): {d['title']} | {d['url']}\n\n")
                continue
            seen.add(d["cricos"])
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

    print(f"💾 xlsx -> {EXCEL_PATH}")

    def cell(v):
        return ("" if v in (None, "NULL") else str(v).replace("''", "'"))[:32000]

    pd.DataFrame([{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "total_course_duration": cell(d["total_course_duration"]),
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "intake": cell(d["intake"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    skipped = sum(1 for d in results if not d["cricos"])
    print(f"\n🏁 Done. {written} course UPDATEs, {skipped} skipped. Provider intake: {intake_date}")


if __name__ == "__main__":
    main()
