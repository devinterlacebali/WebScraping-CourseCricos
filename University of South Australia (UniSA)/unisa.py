import os
import re
import sys
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Ensure correct terminal output encoding for Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- Paths & Constants ---
_ROOT = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(_ROOT, "unisa.xlsx")
OUTPUT_SQL = os.path.join(_ROOT, "unisa_courses_update.sql")
OUTPUT_EXCEL = os.path.join(_ROOT, "unisa_scraped_all.xlsx")

# Import ai_formatter if available
sys.path.append(os.path.dirname(_ROOT))
try:
    from ai_formatter import format_requirements
except ImportError:
    def format_requirements(text):
        return ""

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- Helper Functions ---
def clean_html(html: str) -> str:
    if not html:
        return ""
    # Replaces single quotes with double single quotes for SQL insertion
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

def num_fee(val):
    if not val:
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v:
        return "NULL"
    try:
        n = float(v)
        return str(int(n)) if n > 0 else "NULL"
    except ValueError:
        return "NULL"

def parse_weeks_from_duration(duration_text):
    if not duration_text:
        return "NULL"
    # Search for years (e.g. 3 years, 3 year(s), 1.5 years)
    m = re.search(r"([\d.]+)\s*year", duration_text, re.I)
    if m:
        try:
            years = float(m.group(1))
            return str(int(round(years * 52)))
        except ValueError:
            pass
    # Search for months (e.g. 18 months, 6 month)
    m = re.search(r"([\d.]+)\s*month", duration_text, re.I)
    if m:
        try:
            months = float(m.group(1))
            return str(int(round((months / 12) * 52)))
        except ValueError:
            pass
    return "NULL"

def scrape_course_page(url):
    """Scrape course details from the given URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # Try international page first
    int_url = url.rstrip("/") + "/int/"
    html = ""
    target_url = int_url
    
    try:
        r = requests.get(int_url, headers=headers, timeout=20)
        if r.status_code == 200:
            html = r.text
        else:
            # Fallback to domestic
            dom_url = url.rstrip("/") + "/dom/"
            target_url = dom_url
            r = requests.get(dom_url, headers=headers, timeout=20)
            if r.status_code == 200:
                html = r.text
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None

    if not html:
        print(f"  Empty response for {url}")
        return None

    soup = BeautifulSoup(html, "html.parser")
    
    # --- 1. CRICOS Code ---
    cricos = ""
    # A. Meta Tags
    m = re.search(r'<meta[^>]*property="cricosCode"[^>]*content="([^"]+)"', html)
    if m:
        cricos = m.group(1).strip()
    if not cricos:
        m = re.search(r'<meta[^>]*name="cricosCode"[^>]*content="([^"]+)"', html)
        if m:
            cricos = m.group(1).strip()
            
    # B. Label search
    if not cricos:
        label = soup.find("span", string=re.compile(r"^\s*CRICOS code\s*$", re.I))
        if label:
            container = label.find_parent(class_=re.compile(r"degree-details-content-section-icon-list-top"))
            if container:
                val = container.select_one(".degree-details-content-section-subtitle span")
                if val:
                    cricos = val.get_text(strip=True)
                    
    # C. Generic Pattern Fallback (ignore provider numbers)
    if not cricos:
        matches = re.findall(r"\b(\d{5,6}[A-Za-z]|\d{7})\b", html)
        if matches:
            valid_codes = [c for c in matches if c not in ("04249J", "00121B", "00123M")]
            if valid_codes:
                cricos = valid_codes[0]

    # --- 2. Overview / Description ---
    course_description = ""
    overview = soup.find("h3", string=re.compile(r"^\s*Overview\s*$", re.I))
    if overview:
        paragraphs = []
        for tag in overview.find_all_next():
            if tag.name == "h3" and tag.get_text(strip=True).lower() != "overview":
                break
            if tag.name == "p":
                paragraphs.append(str(tag))
        course_description = clean_html("".join(paragraphs))

    # --- 3. Entry Requirements ---
    entry_requirements = ""
    block = soup.select_one("div.block-content-wrapper")
    if not block:
        block = soup.select_one("div.entryrequirements")
    
    if block:
        raw_reqs = str(block)
        # Try AI reformatting if enabled
        plain_text = block.get_text("\n").strip()
        ai_table = format_requirements(plain_text)
        entry_requirements = clean_html(ai_table if ai_table else raw_reqs)

    # --- 4. Duration ---
    total_course_duration = ""
    dur_span = soup.find("span", string=re.compile("year", re.I))
    if dur_span:
        total_course_duration = dur_span.get_text(strip=True)
    weeks = parse_weeks_from_duration(total_course_duration)

    # --- 5. Offshore Tuition Fee ---
    offshore_fee_str = ""
    fee_span = soup.select_one("div.degree-details-content-section-subtitle span")
    if fee_span and "$" in fee_span.get_text():
        offshore_fee_str = fee_span.get_text(strip=True)
    else:
        text_with_dollar = soup.find(string=re.compile(r"\$[0-9,]+"))
        if text_with_dollar:
            offshore_fee_str = text_with_dollar.strip()
    
    offshore_tuition_fee = num_fee(offshore_fee_str)

    # --- 6. Intake Months ---
    intake_months = []
    text_content = soup.get_text()
    for month in MONTH_ORDER:
        if re.search(rf"\b{month}\b", text_content, re.I):
            intake_months.append(month)

    return {
        "cricos": cricos,
        "course_description": course_description,
        "entry_requirements": entry_requirements,
        "total_course_duration": total_course_duration,
        "course_duration_per_week": weeks,
        "offshore_tuition_fee": offshore_tuition_fee,
        "apply_form": url,
        "intake_months": intake_months
    }

def main():
    print(f"📖 Reading driver file: {INPUT_FILE}")
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: driver spreadsheet {INPUT_FILE} not found!")
        sys.exit(1)
        
    df = pd.read_excel(INPUT_FILE)
    if "url" not in df.columns:
        print("❌ Error: 'url' column not found in spreadsheet!")
        sys.exit(1)

    urls = df["url"].dropna().unique().tolist()
    print(f"Loaded {len(urls)} URLs to scrape.")

    results = []
    emitted = set()

    for idx, url in enumerate(urls, 1):
        print(f"[{idx}/{len(urls)}] Scraping: {url}")
        res = scrape_course_page(url)
        if not res:
            print("  ⚠️ Scrape failed")
            continue

        cricos = res["cricos"]
        if not cricos:
            # Fallback to driver's cricos code if page doesn't explicitly display it
            driver_row = df[df["url"] == url]
            if not driver_row.empty and "cricos_course_code" in df.columns:
                cricos = str(driver_row.iloc[0]["cricos_course_code"]).strip()
                res["cricos"] = cricos

        if not cricos or cricos == "nan":
            print("  ⚠️ CRICOS code not found, skipped.")
            continue

        # Get course title from spreadsheet to output in Excel
        driver_row = df[df["url"] == url]
        title = driver_row.iloc[0]["course_name"] if not driver_row.empty and "course_name" in df.columns else ""
        res["title"] = title

        results.append(res)
        print(f"  ✅ CRICOS: {cricos} | Fee: {res['offshore_tuition_fee']} | Duration: {res['total_course_duration']}")
        
        # Polite delay to not overload server
        time.sleep(0.5)

    if not results:
        print("❌ No course data could be parsed!")
        sys.exit(1)

    # --- Write SQL Updates ---
    print(f"💾 Writing SQL update queries: {OUTPUT_SQL}")
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write("-- University of South Australia (UniSA) course updates\n\n")
        for r in results:
            cricos = r["cricos"]
            if cricos in emitted:
                continue
            emitted.add(cricos)
            
            f.write(f"-- Course: {r.get('title', 'Unknown')} ({cricos})\n")
            f.write("UPDATE courses SET\n")
            f.write(f"    course_description = '{r['course_description']}',\n")
            
            weeks_val = r['course_duration_per_week']
            f.write(f"    course_duration_per_week = {weeks_val},\n")
            f.write(f"    total_course_duration = '{r['total_course_duration']}',\n")
            
            fee_val = r['offshore_tuition_fee']
            f.write(f"    offshore_tuition_fee = {fee_val},\n")
            f.write("    onshore_tuition_fee = NULL,\n")
            f.write(f"    entry_requirements = '{r['entry_requirements']}',\n")
            f.write(f"    apply_form = '{r['apply_form']}',\n")
            f.write("    updated_at = NOW()\n")
            f.write(f"WHERE cricos_course_code = '{cricos}';\n\n")

    # --- Write Excel Output ---
    print(f"💾 Saving enriched results: {OUTPUT_EXCEL}")
    excel_rows = []
    for r in results:
        excel_rows.append({
            "cricos": r["cricos"],
            "title": r.get("title", ""),
            "url": r["apply_form"],
            "course_duration_per_week": r["course_duration_per_week"] if r["course_duration_per_week"] != "NULL" else "",
            "offshore_tuition_fee": r["offshore_tuition_fee"] if r["offshore_tuition_fee"] != "NULL" else "",
            "intake": ", ".join(r["intake_months"]),
            "course_description": r["course_description"].replace("''", "'"),
            "entry_requirements": r["entry_requirements"].replace("''", "'"),
            "note": "Scraped from Adelaide Uni merged portal"
        })
    df_out = pd.DataFrame(excel_rows)
    df_out.to_excel(OUTPUT_EXCEL, index=False)

    print(f"\n🎉 Scrape finished successfully!")
    print(f"   - Total courses processed: {len(emitted)}")
    print(f"   - SQL Update Script: {OUTPUT_SQL}")
    print(f"   - Excel Spreadsheet: {OUTPUT_EXCEL}")

if __name__ == "__main__":
    main()
