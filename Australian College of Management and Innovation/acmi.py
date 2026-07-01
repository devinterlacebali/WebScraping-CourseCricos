import re
import pandas as pd
import sys
import os
from scrapling import StealthyFetcher

PROVIDER_CODE = "03800K"

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December", "january": "January",
    "february": "February", "march": "March", "april": "April", "june": "June",
    "july": "July", "august": "August", "september": "September",
    "october": "October", "november": "November", "december": "December",
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# ===============================================================
# CLEAN HTML AND STRING HELPERS
# ===============================================================
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = html.replace("\n", " ").replace("\r", " ")
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")  # SQL safe
    return html.strip()

def clean_numeric_fee(val: str) -> str:
    if not val or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    val_clean = re.sub(r"[^\d\.]", "", str(val))
    if not val_clean:
        return "NULL"
    return val_clean

# ===============================================================
# EXTRACTION HELPERS
# ===============================================================
def get_accordion_body_by_title(page, title_pattern):
    pattern = re.compile(title_pattern, re.I)
    
    # Iterate all elements with class accordion-button or accordion-header
    for btn in page.css('.accordion-button, .accordion-header'):
        btn_text = btn.get_all_text() or btn.text or ""
        if pattern.search(btn_text):
            target = btn.attrib.get('data-bs-target') or btn.attrib.get('href')
            if target:
                body = page.css(target)
                if body:
                    return body[0]
            
            # Fallback: search parent accordion-item
            parent = btn.parent
            depth = 0
            while parent and depth < 5:
                cls = parent.attrib.get('class') or ""
                if 'accordion-item' in cls:
                    body = parent.css('.accordion-collapse, .accordion-body')
                    if body:
                        return body[0]
                parent = parent.parent
                depth += 1
    return None

def extract_description(page):
    body = get_accordion_body_by_title(page, r"About|Description")
    if body:
        return clean_html(body.html_content)
    return ""

def extract_duration(page):
    body = get_accordion_body_by_title(page, r"Duration")
    if body:
        text = body.get_all_text() or body.text or ""
        m = re.search(r"\b(\d+)\s*weeks?\b", text, re.I)
        if m:
            return f"{m.group(1)} weeks"
        m_yr = re.search(r"\b(\d+|one|two|three)\s*years?\b", text, re.I)
        if m_yr:
            return f"{m_yr.group(1)} year"
        return clean_html(text)
    return ""

def extract_fees(page):
    body = get_accordion_body_by_title(page, r"Fees")
    tuition = "NULL"
    materials = "NULL"
    enrolment = "NULL"
    if body:
        text = body.get_all_text() or body.text or ""
        # Extract tuition fee
        m_tuition = re.search(r"Tuition Fees?\s*(?:AUD\s*)?\$?\s*([\d,]+)", text, re.I)
        if m_tuition:
            tuition = clean_numeric_fee(m_tuition.group(1))
        
        # Extract material fee
        m_mat = re.search(r"Material\s*Fees?\s*(?:AUD\s*)?\$?\s*([\d,]+)", text, re.I)
        if m_mat:
            materials = clean_numeric_fee(m_mat.group(1))
            
        # Extract application / enrolment fee
        m_enr = re.search(r"(?:Application|Enrolment)\s*Fees?\s*(?:\(Non-refundable\))?\s*(?:AUD\s*)?\$?\s*([\d,]+)", text, re.I)
        if m_enr:
            enrolment = clean_numeric_fee(m_enr.group(1))
            
    return tuition, materials, enrolment

def extract_requirements(page):
    body = get_accordion_body_by_title(page, r"Requirement")
    if body:
        return clean_html(body.html_content)
    return ""

def extract_cricos(page):
    text_content = page.get_all_text() or page.text or ""
    matches = re.findall(r"\b([0-9]{6,7}[A-Z])\b", text_content)
    # Exclude provider code 03800K
    matches = [m for m in matches if m != "03800K"]
    if matches:
        return matches[0]
    return "UNKNOWN"

def extract_intake_months(page):
    body = get_accordion_body_by_title(page, r"Intake")
    if not body:
        return []
    text = body.get_all_text() or body.text or ""
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", text):
        key = tok.lower()
        if key in MONTHS:
            val = MONTHS[key]
            if val not in found:
                found.append(val)
    return found

# ===============================================================
# SCRAPER CORE FUNCTION
# ===============================================================
def scrape_acmi(url, retry=3):
    for attempt in range(retry):
        try:
            # StealthyFetcher handles cookies, headers, and anti-bot automatically
            page = StealthyFetcher.fetch(url, headless=True)
            
            tuition, materials, enrolment = extract_fees(page)
            intake_months = extract_intake_months(page)
            
            data = {
                "url": url,
                "course_description": extract_description(page),
                "total_course_duration": extract_duration(page),
                "offshore_tuition_fee": tuition,
                "onshore_tuition_fee": tuition,
                "enrolment_fee": enrolment,
                "materials_fee": materials,
                "entry_requirements": extract_requirements(page),
                "cricos_course_code": extract_cricos(page),
                "apply_form": url,
                "intake_months": intake_months
            }

            print(f"\n--- Scraped {url} ---")
            print(f"CRICOS: {data['cricos_course_code']}")
            print(f"Duration: {data['total_course_duration']}")
            print(f"Offshore Fee: {data['offshore_tuition_fee']}")
            print(f"Onshore Fee: {data['onshore_tuition_fee']}")
            print(f"Materials Fee: {data['materials_fee']}")
            print(f"Enrolment Fee: {data['enrolment_fee']}")
            print(f"Intake Months: {data['intake_months']}")
            sys.stdout.flush()

            return data

        except Exception as e:
            print(f"[ERROR] {url} (Attempt {attempt+1}/{retry}): {e}")
            import time
            time.sleep(1)

    return None

# ===============================================================
# MAIN LOOP
# ===============================================================
def main():
    excel_path = "Australian College of Management and Innovation/acmi.xlsx"
    if not os.path.exists(excel_path):
        excel_path = "acmi.xlsx"

    df = pd.read_excel(excel_path)
    urls = df["url"].dropna().tolist()

    out_file = "Australian College of Management and Innovation/acmi_courses_update.sql"
    if not os.path.exists("Australian College of Management and Innovation"):
        out_file = "acmi_courses_update.sql"

    results = []

    for idx, row in df.iterrows():
        url = row["url"]
        title = row["title"]
        print(f"[{idx+1}/{len(df)}] Scraping: {url}")
        res = scrape_acmi(url)
        if res:
            res["title"] = title
            results.append(res)

    # Determine global unique intake months
    all_months = set()
    for d in results:
        all_months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)

    # Save to SQL script
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '{intake_date}',
    updated_at = NOW()
WHERE cricos_provider_code = '{PROVIDER_CODE}';

""")
        for d in results:
            if d["cricos_course_code"] == "UNKNOWN":
                f.write(f"-- ⚠️ Skipped (no/unreliable CRICOS course code): {d['url']}\n\n")
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
WHERE cricos_course_code = '{d["cricos_course_code"]}';
""")

    # Save to Excel spreadsheet (AIBI style columns)
    excel_records = []
    for d in results:
        excel_records.append({
            "cricos": d["cricos_course_code"],
            "title": d["title"],
            "url": d["url"],
            "total_course_duration": d["total_course_duration"],
            "offshore_tuition_fee": d["offshore_tuition_fee"],
            "onshore_tuition_fee": d["onshore_tuition_fee"],
            "enrolment_fee": d["enrolment_fee"],
            "materials_fee": d["materials_fee"],
            "intake": ", ".join(d["intake_months"]),
            "course_description": d["course_description"],
            "entry_requirements": d["entry_requirements"],
        })
    out_df = pd.DataFrame(excel_records)
    out_df.to_excel(excel_path, index=False)

    print(f"\n=== DONE! SQL saved to {out_file} ===")
    print(f"=== Excel saved to {excel_path} ===")
    print(f"Global Intake Months: {intake_date}")

if __name__ == "__main__":
    main()
