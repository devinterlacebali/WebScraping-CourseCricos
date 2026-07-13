"""
Australian Catholic University (ACU) course scraper — upgraded version.

Provider CRICOS code: 00004G.

Rewritten from the old `requests`-based script to the repo's standard shape:
  * Scrapling stealthy fetch (no browser).
  * Clean semantic HTML via sanitise() (no wrapper divs / style attrs).
  * Provider `intake_date` UPDATE + per-course UPDATEs.
  * Driver + enriched record written to acu.xlsx.

Driver list: `Courses - ACU.txt` (tab-separated `cricos_course_code<TAB>course name`), which
is authoritative for the CRICOS codes. Each course has an onshore page
`/course/<slug>` and an international page `/course/<slug>?type=International`.

Fees are stored as **total course cost** (user preference):
  * offshore = ACU's published "Estimate total cost" (International), else first-year x years.
  * onshore  = domestic first-year (CSP) x number of full-time years (ACU publishes no
    domestic total; ACU's own total = first-year x years).
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

PROVIDER_CODE = "00004G"
DIR = "Australian Catholic University"
SLUG = "acu"
COURSES_FILE = f"{DIR}/Courses - ACU.txt"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
BASE = "https://www.acu.edu.au/course/"
DELAY = 1.0

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
    for p in frag.find_all("p"):
        s = p.get_text(strip=True)
        if s.endswith(":") and len(s) < 60 and not p.find(["strong", "b", "a"]):
            p.string = ""
            strong = frag.new_tag("strong")
            strong.string = s
            p.append(strong)
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)


def slugify(name: str) -> str:
    s = name.lower().replace("’", "").replace("'", "")
    s = s.replace("&", "and")
    s = re.sub(r"[()]", "", s)
    s = re.sub(r"\s*/\s*", "", s)       # ACU concatenates double degrees with no separator
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-]", "", s)
    return re.sub(r"-+", "-", s).strip("-")


def fee_number(text) -> str:
    m = re.search(r"\$?\s*([\d,]{3,})", str(text or ""))
    return m.group(1).replace(",", "") if m else ""


def parse_years(duration_text: str):
    """Number of full-time years from a duration string, or None."""
    if not duration_text:
        return None
    m = re.search(r"(\d+(?:\.\d+)?)\s*years?", duration_text, re.I)
    if m:
        return float(m.group(1))
    m = re.search(r"(\d+(?:\.\d+)?)\s*months?", duration_text, re.I)
    if m:
        return float(m.group(1)) / 12.0
    return None


def as_fee(value: float) -> str:
    if value is None:
        return ""
    return str(int(round(value)))


def months_in(text: str):
    found = []
    # ACU: "Semester 1 intake: Beginning March 2026 ... Midyear (Semester 2) intake: Beginning August 2026"
    for m in re.finditer(r"intake:\s*Beginning\s+([A-Za-z]+)", text, re.I):
        mon = MONTHS.get(m.group(1).lower())
        if mon and mon not in found:
            found.append(mon)
    return found


# ---------- per-course scraping ----------
def scrape_course(cricos, name):
    onshore_url = f"{BASE}{slugify(name)}"
    offshore_url = f"{onshore_url}?type=International"
    d = {
        "cricos": cricos, "title": name, "url": onshore_url,
        "course_description": "", "total_course_duration": "",
        "offshore_tuition_fee": "", "onshore_tuition_fee": "",
        "entry_requirements": "", "apply_form": onshore_url,
        "intake": "", "ok": False,
    }

    r = Fetcher.get(onshore_url, stealthy_headers=True)
    if r.status != 200:
        print(f"⚠️  {name}: onshore page {r.status}")
        return d
    soup = BeautifulSoup(r.html_content, "html.parser")
    text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))
    d["ok"] = True

    # Description
    desc = soup.find(id="overview-description")
    if desc:
        d["course_description"] = clean_html(f"<h4>Course Information</h4>{sanitise(str(desc))}")

    # Duration — "Duration" dt/th followed by dd/td
    duration_text = ""
    for lbl in soup.find_all(["dt", "th"]):
        if lbl.get_text(strip=True).lower().startswith("duration"):
            sib = lbl.find_next(["dd", "td"])
            if sib:
                duration_text = sib.get_text(" ", strip=True)
                break
    if not duration_text:
        m = re.search(r"(\d+(?:\.\d+)?\s*years?[^.,;]*)", text)
        duration_text = m.group(1).strip() if m else ""
    d["total_course_duration"] = clean_html(duration_text)
    years = parse_years(duration_text)

    # Onshore (domestic/CSP) first-year fee
    onshore_fy = ""
    fee_link = soup.find("a", href="#feeaccordion")
    if fee_link:
        onshore_fy = fee_number(fee_link.get_text(" ", strip=True))
    if not onshore_fy:
        m = re.search(r"Average first year fee\*?\s*\$?([\d,]+)", text)
        onshore_fy = m.group(1).replace(",", "") if m else ""
    if onshore_fy:
        d["onshore_tuition_fee"] = as_fee(float(onshore_fy) * years) if years else onshore_fy

    # Intake months
    intake_months = months_in(text)
    d["intake"] = ", ".join(intake_months)

    # Entry requirements accordion (h2 "Entry requirements")
    for div in soup.find_all("div", class_="col-md-12 side-accordion--multi"):
        h = div.find(["h2", "h1"])
        if h and "entry requirements" in h.get_text(strip=True).lower():
            d["entry_requirements"] = build_entry_reqs(str(div))
            break

    # Offshore (international) total course cost
    r2 = Fetcher.get(offshore_url, stealthy_headers=True)
    if r2.status == 200:
        t2 = re.sub(r"\s+", " ", BeautifulSoup(r2.html_content, "html.parser").get_text(" ", strip=True))
        m = re.search(r"Estimate total cost[:\*]*\s*\$([\d,]+)", t2, re.I)
        if m:
            d["offshore_tuition_fee"] = m.group(1).replace(",", "")
        else:
            m2 = re.search(r"first year fee[:\*]*\s*\$([\d,]+)", t2, re.I)
            if m2:
                fy = float(m2.group(1).replace(",", ""))
                d["offshore_tuition_fee"] = as_fee(fy * years) if years else str(int(fy))

    return d, intake_months


def build_entry_reqs(html):
    # Drop the section's own heading so it doesn't leak into the body text.
    frag = BeautifulSoup(html, "html.parser")
    for h in frag.find_all(["h1", "h2", "h3", "h4"]):
        h.decompose()
    body = sanitise(str(frag))
    return clean_html(f"<h4>Entry Requirements</h4>{body}")


# ---------- main ----------
def main():
    with open(COURSES_FILE, encoding="utf-8") as f:
        pairs = []
        for line in f:
            line = line.rstrip("\n")
            if "\t" in line:
                code, nm = line.split("\t", 1)
                if code.strip() and nm.strip():
                    pairs.append((code.strip(), nm.strip()))
    print(f"📋 {len(pairs)} courses in driver\n")

    results = []
    all_months = set()
    for idx, (code, nm) in enumerate(pairs, 1):
        try:
            out = scrape_course(code, nm)
            d, months = out if isinstance(out, tuple) else (out, [])
        except Exception as e:
            print(f"❌ [{idx}/{len(pairs)}] {nm}: {e}")
            continue
        all_months.update(months)
        results.append(d)
        if d["ok"]:
            print(f"✅ [{idx}/{len(pairs)}] {nm[:42]} | off ${d['offshore_tuition_fee'] or '-'} "
                  f"| on ${d['onshore_tuition_fee'] or '-'} | {d['total_course_duration'][:22]}")
        time.sleep(DELAY)

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
            if not d["ok"]:
                f.write(f"-- ⚠️ Skipped (page not found): {d['title']} | {d['url']}\n\n")
                continue
            written += 1
            f.write(
                "UPDATE courses SET\n"
                f"    course_description = '{d['course_description']}',\n"
                f"    offshore_tuition_fee = '{d['offshore_tuition_fee']}',\n"
                f"    onshore_tuition_fee = '{d['onshore_tuition_fee']}',\n"
                f"    entry_requirements = '{d['entry_requirements']}',\n"
                f"    total_course_duration = '{d['total_course_duration']}',\n"
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
        "intake": cell(d["intake"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    skipped = sum(1 for d in results if not d["ok"])
    print(f"\n🏁 Done. {written} course UPDATEs, {skipped} skipped. Provider intake: {intake_date}")


if __name__ == "__main__":
    main()
