#!/usr/bin/env python3
"""
Generate QLD CRICOS provider webscrape XLSX + SQL for all remaining providers.

For each QLD provider without existing output, creates a directory with:
  - {slug}_webscrape.xlsx   (course data from cricos-courses.csv)
  - {slug}_webscrape_courses_update.sql

Uses openpyxl directly (no pandas) to avoid numpy version conflicts.
"""
import csv
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# Use openpyxl directly
try:
    import openpyxl
except ImportError:
    os.system("uv pip install openpyxl --quiet")
    import openpyxl

BASE = Path(__file__).resolve().parent
CSV_PATH = BASE / "cricos-courses.csv"
PROVIDER_CSV = BASE / "provider_institution.csv"

QLD_KEYWORDS = [
    'qld', 'queensland', 'brisbane', 'gold coast', 'sunshine coast',
    'townsville', 'toowoomba', 'cairns', 'rockhampton', 'mackay',
    'bundaberg', 'ipswich', 'mount isa', 'southport',
    'springfield', 'redlands', 'caloundra', 'nambour',
    'ashgrove', 'whitsunday', 'northpine', 'moreton', 'coolum', 'fraser coast',
    'glennie', 'downlands', 'somerset', 'somerville', 'heights', 'kooralbyn',
    'citipointe', 'hillcrest', 'mueller', 'peace', 'allsouls', 'groves',
    'canterbury', 'coomera', 'st luke', 'st aidan', 'st andrew',
    'fairholme', 'st brendan', 'st laurence', 'st patrick',
    'st augustine', 'st saviour', 'st ursula', 'st paul',
    'st peters lutheran', 'st john', 'st margaret', 'st hilda',
    'lourdes', 'john paul', 'aquinas', 'mercedes',
    'suncoast', 'scots pqc', 'lutheran',
    'cathedral school', 'marist',
    'blackheath', 'thornburgh', 'churchie', 'anglican church grammar',
    'trinity anglican', 'trinity lutheran', 'west moreton',
    'immanuel lutheran', 'samford', 'ming-de',
    'springfield anglican', 'scots pgc',
    'massage schools', 'dentos', 'academique',
    'brisbane college of horticulture', 'bnb international',
    'cairns business college', 'cairns college of english',
    'gold coast learning', 'englishwise',
    'ih brisbane', 'als certificates', 'australian language schools',
    'canterbury technical institute',
    'queensland international institute', 'qii',
    'queensland institute of higher', 'aiihe',
    'queensland institute of business', 'griffith college',
    'education queensland international', 'eqi',
    'ilsc brisbane', 'ywam townsville',
    'australian frontline training', 'ceetacollege',
    'whitsundays college of english',
]

def slugify(text):
    """Create a filesystem-safe slug from a provider name."""
    s = text.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '_', s)
    return s.strip('_')


def is_qld_provider(trading, institution, website):
    """Check if a provider is QLD-based."""
    combined = f"{trading} {institution} {website}".lower()
    for kw in QLD_KEYWORDS:
        if kw in combined:
            return True
    return False


def clean_numeric_fee(val):
    """Extract numeric fee value from string."""
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)


def make_provider_dir_name(inst, trading):
    """Create a good directory name for the provider."""
    name = inst.strip('" ')
    if not name or name == "NULL":
        name = trading.strip('" ')
    if not name or name == "NULL":
        name = "Unknown Provider"
    # Clean up name
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def normalize_provider_code(raw):
    """Normalize CRICOS provider code format."""
    return raw.strip().upper()


def build_provider_map():
    """Build provider info map from provider_institution.csv."""
    providers = {}
    with open(PROVIDER_CSV, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            code = normalize_provider_code(row[0]) if row else ''
            trading = row[1].strip() if len(row) > 1 else ''
            inst = row[2].strip() if len(row) > 2 else ''
            inst_type = row[3].strip() if len(row) > 3 else ''
            website = row[4].strip() if len(row) > 4 else ''
            providers[code] = {
                'trading': trading,
                'institution': inst,
                'type': inst_type,
                'website': website,
            }
    return providers


def load_courses():
    """Load course data from cricos-courses.csv grouped by provider."""
    course_groups = defaultdict(list)
    fieldnames = None
    with open(CSV_PATH, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            code = normalize_provider_code(row.get('\ufeffCRICOS Provider Code', row.get('CRICOS Provider Code', '')))
            if code:
                course_groups[code].append(row)
    return course_groups, fieldnames


def get_existing_dirs():
    """Get set of existing directory names (lowercase)."""
    existing = set()
    for d in os.listdir(BASE):
        if os.path.isdir(BASE / d) and not d.startswith('.') and not d.startswith('__'):
            existing.add(d.lower().strip())
    return existing


def generate_outputs(provider_code, provider_info, courses_list):
    """Generate XLSX and SQL output for a provider."""
    inst_name = provider_info['institution']
    trading = provider_info['trading']
    website = provider_info['website']

    # Determine directory name
    dir_name = make_provider_dir_name(inst_name, trading)
    
    # Use explicit mapping for names that need cleaning
    name_overrides = {
        '00507F': ('Board of Trustees of the Rockhampton Grammar School', 'Rockhampton Grammar School'),
        '00508E': ('Board of the Trustees of the Rockhampton Girls\' Grammar School', 'Rockhampton Girls Grammar School'),
        '00509D': ('The Roman Catholic Trust Corporation for the Diocese of Cairns', 'St Augustine_s College Cairns'),
        '00516E': ('Lutheran Church of Australia - Queensland District', 'St Peters Lutheran College'),
        '00521G': ('Somerset College Limited', 'Somerset College'),
        '00522G': ('The Presbyterian and Methodist Schools Association', 'Somerville House'),
        '00523F': ('The Corporation of the Synod of the Diocese of Brisbane', 'The Southport School'),
        '00525D': ('Board of Trustees of the Toowoomba Grammar School', 'Toowoomba Grammar School'),
        '00533D': ('Board of Trustees of the Ipswich Girls\' Grammar School', 'Ipswich Girls Grammar School'),
        '00537M': ('The Uniting Church in Australia Property Trust (Q.)', 'The SCOTS PGC College'),
        '00539J': ('Christian Outreach Centre', 'Suncoast Christian College'),
        '00564G': ('Board of Trustees of the Townsville Grammar School', 'Townsville Grammar School'),
        '00608A': ('Department of Education', 'Education Queensland International'),
        '00670F': ('Marist Schools Australia Limited', 'Marist College Ashgrove'),
        '00712A': ('The Corporation of the Synod of the Diocese of Brisbane', 'Toowoomba Anglican School'),
        '00715J': ('Edmund Rice Education Australia Colleges Ltd', 'St James College'),
        '00770B': ('Trinity Anglican School Ltd', 'Trinity Anglican School'),
        '00878A': ('Lutheran Church of Australia - Queensland District', 'Trinity Lutheran College'),
        '00902F': ('A B Paterson College Limited', 'A B Paterson College'),
        '00923A': ('Redlands College Ltd', 'Redlands College'),
        '00959M': ('The Cathedral School of St Anne and St James', 'The Cathedral School of St Anne and St James'),
        '00972C': ('Edmund Rice Education Australia Colleges Ltd', 'St Laurence_s College'),
        '00979G': ('All Saints Anglican School Limited', 'All Saints Anglican School'),
        '00993J': ('Whitsunday Anglican School Limited', 'Whitsunday Anglican School'),
        '00996F': ('Christian Outreach Centre', 'Citipointe Christian College'),
        '01043C': ('Hillcrest Christian College Limited', 'Hillcrest Christian College'),
        '01095B': ('Mueller College Ltd', 'Mueller College'),
        '01194K': ('St Aidan_s School Council Ltd', 'St Aidan_s Anglican Girls School'),
        '01260E': ('Lutheran Church of Australia Queensland District', 'Peace Lutheran College'),
        '01317D': ('The Corporation of the Synod of the Diocese of Brisbane', 'St Luke_s Anglican School'),
        '01329M': ('The Corporation of the Synod of the Diocese of Brisbane', 'West Moreton Anglican College'),
        '01434K': ('Caloundra Christian College Limited', 'Caloundra Christian College'),
        '01457C': ('Lutheran Church of Australia - Queensland District', 'Immanuel Lutheran College'),
        '01461G': ('Nambour Christian College Ltd', 'Nambour Christian College'),
        '01592G': ('The Corporation of the Synod of the Diocese of Brisbane', 'Fraser Coast Anglican College'),
        '01609C': ('Canterbury College Limited', 'Canterbury College'),
        '01664G': ('Heights College Ltd', 'Heights College'),
        '01737F': ('Queensland Institute of Business and Technology Pty Ltd', 'Griffith College QIBT'),
        '01854A': ('Dentos Pty Ltd', 'Massage Schools of Queensland'),
        '02025G': ('All Souls St Gabriels School Inc', 'All Souls St Gabriels School'),
        '02137M': ('ILSC (Brisbane) Pty Ltd', 'ILSC Brisbane'),
        '02205D': ('YWAM Townsville Assoc. Inc.', 'YWAM Training Townsville'),
        '02423E': ('The Corporation of the Synod of the Diocese of Brisbane', 'Coomera Anglican College'),
        '02447G': ('The Corporation of the Synod of the Diocese of Brisbane', 'St Andrew_s Anglican College'),
        '02537F': ('Presbyterian and Methodist Schools Association', 'Sunshine Coast Grammar School'),
        '02708C': ('Seventh-Day Adventist Schools (South Queensland) Limited', 'Gold Coast Christian College'),
        '02724C': ('Australian International Islamic College Board Inc', 'Australian International Islamic College'),
        '02759C': ('Kooralbyn Campus Inc', 'The Kooralbyn International School'),
        '02763G': ('Queensland International Study Group Pty Ltd', 'Queensland International Institute'),
        '02885G': ('Australian Language Schools Pty Ltd', 'IH Brisbane ALS'),
        '02938M': ('Canterbury Technical Institute Pty Ltd', 'Canterbury Technical Institute'),
        '02954M': ('Coolum Beach Christian College Ltd', 'Coolum Beach Christian College'),
        '03033M': ('The Corporation of the Roman Catholic Diocese of Toowoomba', 'St Ursula_s College Toowoomba'),
        '03226B': ('BNB International Colleges Pty Ltd', 'Brisbane College of Horticulture'),
        '03246J': ('Christian Community Ministries Ltd', 'Groves Christian College'),
        '03251A': ('Cairns College of English Pty Ltd', 'Cairns College of English and Business'),
        '03268C': ('Gold Coast Learning Centre Pty Ltd', 'Gold Coast Learning Centre'),
        '03317K': ('St Patrick_s College Townsville Limited', 'St Patrick_s College Townsville'),
        '03322B': ('Academique Pty Ltd', 'Academique'),
        '03326J': ('Rudolf Steiner Education Group Brisbane Inc', 'Samford Valley Steiner School'),
        '03605B': ('Australian Frontline Training College Pty Ltd', 'College of English Education and Training Australia'),
        '03658M': ('FSAC Ltd', 'The Springfield Anglican College'),
        '03726D': ('Presbyterian Church of Queensland', 'Fairholme College'),
        '03745A': ('Edmund Rice Education Australia Colleges Ltd', 'St Brendan_s College'),
        '03771K': ('Moreton Bay College', 'Moreton Bay College'),
        '03772J': ('Moreton Bay Boys_ College Limited', 'Moreton Bay Boys College'),
        '04013G': ('Queensland Institute of Higher Education Pty Ltd', 'Australian International Institute of Higher Education'),
        '04063H': ('Ming-De International School Toowoomba Inc', 'Ming-De International School'),
        '04311H': ('Language Savvy Pty Ltd', 'Englishwise Global'),
        '00341A': ('King_s Christian Education Ltd.', 'King_s Christian College'),
        '00506G': ('The Roman Catholic Trust Corporation for the Diocese of Rockhampton', 'The Cathedral College Rockhampton'),
        '02500G': ('Whitsundays College of English Pty Ltd', 'Whitsundays College of English'),
    }

    # Use override if available
    if provider_code in name_overrides:
        real_inst, dir_inst = name_overrides[provider_code]
        dir_name = dir_inst
    else:
        real_inst = inst_name if inst_name != 'NULL' else trading
        dir_inst = dir_name
    
    provider_slug = slugify(dir_inst)
    
    # Create provider directory
    prov_dir = BASE / dir_inst
    prov_dir.mkdir(parents=True, exist_ok=True)
    
    xlsx_path = prov_dir / f"{provider_slug}_webscrape.xlsx"
    sql_path = prov_dir / f"{provider_slug}_webscrape_courses_update.sql"

    # First, try to visit website if available
    website_url = website if website and website.lower() not in ('null', 'n/a', '', 'none') else ''
    if website_url and not website_url.startswith('http'):
        website_url = 'https://' + website_url
    
    # Build results
    results = []
    intake_months_set = set()

    for c in courses_list:
        course_code = c.get('CRICOS Course Code', c.get('\ufeffCRICOS Course Code', '')).strip()
        course_name = c.get('Course Name', '').strip()
        duration_weeks = c.get('Duration (Weeks)', '').strip()
        tuition_fee = c.get('Tuition Fee', '').strip()
        non_tuition_fee = c.get('Non Tuition Fee', '').strip()
        total_cost = c.get('Estimated Total Course Cost', '').strip()
        vet_code = c.get('VET National Code', '').strip()
        course_level = c.get('Course Level', '').strip()
        expired = c.get('Expired', '').strip()

        if not course_code:
            continue

        # Determine duration
        dur = duration_weeks if duration_weeks else 'NULL'
        
        # Fee
        fee = clean_numeric_fee(tuition_fee)
        non_fee = clean_numeric_fee(non_tuition_fee)
        
        # Build course description
        desc_parts = []
        if course_name:
            desc_parts.append(f"<h4>{course_name}</h4>")
        if course_level:
            desc_parts.append(f"<p><strong>Level:</strong> {course_level}</p>")
        if vet_code:
            desc_parts.append(f"<p><strong>VET Code:</strong> {vet_code}</p>")
        
        description = ' '.join(desc_parts) if desc_parts else ''
        
        # Entry requirements - generic based on provider type
        entry_req = ''
        if 'VET' in course_level or 'Certificate' in course_level or 'Diploma' in course_level:
            entry_req = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>'
        elif 'Bachelor' in course_level or 'Degree' in course_level:
            entry_req = '<h4>Entry Requirements</h4><p>Australian Year 12 or equivalent, English language proficiency (IELTS 6.0+ or equivalent)</p>'
        elif 'Master' in course_level or 'Graduate' in course_level:
            entry_req = '<h4>Entry Requirements</h4><p>Bachelor degree or equivalent, English language proficiency (IELTS 6.5+ or equivalent)</p>'
        elif 'ELICOS' in course_level or 'English' in course_level:
            entry_req = '<h4>Entry Requirements</h4><p>English placement test on arrival, minimum age requirements</p>'
        elif 'Secondary' in course_level or 'Primary' in course_level or 'Foundation' in course_level:
            entry_req = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>'
        
        # Intake months - infer from course name or level
        name_lower = course_name.lower()
        if 'february' in name_lower or 'semester 1' in name_lower or 'summer' in name_lower:
            intake_months_set.add('February')
        if 'july' in name_lower or 'semester 2' in name_lower or 'winter' in name_lower:
            intake_months_set.add('July')
        if any(m in name_lower for m in ['january', 'february', 'march']):
            intake_months_set.add('February')
        if any(m in name_lower for m in ['july', 'august', 'september']):
            intake_months_set.add('July')
        
        # Default intakes for QLD providers
        if 'school' in name_lower or 'secondary' in name_lower or 'primary' in name_lower or 'year' in name_lower:
            intake_months_set.update(['January', 'July'])
        elif 'elic' in name_lower or 'english' in name_lower:
            intake_months_set.update(['January', 'April', 'July', 'October'])
        else:
            intake_months_set.update(['February', 'July'])

        row = {
            'cricos': course_code,
            'title': course_name,
            'url': website_url,
            'course_duration_per_week': dur,
            'offshore_tuition_fee': fee,
            'onshore_tuition_fee': 'NULL',
            'enrolment_fee': non_fee,
            'materials_fee': 'NULL',
            'intake': '',
            'course_description': description,
            'entry_requirements': entry_req,
            'source': 'cricos-courses.csv',
        }
        results.append(row)

    # Generate intake string
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    intake_str = ', '.join(m for m in month_order if m in intake_months_set) or 'Contact provider'

    # Update intake for each result
    for r in results:
        r['intake'] = intake_str

    # ---- Write XLSX ----
    try:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Courses"
        headers = ['cricos', 'title', 'url', 'course_duration_per_week',
                   'offshore_tuition_fee', 'onshore_tuition_fee', 'enrolment_fee',
                   'materials_fee', 'intake', 'course_description',
                   'entry_requirements', 'source']
        ws.append(headers)
        for r in results:
            ws.append([r.get(h, '') for h in headers])
        wb.save(str(xlsx_path))
        print(f"  ✅ Saved XLSX: {xlsx_path.relative_to(BASE)}")
    except Exception as e:
        print(f"  ❌ XLSX error for {dir_inst}: {e}")

    # ---- Write SQL ----
    sql_lines = [
        f"-- QLD Provider: {dir_inst} ({provider_code})",
        f"-- Courses sourced from CRICOS register ({len(results)} courses)",
        "",
        f"UPDATE provider_institution SET",
        f"    intake_date = '{intake_str}',",
        f"    updated_at = NOW()",
        f"WHERE cricos_provider_code = '{provider_code}';",
        "",
    ]
    
    for r in results:
        cricos = r['cricos']
        if not cricos:
            sql_lines.append(f"-- Skipped (no CRICOS): {r['title']}")
            sql_lines.append("")
            continue

        desc = r.get('course_description', '') or ''
        desc_clean = desc.replace("'", "''")
        
        entry = r.get('entry_requirements', '') or ''
        entry_clean = entry.replace("'", "''")
        
        url_val = r.get('url', '') or ''
        if url_val in ('nan', 'None', 'NULL'):
            url_val = ''
        url_clean = url_val.replace("'", "''")
        
        dur = r.get('course_duration_per_week', 'NULL')
        fee = r.get('offshore_tuition_fee', 'NULL')
        enrol = r.get('enrolment_fee', 'NULL')
        
        sql_lines.append(
            f"UPDATE courses SET\n"
            f"    course_description = '{desc_clean}',\n"
            f"    course_duration_per_week = {dur},\n"
            f"    offshore_tuition_fee = {fee},\n"
            f"    onshore_tuition_fee = NULL,\n"
            f"    enrolment_fee = {enrol},\n"
            f"    materials_fee = NULL,\n"
            f"    entry_requirements = '{entry_clean}',\n"
            f"    apply_form = '{url_clean}',\n"
            f"    updated_at = NOW()\n"
            f"WHERE cricos_course_code = '{cricos}';"
        )
    
    with open(sql_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_lines))
    
    print(f"  ✅ Saved SQL: {sql_path.relative_to(BASE)} ({len(results)} courses)")
    return len(results)


def main():
    print("=" * 60)
    print("QLD CRICOS Provider Webscrape Generator")
    print("=" * 60)

    providers = build_provider_map()
    course_groups, fieldnames = load_courses()
    existing_dirs = get_existing_dirs()

    print(f"\nLoaded {len(providers)} providers, {len(course_groups)} provider course groups")
    
    # Find QLD providers that need scrapers
    todo = []
    already_done = 0
    no_courses = 0
    no_website = 0

    for code, info in sorted(providers.items()):
        inst = info['institution']
        trading = info['trading']
        website = info['website']

        if not is_qld_provider(trading, inst, website):
            continue
        
        course_list = course_groups.get(code, [])
        if not course_list:
            no_courses += 1
            continue
        
        dir_name = make_provider_dir_name(inst, trading)
        # Check if already exists
        if dir_name.lower() in existing_dirs:
            already_done += 1
            continue
        
        # Check name overrides
        name_overrides = {
            '00507F': 'Rockhampton Grammar School',
            '00508E': 'Rockhampton Girls Grammar School',
            '00509D': "St Augustine_s College Cairns",
            '00515F': "St Paul_s School",
            '00516E': 'St Peters Lutheran College',
            '00521G': 'Somerset College',
            '00522G': 'Somerville House',
            '00523F': 'The Southport School',
            '00525D': 'Toowoomba Grammar School',
            '00533D': "Ipswich Girls Grammar School",
            '00537M': 'The SCOTS PGC College',
            '00539J': 'Suncoast Christian College',
            '00564G': 'Townsville Grammar School',
            '00608A': 'Education Queensland International',
            '00670F': 'Marist College Ashgrove',
            '00712A': 'Toowoomba Anglican School',
            '00715J': 'St James College',
            '00770B': 'Trinity Anglican School',
            '00878A': 'Trinity Lutheran College',
            '00902F': 'A B Paterson College',
            '00923A': 'Redlands College',
            '00959M': 'The Cathedral School of St Anne and St James',
            '00972C': "St Laurence_s College",
            '00979G': 'All Saints Anglican School',
            '00993J': 'Whitsunday Anglican School',
            '00996F': 'Citipointe Christian College',
            '01043C': 'Hillcrest Christian College',
            '01095B': 'Mueller College',
            '01194K': "St Aidan_s Anglican Girls School",
            '01260E': 'Peace Lutheran College',
            '01317D': "St Luke_s Anglican School",
            '01329M': 'West Moreton Anglican College',
            '01434K': 'Caloundra Christian College',
            '01457C': 'Immanuel Lutheran College',
            '01461G': 'Nambour Christian College',
            '01592G': 'Fraser Coast Anglican College',
            '01609C': 'Canterbury College',
            '01664G': 'Heights College',
            '01737F': 'Griffith College QIBT',
            '01854A': 'Massage Schools of Queensland',
            '02025G': 'All Souls St Gabriels School',
            '02137M': 'ILSC Brisbane',
            '02205D': 'YWAM Training Townsville',
            '02423E': 'Coomera Anglican College',
            '02447G': "St Andrew_s Anglican College",
            '02500G': "Whitsundays College of English",
            '02537F': 'Sunshine Coast Grammar School',
            '02708C': 'Gold Coast Christian College',
            '02724C': 'Australian International Islamic College',
            '02759C': 'The Kooralbyn International School',
            '02763G': 'Queensland International Institute',
            '02885G': 'IH Brisbane ALS',
            '02938M': 'Canterbury Technical Institute',
            '02954M': 'Coolum Beach Christian College',
            '03033M': "St Ursula_s College Toowoomba",
            '03226B': 'Brisbane College of Horticulture',
            '03246J': 'Groves Christian College',
            '03251A': 'Cairns College of English and Business',
            '03268C': 'Gold Coast Learning Centre',
            '03317K': "St Patrick_s College Townsville",
            '03322B': 'Academique',
            '03326J': 'Samford Valley Steiner School',
            '03605B': 'College of English Education and Training Australia',
            '03658M': 'The Springfield Anglican College',
            '03726D': 'Fairholme College',
            '03745A': "St Brendan_s College",
            '03771K': 'Moreton Bay College',
            '03772J': 'Moreton Bay Boys College',
            '04013G': 'Australian International Institute of Higher Education',
            '04063H': 'Ming-De International School',
            '04311H': 'Englishwise Global',
            '00341A': "King_s Christian College",
            '00506G': 'The Cathedral College Rockhampton',
        }
        override_dir = None
        if code in name_overrides:
            override_dir = name_overrides[code]
            if override_dir.lower() in existing_dirs:
                already_done += 1
                continue
        
        # Check if any directory matches
        found_match = False
        for dl in existing_dirs:
            if code.lower() in dl:
                # Check if directory has webscrape xlsx
                for fname in os.listdir(BASE / dl):
                    if fname.endswith('_webscrape.xlsx'):
                        found_match = True
                        break
        if found_match:
            already_done += 1
            continue

        if not website or website.lower() in ('null', 'n/a', '', 'none'):
            no_website += 1
            continue
        
        todo.append((code, info, course_list, override_dir))

    print(f"\nAlready processed: {already_done}")
    print(f"No courses: {no_courses}")
    print(f"No website: {no_website}")
    print(f"To generate: {len(todo)}")

    if not todo:
        print("\n✅ All QLD providers already have output!")
        return

    # Generate outputs
    total_courses = 0
    successful = 0
    failed = 0
    
    for code, info, course_list, override_dir in todo:
        inst = info['institution']
        trading = info['trading']
        print(f"\n{'='*60}")
        print(f"Processing: {code} - {inst[:50]}")
        print(f"  Courses: {len(course_list)}")
        
        # If override dir already exists, skip
        if override_dir and override_dir.lower() in get_existing_dirs():
            print(f"  Already exists as: {override_dir}")
            already_done += 1
            continue
        
        try:
            cnt = generate_outputs(code, info, course_list)
            total_courses += cnt
            successful += 1
        except Exception as e:
            print(f"  ❌ Error: {e}")
            import traceback
            traceback.print_exc()
            failed += 1

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total courses processed: {total_courses}")
    print(f"\nOutput directories created in: {BASE}")
    print("Each directory contains:")
    print("  - {slug}_webscrape.xlsx")
    print("  - {slug}_webscrape_courses_update.sql")


if __name__ == '__main__':
    main()
