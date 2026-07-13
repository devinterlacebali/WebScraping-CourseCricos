"""
Holmesglen Institute — international course scraper.

Provider CRICOS code: 00012G.

Holmesglen runs on Adobe AEM. The international course catalogue is served by a POST
API — `/bin/courseList` with `{searchPath:"", international:"true", ...}` returns every
international course (title, cricosCode, overview, duration, intakes, pagePath). Fees and
entry requirements are not in that feed, so we fetch each course's (server-rendered)
detail page for those.

Fees are stored as **total course fee**:
  * "International Fee $X Per Year"  -> X * number of years (multi-year courses).
  * "International Fee $X" (no unit) -> X as-is (already the whole-course price;
    verified: Diploma of Nursing, 18 months, $39,090 with no unit).
  * "Full Fee $X Per week"           -> X * weeks (ELICOS pathway).
  offshore_tuition_fee = that total; materials_fee = "Materials fee $X";
  onshore_tuition_fee / enrolment_fee = NULL (these are international-only pages).

Data-quality handling:
  * Several specialisation streams share one CRICOS (the code registers the qualification,
    not the stream), so rows are DEDUPED by cricos_course_code — one UPDATE per code, with
    the shared streams listed in a comment.
  * A non-standard CRICOS (e.g. Pathway English "0102054") is flagged and skipped.
"""
import re
import sys
import json
import time
import html as html_lib
import pandas as pd
from bs4 import BeautifulSoup
from scrapling.fetchers import Fetcher

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROVIDER_CODE = "00012G"
DIR = "Holmesglen Institute"
SLUG = "holmesglen"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
BASE = "https://www.holmesglen.edu.au"
API = f"{BASE}/bin/courseList"

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


def fetch_courses():
    body = {"searchPath": "", "pageType": None, "theme": "holmesglen", "pageNo": 1,
            "international": "true", "limit": 500, "sortBy": "",
            "openDayBookNowURL": "", "upcomingOpenDays": "", "applicationFormUrl": ""}
    p = Fetcher.post(API, json=body, headers={"Content-Type": "application/json"},
                     stealthy_headers=True)
    return json.loads(p.body.decode("utf-8", "ignore")).get("courseData", [])


def duration_units(duration_list):
    """(years, weeks) from a duration like ['Full Time', '18 Months'] / ['Full Time', '3 Year(s)']."""
    txt = " ".join(duration_list or [])
    m = re.search(r"(\d+(?:\.\d+)?)\s*year", txt, re.I)
    if m:
        y = float(m.group(1))
        return y, y * 52
    m = re.search(r"(\d+(?:\.\d+)?)\s*month", txt, re.I)
    if m:
        mo = float(m.group(1))
        return mo / 12.0, mo * 4.345
    return None, None


def intake_months(intakes):
    """['July-July 2026-202620', 'February-February 2027-202710'] -> ['July','February']."""
    out = []
    for s in intakes or []:
        m = re.match(r"\s*([A-Za-z]+)", str(s))
        if m:
            mon = MONTHS.get(m.group(1).lower())
            if mon and mon not in out:
                out.append(mon)
    return out


def section_html(soup, name):
    """Sanitised HTML of an AEM section: heading in a title component, content in the
    following sibling container. Climb from the heading until an ancestor has a
    content-bearing next sibling."""
    h = soup.find(["h2", "h3"], string=re.compile(r"^\s*" + re.escape(name) + r"\s*$", re.I))
    if not h:
        return ""
    node = h
    for _ in range(6):
        node = node.parent
        if node is None:
            break
        sib = node.find_next_sibling()
        # First substantial sibling that is not itself a title component (the content
        # block for this section — it may legitimately contain <h3> sub-headings).
        if sib and len(sib.get_text(strip=True)) > 40:
            cls = " ".join(sib.get("class") or [])
            if "title" not in cls:
                # Some pages store double-encoded HTML (literal "&lt;br&gt;"); unescape
                # once so those tags render instead of showing as text.
                return sanitise(html_lib.unescape(str(sib)))
    return ""


def total_fee(text, years, weeks):
    """(offshore_total, materials) parsed from page text per the fee rule."""
    m = re.search(r"(?:International Fee|Full Fee)\s*\$([\d,]+)\s*(Per Year|Per week|Per Study Period)?",
                  text, re.I)
    offshore = None
    if m:
        amt = float(m.group(1).replace(",", ""))
        unit = (m.group(2) or "").lower()
        if unit == "per year" and years:
            offshore = round(amt * years)
        elif unit == "per week" and weeks:
            offshore = round(amt * weeks)
        else:                       # no unit -> already the whole-course price
            offshore = round(amt)
    mat = re.search(r"Materials fee\s*\$([\d,]+)", text, re.I)
    materials = mat.group(1).replace(",", "") if mat else None
    return (str(offshore) if offshore is not None else None), materials


def base_title(title):
    return re.sub(r"\s*\([^)]*\)\s*$", "", title).strip()


# ---------- main ----------
def main():
    courses = fetch_courses()
    print(f"📋 {len(courses)} international courses from API")

    # Group by CRICOS (specialisation streams share one code).
    groups = {}
    order = []
    for c in courses:
        cc = (c.get("cricosCode") or "").strip()
        key = cc or f"__nocricos_{c['pagePath']}"
        if key not in groups:
            groups[key] = []
            order.append(key)
        groups[key].append(c)
    print(f"   {len(order)} unique CRICOS groups\n")

    results = []
    all_months = set()
    for i, key in enumerate(order, 1):
        grp = groups[key]
        rep = grp[0]
        cricos = (rep.get("cricosCode") or "").strip()
        title = base_title(rep["qualification"]) if len(grp) > 1 else rep["qualification"]
        variants = [g["qualification"] for g in grp] if len(grp) > 1 else []
        url = BASE + rep["pagePath"]
        years, weeks = duration_units(rep.get("duration"))
        months = intake_months(rep.get("intakes"))

        d = {"cricos": cricos, "title": title, "url": url,
             "course_description": "", "total_course_duration": " ".join(rep.get("duration") or []),
             "offshore_tuition_fee": None, "onshore_tuition_fee": None,
             "enrolment_fee": None, "materials_fee": None,
             "entry_requirements": "", "apply_form": url,
             "intake": ", ".join(m for m in MONTH_ORDER if m in months),
             "variants": variants, "valid": bool(re.fullmatch(r"[0-9]{6}[A-Z]", cricos))}

        # Description from the API overview (present for all), enriched HTML.
        if rep.get("overview"):
            d["course_description"] = clean_html(
                f"<h4>Course Overview</h4>{sanitise(html_lib.unescape(rep['overview']))}")

        try:
            soup = BeautifulSoup(get(url).html_content, "html.parser")
            text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))
            d["offshore_tuition_fee"], d["materials_fee"] = total_fee(text, years, weeks)
            entry = section_html(soup, "Entry Requirements")
            if entry:
                d["entry_requirements"] = clean_html(f"<h4>Entry Requirements</h4>{entry}")
        except Exception as e:
            print(f"❌ [{i}/{len(order)}] {title}: {e}")

        # Only real (valid-CRICOS) courses define the provider intake; the skipped
        # ELICOS pathway has monthly starts and would otherwise flood it with all 12.
        if d["valid"]:
            all_months.update(months)

        results.append(d)
        tag = f"CRICOS {cricos}" if d["valid"] else f"UNRELIABLE '{cricos}'"
        vtag = f" (+{len(variants)-1} streams)" if variants else ""
        print(f"✅ [{i}/{len(order)}] {title[:40]:42} | {tag} | ${d['offshore_tuition_fee'] or '-'}{vtag}")
        time.sleep(0.3)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)

    # ---- SQL ----
    print(f"\n💾 SQL -> {SQL_PATH}")

    def sql_num(v):
        return v if v else "NULL"

    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        written = 0
        for d in results:
            if not d["valid"]:
                f.write(f"-- ⚠️ Skipped (unreliable CRICOS '{d['cricos']}'): {d['title']} | {d['url']}\n\n")
                continue
            if d["variants"]:
                f.write(f"-- Shared CRICOS {d['cricos']} across streams: "
                        + "; ".join(d["variants"]) + "\n")
            written += 1
            f.write(
                "UPDATE courses SET\n"
                f"    course_description = '{d['course_description']}',\n"
                f"    total_course_duration = '{clean_html(d['total_course_duration'])}',\n"
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
        "materials_fee": cell(d["materials_fee"]),
        "intake": cell(d["intake"]),
        "streams": cell("; ".join(d["variants"])),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    skipped = sum(1 for d in results if not d["valid"])
    print(f"\n🏁 Done. {written} course UPDATEs, {skipped} skipped. Provider intake: {intake_date}")


if __name__ == "__main__":
    main()
