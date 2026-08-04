import pandas as pd
import re
import os

PROVIDER_CODE = "00115M"
SLUG = "latrobe"
DIR = "La Trobe University (La Trobe)"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

def clean_html(html_str: str) -> str:
    if not html_str or pd.isna(html_str):
        return ""
    html_str = re.sub(r"\s+", " ", str(html_str))
    return html_str.replace("'", "''").strip()

def clean_numeric_fee(val) -> str:
    if val is None or pd.isna(val) or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def main():
    if not os.path.exists(EXCEL_PATH):
        print(f"Excel not found: {EXCEL_PATH}")
        return
        
    df = pd.read_excel(EXCEL_PATH)
    print(f"Loaded {len(df)} rows from {EXCEL_PATH}")
    
    # Union all intakes
    intake_months = set()
    for row in df.itertuples():
        intake_str = getattr(row, "intake", "")
        if pd.notna(intake_str) and str(intake_str).strip():
            months = [m.strip() for m in str(intake_str).split(",") if m.strip()]
            intake_months.update(months)
            
    intake_date = ", ".join(m for m in MONTH_ORDER if m in intake_months)
    if not intake_date:
        intake_date = "March, July, November"
        
    print(f"Writing SQL queries to {SQL_PATH}...")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        emitted = set()
        for row in df.itertuples():
            cricos_val = getattr(row, "cricos", "")
            title = getattr(row, "title", "")
            url = getattr(row, "url", "")
            source = getattr(row, "source", "")
            note = getattr(row, "note", "")
            
            course_duration_per_week = getattr(row, "course_duration_per_week", "")
            offshore_tuition_fee = getattr(row, "offshore_tuition_fee", "")
            onshore_tuition_fee = getattr(row, "onshore_tuition_fee", "")
            enrolment_fee = getattr(row, "enrolment_fee", "")
            materials_fee = getattr(row, "materials_fee", "")
            course_description = getattr(row, "course_description", "")
            entry_requirements = getattr(row, "entry_requirements", "")
            
            if pd.isna(cricos_val) or not str(cricos_val).strip():
                reason = str(note).replace("\n", " ").replace("\r", "") if pd.notna(note) else "no CRICOS course code found"
                f.write(f"-- ⚠️ Skipped ({reason}): {title} | {url}\n\n")
                continue
                
            # Extract all valid CRICOS codes from string (can be 5 to 7 digits followed by optional letter)
            codes = re.findall(r"\b\d{5,7}[A-Za-z]?\b", str(cricos_val))
            if not codes:
                codes = [str(cricos_val).strip()]
                
            for code in codes:
                code_upper = code.upper().strip()
                if code_upper in emitted:
                    f.write(f"-- ⚠️ Skipped (CRICOS {code_upper} already emitted — duplicate code): {title} | {url}\n\n")
                    continue
                    emitted.add(code_upper)
                emitted.add(code_upper)
                
                duration_val = "NULL"
                if pd.notna(course_duration_per_week) and str(course_duration_per_week).strip():
                    dur = re.sub(r"[^\d]", "", str(course_duration_per_week))
                    if dur:
                        duration_val = dur
                        
                apply_form = url # Default apply form
                
                # Check for apply form link in note or fallback
                # Since the original scraper wrote apply_form to the SQL file directly, 
                # let's write the course URL, or if it is a register fallback, use standard application link.
                if source == "register":
                    f.write(f"""-- From CRICOS register fallback: {title}
UPDATE courses SET
    course_duration_per_week = {duration_val},
    offshore_tuition_fee = {clean_numeric_fee(offshore_tuition_fee)},
    enrolment_fee = {clean_numeric_fee(enrolment_fee)},
    apply_form = '{apply_form}',
    updated_at = NOW()
WHERE cricos_course_code = '{code_upper}';\n\n""")
                    continue
                    
                # Standard web scraped update
                f.write(f"""UPDATE courses SET
    course_description = '{clean_html(course_description)}',
    course_duration_per_week = {duration_val},
    offshore_tuition_fee = {clean_numeric_fee(offshore_tuition_fee)},
    onshore_tuition_fee = {clean_numeric_fee(onshore_tuition_fee)},
    enrolment_fee = {clean_numeric_fee(enrolment_fee)},
    materials_fee = {clean_numeric_fee(materials_fee)},
    entry_requirements = '{clean_html(entry_requirements)}',
    apply_form = '{apply_form}',
    updated_at = NOW()
WHERE cricos_course_code = '{code_upper}';\n\n""")
                
    print(f"SQL update successfully regenerated: {SQL_PATH}")

if __name__ == "__main__":
    main()
