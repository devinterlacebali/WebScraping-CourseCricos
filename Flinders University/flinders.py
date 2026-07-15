"""
Flinders University course scraper (Scrapling, plain HTTP).

Driver = the site's Algolia search index (`flinders_main_search`, filter
`dir2:courses`). One POST returns every course; we keep those whose `availability`
includes "International" (~144). The feed has no CRICOS/fees, so each course page
is scraped for: CRICOS, international (FFP) fee, entry requirements. Duration and
intake come from the feed.

Fees on the page are the *annual* indicative FFP figure -> total = annual x years
(repo standard, matching the Federation/Swinburne scrapers).

Output: swinburne-style -> swinburne_courses_update.sql equivalent
(flinders_courses_update.sql) + flinders.xlsx enriched record.
"""
import re
import sys
import os
import json
import time
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from scrapling.fetchers import Fetcher

# Append parent directory to sys.path to import ai_formatter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from ai_formatter import format_requirements
except ImportError:
    def format_requirements(text):
        return ""

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- constants -------------------------------------------------------------
PROVIDER_CODE = "00114A"                        # Flinders University
SLUG = "flinders"
DIR = "Flinders University"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

ALGOLIA_APP = "EDB1U8JSME"
ALGOLIA_KEY = "5292c8a20c605ac1c7c48baa60e8317e"
ALGOLIA_INDEX = "flinders_main_search"

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
    for t in frag.select("nav, script, style, noscript, form, iframe, img, svg, button, "
                         "[class*='breadcrumb'], .domestic_content_marker"):
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

def money(s):
    m = re.search(r"\$\s?([\d,]+)", s or "")
    if not m:
        return None
    v = int(m.group(1).replace(",", ""))
    return v if v > 0 else None

def get_page(url, tries=3):
    last = RuntimeError("unreachable")
    for i in range(tries):
        try:
            return Fetcher.get(url, stealthy_headers=True)
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last

# --- feed (Algolia) --------------------------------------------------------
def fetch_courses():
    url = f"https://{ALGOLIA_APP}-dsn.algolia.net/1/indexes/{ALGOLIA_INDEX}/query"
    body = json.dumps({"params": "query=&hitsPerPage=1000&filters=dir2:courses"}).encode()
    headers = {
        "X-Algolia-Application-Id": ALGOLIA_APP,
        "X-Algolia-API-Key": ALGOLIA_KEY,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    hits = None
    for i in range(3):
        try:
            req = urllib.request.Request(url, data=body, method="POST", headers=headers)
            hits = json.loads(urllib.request.urlopen(req, timeout=40).read().decode())["hits"]
            break
        except Exception:
            time.sleep(1.5 * (i + 1))
    if hits is None:
        raise RuntimeError("Algolia feed fetch failed after retries")
    courses, seen = [], set()
    for h in hits:
        if "International" not in (h.get("availability") or []):
            continue
        url = (h.get("courseLink") or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        dur = h.get("duration")
        try:
            years = float(dur)
        except (TypeError, ValueError):
            years = None
        courses.append({
            "title": h.get("courseName", "").strip(),
            "url": url,
            "years": years,
            "intake_months": [m for m in (h.get("startDatesInt") or []) if m in MONTH_ORDER],
            "meta": (h.get("description") or "").strip(),
        })
    return courses

# --- page field extraction -------------------------------------------------
CRICOS_RE = re.compile(r"\b(\d{6}[A-Z]|\d{7})\b")
CRICOS_LABEL = re.compile(r"^CRICOS(\s+code)?$", re.I)

def extract_cricos(soup):
    # new template: a .cricos quick-fact block carries the code inline
    for c in soup.select("[class*='cricos']"):
        m = CRICOS_RE.search(txt(c))
        if m:
            return m.group(1)
    # other templates carry a "CRICOS [code]" label followed by the code in the
    # next element (<strong>+<p>, .content_header+.content_detail, .label+.contents…)
    for lab in soup.find_all(["strong", "div", "span", "p", "dt", "th"]):
        if CRICOS_LABEL.match(txt(lab)):
            for nxt in lab.find_all_next(["p", "div", "span", "dd", "td"], limit=3):
                m = CRICOS_RE.search(txt(nxt))
                if m:
                    return m.group(1)
    return ""

def extract_years(soup, feed_years):
    if feed_years:
        return feed_years
    meta = soup.find("meta", attrs={"property": "duration"})
    if meta and meta.get("content"):
        m = re.search(r"([\d.]+)", meta["content"])   # "1.5 or 2" -> 1.5
        if m:
            return float(m.group(1))
    return None

def extract_offshore_annual(soup):
    """Annual international fee across templates. Domestic is the Commonwealth
    Supported Place ("(CSP)"); international is the Full Fee Paying figure —
    labelled "(FFP)" on new pages, unlabelled on double-degree pages. We take the
    FFP amount, else the largest non-CSP fee (international always exceeds CSP)."""
    cands = []   # (amount, is_ffp, is_csp)
    for el in soup.select(".international_content_marker, .content_detail, .contents, "
                          "[class*='fee'] .content_detail, [class*='fee']"):
        s = txt(el)
        if "$" not in s or "fee" not in s.lower() and not re.search(r"\d{4}\s*:", s):
            # only trust $ amounts that sit in a fee context
            if "CSP" not in s and "FFP" not in s:
                continue
        for m in re.finditer(r"\$\s?([\d,]+)", s):
            amt = int(m.group(1).replace(",", ""))
            if amt > 0:
                cands.append((amt, "FFP" in s, "CSP" in s))
    if not cands:
        return None
    ffp = [a for a, f, c in cands if f]
    if ffp:
        return max(ffp)
    non_csp = [a for a, f, c in cands if not c]
    return max(non_csp) if non_csp else None

def extract_description(soup, meta):
    md = soup.find("meta", attrs={"name": "description"})
    desc = (md.get("content").strip() if md and md.get("content") else "") or meta
    return f"<h4>Overview</h4><p>{desc}</p>" if desc else ""

def extract_entry(soup):
    """International English-language + prerequisite requirements."""
    parts = []
    for c in soup.select("[class*='international_content_marker']"):
        s = txt(c)
        if re.search(r"IELTS|Pearson|TOEFL|English language", s):
            parts.append(("English language requirements",
                          re.split(r"English language requirements", s)[0].strip() or s))
            break
    for qf in soup.select("[class*='as_icon'], [class*='key-fact']"):
        s = txt(qf)
        if s.lower().startswith("prerequisites"):
            parts.append(("Prerequisites", s[len("Prerequisites"):].strip()))
            break
    if not any(h == "English language requirements" for h, _ in parts):
        # fallback for old/double-degree templates without international markers
        m = re.search(r"(IELTS[^<]{0,180})", soup.get_text(" "))
        if m:
            eng = re.split(r"English language requirements|Entry requirements", m.group(1))[0].strip()
            if len(eng) > 8:
                parts.insert(0, ("English language requirements", eng))
    if not parts:
        return ""

    # Construct raw text for AI formatting
    raw_text_parts = []
    for head, body in parts:
        if body:
            raw_text_parts.append(f"{head}: {body}")
    raw_text = "\n".join(raw_text_parts)

    try:
        formatted_html = format_requirements(raw_text)
        if formatted_html and formatted_html.strip():
            return formatted_html
    except Exception as e:
        print(f"AI Formatting failed: {e}")

    # Fallback to deterministic HTML table
    out = "<table><tbody>"
    for head, body in parts:
        if body:
            if "english" in head.lower():
                cat = "English Proficiency"
            elif "prerequisite" in head.lower():
                cat = "Academic Requirements"
            else:
                cat = head
            out += f"<tr><td><strong>{cat}</strong></td><td><ul><li>{body}</li></ul></td></tr>"
    out += "</tbody></table>"
    return out

# --- per course ------------------------------------------------------------
def scrape_course(c):
    d = {"cricos": "", "title": c["title"], "url": c["url"],
         "course_description": "", "course_duration_per_week": "",
         "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
         "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": c["url"],
         "intake_months": c["intake_months"], "note": ""}
    try:
        soup = BeautifulSoup(str(get_page(c["url"]).html_content), "html.parser")
        d["cricos"] = extract_cricos(soup)
        years = extract_years(soup, c["years"])
        if years:
            d["course_duration_per_week"] = str(int(round(years * 52)))
        annual = extract_offshore_annual(soup)
        if annual:
            # annual FFP fee -> total over the course; never scale below one year
            # (sub-year certs quote the whole-course figure as the "annual" fee).
            d["offshore_tuition_fee"] = str(int(round(annual * max(1.0, years or 1))))
        d["course_description"] = clean_html(extract_description(soup, c["meta"]))
        d["entry_requirements"] = clean_html(extract_entry(soup))
        if not d["cricos"]:
            d["note"] = "no CRICOS on page"
        print(f"{'✅' if d['cricos'] else '⚠️ '} {d['title'][:46]:46} → "
              f"CRICOS {d['cricos'] or '—'} | offshore {d['offshore_tuition_fee']} "
              f"| {d['course_duration_per_week'] or '?'}w")
    except Exception as e:
        d["note"] = f"error: {e}"
        print(f"❌ {c['url']}: {e}")
    return d

# --- main ------------------------------------------------------------------
def main():
    courses = fetch_courses()
    print(f"Algolia: {len(courses)} international courses\n")
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
        "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
        "note": d["note"],
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    print(f"\n✅ {len(emitted)}/{len(results)} courses with CRICOS. Intake: {intake_date}\n"
          f"SQL  -> {SQL_PATH}\nxlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
