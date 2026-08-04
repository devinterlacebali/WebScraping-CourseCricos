"""
La Trobe University course scraper (Playwright + BeautifulSoup).

Scrapes course details by navigating directly to La Trobe's JSON API endpoints using fresh contexts to bypass Cloudflare.
Aligns with the repository's scraping structure and DB updates.
"""
import os
import re
import sys
import csv
import json
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Configure standard encoding for Windows environment
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Append parent directory to sys.path to import ai_formatter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from ai_formatter import format_requirements
except ImportError:
    def format_requirements(text):
        return ""

PROVIDER_CODE = "00115M"
SLUG = "latrobe"
DIR = "La Trobe University (La Trobe)"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

REGISTER_CSV = "cricos-courses.csv"

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December", "january": "January",
    "february": "February", "march": "March", "april": "April", "june": "June",
    "july": "July", "august": "August", "september": "September",
    "october": "October", "november": "November", "december": "December",
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- helper functions ------------------------------------------------------
def clean_html(html_str: str) -> str:
    if not html_str:
        return ""
    html_str = re.sub(r"\s+", " ", html_str)
    return html_str.replace("'", "''").strip()

def clean_numeric_fee(val) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html_content: str) -> str:
    if not html_content:
        return ""
    frag = BeautifulSoup(html_content, "html.parser")
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

def extract_duration_weeks(duration_str: str) -> str:
    if not duration_str:
        return ""
    match = re.search(r"([0-9.]+)\s*year", duration_str, re.IGNORECASE)
    if match:
        years = float(match.group(1))
        return str(int(round(years * 52)))
    match = re.search(r"([0-9.]+)\s*month", duration_str, re.IGNORECASE)
    if match:
        months = float(match.group(1))
        return str(int(round(months * 4.33)))
    match = re.search(r"([0-9.]+)\s*week", duration_str, re.IGNORECASE)
    if match:
        return str(int(round(float(match.group(1)))))
    return ""

# --- parsing functions -----------------------------------------------------
def extract_course_description(c_data):
    desc = c_data.get("courseDescription") or ""
    return sanitise(desc) if desc else ""

def extract_fees(c_data):
    fees_data = c_data.get("fees") or {}
    raw_fees = fees_data.get("rawFees") or []
    
    offshore_fee = ""
    for item in raw_fees:
        if item.get("Fee_Type") == "International":
            offshore_fee = item.get("Fee_Amount") or ""
            break
            
    # Fallback to feesLegacy
    if not offshore_fee:
        fees_legacy = c_data.get("feesLegacy") or {}
        desc = fees_legacy.get("amountDescription") or fees_legacy.get("overview") or ""
        m = re.search(r"\$\s*([\d,]+)", desc)
        if m:
            offshore_fee = m.group(1).replace(",", "")
            
    return offshore_fee

def extract_intake_months(c_data):
    start_dates = c_data.get("startDates") or ""
    found_months = []
    for key in MONTHS:
        if re.search(r"\b" + key + r"\b", start_dates, re.IGNORECASE):
            m = MONTHS[key]
            if m not in found_months:
                found_months.append(m)
                
    if not found_months:
        # Fallback common intakes
        for m_name in ["March", "July", "November"]:
            if re.search(r"\b" + m_name + r"\b", start_dates, re.IGNORECASE):
                found_months.append(m_name)
    return found_months

def extract_entry_requirements(c_data):
    entry_req = c_data.get("entryReq") or {}
    rse = entry_req.get("rse") or {}
    prereq = rse.get("prerequisite") or ""
    eng_req = entry_req.get("engReq") or ""
    
    parts = []
    if prereq and prereq.strip():
        parts.append(f"<h4>Academic Requirements</h4>{prereq.strip()}")
    if eng_req and eng_req.strip():
        parts.append(f"<h4>English Language Requirements</h4>{eng_req.strip()}")
        
    entry_html = "\n".join(parts)
    sanitised_entry = sanitise(entry_html)
    if not sanitised_entry:
        return ""
        
    soup_entry = BeautifulSoup(entry_html, "html.parser")
    raw_text = soup_entry.get_text("\n", strip=True)
    
    try:
        formatted_html = format_requirements(raw_text)
        if formatted_html and formatted_html.strip():
            return formatted_html
    except Exception as e:
        print(f"  AI Formatting failed: {e}")
        
    return sanitised_entry

# --- CRICOS Register Backfill ----------------------------------------------
def _norm_title(s):
    s = str(s).lower()
    s = re.sub(r"\b(in|of|the|and|a|an|de)\b", " ", s)
    return re.sub(r"[^a-z0-9]", "", s)

def load_register():
    if not os.path.exists(REGISTER_CSV):
        return {}, {}
    buckets, by_code = {}, {}
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["CRICOS Provider Code"].strip() != PROVIDER_CODE:
                continue
            if r["Expired"].strip().lower() == "yes":
                continue
            buckets.setdefault(_norm_title(r["Course Name"]), []).append(r)
            by_code[r["CRICOS Course Code"].strip()] = r
    by_title = {k: rows[0] for k, rows in buckets.items()
                if len({r["CRICOS Course Code"] for r in rows}) == 1}
    return by_title, by_code

def _fee_num(val):
    v = re.sub(r"[^\d.]", "", str(val or ""))
    return str(int(float(v))) if v else "NULL"

def backfill_from_register(results):
    by_title, by_code = load_register()
    used = {d["cricos"] for d in results if d["cricos"]}
    filled = 0
    
    # 1) Fill missing CRICOS codes from register
    for d in results:
        if d["cricos"]:
            continue
        nt = _norm_title(d["title"])
        row = by_title.get(nt)
        if not row:
            continue
        code = row["CRICOS Course Code"].strip()
        if code in used:
            continue
        used.add(code)
        d["cricos"] = code
        d["offshore_tuition_fee"] = _fee_num(row.get("Tuition Fee"))
        d["enrolment_fee"] = _fee_num(row.get("Non Tuition Fee"))
        dur = re.sub(r"[^\d]", "", str(row.get("Duration (Weeks)") or ""))
        if dur:
            d["course_duration_per_week"] = dur
        d["source"] = "register"
        d["note"] = "CRICOS + fees from register fallback"
        filled += 1
        
    # 2) For all rows with a CRICOS, fill/overwrite international fees and duration from register
    for d in results:
        if not d["cricos"]:
            continue
        row = by_code.get(d["cricos"]) or by_title.get(_norm_title(d["title"]))
        if row and row["CRICOS Course Code"].strip() == d["cricos"]:
            fee = _fee_num(row.get("Tuition Fee"))
            if fee != "NULL":
                d["offshore_tuition_fee"] = fee
            non_fee = _fee_num(row.get("Non Tuition Fee"))
            if non_fee != "NULL":
                d["enrolment_fee"] = non_fee
            dur = re.sub(r"[^\d]", "", str(row.get("Duration (Weeks)") or ""))
            if dur:
                d["course_duration_per_week"] = dur
            d["note"] = (d["note"] + " | fees & duration updated from CRICOS register").strip(" | ")
            
    return filled

# --- scraping workflow ----------------------------------------------------
async def fetch_course_json_with_fresh_context(browser, url):
    slug = url.split("/courses/")[-1]
    
    campuses = ["bu", "on", "sy", "be", "al", "sh"]
    years = ["2026", "2027"]
    student_types = ["international", "domestic"]
    
    # Try combinations
    for year in years:
        for s_type in student_types:
            for campus in campuses:
                # Create fresh context to avoid bot detection cookie build-up
                context = await browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
                page = await context.new_page()
                
                api_url = f"https://www.latrobe.edu.au/courses/data/{year}/{s_type}/{campus}/{slug}"
                try:
                    # Navigate directly to the JSON endpoint
                    response = await page.goto(api_url, wait_until="domcontentloaded", timeout=20000)
                    status = response.status if response else 0
                    
                    if status == 404:
                        # Direct 404 is fast, move to next campus/year
                        await context.close()
                        continue
                        
                    if status == 403:
                        # Cloudflare Turnstile block - wait 10 seconds for Playwright to solve
                        await page.wait_for_timeout(10000)
                        
                    text = await page.evaluate("() => document.body.innerText")
                    if "{" in text and "availability" in text:
                        data = json.loads(text)
                        if data.get("availability") is True:
                            await context.close()
                            return data, campus, year, s_type
                except Exception:
                    pass
                finally:
                    await context.close()
                    
    return None, None, None, None

async def scrape_course(browser, url):
    url = url.strip()
    d = {"cricos": "", "title": "", "url": url, "course_description": "",
         "course_duration_per_week": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": [], "source": "page", "note": ""}
         
    try:
        data, campus, year, s_type = await fetch_course_json_with_fresh_context(browser, url)
        if data:
            c_data = data.get("data") or {}
            
            # Title
            d["title"] = c_data.get("awardTitle") or "Unknown Course"
            
            # CRICOS
            d["cricos"] = c_data.get("cricosCourseCode") or ""
            
            # Description
            d["course_description"] = clean_html(extract_course_description(c_data))
            
            # Duration
            dur_str = c_data.get("duration") or ""
            d["course_duration_per_week"] = extract_duration_weeks(dur_str)
            
            # Fees
            fee = extract_fees(c_data)
            d["onshore_tuition_fee"] = clean_numeric_fee(fee)
            d["offshore_tuition_fee"] = clean_numeric_fee(fee)
            
            # Entry Requirements
            d["entry_requirements"] = clean_html(extract_entry_requirements(c_data))
            
            # Intake Months
            d["intake_months"] = extract_intake_months(c_data)
            
            # Application Link
            soft_content = data.get("softContent") or {}
            contact_cta = soft_content.get("contactCta") or {}
            primary_cta = contact_cta.get("primaryCta") or {}
            cta_link = primary_cta.get("link")
            if cta_link:
                d["apply_form"] = cta_link
                
            d["note"] = f"Scraped from data API ({campus}/{year}/{s_type})"
            print(f"✅ {d['cricos'] or '—'} | {d['title']} | {campus}/{year} | {url}")
        else:
            d["note"] = "API returned no data or 404 for all campuses"
            print(f"❌ Failed: No data found for {url}")
            
    except Exception as e:
        d["note"] = f"Error: {e}"
        print(f"❌ Error scraping {url}: {e}")
        
    return d

async def run_scraper():
    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Excel not found: {EXCEL_PATH}")
        return
        
    df = pd.read_excel(EXCEL_PATH)
    print(f"Discovered {len(df)} course URLs in {EXCEL_PATH}")
    
    print("Launching Playwright...")
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        for idx, row in enumerate(df.itertuples(), start=1):
            url = getattr(row, "url", "")
            title = getattr(row, "title", "")
            if not url:
                continue
            print(f"[{idx}/{len(df)}] ", end="")
            res = await scrape_course(browser, url)
            if not res["title"] or res["title"] == "Unknown Course":
                res["title"] = title
            results.append(res)
            
            # Cooperative delay between course scrapings
            await asyncio.sleep(0.5)
            
        await browser.close()
        
    # Backfill from register
    backfilled = backfill_from_register(results)
    
    # Compile intake dates union
    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)
    if not intake_date:
        intake_date = "March, July, November"
        
    # Write SQL updates
    print(f"Writing SQL queries to {SQL_PATH}...")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        emitted = set()
        for d in results:
            if not d["cricos"]:
                reason = (d["note"] or "no CRICOS course code found").replace("\n", " ").replace("\r", "")
                f.write(f"-- ⚠️ Skipped ({reason}): {d['title']} | {d['url']}\n\n")
                continue
            
            # Find all valid CRICOS codes in the string (e.g. "Low cost: 0100699; High cost: 0100698" -> ["0100699", "0100698"])
            codes = re.findall(r"\b\d{5,7}[A-Za-z]?\b", d["cricos"])
            if not codes:
                codes = [d["cricos"]]
                
            for code in codes:
                code_upper = code.upper().strip()
                if code_upper in emitted:
                    f.write(f"-- ⚠️ Skipped (CRICOS {code_upper} already emitted — duplicate code): {d['title']} | {d['url']}\n\n")
                    continue
                emitted.add(code_upper)
                
                if d["source"] == "register":
                    f.write(f"""-- From CRICOS register fallback: {d['title']}
UPDATE courses SET
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {clean_numeric_fee(d["offshore_tuition_fee"])},
    enrolment_fee = {clean_numeric_fee(d["enrolment_fee"])},
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{code_upper}';\n\n""")
                    continue
                    
                f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {clean_numeric_fee(d["offshore_tuition_fee"])},
    onshore_tuition_fee = {clean_numeric_fee(d["onshore_tuition_fee"])},
    enrolment_fee = {clean_numeric_fee(d["enrolment_fee"])},
    materials_fee = {clean_numeric_fee(d["materials_fee"])},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{code_upper}';\n\n""")
                
    # Update Excel
    print(f"Writing Excel sheet to {EXCEL_PATH}...")
    def cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]
        
    output_rows = []
    for d in results:
        output_rows.append({
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
            "source": d["source"],
            "note": d["note"],
        })
    df_out = pd.DataFrame(output_rows)
    df_out.to_excel(EXCEL_PATH, index=False)
    
    ok = sum(1 for d in results if d["cricos"])
    print(f"\n✅ {ok}/{len(results)} courses with CRICOS "
          f"({ok - backfilled} from page, {backfilled} from register).")
    print(f"SQL update written to: {SQL_PATH}")
    print(f"Excel driver written to: {EXCEL_PATH}")

def main():
    asyncio.run(run_scraper())

if __name__ == "__main__":
    main()
