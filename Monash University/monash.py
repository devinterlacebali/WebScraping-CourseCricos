import os
import re
import sys
import json
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from curl_cffi import requests
from curl_cffi.requests import AsyncSession

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Try importing the shared ai_formatter helper if it exists in parent directory
try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import ai_formatter
except ImportError:
    ai_formatter = None

# --- Constants -------------------------------------------------------------
PROVIDER_CODE = "00008C"                   # Monash University CRICOS Provider Code
SLUG = "monash"
DIR = "Monash University"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- Shared Helpers --------------------------------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html: str) -> str:
    frag = BeautifulSoup(html, "html.parser")
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

# --- Course Discovery ------------------------------------------------------
def discover_courses():
    url = "https://handbook.monash.edu/api/search/search-academic-items"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    courses = []
    page_size = 100
    from_idx = 0
    total = 1
    
    print("Discovering Monash courses from Handbook API...")
    while from_idx < total:
        payload = {
            "siteId": "monash-prod-pres",
            "query": "",
            "contenttype": "course",
            "searchFilters": [
                {"filterField": "implementationYear", "filterValue": ["2026"], "isExactMatch": False}
            ],
            "from": from_idx,
            "size": page_size
        }
        try:
            response = requests.post(url, json=payload, headers=headers, impersonate="chrome120")
            if response.status_code == 200:
                data = response.json().get("data", {})
                results = data.get("results", [])
                total = data.get("total", 0)
                for item in results:
                    code = item.get("code")
                    title = item.get("title")
                    uri = item.get("uri")
                    course_url = f"https://handbook.monash.edu{uri}"
                    courses.append({
                        "cricos": "",
                        "title": title,
                        "url": course_url,
                        "code": code
                    })
                from_idx += page_size
            else:
                print(f"Error fetching search results at index {from_idx}: {response.text}")
                break
        except Exception as e:
            print(f"Exception during course discovery: {e}")
            break
            
    print(f"Discovered {len(courses)} courses in total.")
    return courses

# --- Course Detail Fetching ------------------------------------------------
async def fetch_course_detail(session, sem, url, title, cricos_input):
    d = {
        "cricos": cricos_input, "title": title, "url": url, "course_description": "",
        "course_duration_per_week": "", "offshore_tuition_fee": "NULL",
        "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL", "materials_fee": "NULL",
        "entry_requirements": "", "apply_form": url, "intake_months": ["February", "July"]
    }
    
    async with sem:
        try:
            response = await session.get(url, impersonate="chrome120")
            if response.status_code == 200:
                html = response.text
                m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
                if m:
                    data = json.loads(m.group(1))
                    page_content = data.get("props", {}).get("pageProps", {}).get("pageContent", {})
                    
                    # Extract CRICOS code if not provided
                    scraped_cricos = page_content.get("cricos_code")
                    if scraped_cricos and str(scraped_cricos).strip().lower() not in ("nan", "none", "null", ""):
                        d["cricos"] = str(scraped_cricos).strip()
                    
                    # Extract Course Description (Overview + Structure)
                    overview = page_content.get("overview", "") or ""
                    structure = page_content.get("structure", "") or ""
                    desc_html = ""
                    if overview:
                        desc_html += f"<h4>Overview</h4>{sanitise(overview)}"
                    if structure:
                        desc_html += f"<h4>Structure</h4>{sanitise(structure)}"
                    d["course_description"] = clean_html(desc_html)
                    
                    # Extract Entry & English Requirements
                    entry = page_content.get("entry", "") or ""
                    english = page_content.get("english_language", "") or ""
                    req_html = ""
                    if entry:
                        req_html += f"<h4>Entry Requirements</h4>{sanitise(entry)}"
                    if english:
                        req_html += f"<h4>English Language Requirements</h4>{sanitise(english)}"
                    
                    # Apply LLM formatting if configured
                    plain_reqs = re.sub(r'<[^>]+>', ' ', req_html).strip()
                    if ai_formatter is not None and ai_formatter.enabled():
                        formatted = ai_formatter.format_requirements(plain_reqs)
                        if formatted:
                            req_html = formatted
                    d["entry_requirements"] = clean_html(req_html)
                    
                    # Extract Duration
                    full_time_duration = page_content.get("full_time_duration", [])
                    if full_time_duration and isinstance(full_time_duration, list):
                        item = full_time_duration[0]
                        duration_number = item.get("duration_number")
                        duration_period = item.get("duration_period", {}).get("value", "")
                        try:
                            num = float(duration_number)
                            period = str(duration_period).lower()
                            if "year" in period:
                                d["course_duration_per_week"] = str(int(num * 52))
                            elif "month" in period:
                                d["course_duration_per_week"] = str(int(num * 4.333))
                            elif "week" in period:
                                d["course_duration_per_week"] = str(int(num))
                        except (ValueError, TypeError):
                            pass
                            
                else:
                    print(f"[-] No __NEXT_DATA__ script tag found for {url}")
            else:
                print(f"[-] HTTP {response.status_code} for {url}")
        except Exception as e:
            print(f"[-] Error fetching {url}: {e}")
            
    print(f"[{'OK' if d['cricos'] else 'NO_CRICOS'}] {url}")
    return d

async def run_scraper(rows):
    sem = asyncio.Semaphore(10)  # limit concurrency to 10 requests at a time
    async with AsyncSession(max_clients=20) as session:
        tasks = [
            fetch_course_detail(session, sem, r["url"], r["title"], r["cricos"])
            for r in rows
        ]
        return await asyncio.gather(*tasks)

# --- Main Scraper Entry ----------------------------------------------------
def main():
    os.makedirs(DIR, exist_ok=True)
    
    # 1. Discover courses if the driver Excel file doesn't exist
    if not os.path.exists(EXCEL_PATH):
        courses = discover_courses()
        if not courses:
            print("❌ No courses discovered. Exiting.")
            return
        df_driver = pd.DataFrame(courses)[["cricos", "title", "url"]]
        df_driver.to_excel(EXCEL_PATH, index=False)
        print(f"Saved initial driver to {EXCEL_PATH}")
    else:
        print(f"Using existing driver file: {EXCEL_PATH}")
        df_driver = pd.read_excel(EXCEL_PATH)
        
    # Convert driver rows to a list of dicts
    driver_rows = []
    for _, r in df_driver.iterrows():
        cricos = str(r.get("cricos", "")).strip()
        if cricos.lower() in ("nan", "none", "null"):
            cricos = ""
        driver_rows.append({
            "cricos": cricos,
            "title": str(r.get("title", "")).strip(),
            "url": str(r.get("url", "")).strip()
        })
        
    print(f"Scraping {len(driver_rows)} courses concurrently...")
    
    # Run async scraping loop
    results = asyncio.run(run_scraper(driver_rows))
    
    # Calculate unique intake months
    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)
    
    # 2. Write SQL output file
    print(f"Writing SQL updates to {SQL_PATH}...")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped (no/unreliable CRICOS course code): {d['title']} | {d['url']}\n\n")
                continue
                
            f.write(f"UPDATE courses SET\n"
                    f"    course_description = '{d['course_description']}',\n"
                    f"    course_duration_per_week = {d['course_duration_per_week'] or 'NULL'},\n"
                    f"    offshore_tuition_fee = {d['offshore_tuition_fee']},\n"
                    f"    onshore_tuition_fee = {d['onshore_tuition_fee']},\n"
                    f"    enrolment_fee = {d['enrolment_fee']},\n"
                    f"    materials_fee = {d['materials_fee']},\n"
                    f"    entry_requirements = '{d['entry_requirements']}',\n"
                    f"    apply_form = '{d['apply_form']}',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{d['cricos']}';\n\n")
                    
    # 3. Write enriched Excel output
    print(f"Writing enriched Excel file to {EXCEL_PATH}...")
    def cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]
        
    pd.DataFrame([{
        "cricos": d["cricos"],
        "title": d["title"],
        "url": d["url"],
        "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "enrolment_fee": cell(d["enrolment_fee"]),
        "materials_fee": cell(d["materials_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)
    
    print(f"\n✅ {len(results)} courses scraped.")
    print(f"Intake: {intake_date}")
    print(f"SQL file -> {SQL_PATH}")
    print(f"Excel file -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
