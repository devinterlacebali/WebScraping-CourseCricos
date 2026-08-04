"""
Curtin University course scraper — CSV + handbook hybrid.

Curtin site: React SPA + Cloudflare.
Strategy: handbook course URLs + CSV CRICOS/fee matching.
Fallback: page extraction for description/entry reqs.
Provider: 00301J
"""
import os, re, sys, csv, time, json

sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception: pass

from bs4 import BeautifulSoup
from curl_cffi import requests as curl_requests
import pandas as pd

# --- constants ---
PROVIDER_CODE = "00301J"
SLUG = "curtin"
DIR = "Curtin University"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
HANDBOOK_SITEMAP = "https://handbook.curtin.edu.au/sitemap.xml"
TIMEOUT = 60

MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# --- shared helpers ---
ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5"}

def sanitise(html):
    if not html: return ""
    frag = BeautifulSoup(html, "html.parser")
    for t in frag.find_all(["style","script","noscript","form","iframe","img","svg","button"]):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href": del t[a]
    for t in frag.find_all("span"): t.unwrap()
    while True:
        div = frag.find("div")
        if div is None: break
        if div.find(["p","ul","ol","li","div","table","h5"]): div.unwrap()
        else: div.name = "p"
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS: t.unwrap()
    for t in frag.find_all(["p","li"]):
        if not t.get_text(strip=True) and not t.find("br"): t.decompose()
    return str(frag)

def clean_html(html):
    if not html: return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

def get_page(url, tries=3):
    for i in range(tries):
        try:
            r = curl_requests.get(url, impersonate='chrome120', timeout=TIMEOUT)
            if len(r.text) < 500: return None
            return r
        except Exception:
            time.sleep(1.5 * (i+1))
    return None

# --- CSV data load ---
def load_csv_data():
    csv_courses = []
    try:
        with open("cricos-courses.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)
            for row in reader:
                if not row or len(row) < 5: continue
                if row[0].strip() == PROVIDER_CODE:
                    csv_courses.append({
                        "cricos": row[2].strip(),
                        "name": row[3].strip(),
                        "duration_weeks": row[19].strip() if len(row) > 19 else "",
                        "tuition_fee": row[20].strip().replace("$","").replace(",","") if len(row) > 20 else "",
                        "vet_code": row[4].strip() if len(row) > 4 else "",
                    })
    except FileNotFoundError: pass
    return csv_courses

def _normalise(name):
    n = re.sub(r"[^a-z0-9\s]", " ", name.lower())
    return re.sub(r"\s+", " ", n).strip()

def match_csv(title, csv_courses):
    """Match a course title to CSV entry by normalised name similarity."""
    if not title: return None
    norm = _normalise(title)
    best = None
    best_score = 0
    for c in csv_courses:
        csv_norm = _normalise(c["name"])
        tw = set(norm.split())
        cw = set(csv_norm.split())
        if not tw or not cw: continue
        overlap = len(tw & cw)
        score = overlap / max(len(tw), len(cw))
        if score > best_score:
            best_score = score
            best = c
    if best_score >= 0.5:
        return best
    # Try substring match
    for c in csv_courses:
        csv_norm = _normalise(c["name"])
        if csv_norm in norm or norm in csv_norm:
            return c
    return None

# --- get all course URLs from handbook ---
def build_driver(csv_lookup):
    """Get only handbook course URLs that match CSV entries."""
    r = get_page(HANDBOOK_SITEMAP)
    if not r: return pd.DataFrame()
    urls = re.findall(r'<loc>(.*?)</loc>', r.text)
    course_urls = sorted(set(u for u in urls if '/courses/course-' in u.lower()))
    print(f"Handbook course URLs: {len(course_urls)}")
    rows = []
    matched = 0
    for u in course_urls:
        slug = u.rstrip("/").split("/")[-1]
        title = slug.split("--")[0] if "--" in slug else slug
        for pfx in ["course-ug-", "course-pg-", "course-brg-", "course-vet-"]:
            if title.startswith(pfx): title = title[len(pfx):]
        title_clean = title.replace("-", " ").title()
        # Only include if matches CSV
        if match_csv(title_clean, csv_lookup):
            rows.append({"title": title_clean, "url": u})
            matched += 1
    print(f"  Matched CSV: {matched}")
    return pd.DataFrame(rows)

# --- extract from page ---
def extract_course_title(page):
    h1 = page.find("h1")
    return h1.get_text(strip=True) if h1 else ""

def extract_course_description(page):
    """Try to extract description from handbook page."""
    # Look for "About" or "Outline" section
    for heading_text in ["About this course", "Course outline", "Overview", "Description"]:
        h = page.find(["h2","h3"], string=re.compile(heading_text, re.I))
        if h:
            parts = []
            for sib in h.find_all_next(["p","ul","ol"], limit=6):
                if sib.name == "h2": break
                if sib.get_text(strip=True): parts.append(str(sib))
            if parts: return clean_html(sanitise("".join(parts)))
    return ""

def extract_entry_requirements(page):
    for heading_text in ["Admission requirements", "Entry requirements", "Admission criteria"]:
        h = page.find(["h2","h3"], string=re.compile(heading_text, re.I))
        if h:
            parts = []
            for sib in h.find_all_next(["p","ul","ol"], limit=8):
                if sib.name == "h2": break
                if sib.get_text(strip=True): parts.append(str(sib))
            if parts: return clean_html(sanitise("".join(parts)))
    return ""

# --- scrape course ---
def scrape_course(row, csv_lookup):
    """Scrape a course - use CSV data matched by title, plus page description."""
    url = row["url"]
    title = row["title"]
    
    # Match CSV
    csv_match = match_csv(title, csv_lookup)
    
    # Try to get page for description/entry reqs
    rp = get_page(url)
    description = ""
    entry_reqs = ""
    
    if rp:
        page = BeautifulSoup(rp.text, "html.parser")
        page_title = extract_course_title(page)
        if page_title:
            title = page_title
        description = extract_course_description(page)
        entry_reqs = extract_entry_requirements(page)
    
    # Use CSV data for CRICOS, fee, duration
    cricos = csv_match["cricos"] if csv_match else ""
    fee = csv_match["tuition_fee"] if csv_match and csv_match["tuition_fee"] else "NULL"
    dur = csv_match["duration_weeks"] if csv_match else ""
    
    return {
        "cricos": cricos,
        "title": title,
        "url": url,
        "course_description": description,
        "course_duration_per_week": dur,
        "offshore_tuition_fee": fee,
        "onshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL",
        "materials_fee": "NULL",
        "entry_requirements": entry_reqs,
        "intake": "",
    }

# --- output ---
def save_output(results, intake_date):
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write(f"UPDATE provider_institution SET intake_date = '{intake_date}', "
                f"updated_at = NOW() WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d.get("cricos"):
                f.write(f"-- ⏭️ (no CRICOS): {d['title']} | {d['url']}\n\n")
                continue
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    onshore_tuition_fee = {d["onshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    materials_fee = {d["materials_fee"]},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["url"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")
    def cell(v):
        return (v or "").replace("''", "'")[:32000] if v not in (None, "NULL") else ""
    pd.DataFrame([{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "enrolment_fee": cell(d["enrolment_fee"]), "materials_fee": cell(d["materials_fee"]),
        "intake": d.get("intake", ""), "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

# --- main ---
def main():
    csv_lookup = load_csv_data()
    print(f"CSV courses for {PROVIDER_CODE}: {len(csv_lookup)}")
    
    df = build_driver(csv_lookup)
    print(f"Driver: {len(df)} courses")
    
    results = []
    for i, (_, row) in enumerate(df.iterrows(), 1):
        d = scrape_course(row.to_dict(), csv_lookup)
        results.append(d)
        marker = "✅" if d.get("cricos") else "⏭️"
        print(f"  {marker} [{i}/{len(df)}] {d['title'][:50]} | CRICOS={d.get('cricos','')} | Fee={d.get('offshore_tuition_fee','NULL')}")
    
    intake_date = "January, February, March, April, May, June, July, August, September, October, November, December"
    save_output(results, intake_date)
    
    with_cricos = sum(1 for d in results if d.get("cricos"))
    with_fee = sum(1 for d in results if d.get("offshore_tuition_fee","NULL") not in ("NULL",""))
    with_dur = sum(1 for d in results if d.get("course_duration_per_week"))
    
    print(f"\n✅ {len(results)} courses.")
    print(f"   CRICOS: {with_cricos}")
    print(f"   Fee: {with_fee}")
    print(f"   Duration: {with_dur}")
    print(f"   SQL -> {SQL_PATH}")
    print(f"   xlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
