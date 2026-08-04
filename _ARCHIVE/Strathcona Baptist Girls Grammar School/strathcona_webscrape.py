"""
Strathcona Baptist Girls Grammar School - Web Scraper (00577C).
Data sources: https://www.strathcona.vic.edu.au/enrolment/international
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

PROVIDER_CODE = "00577C"
PROVIDER_NAME = "Strathcona Baptist Girls Grammar School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "strathcona"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
INTL_URL = "https://www.strathcona.vic.edu.au/enrolment/international"
WEBSITE = "https://www.strathcona.vic.edu.au"


def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def load_register():
    reg = {}
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if r["Expired"].strip().lower() == "yes": continue
            reg[r["CRICOS Course Code"].strip()] = r
    return reg

def main():
    print("  " + PROVIDER_NAME + " Web Scraper (" + PROVIDER_CODE + ")")
    print("  " + "="*50)
    
    reg = load_register()
    print("  Courses in register: " + str(len(reg)))
    
    fees = {}
    entry_req = ""
    intake = ""
    
    try:
        urls_to_try = [INTL_URL, WEBSITE.rstrip("/") + "/fees", 
                       WEBSITE.rstrip("/") + "/enrolment/fees",
                       WEBSITE.rstrip("/") + "/admissions",
                       WEBSITE.rstrip("/") + "/international-students/fees",
                       WEBSITE.rstrip("/") + "/enrolment/international-students"]
        for url in urls_to_try:
            r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            if r.status_code == 200:
                text = r.text
                # Extract fee info
                fbodies = re.findall(r'(?:Year|Prep|Primary|Secondary|Junior|Senior).{0,30}?\$\s*[\d,]+', text, re.IGNORECASE)
                for fb in fbodies:
                    m = re.search(r'(Year\s*\d+[\s-]*\d*|Prep|Primary|Secondary|Junior|Senior).{0,30}?\$\s*([\d,]+)', fb, re.IGNORECASE)
                    if m:
                        yr = m.group(1).strip()
                        amt = int(m.group(2).replace(",",""))
                        fees[yr] = amt
                
                er_match = re.search(r'(?:entry requirement|IELTS|AEAS|English)[^.]{10,200}\.', text, re.IGNORECASE | re.DOTALL)
                if er_match:
                    entry_req = er_match.group(0).strip()[:300]
                
                int_match = re.search(r'(?:intake|start date|commence|term)[^.]{10,200}\.', text, re.IGNORECASE | re.DOTALL)
                if int_match:
                    intake = int_match.group(0).strip()[:200]
                    
                print("  " + url + ": " + str(r.status_code) + " (" + str(len(text)) + "b)")
                if fees:
                    break
    except Exception as e:
        print("  Fetch error: " + str(e))
    
    rows = []
    for cricos_code, reg_rec in reg.items():
        name_raw = reg_rec.get("Course Name", "").strip()
        duration_weeks = re.sub(r"[^\d]", "", reg_rec.get("Duration (Weeks)","") or "")
        csv_fee = reg_rec.get("Estimated Total Course Cost","") or ""
        csv_fee = clean_numeric_fee(csv_fee.replace("$","")) if csv_fee else "NULL"
        
        total_fee = "NULL"
        years = 0
        if duration_weeks and duration_weeks.isdigit():
            years = max(1, round(int(duration_weeks) / 52))
        if fees:
            annual_fees = list(fees.values())
            if annual_fees:
                avg_annual = max(annual_fees)
                if years:
                    total_fee = str(int(avg_annual) * years)
                else:
                    total_fee = str(int(avg_annual))
        else:
            total_fee = csv_fee
        
        enr_fee = clean_numeric_fee(reg_rec.get("Non Tuition Fee",""))
        
        rows.append({
            "cricos": cricos_code,
            "title": name_raw,
            "url": INTL_URL,
            "course_duration_per_week": duration_weeks if duration_weeks else "NULL",
            "offshore_tuition_fee": total_fee,
            "onshore_tuition_fee": "NULL",
            "enrolment_fee": enr_fee,
            "materials_fee": "NULL",
            "intake": intake,
            "course_description": "<h4>Course overview</h4><p>" + name_raw + "</p>" if name_raw else "",
            "entry_requirements": "<h4>Entry Requirements</h4><p>" + entry_req + "</p>" if entry_req else "",
            "source": "website" if fees else "register",
            "note": "Fees from website fee table" if fees else "CSV fallback - no fee table found"
        })
    
    # Write XLSX
    import openpyxl
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Courses"
    headers = ["cricos","title","url","course_duration_per_week","offshore_tuition_fee",
               "onshore_tuition_fee","enrolment_fee","materials_fee","intake",
               "course_description","entry_requirements","source","note"]
    ws.append(headers)
    for row in rows:
        ws.append([row[h] for h in headers])
    wb.save(str(OUTPUT_XLSX))
    print("  XLSX: " + str(len(rows)) + " rows -> " + str(OUTPUT_XLSX))
    
    # Write SQL
    sql_lines = []
    sql_lines.append("-- Update provider institution details")
    sql_lines.append("UPDATE provider_institution SET")
    sql_lines.append("    intake_date = '" + intake.replace("'", "''") + "',")
    sql_lines.append("    updated_at = NOW()")
    sql_lines.append("WHERE cricos_provider_code = '" + PROVIDER_CODE + "';")
    
    for row in rows:
        desc_esc = row["course_description"].replace("'", "''") if row["course_description"] else ""
        entry_esc = row["entry_requirements"].replace("'", "''") if row["entry_requirements"] else ""
        sql_lines.append("")
        sql_lines.append("-- " + row['title'])
        sql_lines.append("UPDATE courses SET")
        sql_lines.append("    course_description = '" + desc_esc + "',")
        
        dw = row["course_duration_per_week"]
        if dw != "NULL":
            sql_lines.append("    course_duration_per_week = " + dw + ",")
        else:
            sql_lines.append("    course_duration_per_week = NULL,")
        
        sql_lines.append("    offshore_tuition_fee = " + row['offshore_tuition_fee'] + ",")
        sql_lines.append("    onshore_tuition_fee = " + row['onshore_tuition_fee'] + ",")
        sql_lines.append("    enrolment_fee = " + row['enrolment_fee'] + ",")
        sql_lines.append("    materials_fee = " + row['materials_fee'] + ",")
        sql_lines.append("    entry_requirements = '" + entry_esc + "',")
        sql_lines.append("    updated_at = NOW()")
        sql_lines.append("WHERE cricos_course_code = '" + row['cricos'] + "';")
    
    sql_content = "\n".join(sql_lines)
    OUTPUT_SQL.write_text(sql_content, encoding="utf-8")
    print("  SQL: " + str(len(rows)) + " statements -> " + str(OUTPUT_SQL))
    print("  Done!")

if __name__ == "__main__":
    main()
