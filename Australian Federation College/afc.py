import re
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
from scrapling.fetchers import Fetcher

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROVIDER_CODE = "03854G"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

MONTH_MAP = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

# ===============================================================
# CLEANING HELPERS
# ===============================================================
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = html.replace("\n", " ").replace("\r", " ")
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")  # SQL safe
    return html.strip()

def clean_numeric_fee(val: str) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    val_clean = re.sub(r"[^\d\.]", "", str(val))
    if not val_clean:
        return "NULL"
    num = float(val_clean)
    return str(int(num)) if num.is_integer() else str(num)

def _sanitise(html: str) -> str:
    if not html:
        return ""
    frag = BeautifulSoup(html, "html.parser")
    for tag in frag.find_all(["style", "script", "noscript", "form", "iframe", "button", "img", "svg"]):
        tag.decompose()
    for tag in frag.find_all(True):
        for attr in list(tag.attrs):
            if attr != "href":
                del tag[attr]
    return str(frag)

# ===============================================================
# ACCORDION & EXTRACTION HELPERS
# ===============================================================
def get_accordion_by_title(page, title_pattern):
    pattern = re.compile(title_pattern, re.I)
    for item in page.css('.eael-accordion-list'):
        header = item.css('.eael-accordion-header')
        content = item.css('.eael-accordion-content')
        if header and content:
            header_text = header[0].get_all_text() or ""
            if pattern.search(header_text):
                return content[0]
    return None

def extract_overview(page):
    # Iterate text-editor widgets to find the first long overview block
    for w in page.css('.elementor-widget-text-editor'):
        text = w.get_all_text() or ""
        if len(text.strip()) > 100 and "ABN:" not in text and "Learnvault" not in text:
            return w.html_content
    return ""

def extract_course_description(page):
    overview_html = extract_overview(page)
    if overview_html:
        return clean_html(_sanitise(overview_html))
    return ""

def extract_duration(page):
    duration_panel = get_accordion_by_title(page, r"Duration")
    if duration_panel:
        text = duration_panel.get_all_text() or ""
        # e.g., "delivered over 78 weeks" or "10-70 weeks"
        m = re.search(r"\b(\d+(?:\-\d+)?)\s*weeks?\b", text, re.I)
        if m:
            return f"{m.group(1)} weeks"
        return clean_html(text)
    return ""

def extract_fees(page):
    fees_panel = get_accordion_by_title(page, r"Fees")
    tuition = "NULL"
    materials = "NULL"
    enrolment = "NULL"
    if fees_panel:
        text = fees_panel.get_all_text() or ""
        
        m_tuition = re.search(r"Tuition\s+Fees?:\s*(?:AUD\s*)?\$?\s*([\d,]+)", text, re.I)
        if m_tuition:
            tuition = clean_numeric_fee(m_tuition.group(1))
            
        m_mat = re.search(r"Material\s*fees?:\s*(?:AUD\s*)?\$?\s*([\d,]+)", text, re.I)
        if m_mat:
            materials = clean_numeric_fee(m_mat.group(1))
            
        m_enr = re.search(r"(?:Enrolment|Application)\s+fees?:\s*(?:\(Non-refundable\))?\s*(?:AUD\s*)?\$?\s*([\d,]+)", text, re.I)
        if m_enr:
            enrolment = clean_numeric_fee(m_enr.group(1))
            
    return tuition, materials, enrolment

def extract_entry_requirements(page):
    req_panel = get_accordion_by_title(page, r"Requirements")
    if req_panel:
        return clean_html(f"<h4>Entry Requirements</h4>{_sanitise(req_panel.html_content)}")
    return ""

def extract_cricos(page):
    text = page.get_all_text() or ""
    matches = re.findall(r"\b([0-9]{6,7}[A-Z])\b", text)
    matches = [m for m in matches if m != "03854G"]
    if matches:
        return matches[0]
    return "UNKNOWN"

def fetch_global_intakes():
    try:
        page = Fetcher.get("https://afcollege.edu.au/intake-dates/", stealthy_headers=True)
        text = page.get_all_text() or ""
        dates = re.findall(r"\b\d{2}/(\d{2})/\d{4}\b", text)
        months = set()
        for d in dates:
            if d in MONTH_MAP:
                months.add(MONTH_MAP[d])
        if months:
            return [m for m in MONTH_ORDER if m in months]
    except Exception as e:
        print(f"⚠️ Could not load intake dates page: {e}")
    # Fallback to default 8 months
    return ["January", "February", "April", "May", "July", "August", "September", "November"]

# ===============================================================
# CORE SCRAPER ACTION
# ===============================================================
def scrape_course(row, global_intakes):
    url = str(row["url"]).strip()
    title = str(row["title"]).strip()
    
    data = {
        "cricos": "UNKNOWN", "title": title, "url": url,
        "course_description": "", "total_course_duration": "",
        "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL", "materials_fee": "NULL",
        "entry_requirements": "", "apply_form": url, "intake_months": global_intakes
    }
    
    try:
        page = Fetcher.get(url, stealthy_headers=True)
        
        data["cricos"] = extract_cricos(page)
        data["course_description"] = extract_course_description(page)
        data["total_course_duration"] = extract_duration(page)
        
        tuition, materials, enrolment = extract_fees(page)
        data["offshore_tuition_fee"] = tuition
        data["onshore_tuition_fee"] = tuition
        data["materials_fee"] = materials
        data["enrolment_fee"] = enrolment
        
        data["entry_requirements"] = extract_entry_requirements(page)
        
        print(f"\n--- Scraped {url} ---")
        print(f"CRICOS: {data['cricos']}")
        print(f"Duration: {data['total_course_duration']}")
        print(f"Offshore Fee: {data['offshore_tuition_fee']}")
        print(f"Onshore Fee: {data['onshore_tuition_fee']}")
        print(f"Materials Fee: {data['materials_fee']}")
        print(f"Enrolment Fee: {data['enrolment_fee']}")
        print(f"Intake Months: {data['intake_months']}")
        sys.stdout.flush()
        
    except Exception as e:
        print(f"[ERROR] Scraping {url}: {e}")
        
    return data

# ===============================================================
# MAIN METHOD
# ===============================================================
def main():
    excel_path = "Australian Federation College/afc.xlsx"
    sql_path = "Australian Federation College/afc_courses_update.sql"
    
    if not os.path.exists(excel_path):
        excel_path = "afc.xlsx"
        sql_path = "afc_courses_update.sql"

    df = pd.read_excel(excel_path)
    
    print("Fetching global intake dates...")
    global_intakes = fetch_global_intakes()
    print(f"Global Intakes found: {global_intakes}")
    
    results = []
    for idx, row in df.iterrows():
        print(f"[{idx+1}/{len(df)}] Scraping: {row['url']}")
        results.append(scrape_course(row, global_intakes))
        
    intake_date_str = ", ".join(global_intakes)
    
    # Save SQL Script
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '{intake_date_str}',
    updated_at = NOW()
WHERE cricos_provider_code = '{PROVIDER_CODE}';

""")
        for d in results:
            if d["cricos"] == "UNKNOWN":
                f.write(f"-- ⚠️ Skipped (no/unreliable CRICOS course code): {d['title']} | {d['url']}\n\n")
                continue
            
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["total_course_duration"]}',
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    onshore_tuition_fee = {d["onshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    materials_fee = {d["materials_fee"]},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")
            
    # Save to Excel
    def _cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]

    enriched = [{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "total_course_duration": d["total_course_duration"],
        "offshore_tuition_fee": _cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": _cell(d["onshore_tuition_fee"]),
        "enrolment_fee": _cell(d["enrolment_fee"]),
        "materials_fee": _cell(d["materials_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": _cell(d["course_description"]),
        "entry_requirements": _cell(d["entry_requirements"]),
    } for d in results]
    
    pd.DataFrame(enriched).to_excel(excel_path, index=False)
    
    print(f"\n=== DONE! SQL saved to {sql_path} ===")
    print(f"=== Excel saved to {excel_path} ===")
    print(f"Global Intake Months: {intake_date_str}")

if __name__ == "__main__":
    main()
