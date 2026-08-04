"""
St Mary's Anglican Girls' School - Web Scraper (00454C).
Data sources: https://www.stmarys.wa.edu.au/enrol/international-students/
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00454C"
PROVIDER_NAME = "St Mary's Anglican Girls' School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "st-marys-wa"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
INTL_URL = "https://www.stmarys.wa.edu.au/enrol/international-students/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v: return "NULL"
    try:
        n = float(v)
        return str(int(n)) if n.is_integer() else str(round(n, 2))
    except:
        return "NULL"

def extract_fees_from_html(html):
    """Look for international fee amounts in HTML."""
    fees = {}
    # Find dollar amounts near year levels
    for yr in [f"Year {i}" for i in range(1,13)] + ["Prep", "Kindergarten", "Pre-Primary", "PP"]:
        pattern = re.escape(yr) + r".{0,300}?\$([\d,]+(?:\.\d{2})?)"
        for m in re.finditer(pattern, html, re.DOTALL):
            try:
                amt = float(m.group(1).replace(",", ""))
                if 1000 < amt < 200000:
                    fees[yr] = amt
            except:
                pass
    return fees if fees else None

def main():
    print(f"\n  === {PROVIDER_NAME} Web Scraper ===")
    print(f"  Provider: {PROVIDER_CODE}")
    print(f"  Website: {INTL_URL}\n")

    # Fetch the international page
    fees_data = None
    try:
        r = requests.get(INTL_URL, timeout=15, headers=HEADERS)
        print(f"  Intl page: {r.status_code} ({len(r.text)}b)")
        if r.status_code == 200:
            text = r.text
            if len(text) >= 500 and not re.search(r"(page not found|404|oops|sorry.*page)", text[:500], re.IGNORECASE):
                fees_data = extract_fees_from_html(text)
                if fees_data:
                    print(f"  Found fee data: {fees_data}")
                # Also extract amounts near "international" keyword
                idx = text.lower().find("international")
                if idx > 0:
                    chunk = text[idx:idx+2000]
                    amounts = re.findall(r"\$([\d,]+(?:\.\d{2})?)", chunk)
                    print(f"  Found {len(amounts)} fee amounts near international keyword")
    except Exception as e:
        print(f"  Fetch error: {e}")

    # Also try alternative paths for fees
    alt_urls = []
    if "/international" in INTL_URL:
        alt_urls.append(INTL_URL.replace("/international", "/fees"))
    alt_urls.append(INTL_URL.rstrip("/") + "/fees/")
    for au in alt_urls:
        if au == INTL_URL:
            continue
        try:
            r2 = requests.get(au, timeout=10, headers=HEADERS)
            if r2.status_code == 200 and len(r2.text) > 500:
                fees2 = extract_fees_from_html(r2.text)
                if fees2:
                    fees_data = fees2
                    print(f"  Found fee data from fees page: {fees2}")
        except:
            pass

    # Load CSV register
    rows = []
    with open(REGISTER_CSV, encoding='utf-8-sig') as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE:
                continue
            if rec["Expired"].strip().lower() == "yes":
                continue

            cricos = rec["CRICOS Course Code"].strip()
            course_name = rec["Course Name"].strip()
            dur_str = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            dur = int(dur_str) if dur_str.isdigit() else 0

            csv_fee = rec.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            total_csv = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")

            annual_fee = 0
            if csv_fee:
                try:
                    annual_fee = float(csv_fee)
                except:
                    pass

            # Determine entry requirements by course type
            if "ELICOS" in course_name or "English" in course_name or "ESL" in course_name:
                entry_req = 'English proficiency assessment required. IELTS 5.0+ or equivalent.'
            elif "Foundation" in course_name or "Bridging" in course_name:
                entry_req = 'AEAS test recommended. IELTS 5.5+. Academic transcripts.'
            elif "International Baccalaureate" in course_name:
                entry_req = 'AEAS test, English proficiency, academic transcripts. Interview may be required.'
            elif "Diploma" in course_name or "Certificate" in course_name:
                entry_req = 'Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.'
            else:
                entry_req = 'AEAS test and interview. Minimum English proficiency required. Academic transcripts.'

            intake = 'Term 1 (January), Term 3 (July)'

            # Determine year level
            yr_level = "All levels"
            if "Primary" in course_name or "Pre-Primary" in course_name or "Kindergarten" in course_name:
                yr_level = "PP-6"
            elif "Senior" in course_name or "Years 11" in course_name:
                yr_level = "11-12"
            elif "Secondary" in course_name or "Years 7" in course_name or "Junior" in course_name:
                yr_level = "7-10"
            elif "Foundation" in course_name or "Foundation Studies" in course_name:
                yr_level = "Foundation"
            elif "ELICOS" in course_name or "English" in course_name:
                yr_level = "ESL"
            elif "IB" in course_name or "International Baccalaureate" in course_name:
                yr_level = "IB"

            # Build course description
            desc = '<h4>%s - %s</h4>' % (PROVIDER_NAME, course_name)
            desc += '<p>%s offers %s for international students. ' % (PROVIDER_NAME, course_name.lower())
            desc += 'Located in Perth, Western Australia. CRICOS course code: %s.</p>' % cricos

            note_parts = []
            if fees_data:
                note_parts.append("Fee data found on website")
            else:
                note_parts.append("CSV fallback - fee data not on website (likely in PDF)")
            if total_csv:
                note_parts.append("CSV cost: $%s" % total_csv)

            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": INTL_URL,
                "course_description": desc,
                "course_duration_per_week": dur,
                "offshore_tuition_fee": int(annual_fee) if annual_fee else "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(int(float(nt))) if nt and float(nt) < 10000000 else "",
                "materials_fee": "",
                "intake": intake,
                "entry_requirements": entry_req,
                "apply_form": INTL_URL,
                "source": "webscrape",
                "note": " | ".join(note_parts),
            })

    print(f"  Courses found: {len(rows)}")
    if not rows:
        print(f"  !! No courses in CSV for provider {PROVIDER_CODE}")
        return

    # Write XLSX
    out = []
    for r in rows:
        out.append({
            "cricos": r["cricos"],
            "title": r["title"],
            "url": r["url"],
            "course_duration_per_week": r["course_duration_per_week"],
            "offshore_tuition_fee": r["offshore_tuition_fee"],
            "onshore_tuition_fee": r["onshore_tuition_fee"],
            "enrolment_fee": r["enrolment_fee"],
            "materials_fee": r["materials_fee"],
            "intake": r["intake"],
            "course_description": r["course_description"],
            "entry_requirements": r["entry_requirements"],
            "source": r["source"],
            "note": r["note"],
        })

    df = pd.DataFrame(out)
    df.to_excel(OUTPUT_XLSX, index=False)
    print(f"  -> {OUTPUT_XLSX.name}")

    # Write SQL
    emitted = set()
    with open(OUTPUT_SQL, 'w', encoding='utf-8') as f:
        f.write("-- %s (%s) - Course updates\n" % (PROVIDER_NAME, PROVIDER_CODE))
        f.write("-- Source: %s\n\n" % INTL_URL)
        f.write("UPDATE provider_institution SET\n")
        f.write("    intake_date = '%s',\n" % intake)
        f.write("    updated_at = NOW()\n")
        f.write("WHERE cricos_provider_code = '%s';\n\n" % PROVIDER_CODE)

        for r in rows:
            if r["cricos"] in emitted:
                continue
            emitted.add(r["cricos"])

            dur_val = str(r["course_duration_per_week"]) if r["course_duration_per_week"] else "NULL"
            fee_val = clean_numeric_fee(r["offshore_tuition_fee"])
            enr_val = clean_numeric_fee(r["enrolment_fee"])
            desc = r["course_description"].replace("\'", "\'\'")
            entry = r["entry_requirements"].replace("\'", "\'\'")

            f.write("UPDATE courses SET\n")
            f.write("    course_description = \'<h4>Course overview</h4><p>%s</p>\',\n" % desc)
            f.write("    course_duration_per_week = %s,\n" % dur_val)
            f.write("    offshore_tuition_fee = %s,\n" % fee_val)
            f.write("    onshore_tuition_fee = NULL,\n")
            f.write("    enrolment_fee = %s,\n" % enr_val)
            f.write("    materials_fee = NULL,\n")
            f.write("    entry_requirements = \'<h4>Entry Requirements</h4><p>%s</p>\',\n" % entry)
            f.write("    apply_form = \'%s\',\n" % r["apply_form"])
            f.write("    updated_at = NOW()\n")
            f.write("WHERE cricos_course_code = \'%s\';\n\n" % r["cricos"])

    print(f"  -> {OUTPUT_SQL.name}")
    print(f"  Done: {len(emitted)} courses.\n")

if __name__ == "__main__":
    main()
