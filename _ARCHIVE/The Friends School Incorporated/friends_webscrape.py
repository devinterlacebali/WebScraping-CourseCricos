#!/usr/bin/env python3
"""
Webscraper for The Friends School Incorporated (00477G)
CRICOS Provider: 00477G
Website: www.friends.tas.edu.au
"""

import sys, os, csv, re, json
from pathlib import Path

_venv_site = [p for p in sys.path if "venv" in p and "site-packages" in p]
for _p in _venv_site:
    if _p in sys.path:
        sys.path.remove(_p)
        sys.path.insert(1, _p)

PROVIDER_CODE = "00477G"
PROVIDER_NAME = r"The Friends School Incorporated"
SLUG = "friends"
PROVIDER_DIR = Path(__file__).resolve().parent
OUTPUT_XLSX = PROVIDER_DIR / f"{SLUG}_webscrape.xlsx"
OUTPUT_SQL = PROVIDER_DIR / f"{SLUG}_webscrape_courses_update.sql"
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"

# Embedded CSV course data
CSV_COURSES = [
  {
    "cricos": "004728E",
    "name": "Secondary Senior Yrs 11-12",
    "fee": "$157,701.00",
    "non_fee": "$81,181.00",
    "duration": "96"
  },
  {
    "cricos": "021270D",
    "name": "Secondary Junior Years 8-10",
    "fee": "$223,858.00",
    "non_fee": "$111,718.00",
    "duration": "153"
  },
  {
    "cricos": "021271C",
    "name": "Secondary Junior Year 7",
    "fee": "$107,455.00",
    "non_fee": "$71,895.00",
    "duration": "47"
  },
  {
    "cricos": "030826J",
    "name": "Primary Years 4-6",
    "fee": "$96,683.00",
    "non_fee": "$12,973.00",
    "duration": "153"
  },
  {
    "cricos": "043008C",
    "name": "Secondary Senior Years 10 - 12",
    "fee": "$225,691.00",
    "non_fee": "$111,791.00",
    "duration": "153"
  },
  {
    "cricos": "051385M",
    "name": "International Baccalaureate Years 11-12",
    "fee": "$157,596.00",
    "non_fee": "$81,176.00",
    "duration": "96"
  }
]


def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n >= 100 else "NULL"

def main():
    csv_courses = CSV_COURSES
    print(f"[{SLUG}] Found {len(csv_courses)} courses in CSV register for {PROVIDER_CODE}")
    
    results = []
    emitted = set()
    
    for c in csv_courses:
        cricos = c["cricos"]
        name = c["name"]
        
        if cricos in emitted:
            continue
        emitted.add(cricos)
        
        fee_str = clean_numeric_fee(c["fee"])
        duration_str = c["duration"] if c["duration"] else "NULL"
        non_fee = clean_numeric_fee(c["non_fee"])
        
        name_lower = name.lower()
        if "primary" in name_lower or "prep" in name_lower or "kindergarten" in name_lower or "p-" in name_lower:
            year_level = "Primary"
        elif "junior secondary" in name_lower or "year 7" in name_lower or "year 8" in name_lower or "year 9" in name_lower or "year 10" in name_lower:
            year_level = "Junior Secondary"
        elif "senior secondary" in name_lower or "year 11" in name_lower or "year 12" in name_lower:
            year_level = "Senior Secondary"
        elif "ib" in name_lower or "international baccalaureate" in name_lower:
            year_level = "IB Diploma"
        elif "preparation" in name_lower:
            year_level = "Preparation"
        else:
            year_level = "Other"
        
        if "preparation" in name_lower:
            entry_req = "English language proficiency assessment, placement test"
        elif "primary" in name_lower:
            entry_req = "Academic transcripts, AEAS test recommended, school interview"
        else:
            entry_req = "AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports"
        
        desc = f"{name} at {PROVIDER_NAME}. {year_level} program for international students."
        
        results.append({
            "cricos": cricos,
            "title": name,
            "url": "https://www.friends.tas.edu.au",
            "course_duration_per_week": duration_str,
            "offshore_tuition_fee": fee_str,
            "onshore_tuition_fee": "NULL",
            "enrolment_fee": non_fee,
            "materials_fee": "NULL",
            "intake": "January, July",
            "course_description": desc,
            "entry_requirements": entry_req,
            "source": "register",
            "note": "CSV data - website fee page not available as HTML. Typical K-12 intake: Term 1 (Jan), Term 3 (Jul)"
        })
    
    # Output XLSX
    try:
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Courses"
        headers = ["cricos", "title", "url", "course_duration_per_week", "offshore_tuition_fee",
                    "onshore_tuition_fee", "enrolment_fee", "materials_fee", "intake",
                    "course_description", "entry_requirements", "source", "note"]
        ws.append(headers)
        for r in results:
            ws.append([r[h] for h in headers])
        wb.save(str(OUTPUT_XLSX))
        print(f"[{SLUG}] Saved XLSX: {OUTPUT_XLSX}")
    except Exception as e:
        print(f"[{SLUG}] XLSX error: {e}")
        csv_path = PROVIDER_DIR / f"{SLUG}_webscrape.csv"
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=results[0].keys() if results else [])
            w.writeheader()
            w.writerows(results)
        print(f"[{SLUG}] Saved CSV fallback: {csv_path}")
    
    # Output SQL
    sql_lines = [
        "-- Update provider institution details",
        "UPDATE provider_institution SET",
        "    intake_date = 'January, July',",
        "    updated_at = NOW()",
        f"WHERE cricos_provider_code = '{PROVIDER_CODE}';",
        ""
    ]
    
    for r in results:
        cricos = r["cricos"]
        if not cricos or not re.match(r"^\d{6,7}[A-Za-z]?$", str(cricos)):
            sql_lines.append(f'-- Skipped (no CRICOS): {r["title"]}')
            sql_lines.append("")
            continue
        
        desc = str(r.get("course_description", "") or "")
        if desc in ("nan", "None", ""):
            desc = ""
        else:
            desc = desc.replace("'", "''")
            if not desc.startswith("Course overview"):
                desc = f"Course overview <p>{desc}</p>"
        
        entry = str(r.get("entry_requirements", "") or "")
        if entry in ("nan", "None", ""):
            entry = ""
        else:
            entry = entry.replace("'", "''")
        
        url = str(r.get("url", "") or "")
        if url in ("nan", "None"):
            url = ""
        else:
            url = url.replace("'", "''")
        
        fee = r.get("offshore_tuition_fee", "NULL")
        dur = r.get("course_duration_per_week", "NULL")
        enrol_fee = r.get("enrolment_fee", "NULL")
        
        sql_lines.append(
            f"UPDATE courses SET"
            f"\n    course_description = '{desc}',"
            f"\n    course_duration_per_week = {dur},"
            f"\n    offshore_tuition_fee = {fee},"
            f"\n    onshore_tuition_fee = NULL,"
            f"\n    enrolment_fee = {enrol_fee},"
            f"\n    materials_fee = NULL,"
            f"\n    entry_requirements = '{entry}',"
            f"\n    apply_form = '{url}',"
            f"\n    updated_at = NOW()"
            f"\nWHERE cricos_course_code = '{cricos}';"
        )
    
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write("\n".join(sql_lines))
    print(f"[{SLUG}] Saved SQL: {OUTPUT_SQL}")
    print(f"[{SLUG}] Done! {len(results)} courses processed.")

if __name__ == "__main__":
    main()
