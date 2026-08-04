import csv
import re
import os

PROVIDER_CODE = "00114A"
REGISTER_CSV = "cricos-courses.csv"
SQL_PATH = "Flinders University/flinders_courses_update.sql"

def load_register():
    if not os.path.exists(REGISTER_CSV):
        print(f"Error: {REGISTER_CSV} not found")
        return []
        
    active_courses = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r["CRICOS Provider Code"].strip() == PROVIDER_CODE:
                if r["Expired"].strip().lower() != "yes":
                    active_courses.append({
                        "code": r["CRICOS Course Code"].strip(),
                        "name": r["Course Name"].strip(),
                        "duration": r.get("Duration (Weeks)", "").strip(),
                        "fee": r.get("Tuition Fee", "").strip(),
                    })
    return active_courses

def load_sql_updated():
    if not os.path.exists(SQL_PATH):
        print(f"Error: {SQL_PATH} not found")
        return set()
        
    updated_codes = set()
    with open(SQL_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all WHERE cricos_course_code = '...';
    matches = re.findall(r"WHERE cricos_course_code\s*=\s*'([0-9]{5,7}[A-Za-z]?)'", content)
    for m in matches:
        updated_codes.add(m.strip())
    return updated_codes

def load_sql_skipped():
    if not os.path.exists(SQL_PATH):
        return set(), {}
        
    skipped_codes = set()
    skipped_details = {}
    with open(SQL_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("--") and "Skipped" in line:
                # E.g. -- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Spanish | https://www.flinders.edu.au/study/courses/major-spanish
                # Or -- ⚠️ Skipped (no CRICOS on page): ...
                # Let's extract any CRICOS codes mentioned in the skip comment
                m = re.search(r"CRICOS\s+([0-9]{5,7}[A-Za-z]?)", line)
                if m:
                    code = m.group(1).strip()
                    skipped_codes.add(code)
                    skipped_details[code] = line.strip()
    return skipped_codes, skipped_details

def main():
    register_courses = load_register()
    updated_codes = load_sql_updated()
    skipped_codes, skipped_details = load_sql_skipped()
    
    print(f"--- FLINDERS UNIVERSITY COVERAGE REPORT ---")
    print(f"Total active CRICOS courses in register for Flinders (00114A): {len(register_courses)}")
    print(f"Total courses UPDATED in SQL: {len(updated_codes)}")
    
    # Check register courses that are updated
    updated_register = []
    missing_register = []
    
    for rc in register_courses:
        if rc["code"] in updated_codes:
            updated_register.append(rc)
        else:
            missing_register.append(rc)
            
    print(f"Active register courses UPDATED in SQL: {len(updated_register)}")
    print(f"Active register courses MISSING from SQL: {len(missing_register)}")
    
    print("\nSample of missing courses from SQL:")
    for idx, mc in enumerate(missing_register[:15], 1):
        skipped_info = ""
        if mc["code"] in skipped_codes:
            skipped_info = f" (Commented as skipped: {skipped_details[mc['code']][:80]}...)"
        print(f"  {idx}. Code: {mc['code']} | {mc['name']}{skipped_info}")
        
    # Check if there are codes updated in SQL that are NOT in the active register
    reg_codes_set = {rc["code"] for rc in register_courses}
    extra_in_sql = [code for code in updated_codes if code not in reg_codes_set]
    print(f"\nCodes updated in SQL but NOT active in current register: {len(extra_in_sql)}")
    for esc in extra_in_sql[:10]:
        print(f"  - {esc}")

if __name__ == "__main__":
    main()
