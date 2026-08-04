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

PROVIDER_CODE = "03882C"

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
def get_accordion_content_by_title(page, title_pattern):
    pattern = re.compile(title_pattern, re.I)
    holders = page.css('.mkdf-accordion-holder')
    if not holders:
        return None
    holder = holders[0]
    titles = holder.css('.mkdf-accordion-title')
    contents = holder.css('.mkdf-accordion-content')
    for idx, t in enumerate(titles):
        t_text = t.get_all_text().strip()
        if pattern.search(t_text) and idx < len(contents):
            return contents[idx]
    return None

def extract_course_description(page):
    # Overview is extracted from the 'Course Description' accordion content
    content_el = get_accordion_content_by_title(page, r"Course\s+Description")
    if content_el:
        return clean_html(_sanitise(content_el.html_content))
    return ""

def extract_duration(page):
    content_el = get_accordion_content_by_title(page, r"Duration")
    if content_el:
        text = content_el.get_all_text().strip()
        text_clean = re.sub(r'\s+', ' ', text)
        m = re.search(r"\b(\d+)\s*weeks\b", text_clean, re.I)
        if m:
            return clean_numeric_fee(m.group(1))
        m_num = re.search(r"\b(\d+)\b", text_clean)
        if m_num:
            return clean_numeric_fee(m_num.group(1))
    return "NULL"

def extract_fees(page, url):
    if "general-english" in url.lower():
        # General English has unique layout: Tuition=15000, Materials=600, Enrolment=250
        return "15000", "600", "250"
        
    content_el = get_accordion_content_by_title(page, r"Costs")
    tuition = "NULL"
    materials = "NULL"
    enrolment = "NULL"
    
    if content_el:
        text = content_el.get_all_text().strip()
        text_clean = re.sub(r'\s+', ' ', text)
        
        # Enrolment
        m_enr = re.search(r"Enrolment\s+fee:\s*\$?\s*([\d,]+)", text_clean, re.I)
        if m_enr:
            enrolment = clean_numeric_fee(m_enr.group(1))
            
        # Tuition
        m_tui = re.search(r"(?:Tuition|Course)\s+fees?:\s*\$?\s*([\d,]+)", text_clean, re.I)
        if m_tui:
            tuition = clean_numeric_fee(m_tui.group(1))
            
        # Materials
        m_mat_section = re.search(r"Materials\s+fees?[^:]*:\s*(.*?)(?:Total|Work|Uniform|Note|$)", text_clean, re.I)
        if m_mat_section:
            mat_text = m_mat_section.group(1).strip()
            m_total = re.search(r"\$?\s*([\d,]+)\s+for\s+\d+\s+terms", mat_text, re.I)
            if m_total:
                materials = clean_numeric_fee(m_total.group(1))
            else:
                nums = re.findall(r"\$?\s*([\d,]+)", mat_text)
                if nums:
                    materials = clean_numeric_fee(nums[-1])
            
    return tuition, materials, enrolment

def extract_entry_requirements(page):
    content_el = get_accordion_content_by_title(page, r"Entry\s+Requirements?")
    if content_el:
        return clean_html(f"<h4>Entry Requirements</h4>{_sanitise(content_el.html_content)}")
    return ""

def extract_cricos(page):
    text = page.get_all_text() or ""
    matches = re.findall(r"\b([0-9]{6,7}[A-Z])\b", text)
    matches = [m for m in matches if m != "03882C"]
    if matches:
        return matches[0]
    return "UNKNOWN"

def fetch_global_intakes():
    try:
        page = Fetcher.get("https://rockford.edu.au/intake-dates/", stealthy_headers=True)
        soup = BeautifulSoup(page.html_content, 'html.parser')
        months = set()
        for row in soup.find_all('tr'):
            tds = row.find_all('td')
            # Only Term start and Mid Term columns (excluding holiday rows)
            if len(tds) >= 4:
                for i in (1, 2):
                    found = re.findall(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', tds[i].get_text(), re.I)
                    for m in found:
                        months.add(m.title())
        if months:
            return [m for m in MONTH_ORDER if m in months]
    except Exception as e:
        print(f"⚠️ Could not load intake dates page: {e}")
    # Fallback to standard VET intake months
    return ["January", "February", "April", "May", "July", "August", "October", "November"]

# ===============================================================
# CORE SCRAPER ACTION
# ===============================================================
def scrape_course(row, global_intakes):
    url = str(row["url"]).strip()
    title = str(row["title"]).strip()
    
    data = {
        "cricos": "UNKNOWN", "title": title, "url": url,
        "course_description": "", "course_duration_per_week": "",
        "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL", "materials_fee": "NULL",
        "entry_requirements": "", "apply_form": url, "intake_months": global_intakes
    }
    
    try:
        page = Fetcher.get(url, stealthy_headers=True)
        
        data["cricos"] = extract_cricos(page)
        data["course_description"] = extract_course_description(page)
        data["course_duration_per_week"] = extract_duration(page)
        
        tuition, materials, enrolment = extract_fees(page, url)
        data["offshore_tuition_fee"] = tuition
        data["onshore_tuition_fee"] = tuition
        data["materials_fee"] = materials
        data["enrolment_fee"] = enrolment
        
        data["entry_requirements"] = extract_entry_requirements(page)
        
        print(f"\n--- Scraped {url} ---")
        print(f"CRICOS: {data['cricos']}")
        print(f"Duration: {data['course_duration_per_week']}")
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
    excel_path = "Rockford College/rockford.xlsx"
    sql_path = "Rockford College/rockford_courses_update.sql"
    
    if not os.path.exists(excel_path):
        excel_path = "rockford.xlsx"
        sql_path = "rockford_courses_update.sql"

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
    course_duration_per_week = {d["course_duration_per_week"]},
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
        "course_duration_per_week": d["course_duration_per_week"],
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
