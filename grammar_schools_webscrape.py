"""
Grammar Schools Web Scraper - Visits each school website to extract course data.

For each provider:
1. Visit school website → find International Students page or course info
2. Extract: tuition fees, duration, entry requirements, intake dates from the website
3. Validate against CRICOS data from cricos-courses.csv
4. Generate {slug}_webscrape.xlsx and {slug}_webscrape_courses_update.sql
"""
import os, re, sys, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
REGISTER_CSV = BASE_DIR / "cricos-courses.csv"

# ---- Provider definitions ----
PROVIDERS = [
    {
        "code": "00341A", "name": "King's Christian College", "slug": "kings-christian-college",
        "url": "https://www.kingscollege.qld.edu.au",
        "intl_path": "/enrolments/international-students",
    },
    {
        "code": "00343K", "name": "St Leonard's College", "slug": "st-leonards",
        "url": "https://www.stleonards.vic.edu.au",
        "intl_path": "/international",
    },
    {
        "code": "00344J", "name": "St Margaret's School", "slug": "st-margarets",
        "url": "https://www.stmargarets.vic.edu.au",
        "intl_path": "/enrolment/international-enrolment",
    },
    {
        "code": "00345G", "name": "St Michael's Grammar School", "slug": "st-michaels-grammar",
        "url": "https://www.stmichaels.vic.edu.au",
        "intl_path": "/enrolment/international-students",
    },
    {
        "code": "00348E", "name": "Tintern Grammar", "slug": "tintern-grammar",
        "url": "https://www.tintern.vic.edu.au",
        "intl_path": "/international-students",
    },
    {
        "code": "00349D", "name": "Toorak College", "slug": "toorak-college",
        "url": "https://www.toorakcollege.vic.edu.au",
        "intl_path": "/enrolment/international",
    },
    {
        "code": "00350M", "name": "Trinity Grammar School Kew", "slug": "trinity-grammar-kew",
        "url": "https://www.trinity.vic.edu.au",
        "intl_path": "/enrolment/international-students",
    },
    {
        "code": "00354G", "name": "Wesley College Melbourne", "slug": "wesley-college",
        "url": "https://www.wesleycollege.edu.au",
        "intl_path": "/international-students",
    },
    {
        "code": "00355F", "name": "Westbourne Grammar School", "slug": "westbourne-grammar",
        "url": "https://www.westbournegrammar.com",
        "intl_path": "/enrolment/international-students",
    },
    {
        "code": "00356E", "name": "Yarra Valley Grammar School", "slug": "yarra-valley-grammar",
        "url": "https://www.yvg.vic.edu.au",
        "intl_path": "/enrolment/international-students",
    },
    {
        "code": "00360J", "name": "Concordia College Inc", "slug": "concordia-college",
        "url": "https://www.concordia.sa.edu.au",
        "intl_path": "/international-students",
    },
]

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "oct": "October", "nov": "November", "dec": "December",
}

MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n >= 100 else "NULL"


def fetch_html(url, timeout=20):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text
    except Exception as e:
        print(f"  ⚠️  Failed {url}: {e}")
        return ""


def extract_text(soup):
    """Get all visible text from parsed HTML."""
    for tag in soup.find_all(["script", "style", "noscript", "nav", "footer", "header"]):
        tag.decompose()
    return re.sub(r"\s+", " ", soup.get_text()).strip()


def find_intake_months(text):
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", text):
        k = tok.lower()
        if k in MONTHS and MONTHS[k] not in found:
            found.append(MONTHS[k])
    return found


def scrape_school(prov):
    """Visit school website, find international page, extract course info."""
    code = prov["code"]
    name = prov["name"]
    slug = prov["slug"]
    base_url = prov["url"]
    intl_path = prov["intl_path"]

    print(f"\n  {'='*55}")
    print(f"  {name} ({code})")
    print(f"  {'='*55}")

    # Load CRICOS register data for this provider
    cricos_courses = []
    if REGISTER_CSV.exists():
        with open(REGISTER_CSV, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r["CRICOS Provider Code"].strip() != code:
                    continue
                if r["Expired"].strip().lower() == "yes":
                    continue
                dur_str = re.sub(r"[^\d]", "", r.get("Duration (Weeks)", "") or "")
                fee_str = r.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")
                nt_str = r.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
                cricos_courses.append({
                    "cricos": r["CRICOS Course Code"].strip(),
                    "title": r["Course Name"].strip(),
                    "duration_weeks": int(dur_str) if dur_str.isdigit() else "",
                    "fee_total": fee_str,
                    "non_tuition_fee": nt_str,
                    "level": r.get("Course Level", "").strip(),
                })
    print(f"  CRICOS courses on register: {len(cricos_courses)}")

    # Try to fetch the international page(s)
    intl_urls_to_try = [
        base_url + intl_path,
        base_url + "/international",
        base_url + "/international-students",
        base_url + "/enrolment/international-students",
        base_url + "/admissions/international-students",
        base_url + "/fees",
        base_url + "/enrolment",
    ]

    intl_html = ""
    intl_url = ""
    for u in intl_urls_to_try:
        h = fetch_html(u)
        if h:
            intl_html = h
            intl_url = u
            print(f"  ✅ Found page: {u}")
            break

    if not intl_html:
        print(f"  ⚠️  No international page found, scraping homepage")
        intl_html = fetch_html(base_url)
        intl_url = base_url

    soup = BeautifulSoup(intl_html, "html.parser")
    text = extract_text(soup)

    # Try to find a fee table or course list on the page
    fees = extract_fees_from_page(soup, text)
    intake = extract_intake_from_page(soup, text)
    entry_req = extract_entry_requirements(soup, text)
    
    print(f"  Fees found: {fees}")
    print(f"  Intake: {intake}")
    print(f"  Entry req: {'…found…' if entry_req else 'not found'}")

    # Build course records - use CRICOS data where website data is sparse
    rows = []
    
    # also try to find courses listed on the page
    web_courses = find_courses_on_page(soup, text)
    
    if web_courses:
        print(f"  Courses from website: {len(web_courses)}")
        for wc in web_courses:
            # Try to match with CRICOS data
            cricos_match = None
            for cc in cricos_courses:
                if wc["title"].lower() in cc["title"].lower() or cc["title"].lower() in wc["title"].lower():
                    cricos_match = cc
                    break
            
            if cricos_match:
                dur = cricos_match["duration_weeks"] if cricos_match["duration_weeks"] else wc.get("duration", "")
                offshore = clean_numeric_fee(wc.get("fee", "")) if wc.get("fee") else clean_numeric_fee(cricos_match.get("fee_total", ""))
            else:
                dur = wc.get("duration", "")
                offshore = clean_numeric_fee(wc.get("fee", ""))
            
            rows.append({
                "cricos": cricos_match["cricos"] if cricos_match else "",
                "title": wc["title"],
                "url": intl_url,
                "course_duration_per_week": dur,
                "offshore_tuition_fee": offshore if offshore != "NULL" else "",
                "onshore_tuition_fee": "",
                "enrolment_fee": "",
                "materials_fee": "",
                "intake": intake,
                "course_description": wc.get("description", ""),
                "entry_requirements": entry_req[:500] if entry_req else "",
                "source": "website",
                "note": "",
            })
    
    # Also include CRICOS courses not matched to website courses
    matched_cricos = set(r["cricos"] for r in rows if r["cricos"])
    for cc in cricos_courses:
        if cc["cricos"] in matched_cricos:
            continue
        rows.append({
            "cricos": cc["cricos"],
            "title": cc["title"],
            "url": intl_url,
            "course_duration_per_week": cc["duration_weeks"],
            "offshore_tuition_fee": clean_numeric_fee(cc["fee_total"]) if clean_numeric_fee(cc["fee_total"]) != "NULL" else "",
            "onshore_tuition_fee": "",
            "enrolment_fee": clean_numeric_fee(cc["non_tuition_fee"]) if clean_numeric_fee(cc["non_tuition_fee"]) != "NULL" else "",
            "materials_fee": "",
            "intake": intake,
            "course_description": "",
            "entry_requirements": entry_req[:500] if entry_req else "",
            "source": "register",
            "note": "CSV-only",
        })
    
    if not rows:
        # Fallback: use CRICOS data directly
        print(f"  ⚠️  No course data found on website, using CRICOS register")
        for cc in cricos_courses:
            rows.append({
                "cricos": cc["cricos"],
                "title": cc["title"],
                "url": intl_url,
                "course_duration_per_week": cc["duration_weeks"],
                "offshore_tuition_fee": clean_numeric_fee(cc["fee_total"]) if clean_numeric_fee(cc["fee_total"]) != "NULL" else "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(cc["non_tuition_fee"]) if clean_numeric_fee(cc["non_tuition_fee"]) != "NULL" else "",
                "materials_fee": "",
                "intake": intake,
                "course_description": "",
                "entry_requirements": entry_req[:500] if entry_req else "",
                "source": "register",
                "note": "",
            })
    
    print(f"  Total courses: {len(rows)}")
    return rows, intake, entry_req


def extract_fees_from_page(soup, text):
    """Try to find fee information from the page."""
    fees = {}
    
    # Look for fee-related text patterns
    # Annual tuition fees
    m = re.search(r"\$[\d,]+[\s]*per[\s]*annum|\$[\d,]+[\s]*\(per[\s]*annum\)|\$[\d,]+[\s]*p\.?a\.?", text, re.IGNORECASE)
    if m:
        fees["annual"] = m.group(0)
    
    # International tuition fee patterns
    m = re.search(r"(?:international|tuition|school)\s*(?:fee|fees|cost).*?\$([\d,]+)", text, re.IGNORECASE)
    if m:
        fees["tuition"] = "$" + m.group(1)
    
    # Find any tables that might contain fee data
    tables = soup.find_all("table")
    for table in tables:
        table_text = table.get_text().lower()
        if any(kw in table_text for kw in ["fee", "cost", "tuition", "international", "year", "annual"]):
            rows = table.find_all("tr")
            for tr in rows:
                cells = tr.find_all(["td", "th"])
                if len(cells) >= 2:
                    key = cells[0].get_text(strip=True)
                    val = cells[1].get_text(strip=True)
                    fees[key] = val
    
    return fees


def extract_intake_from_page(soup, text):
    """Find intake/intake dates from the page."""
    # Look for intake-related sections
    intake_section = soup.find(string=re.compile(r"intake|start\s*date|commencement|study\s*period|term\s*dates", re.IGNORECASE))
    
    months = find_intake_months(text)
    
    # Look for term dates or intake patterns
    term_matches = re.findall(r"(?:Term|Semester|Intake)\s*(\d)", text, re.IGNORECASE)
    
    if months:
        # Sort by calendar order
        ordered = [m for m in MONTH_ORDER if m in months]
        return ", ".join(ordered)
    elif term_matches:
        terms = sorted(set(term_matches))
        term_names = {"1": "Term 1 (Jan/Feb)", "2": "Term 2 (Apr/May)", 
                      "3": "Term 3 (Jul)", "4": "Term 4 (Oct)"}
        return ", ".join(term_names.get(t, f"Term {t}") for t in terms)
    else:
        # Check for mentions of February and July (common for Australian schools)
        found = []
        if re.search(r"february|feb\b", text, re.IGNORECASE):
            found.append("January")
        if re.search(r"july|jul\b", text, re.IGNORECASE):
            found.append("July")
        if found:
            return ", ".join(found)
        
        return "January, July"  # Default for Australian schools


def extract_entry_requirements(soup, text):
    """Find entry requirements text on the page."""
    req_sections = []
    
    # Look for headings containing 'entry requirement', 'admission', 'IELTS', 'AEAS'
    for heading in soup.find_all(["h2", "h3", "h4", "h5", "strong"]):
        h_text = heading.get_text(strip=True).lower()
        if any(kw in h_text for kw in ["entry requirement", "admission", "english", "language", 
                                        "ielts", "aeas", "academic requirement", "enrolment condition"]):
            # Get the content after this heading
            section_text = ""
            el = heading.next_sibling
            max_follow = 5
            while el and max_follow > 0:
                if hasattr(el, "get_text"):
                    section_text += el.get_text(strip=True) + " "
                el = el.next_sibling
                max_follow -= 1
            if section_text:
                req_sections.append(heading.get_text(strip=True) + ": " + section_text.strip())
    
    # Also find paragraphs with entry requirement keywords
    for p in soup.find_all("p"):
        p_text = p.get_text(strip=True).lower()
        if any(kw in p_text for kw in ["ielts", "aeas", "entry requirement", "english language proficiency",
                                        "academic records", "school report"]) and len(p.get_text(strip=True)) > 20:
            req_sections.append(p.get_text(strip=True))
    
    # Check for IELTS/AEAS mentions anywhere
    ielts_match = re.search(r"(?:IELTS|AEAS|English\s*(?:language|proficiency)).*?(?:score|test|level).*?(?:\d+\.?\d*|A\d|B\d)", text, re.IGNORECASE)
    if ielts_match and not req_sections:
        req_sections.append(ielts_match.group(0))
    
    return "\n\n".join(req_sections[:5]) if req_sections else ""


def find_courses_on_page(soup, text):
    """Try to extract course/program listings from the page."""
    courses = []
    
    # Look for tables that list courses with durations/fees
    tables = soup.find_all("table")
    for table in tables:
        table_text = table.get_text().lower()
        if any(kw in table_text for kw in ["course", "program", "year", "level", "primary", "secondary", "year"]) and \
           any(kw in table_text for kw in ["fee", "cost", "tuition", "duration", "age"]):
            rows = table.find_all("tr")
            headers = []
            for th in rows[0].find_all(["td", "th"]):
                headers.append(th.get_text(strip=True).lower())
            
            for tr in rows[1:]:
                cells = tr.find_all("td")
                if len(cells) >= 2:
                    course_info = {"title": "", "fee": "", "duration": "", "description": ""}
                    for i, cell in enumerate(cells):
                        cell_text = cell.get_text(strip=True)
                        if i < len(headers):
                            h = headers[i]
                            if any(kw in h for kw in ["program", "course", "year", "level"]):
                                course_info["title"] = cell_text
                            elif any(kw in h for kw in ["fee", "cost", "tuition"]):
                                course_info["fee"] = cell_text
                            elif any(kw in h for kw in ["duration", "length"]):
                                course_info["duration"] = cell_text
                    if course_info["title"]:
                        courses.append(course_info)
    
    # Look for lists/cards with course names
    if not courses:
        # Find year level mentions
        level_patterns = [
            r"(?:Prep(?:aratory)?\s*(?:Year|–|-|to)\s*\d)",
            r"(?:Year\s*\d+\s*(?:–|-|to)\s*Year\s*\d+)",
            r"(?:Years?\s*\d+\s*(?:–|-|to|and)\s*\d+)",
            r"(?:Primary\s*(?:School|Years?|–|to))",
            r"(?:Secondary\s*(?:School|Years?|–|to))",
            r"(?:Senior\s*(?:School|Years?|Secondary))",
            r"(?:Junior\s*(?:School|Years?|Secondary))",
            r"(?:Early\s*(?:Learning|Years?))",
            r"(?:Foundation|Kindergarten|Prep)",
        ]
        
        found_levels = set()
        for pat in level_patterns:
            for m in re.finditer(pat, text, re.IGNORECASE):
                found_levels.add(m.group(0).strip())
        
        # Common K-12 course structure
        known_courses = [
            "Early Learning Centre / Kindergarten",
            "Primary School (Prep - Year 6)",
            "Primary School (Prep - Year 5)",
            "Primary School (Prep - Year 4)",
            "Junior Secondary (Years 7-10)",
            "Senior Secondary (Years 10-12)",
            "Senior Secondary (Years 11-12)",
            "Secondary School (Years 7-12)",
            "Secondary School (Years 7-10)",
            "Secondary School (Years 10-12)",
            "Junior School (Years 7-9)",
            "Middle School (Years 9-10)",
            "VCE / HSC Program",
            "International Baccalaureate (IB)",
            "Foundation Studies",
        ]
        
        page_text_lower = text.lower()
        for course_name in known_courses:
            if course_name.lower() in page_text_lower:
                courses.append({"title": course_name, "fee": "", "duration": "", "description": ""})
        
        # If found levels, try to construct course names
        if found_levels and not courses:
            for lev in sorted(found_levels):
                courses.append({"title": lev, "fee": "", "duration": "", "description": ""})
    
    return courses


def get_school_dir(prov):
    """Get or create the output directory for a school."""
    dir_name = prov["name"]
    dir_path = BASE_DIR / dir_name
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def generate_outputs(prov, rows, intake_text, entry_req_text):
    """Generate XLSX and SQL output files."""
    slug = prov["slug"]
    code = prov["code"]
    name = prov["name"]
    out_dir = get_school_dir(prov)
    
    xlsx_path = out_dir / f"{slug}_webscrape.xlsx"
    sql_path = out_dir / f"{slug}_webscrape_courses_update.sql"
    
    # Deduplicate by CRICOS code
    seen = {}
    for r in rows:
        key = r["cricos"] or r["title"]
        if key not in seen:
            seen[key] = r
    
    deduped = list(seen.values())
    
    # ---- Generate XLSX ----
    df_data = []
    for r in deduped:
        df_data.append({
            "cricos": r["cricos"],
            "course_title": r["title"],
            "url": r["url"],
            "course_duration_per_week": r["course_duration_per_week"],
            "offshore_tuition_fee": r["offshore_tuition_fee"] if r["offshore_tuition_fee"] != "NULL" else "",
            "onshore_tuition_fee": r["onshore_tuition_fee"] if r["onshore_tuition_fee"] != "NULL" else "",
            "enrolment_fee": r["enrolment_fee"] if r["enrolment_fee"] != "NULL" else "",
            "materials_fee": r["materials_fee"] if r["materials_fee"] != "NULL" else "",
            "intake": r["intake"] or intake_text,
            "course_description": r["course_description"][:200] if r["course_description"] else "",
            "entry_requirements": r["entry_requirements"][:300] if r["entry_requirements"] else entry_req_text[:300],
            "source": r["source"],
        })
    
    if not df_data:
        # Write empty placeholder
        df_data.append({
            "cricos": "", "course_title": "No courses found", "url": "",
            "course_duration_per_week": "", "offshore_tuition_fee": "",
            "onshore_tuition_fee": "", "enrolment_fee": "", "materials_fee": "",
            "intake": intake_text, "course_description": "", "entry_requirements": "",
            "source": "",
        })
    
    df = pd.DataFrame(df_data)
    df.to_excel(xlsx_path, index=False)
    print(f"  ✅ XLSX -> {xlsx_path.name}")
    
    # ---- Generate SQL ----
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(f"-- {name} ({code}) - Web-scraped course data\n")
        f.write(f"-- Generated: from {prov['url']}\n\n")
        f.write("-- Update provider institution details\n")
        f.write(f"UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_text}',\n"
                f"    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{code}';\n\n")
        
        emitted = set()
        for r in deduped:
            cricos = r["cricos"]
            if not cricos or cricos in emitted:
                continue
            emitted.add(cricos)
            
            dur = str(r["course_duration_per_week"]) if r["course_duration_per_week"] else "NULL"
            offshore = clean_numeric_fee(r["offshore_tuition_fee"]) if r.get("offshore_tuition_fee") else "NULL"
            onshore = clean_numeric_fee(r["onshore_tuition_fee"]) if r.get("onshore_tuition_fee") else "NULL"
            enrol = clean_numeric_fee(r["enrolment_fee"]) if r.get("enrolment_fee") else "NULL"
            mat = clean_numeric_fee(r["materials_fee"]) if r.get("materials_fee") else "NULL"
            
            entry_req_sql = (r["entry_requirements"] or "").replace("'", "''")
            desc_sql = (r.get("course_description") or "").replace("'", "''")
            
            f.write(f"UPDATE courses SET\n")
            f.write(f"    course_duration_per_week = {dur},\n")
            f.write(f"    offshore_tuition_fee = {offshore},\n")
            f.write(f"    onshore_tuition_fee = {onshore},\n")
            f.write(f"    enrolment_fee = {enrol},\n")
            f.write(f"    materials_fee = {mat},\n")
            f.write(f"    entry_requirements = '{entry_req_sql[:500]}',\n")
            f.write(f"    apply_form = '',\n")
            f.write(f"    updated_at = NOW()\n")
            f.write(f"WHERE cricos_course_code = '{cricos}';\n\n")
    
    print(f"  ✅ SQL  -> {sql_path.name}")
    print(f"  ✅ {len(emitted)} courses processed. Intake: {intake_text}")


def main():
    print(f"Grammar Schools Web Scraper")
    print(f"{'='*55}")
    print(f"Providers: {len(PROVIDERS)}")
    
    for prov in PROVIDERS:
        try:
            rows, intake_text, entry_req_text = scrape_school(prov)
            generate_outputs(prov, rows, intake_text, entry_req_text)
        except Exception as e:
            print(f"  ❌ Error scraping {prov['name']}: {e}")
            import traceback
            traceback.print_exc()
            # Still try to produce outputs with CRICOS data
            try:
                slug = prov["slug"]
                out_dir = get_school_dir(prov)
                code = prov["code"]
                name = prov["name"]
                
                # Read CRICOS data
                cricos_courses = []
                if REGISTER_CSV.exists():
                    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
                        for r in csv.DictReader(f):
                            if r["CRICOS Provider Code"].strip() != code:
                                continue
                            if r["Expired"].strip().lower() == "yes":
                                continue
                            dur_str = re.sub(r"[^\d]", "", r.get("Duration (Weeks)", "") or "")
                            fee_str = r.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")
                            nt_str = r.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
                            cricos_courses.append({
                                "cricos": r["CRICOS Course Code"].strip(),
                                "title": r["Course Name"].strip(),
                                "duration_weeks": int(dur_str) if dur_str.isdigit() else "",
                                "fee_total": fee_str,
                                "non_tuition_fee": nt_str,
                            })
                
                rows = []
                for cc in cricos_courses:
                    rows.append({
                        "cricos": cc["cricos"],
                        "title": cc["title"],
                        "url": prov["url"],
                        "course_duration_per_week": cc["duration_weeks"],
                        "offshore_tuition_fee": clean_numeric_fee(cc["fee_total"]) if clean_numeric_fee(cc["fee_total"]) != "NULL" else "",
                        "onshore_tuition_fee": "",
                        "enrolment_fee": clean_numeric_fee(cc["non_tuition_fee"]) if clean_numeric_fee(cc["non_tuition_fee"]) != "NULL" else "",
                        "materials_fee": "",
                        "intake": "January, July",
                        "course_description": "",
                        "entry_requirements": "",
                        "source": "register",
                        "note": "Fallback - scrape error",
                    })
                
                generate_outputs(prov, rows, "January, July", "")
            except Exception as e2:
                print(f"  ❌ Also failed fallback for {name}: {e2}")
    
    print(f"\n{'='*55}")
    print(f"All done!\n")


if __name__ == "__main__":
    main()
