"""
Swinburne University of Technology course scraper (Scrapling, plain HTTP).

Driver = the Funnelback (Squiz) course feed (same backend as UNE). One JSON call
lists every course; we keep those whose `Residency` includes "International"
(~435). The feed has no CRICOS or fee amounts, so each international course page
(Adobe AEM, `cmp-tabs`) is scraped for: CRICOS, international Total fee, SSAF,
duration, overview, entry requirements and intake.

Output (repo standard): swinburne_courses_update.sql (1 provider + N course
UPDATEs) + swinburne.xlsx enriched record.
"""
import re
import sys
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
PROVIDER_CODE = "00111D"                       # Swinburne University of Technology
SLUG = "swinburne"
DIR = "Swinburne University of Technology"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

FEED_URL = ("https://sut-search.funnelback.squiz.cloud/s/search.json"
            "?collection=sut~sp-course-search&query=!showall&num_ranks=2000")

# Swinburne semesters -> commencement month (from the course key-dates tables).
SEMESTER_MONTH = {"1": "March", "2": "August"}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- shared helpers --------------------------------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(node) -> str:
    """Flatten an AEM fragment into clean, minimal semantic HTML."""
    if node is None:
        return ""
    frag = BeautifulSoup(str(node), "html.parser")
    # drop chrome: nav/breadcrumb/back-links/media/scripts and the hidden domestic variant
    for t in frag.select("nav, .breadcrumb, [class*='breadcrumb'], [class*='back-to'], "
                          "script, style, noscript, form, iframe, img, svg, button, "
                          ".domestic, [class*='cmp-tabs__tab ']"):
        t.decompose()
    for t in frag.find_all(["h1", "h2", "h3", "h4", "h6"]):
        t.name = "h5"
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
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i", "h5"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def txt(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)) if el else ""

def money(s):
    m = re.search(r"\$([\d,]+)", s or "")
    if not m:
        return None
    v = int(m.group(1).replace(",", ""))
    return v if v > 0 else None            # $0 (exchange programs) is not a real fee

def get_page(url, tries=3):
    """Fetch with a couple of retries — Swinburne occasionally drops the TLS
    connection mid-scrape (curl 35/56)."""
    last = RuntimeError("unreachable")
    for i in range(tries):
        try:
            return Fetcher.get(url, stealthy_headers=True)
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last

# --- feed ------------------------------------------------------------------
def fetch_courses():
    """Return list of international course dicts from the Funnelback feed."""
    resp = get_page(FEED_URL)
    data = json.loads(resp.body.decode("utf-8", "ignore"))
    results = data["response"]["resultPacket"]["results"]
    courses = []
    for r in results:
        lm = r.get("listMetadata") or {}
        if "International" not in (lm.get("Residency") or []):
            continue
        url = r.get("liveUrl") or ""
        if "student_type=" not in url:
            url += ("&" if "?" in url else "?") + "student_type=international"
        courses.append({
            "title": r.get("title", "").strip(),
            "url": url,
            "course_code": (lm.get("CourseCode") or [""])[0],
            "feed_duration": (lm.get("Duration") or [""])[0],
        })
    # de-dupe by url
    seen, uniq = set(), []
    for c in courses:
        if c["url"] not in seen:
            seen.add(c["url"]); uniq.append(c)
    return uniq

# --- page field extraction -------------------------------------------------
def extract_cricos(soup):
    for item in soup.select(".course-codes__item, .course-codes--column"):
        t = txt(item)
        if "CRICOS" in t:
            m = re.search(r"\b(\d{6}[A-Z]|\d{7})\b", t)
            if m:
                return m.group(1)
    return ""

def extract_fees(soup):
    """(offshore_total, ssaf) — international figures. Swinburne quotes the whole-
    course 'Total fee' directly, so no per-year scaling is needed."""
    total = yearly = ssaf = None
    for blk in soup.select("[class*='course-fees']"):
        t = txt(blk)
        if "Total fee" in t and total is None:
            total = money(t.split("Total fee", 1)[1])
        if "Yearly fee" in t and yearly is None:
            yearly = money(t.split("Yearly fee", 1)[1])
        if "SSAF" in t and ssaf is None:
            ssaf = money(t.split("SSAF", 1)[1])
    return (total if total is not None else yearly), ssaf

def extract_duration_weeks(soup, feed_duration):
    dd = soup.select_one("[class*='course-details__duration'], [class*='duration']")
    dur = ""
    if dd:
        intl = dd.select_one("span.international")
        dur = txt(intl) if intl else txt(dd)
    dur = dur or feed_duration
    m = re.search(r"([\d.]+)\s*year", dur, re.I)
    if m:
        return str(int(round(float(m.group(1)) * 52)))
    m = re.search(r"([\d.]+)\s*month", dur, re.I)
    if m:
        return str(int(round(float(m.group(1)) * 4.345)))
    m = re.search(r"([\d.]+)\s*week", dur, re.I)
    return m.group(1) if m else ""

def extract_intake_months(soup):
    months = []
    it = soup.select_one("[class*='course-details__intake']")
    if it:
        it = BeautifulSoup(str(it), "html.parser")
        for d in it.select(".domestic"):
            d.decompose()
        for m in re.findall(r"Semester\s*([12])", txt(it)):
            mo = SEMESTER_MONTH.get(m)
            if mo and mo not in months:
                months.append(mo)
    return months

def panel_for(soup, label):
    """Map tab -> panel. The tab's aria-controls id doesn't reliably match the
    panel id across page templates, so map by position (tabs and panels share
    order), with an aria-controls lookup as a fallback."""
    tabs = soup.select(".cmp-tabs__tab")
    panels = soup.select(".cmp-tabs__tabpanel")
    for i, t in enumerate(tabs):
        if label.lower() in txt(t).lower():
            if i < len(panels):
                return panels[i]
            pid = t.get("aria-controls")
            return soup.find(id=pid) if pid else None
    return None

def extract_section(soup, label, heading):
    panel = panel_for(soup, label)
    if not panel:
        return ""
    inner = sanitise(panel)
    # panels repeat the tab title as their first heading — drop it to avoid a
    # duplicate "<h4>Overview</h4><h5>Overview</h5>".
    inner = re.sub(r"^\s*<h5>\s*" + re.escape(label) + r"\s*</h5>", "", inner, flags=re.I)
    return f"<h4>{heading}</h4>{inner.strip()}" if inner.strip() else ""

# --- per course ------------------------------------------------------------
def scrape_course(c):
    d = {"cricos": "", "title": c["title"], "url": c["url"],
         "course_code": c["course_code"], "course_description": "",
         "course_duration_per_week": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL",
         "materials_fee": "NULL", "entry_requirements": "", "apply_form": c["url"],
         "intake_months": [], "note": ""}
    try:
        soup = BeautifulSoup(str(get_page(c["url"]).html_content), "html.parser")
        d["cricos"] = extract_cricos(soup)
        total, ssaf = extract_fees(soup)
        d["offshore_tuition_fee"] = str(total) if total is not None else "NULL"
        d["enrolment_fee"] = str(ssaf) if ssaf is not None else "NULL"
        d["course_duration_per_week"] = extract_duration_weeks(soup, c["feed_duration"])
        d["course_description"] = clean_html(extract_section(soup, "Overview", "Overview"))
        d["entry_requirements"] = clean_html(
            extract_section(soup, "Entry requirements", "Entry Requirements"))
        d["intake_months"] = extract_intake_months(soup)
        if not d["cricos"]:
            d["note"] = "no CRICOS on page (online/non-accredited?)"
        print(f"{'✅' if d['cricos'] else '⚠️ '} {d['title'][:48]:48} → "
              f"CRICOS {d['cricos'] or '—'} | offshore {d['offshore_tuition_fee']} "
              f"| {d['course_duration_per_week'] or '?'}w")
    except Exception as e:
        d["note"] = f"error: {e}"
        print(f"❌ {c['url']}: {e}")
    return d

# --- main ------------------------------------------------------------------
def main():
    courses = fetch_courses()
    print(f"Feed: {len(courses)} international courses\n")
    results = [scrape_course(c) for c in courses]

    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)

    emitted = set()
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d["cricos"]:
                reason = (d["note"] or "no CRICOS").replace("\n", " ").replace("\r", "")
                f.write(f"-- ⚠️ Skipped ({reason}): {d['title']} | {d['url']}\n\n")
                continue
            if d["cricos"] in emitted:
                f.write(f"-- ⚠️ Skipped (CRICOS {d['cricos']} already emitted): {d['title']} | {d['url']}\n\n")
                continue
            emitted.add(d["cricos"])
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
        "course_code": d["course_code"],
        "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "enrolment_fee": cell(d["enrolment_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
        "note": d["note"],
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    ok = len(emitted)
    print(f"\n✅ {ok}/{len(results)} courses with CRICOS. Intake: {intake_date}\n"
          f"SQL  -> {SQL_PATH}\nxlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
