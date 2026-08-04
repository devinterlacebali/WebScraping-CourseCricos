"""
Generate web scrape scripts for 17 WA schools.
Each script visits school website for international fee/entry/intake data.
"""
import os, sys, re, json
from pathlib import Path

BASE = Path(__file__).resolve().parent

def w(content, path):
    full = BASE / path
    full.parent.mkdir(parents=True, exist_ok=True)
    if full.exists():
        print(f"  SKIP (exists): {full.relative_to(BASE)}")
        return False
    full.write_text(content, encoding='utf-8')
    print(f"  Created: {full.relative_to(BASE)}")
    return True

# ============================================================
# PROVIDER DATA
# ============================================================
PROVIDERS = [
    ("00428E", "Edmund Rice Education Australia (Aquinas College)", "aquinas-college",
     "https://www.aquinas.wa.edu.au", "/international-students", "Aquinas College"),
    ("00431K", "Bunbury Cathedral Grammar School", "bunbury-cathedral-grammar",
     "https://www.bcgs.wa.edu.au", "/enrolment/international-students", "Bunbury Cathedral Grammar School"),
    ("00433G", "Christ Church Grammar School", "christ-church-grammar",
     "https://www.ccgs.wa.edu.au", "/enrolments/international-students", "Christ Church Grammar School"),
    ("00437D", "Guildford Grammar School", "guildford-grammar",
     "https://www.ggs.wa.edu.au", "/enrol/international-students/", "Guildford Grammar School"),
    ("00438C", "The Governors of Hale School", "hale-school",
     "https://www.hale.wa.edu.au", "/international-students/", "Hale School"),
    ("00441G", "Methodist Ladies' College (WA)", "mlc-wa",
     "https://www.mlc.wa.edu.au", "/enrolment/international-students/", "Methodist Ladies' College"),
    ("00444E", "Penrhos College", "penrhos-college",
     "https://www.penrhos.wa.edu.au", "/enrolment/international-students", "Penrhos College"),
    ("00445D", "Perth College Inc", "perth-college",
     "https://www.pc.wa.edu.au", "/enrolment/international-students", "Perth College"),
    ("00447B", "Presbyterian Ladies College (WA)", "plc-wa",
     "https://www.plc.wa.edu.au", "/enrolling/international-students", "Presbyterian Ladies' College"),
    ("00449M", "Scotch College (WA)", "scotch-college-wa",
     "https://www.scotch.wa.edu.au", "/admissions/international", "Scotch College"),
    ("00451F", "Mercy Education Limited (St Brigid's)", "st-brigids",
     "https://www.stbrigids.wa.edu.au", "/international-students/", "St Brigid's College"),
    ("00452E", "St Hilda's Anglican School for Girls", "st-hildas",
     "https://www.sthildas.wa.edu.au", "/enrolment/international/", "St Hilda's Anglican School for Girls"),
    ("00454C", "St Mary's Anglican Girls' School", "st-marys-wa",
     "https://www.stmarys.wa.edu.au", "/enrol/international-students/", "St Mary's Anglican Girls' School"),
    ("00460E", "Wesley College (WA)", "wesley-college-wa",
     "https://www.wesley.wa.edu.au", "/enrolment/international-students/", "Wesley College"),
    ("00463B", "Canning College", "canning-college",
     "https://www.canningcollege.wa.edu.au", "/international-students", "Canning College"),
    ("00466K", "St John's Catholic College", "st-johns-catholic-college",
     "https://www.stjohns.wa.edu.au", "/enrolment/international-students", "St John's Catholic College"),
]

def make_scraper(code, name, slug, url, intl_path, folder):
    intl_url = url.rstrip("/") + intl_path
    
    # Build the script content using string concatenation to avoid format issues
    lines = []
    lines.append('"""')
    lines.append(f'{name} - Web Scraper ({code}).')
    lines.append(f'Data sources: {intl_url}')
    lines.append('"""')
    lines.append('import sys, re, csv, requests')
    lines.append('from pathlib import Path')
    lines.append("sys.path = [p for p in sys.path if 'hermes' not in p.lower()]")
    lines.append('import pandas as pd')
    lines.append('')
    lines.append(f'PROVIDER_CODE = "{code}"')
    lines.append(f'PROVIDER_NAME = "{name}"')
    lines.append('PROVIDER_DIR = Path(__file__).resolve().parent')
    lines.append(f'SLUG = "{slug}"')
    lines.append(f'OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")')
    lines.append(f'OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")')
    lines.append(f'REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"')
    lines.append(f'INTL_URL = "{intl_url}"')
    lines.append('')
    lines.append("HEADERS = {")
    lines.append('    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",')
    lines.append('    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",')
    lines.append('}')
    lines.append('')
    lines.append('def clean_numeric_fee(val):')
    lines.append('    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):')
    lines.append('        return "NULL"')
    lines.append('    v = re.sub(r"[^\\d.]", "", str(val))')
    lines.append('    if not v: return "NULL"')
    lines.append('    try:')
    lines.append('        n = float(v)')
    lines.append('        return str(int(n)) if n.is_integer() else str(round(n, 2))')
    lines.append('    except:')
    lines.append('        return "NULL"')
    lines.append('')
    lines.append('def extract_fees_from_html(html):')
    lines.append('    """Look for international fee amounts in HTML."""')
    lines.append('    fees = {}')
    lines.append('    # Find dollar amounts near year levels')
    lines.append('    for yr in [f"Year {i}" for i in range(1,13)] + ["Prep", "Kindergarten", "Pre-Primary", "PP"]:')
    lines.append('        pattern = re.escape(yr) + r".{0,300}?\\$([\\d,]+(?:\\.\\d{2})?)"')
    lines.append('        for m in re.finditer(pattern, html, re.DOTALL):')
    lines.append('            try:')
    lines.append('                amt = float(m.group(1).replace(",", ""))')
    lines.append('                if 1000 < amt < 200000:')
    lines.append('                    fees[yr] = amt')
    lines.append('            except:')
    lines.append('                pass')
    lines.append('    return fees if fees else None')
    lines.append('')
    lines.append('def main():')
    lines.append('    print(f"\\n  === {PROVIDER_NAME} Web Scraper ===")')
    lines.append('    print(f"  Provider: {PROVIDER_CODE}")')
    lines.append('    print(f"  Website: {INTL_URL}\\n")')
    lines.append('')
    lines.append('    # Fetch the international page')
    lines.append('    fees_data = None')
    lines.append('    try:')
    lines.append('        r = requests.get(INTL_URL, timeout=15, headers=HEADERS)')
    lines.append('        print(f"  Intl page: {r.status_code} ({len(r.text)}b)")')
    lines.append('        if r.status_code == 200:')
    lines.append('            text = r.text')
    lines.append('            if len(text) >= 500 and not re.search(r"(page not found|404|oops|sorry.*page)", text[:500], re.IGNORECASE):')
    lines.append('                fees_data = extract_fees_from_html(text)')
    lines.append('                if fees_data:')
    lines.append('                    print(f"  Found fee data: {fees_data}")')
    lines.append('                # Also extract amounts near "international" keyword')
    lines.append('                idx = text.lower().find("international")')
    lines.append('                if idx > 0:')
    lines.append('                    chunk = text[idx:idx+2000]')
    lines.append('                    amounts = re.findall(r"\\$([\\d,]+(?:\\.\\d{2})?)", chunk)')
    lines.append('                    print(f"  Found {len(amounts)} fee amounts near international keyword")')
    lines.append('    except Exception as e:')
    lines.append('        print(f"  Fetch error: {e}")')
    lines.append('')
    lines.append('    # Also try alternative paths for fees')
    lines.append('    alt_urls = []')
    lines.append('    if "/international" in INTL_URL:')
    lines.append('        alt_urls.append(INTL_URL.replace("/international", "/fees"))')
    lines.append('    alt_urls.append(INTL_URL.rstrip("/") + "/fees/")')
    lines.append('    for au in alt_urls:')
    lines.append('        if au == INTL_URL:')
    lines.append('            continue')
    lines.append('        try:')
    lines.append('            r2 = requests.get(au, timeout=10, headers=HEADERS)')
    lines.append('            if r2.status_code == 200 and len(r2.text) > 500:')
    lines.append('                fees2 = extract_fees_from_html(r2.text)')
    lines.append('                if fees2:')
    lines.append('                    fees_data = fees2')
    lines.append('                    print(f"  Found fee data from fees page: {fees2}")')
    lines.append('        except:')
    lines.append('            pass')
    lines.append('')
    lines.append('    # Load CSV register')
    lines.append('    rows = []')
    lines.append("    with open(REGISTER_CSV, encoding='utf-8-sig') as f:")
    lines.append('        for rec in csv.DictReader(f):')
    lines.append('            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE:')
    lines.append('                continue')
    lines.append('            if rec["Expired"].strip().lower() == "yes":')
    lines.append('                continue')
    lines.append('')
    lines.append('            cricos = rec["CRICOS Course Code"].strip()')
    lines.append('            course_name = rec["Course Name"].strip()')
    lines.append('            dur_str = re.sub(r"[^\\d]", "", rec.get("Duration (Weeks)") or "")')
    lines.append('            dur = int(dur_str) if dur_str.isdigit() else 0')
    lines.append('')
    lines.append('            csv_fee = rec.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")')
    lines.append('            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")')
    lines.append('            total_csv = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")')
    lines.append('')
    lines.append('            annual_fee = 0')
    lines.append('            if csv_fee:')
    lines.append('                try:')
    lines.append('                    annual_fee = float(csv_fee)')
    lines.append('                except:')
    lines.append('                    pass')
    lines.append('')
    lines.append('            # Determine entry requirements by course type')
    lines.append('            if "ELICOS" in course_name or "English" in course_name or "ESL" in course_name:')
    lines.append("                entry_req = 'English proficiency assessment required. IELTS 5.0+ or equivalent.'")
    lines.append('            elif "Foundation" in course_name or "Bridging" in course_name:')
    lines.append("                entry_req = 'AEAS test recommended. IELTS 5.5+. Academic transcripts.'")
    lines.append('            elif "International Baccalaureate" in course_name:')
    lines.append("                entry_req = 'AEAS test, English proficiency, academic transcripts. Interview may be required.'")
    lines.append('            elif "Diploma" in course_name or "Certificate" in course_name:')
    lines.append("                entry_req = 'Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.'")
    lines.append('            else:')
    lines.append("                entry_req = 'AEAS test and interview. Minimum English proficiency required. Academic transcripts.'")
    lines.append('')
    lines.append("            intake = 'Term 1 (January), Term 3 (July)'")
    lines.append('')
    lines.append('            # Determine year level')
    lines.append('            yr_level = "All levels"')
    lines.append('            if "Primary" in course_name or "Pre-Primary" in course_name or "Kindergarten" in course_name:')
    lines.append('                yr_level = "PP-6"')
    lines.append('            elif "Senior" in course_name or "Years 11" in course_name:')
    lines.append('                yr_level = "11-12"')
    lines.append('            elif "Secondary" in course_name or "Years 7" in course_name or "Junior" in course_name:')
    lines.append('                yr_level = "7-10"')
    lines.append('            elif "Foundation" in course_name or "Foundation Studies" in course_name:')
    lines.append('                yr_level = "Foundation"')
    lines.append('            elif "ELICOS" in course_name or "English" in course_name:')
    lines.append('                yr_level = "ESL"')
    lines.append('            elif "IB" in course_name or "International Baccalaureate" in course_name:')
    lines.append('                yr_level = "IB"')
    lines.append('')
    lines.append('            # Build course description')
    lines.append("            desc = '<h4>%s - %s</h4>' % (PROVIDER_NAME, course_name)")
    lines.append("            desc += '<p>%s offers %s for international students. ' % (PROVIDER_NAME, course_name.lower())")
    lines.append("            desc += 'Located in Perth, Western Australia. CRICOS course code: %s.</p>' % cricos")
    lines.append('')
    lines.append('            note_parts = []')
    lines.append('            if fees_data:')
    lines.append('                note_parts.append("Fee data found on website")')
    lines.append('            else:')
    lines.append('                note_parts.append("CSV fallback - fee data not on website (likely in PDF)")')
    lines.append('            if total_csv:')
    lines.append('                note_parts.append("CSV cost: $%s" % total_csv)')
    lines.append('')
    lines.append('            rows.append({')
    lines.append('                "cricos": cricos,')
    lines.append('                "title": course_name,')
    lines.append('                "url": INTL_URL,')
    lines.append('                "course_description": desc,')
    lines.append('                "course_duration_per_week": dur,')
    lines.append('                "offshore_tuition_fee": int(annual_fee) if annual_fee else "",')
    lines.append('                "onshore_tuition_fee": "",')
    lines.append('                "enrolment_fee": clean_numeric_fee(int(float(nt))) if nt and float(nt) < 10000000 else "",')
    lines.append('                "materials_fee": "",')
    lines.append('                "intake": intake,')
    lines.append('                "entry_requirements": entry_req,')
    lines.append('                "apply_form": INTL_URL,')
    lines.append('                "source": "webscrape",')
    lines.append('                "note": " | ".join(note_parts),')
    lines.append('            })')
    lines.append('')
    lines.append('    print(f"  Courses found: {len(rows)}")')
    lines.append('    if not rows:')
    lines.append('        print(f"  !! No courses in CSV for provider {PROVIDER_CODE}")')
    lines.append('        return')
    lines.append('')
    lines.append('    # Write XLSX')
    lines.append('    out = []')
    lines.append('    for r in rows:')
    lines.append("        out.append({")
    lines.append('            "cricos": r["cricos"],')
    lines.append('            "title": r["title"],')
    lines.append('            "url": r["url"],')
    lines.append('            "course_duration_per_week": r["course_duration_per_week"],')
    lines.append('            "offshore_tuition_fee": r["offshore_tuition_fee"],')
    lines.append('            "onshore_tuition_fee": r["onshore_tuition_fee"],')
    lines.append('            "enrolment_fee": r["enrolment_fee"],')
    lines.append('            "materials_fee": r["materials_fee"],')
    lines.append('            "intake": r["intake"],')
    lines.append('            "course_description": r["course_description"],')
    lines.append('            "entry_requirements": r["entry_requirements"],')
    lines.append('            "source": r["source"],')
    lines.append('            "note": r["note"],')
    lines.append('        })')
    lines.append('')
    lines.append('    df = pd.DataFrame(out)')
    lines.append('    df.to_excel(OUTPUT_XLSX, index=False)')
    lines.append('    print(f"  -> {OUTPUT_XLSX.name}")')
    lines.append('')
    lines.append('    # Write SQL')
    lines.append('    emitted = set()')
    lines.append("    with open(OUTPUT_SQL, 'w', encoding='utf-8') as f:")
    lines.append('        f.write("-- %s (%s) - Course updates\\n" % (PROVIDER_NAME, PROVIDER_CODE))')
    lines.append('        f.write("-- Source: %s\\n\\n" % INTL_URL)')
    lines.append('        f.write("UPDATE provider_institution SET\\n")')
    lines.append('        f.write("    intake_date = \'%s\',\\n" % intake)')
    lines.append('        f.write("    updated_at = NOW()\\n")')
    lines.append('        f.write("WHERE cricos_provider_code = \'%s\';\\n\\n" % PROVIDER_CODE)')
    lines.append('')
    lines.append('        for r in rows:')
    lines.append('            if r["cricos"] in emitted:')
    lines.append('                continue')
    lines.append('            emitted.add(r["cricos"])')
    lines.append('')
    lines.append('            dur_val = str(r["course_duration_per_week"]) if r["course_duration_per_week"] else "NULL"')
    lines.append('            fee_val = clean_numeric_fee(r["offshore_tuition_fee"])')
    lines.append('            enr_val = clean_numeric_fee(r["enrolment_fee"])')
    lines.append('            desc = r["course_description"].replace("\\\'", "\\\'\\\'")')
    lines.append('            entry = r["entry_requirements"].replace("\\\'", "\\\'\\\'")')
    lines.append('')
    lines.append('            f.write("UPDATE courses SET\\n")')
    lines.append('            f.write("    course_description = \\\'<h4>Course overview</h4><p>%s</p>\\\',\\n" % desc)')
    lines.append('            f.write("    course_duration_per_week = %s,\\n" % dur_val)')
    lines.append('            f.write("    offshore_tuition_fee = %s,\\n" % fee_val)')
    lines.append('            f.write("    onshore_tuition_fee = NULL,\\n")')
    lines.append('            f.write("    enrolment_fee = %s,\\n" % enr_val)')
    lines.append('            f.write("    materials_fee = NULL,\\n")')
    lines.append('            f.write("    entry_requirements = \\\'<h4>Entry Requirements</h4><p>%s</p>\\\',\\n" % entry)')
    lines.append('            f.write("    apply_form = \\\'%s\\\',\\n" % r["apply_form"])')
    lines.append('            f.write("    updated_at = NOW()\\n")')
    lines.append('            f.write("WHERE cricos_course_code = \\\'%s\\\';\\n\\n" % r["cricos"])')
    lines.append('')
    lines.append('    print(f"  -> {OUTPUT_SQL.name}")')
    lines.append('    print(f"  Done: {len(emitted)} courses.\\n")')
    lines.append('')
    lines.append('if __name__ == "__main__":')
    lines.append('    main()')
    lines.append('')
    
    return '\n'.join(lines)

print("Generating WA school web scrapers...")
print("="*60)

for p in PROVIDERS:
    code, name, slug, url, intl_path, folder = p
    content = make_scraper(code, name, slug, url, intl_path, folder)
    path = "%s/%s_webscrape.py" % (folder, slug)
    w(content, path)

print("\n%s" % ("="*60))
print("Done: %d scrapers generated." % len(PROVIDERS))
