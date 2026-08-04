"""Mass SA/WA/NT CRICOS Provider Web Scraper.
Visits websites to extract fee/duration/entry/intake data for ALL remaining SA/WA/NT providers.
Generates {slug}_webscrape.xlsx and {slug}_webscrape_courses_update.sql per provider.
"""
import os, re, sys, csv, json, time
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

try:
    import requests
except:
    os.system(f"{sys.executable} -m pip install requests beautifulsoup4 openpyxl lxml")
    import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
REGISTER_CSV = BASE_DIR / "cricos-courses.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

MONTH_ORDER = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]

# ============================================================
# PROVIDER DATA - All SA/WA/NT providers that need scraping
# ============================================================
# Format: (code, name, slug, website, intl_paths[], state, provider_type)
PROVIDERS = [
    # ==== SA GRAMMAR/PRIVATE SCHOOLS ====
    ("02485B", "Blackfriars Priory School", "blackfriars-priory",
     "https://www.blackfriars.sa.edu.au", ["/enrolment/international", "/international-students", "/fees"], "SA", "school"),
    ("00629G", "Loreto College", "loreto-college-sa",
     "https://www.loreto.sa.edu.au", ["/enrolment/international-students", "/international/", "/fees"], "SA", "school"),
    ("01611J", "Prescott College", "prescott-college",
     "https://www.prescott.sa.edu.au", ["/international-students", "/enrolments/international/", "/fees"], "SA", "school"),
    ("01536D", "Prescott College Southern", "prescott-southern",
     "https://www.prescott.sa.edu.au", ["/international-students", "/international/"], "SA", "school"),
    ("00603F", "Saint Ignatius' College", "saint-ignatius-college",
     "https://www.ignatius.sa.edu.au", ["/admissions/international", "/international-students", "/fees"], "SA", "school"),
    ("01102G", "St Dominic's Priory College", "st-dominics-priory",
     "https://stdominics.sa.edu.au", ["/international-students", "/enrolment/", "/fees"], "SA", "school"),
    ("01751G", "Tenison Woods College", "tenison-woods-college",
     "https://www.tenison.adl.catholic.edu.au", ["/international-students", "/enrolment/", "/fees"], "SA", "school"),
    ("01645K", "Woodcroft College", "woodcroft-college",
     "https://www.woodcroft.sa.edu.au", ["/enrolment/international-students", "/international/"], "SA", "school"),
    ("00628G", "Seymour College Inc", "seymour-college",
     "https://www.seymour.sa.edu.au", ["/admissions/international", "/enrolment/fees"], "SA", "school"),
    ("00602G", "Westminster School Inc", "westminster-school-sa",
     "https://www.westminster.sa.edu.au", ["/enrolment/international-students", "/international/"], "SA", "school"),
    ("00563J", "Walford Anglican School for Girls", "walford-school",
     "https://walford.net.au", ["/admissions/international", "/enrolment/"], "SA", "school"),
    ("02209M", "Our Lady of the Sacred Heart College", "olsh-college-sa",
     "https://www.olsh.catholic.edu.au", ["/international-students", "/enrolment/"], "SA", "school"),
    ("02799F", "St George College Inc", "st-george-college-sa",
     "https://www.sgc.sa.edu.au", ["/international", "/fees"], "SA", "school"),

    # ==== WA GRAMMAR/PRIVATE SCHOOLS ====
    ("02029D", "All Saints' College Inc.", "allsaints-college-wa",
     "https://www.allsaints.wa.edu.au", ["/admissions/international-students", "/international/"], "WA", "school"),
    ("01688K", "Kennedy Baptist College Association Inc.", "kennedy-baptist",
     "https://www.kennedy.wa.edu.au", ["/international-students", "/enrolment/"], "WA", "school"),
    ("01855M", "Kingsway Christian Education Association Inc.", "kingsway-christian",
     "https://www.kingsway.wa.edu.au", ["/international-students", "/enrolment/"], "WA", "school"),
    ("01488G", "St Andrew's Grammar Inc.", "st-andrews-grammar",
     "https://www.sag.wa.edu.au", ["/international-students", "/enrolment/"], "WA", "school"),
    ("03719C", "St Stephen's School", "st-stephens-school",
     "https://www.ststephens.wa.edu.au", ["/admissions/international-students"], "WA", "school"),
    ("02527G", "The Moerlina School Inc.", "moerlina-school",
     "https://www.moerlina.wa.edu.au", ["/international", "/enrolment/"], "WA", "school"),
    ("01529C", "The Lake Joondalup Baptist College Inc", "lake-joondalup-baptist",
     "https://www.ljbc.wa.edu.au", ["/international-students", "/enrolment/"], "WA", "school"),
    ("01984B", "Rehoboth Christian School", "rehoboth-christian",
     "https://www.rehoboth.wa.edu.au", ["/enrolment/international", "/international/"], "WA", "school"),
    ("03370E", "Baris Education and Culture Foundation Limited", "fountain-college",
     "http://fountain.wa.edu.au", ["/international", "/fees"], "WA", "school"),
    ("02200J", "Victory Life International Bible Training Ctr", "victory-life",
     "www.vlibtc.wa.edu.au", ["/international", "/courses"], "WA", "school"),

    # ==== NT PROVIDERS ====
    ("00971D", "Haileybury Rendall School", "haileybury-rendall",
     "https://www.haileyburyrendall.com.au", ["/enrol/international/", "/international-students"], "NT", "school"),
    ("04033C", "Educate Australia Pty Ltd", "latitude-college",
     "https://www.latitude.edu.au", ["/international", "/courses"], "NT", "vet"),
    ("03920B", "Fox Endeavours Pty Ltd", "fox-endeavours",
     "http://www.fox.edu.au", ["/international-students", "/courses"], "NT", "vet"),
    ("03675K", "Alana Kaye Group Pty Ltd", "alana-kaye-group",
     "", [], "NT", "vet"),
    
    # ==== WA - ENGLISH LANGUAGE CENTRES ====
    ("00057E", "Alexander Language School", "alexander-language-school",
     "https://www.sgis.wa.edu.au", ["/international/english", "/courses"], "WA", "vet"),
    ("00061J", "Milner International College of English", "milner-english",
     "https://www.milner.wa.edu.au", ["/international/english", "/courses"], "WA", "vet"),
    ("02139J", "Language Links International Pty Ltd", "language-links",
     "https://www.languagelinks.wa.edu.au", ["/international-english", "/courses"], "WA", "vet"),
    ("03274E", "Sunset Coast International English School", "sunset-coast-english",
     "http://www.lexisenglish.com", ["/campuses/perth/", "/courses"], "WA", "vet"),
    
    # ==== WA - VET/TRAINING COLLEGES ====
    ("02042G", "Curtin College (WA)", "curtin-college",
     "https://www.curtincollege.edu.au", ["/international", "/fees"], "WA", "vet"),
    ("02898C", "Everthought College of Construction", "everthought-construction",
     "https://www.ecoc.edu.au", ["/international-students", "/courses"], "WA", "vet"),
    ("03564F", "Global College Australasia", "global-college-australasia",
     "https://www.globalcollege.edu.au", ["/international", "/courses"], "WA", "vet"),
    ("02645B", "AIWT Pty Ltd", "aiwt",
     "https://www.aiwt.edu.au", ["/international", "/courses"], "WA", "vet"),
    ("03255G", "Australian Professional Skills Institute", "apsi",
     "https://www.apsi.wa.edu.au", ["/international", "/courses"], "WA", "vet"),
    ("03548F", "Skills Australia Institute", "skills-australia",
     "http://www.skillsaustralia.edu.au/", ["/international", "/courses"], "WA", "vet"),
    
    # ==== SA - VET/TRAINING ====
    ("00092B", "TAFE SA", "tafe-sa",
     "https://www.tafesa.edu.au/international", ["/international", "/courses"], "SA", "vet"),
    ("00561M", "Eynesbury (Navitas)", "eynesbury",
     "https://www.eynesbury.navitas.com", ["/international", "/fees", "/courses"], "SA", "vet"),
    ("02193C", "SAIBT (SA Institute of Business & Tech)", "saibt",
     "http://www.saibt.sa.edu.au", ["/international", "/courses"], "SA", "vet"),
    ("02380M", "Le Cordon Bleu Australia", "le-cordon-bleu",
     "https://www.cordonbleu.edu/australia", ["/international", "/fees"], "SA", "vet"),
    ("02914G", "ICHM Pty Ltd", "ichm",
     "http://www.ichm.edu.au", ["/international", "/courses"], "SA", "vet"),
    
    # ==== TAFE WA (Department of Training & Workforce Development) ====
    ("00020G", "TAFE WA - Dept Training & Workforce Dev", "tafe-wa",
     "http://www.tafeinternational.wa.edu.au/", ["/international", "/courses"], "WA", "vet"),
    ("01723A", "Department of Education (WA Schools)", "dept-ed-wa",
     "https://www.tafeinternational.wa.edu.au", ["/international", "/schools"], "WA", "vet"),
    
    # ==== Additional small providers with websites ====
    ("04298M", "AICE Pty Ltd", "aice",
     "https://www.aice.edu.au/", ["/courses", "/international"], "WA", "vet"),
    ("04377A", "Aroha College Pty Ltd", "aroha-college",
     "www.arohacollege.com.au", ["/courses", "/international"], "WA", "vet"),
    ("03282E", "Perth College of Business & Tech (MVJ)", "pcbt-wa",
     "https://www.perthcollege.com.au", ["/international", "/courses"], "WA", "vet"),
    ("03953D", "Nithi College (Illoura)", "nithi-college",
     "https://www.illoura.edu.au", ["/courses", "/international"], "WA", "vet"),
    
    # ==== No website or likely no international page, CSV-only fallback ====
    ("04050B", "ABBI Educational Services Pty Ltd", "abbi",
     "", [], "SA", "csv-only"),
    ("03187D", "AUSTRA COLLEGE", "austra-college",
     "", [], "SA", "csv-only"),
    ("03753A", "Aspen Education Group Pty Ltd", "aspen-education",
     "", [], "SA", "csv-only"),
    ("04107A", "Atlas Education Pty Ltd", "atlas-education",
     "", [], "SA", "csv-only"),
    ("04032D", "Boston International Pty Ltd", "boston-international",
     "", [], "SA", "csv-only"),
    ("03857D", "Clayton Education Group Pty LTD", "clayton-education",
     "", [], "SA", "csv-only"),
    ("03818M", "Education Investors Pty Ltd", "education-investors",
     "", [], "SA", "csv-only"),
    ("03551M", "Golden Wattle Group Pty Ltd", "golden-wattle",
     "", [], "SA", "csv-only"),
    ("03928E", "Goldthorn International Pty Ltd", "goldthorn-international",
     "", [], "SA", "csv-only"),
    ("04363G", "Hessel Pty Ltd", "hessel",
     "", [], "SA", "csv-only"),
    ("03189B", "Jabin Hopkins Pty Ltd", "jabin-hopkins",
     "", [], "SA", "csv-only"),
    ("04314E", "Lotus Learning and Trades Pty Ltd", "lotus-learning",
     "", [], "SA", "csv-only"),
    ("04432K", "Optimum Training Academy Pty Ltd", "optimum-training",
     "", [], "SA", "csv-only"),
    ("03076M", "SALFORD COLLEGE PTY LTD", "salford-college",
     "", [], "SA", "csv-only"),
    ("03555G", "Swann International Pty Ltd", "swann-international",
     "", [], "SA", "csv-only"),
    ("03999A", "Woodstock International Pty Ltd", "woodstock-international",
     "", [], "SA", "csv-only"),
    ("03782G", "A.M.A. Services (W.A.) Pty Ltd", "ama-wa",
     "", [], "WA", "csv-only"),
    ("03997C", "ANZ College Pty Ltd", "anz-college",
     "", [], "WA", "csv-only"),
    ("03703M", "Apeiro Institute Pty Ltd", "apeiro-institute",
     "", [], "WA", "csv-only"),
    ("04055H", "Auscare Staffing Agency Pty Ltd", "auscare-staffing",
     "", [], "WA", "csv-only"),
    ("04278D", "CW EDUCATION GROUP PTY LTD", "cw-education",
     "", [], "WA", "csv-only"),
    ("03933H", "Contempo Education Pty Ltd", "contempo-education",
     "", [], "WA", "csv-only"),
    ("03910D", "Corporate Business Academy Pty Ltd", "cba-wa",
     "", [], "WA", "csv-only"),
    ("04212M", "ELPIS Education Pty Ltd", "elpis-education",
     "", [], "WA", "csv-only"),
    ("03839F", "Emma Wicks - Paradise Falls Trust", "paradise-falls",
     "", [], "WA", "csv-only"),
    ("04378M", "Greenhouse Education Pty Ltd", "greenhouse-education",
     "", [], "WA", "csv-only"),
    ("04346H", "Hampton College Pty Ltd", "hampton-college",
     "", [], "WA", "csv-only"),
    ("03901E", "Integrated Training Pty Ltd", "integrated-training",
     "", [], "WA", "csv-only"),
    ("03802G", "Major Blue Air Pty Ltd", "major-blue-air",
     "", [], "WA", "csv-only"),
    ("03956A", "Pioneer College Pty Ltd", "pioneer-college",
     "", [], "WA", "csv-only"),
    ("04224G", "School of Engineering Australia Pty Ltd", "soe-australia",
     "", [], "WA", "csv-only"),
    ("03945D", "The Bright College Pty Ltd", "bright-college",
     "", [], "WA", "csv-only"),
    ("04277E", "Western Business Group Pty Ltd", "western-business",
     "", [], "WA", "csv-only"),
    ("04213K", "AUCTUS Consulting Pty Ltd", "auctus-consulting",
     "", [], "SA", "csv-only"),
    ("01774A", "ASHT Pty Ltd", "asht-pty",
     "https://alliancecollege.edu.au/", ["/courses", "/international"], "SA", "vet"),
    ("03039E", "Ironwood Institute", "ironwood-institute",
     "https://www.ironwood.edu.au", ["/courses", "/international"], "SA", "vet"),
    ("03884A", "Skills Training College Pty Ltd", "skills-training-college",
     "", [], "SA", "csv-only"),
]


def fetch_html(url, timeout=20):
    """Fetch HTML with error handling."""
    if not url:
        return ""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text
    except Exception as e:
        return ""


def extract_text_from(html):
    """Extract clean text from HTML."""
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()
    return re.sub(r"\s+", " ", soup.get_text()).strip()


def find_intake(text):
    """Extract intake months from text."""
    months = {}
    for m in ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]:
        if m in text.lower():
            months[m.capitalize()] = True
    ordered = [m for m in MONTH_ORDER if m in months]
    return ", ".join(ordered) if ordered else "February, July"


def find_entry_reqs(text, provider_type="school"):
    """Extract entry requirements from text."""
    reqs = []
    # IELTS
    m = re.search(r"IELTS\s*(?:overall\s*)?(?:score\s*)?(\d+\.?\d*)", text, re.IGNORECASE)
    if m:
        reqs.append(f"IELTS {m.group(1)} overall")
    elif "ielts" in text.lower():
        reqs.append("IELTS required")
    # AEAS
    if "AEAS" in text:
        reqs.append("AEAS test required")
    # Academic
    if "academic" in text.lower() and ("requirement" in text.lower() or "entry" in text.lower()):
        reqs.append("Academic entry requirements apply")
    if not reqs:
        if provider_type == "school":
            return "Contact school for entry requirements. AEAS test and/or interview may be required."
        else:
            return "Contact provider for entry requirements"
    return ". ".join(reqs) + "."


def clean_fee(val):
    """Clean fee value - returns 'NULL' or numeric string."""
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-"):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v:
        return "NULL"
    try:
        n = float(v)
        return str(int(n)) if n >= 100 else "NULL"
    except ValueError:
        return "NULL"


def process_provider(prov):
    """Process one provider: visit website, extract data, generate outputs."""
    code, name, slug, website, intl_paths, state, ptype = prov
    provider_dir = BASE_DIR / name
    provider_dir.mkdir(parents=True, exist_ok=True)
    
    xlsx_path = provider_dir / f"{slug}_webscrape.xlsx"
    sql_path = provider_dir / f"{slug}_webscrape_courses_update.sql"
    
    # Load CSV register for this provider
    courses = []
    total_fee_est = 0
    if REGISTER_CSV.exists():
        with open(REGISTER_CSV, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r["CRICOS Provider Code"].strip() != code:
                    continue
                if r["Expired"].strip().lower() == "yes":
                    continue
                dur_str = re.sub(r"[^\d]", "", r.get("Duration (Weeks)") or "")
                dur = int(dur_str) if dur_str.isdigit() else 0
                fee_str = r.get("Tuition Fee", "").strip().replace("$","").replace(",","")
                nt_str = r.get("Non Tuition Fee", "").strip().replace("$","").replace(",","")
                total_str = r.get("Estimated Total Course Cost", "").strip().replace("$","").replace(",","")
                try:
                    total_fee = int(float(total_str)) if total_str else 0
                except:
                    total_fee = 0
                total_fee_est = max(total_fee_est, total_fee)
                courses.append({
                    "cricos": r["CRICOS Course Code"].strip(),
                    "title": r["Course Name"].strip(),
                    "duration": dur,
                    "fee": fee_str,
                    "non_tuition": nt_str,
                    "total": total_str,
                })
    
    print(f"  {name} ({code}): {len(courses)} courses")
    if not courses:
        print(f"    ⚠️  No active courses - skipping")
        return
    
    # Try to scrape website
    html = ""
    found_url = ""
    if ptype != "csv-only" and website:
        # Try the intl_paths
        for path in intl_paths:
            url = website.rstrip("/") + path
            h = fetch_html(url)
            if h and len(h) > 500:
                html = h
                found_url = url
                print(f"    ✅ Found: {url}")
                break
        # Try just the base URL
        if not html:
            h = fetch_html(website)
            if h and len(h) > 500:
                html = h
                found_url = website
                print(f"    ✅ Base URL: {website}")
    elif ptype == "csv-only" and website:
        # Try base URL anyway
        h = fetch_html(website)
        if h and len(h) > 500:
            html = h
            found_url = website
            print(f"    ✅ Base URL (csv-only): {website}")
    
    if not html:
        print(f"    ⚠️  No page found, using CSV data only")
    
    # Parse text
    text = extract_text_from(html) if html else ""
    intake = find_intake(text) if text else "February, July"
    entry_req = find_entry_reqs(text, ptype) if text else ("Contact provider for entry requirements" if ptype != "csv-only" else "")

    # Build rows
    rows = []
    for c in courses:
        # Try to extract fee from website text (look near course name)
        website_fee = ""
        if text:
            # Find fee amount near course name
            course_name_short = re.sub(r"[^a-z0-9\s]", "", c["title"].lower())[:40]
            if course_name_short in text.lower():
                idx = text.lower().find(course_name_short)
                chunk = text[idx:idx+2000]
                amounts = re.findall(r"\$([\d,]+(?:\.\d{2})?)", chunk)
                if amounts:
                    for amt in amounts:
                        try:
                            a = float(amt.replace(",",""))
                            if 1000 < a < 200000:
                                website_fee = str(int(a))
                                break
                        except:
                            pass
        
        fee_val = clean_fee(website_fee) if website_fee else clean_fee(c["fee"])
        nt_val = clean_fee(c["non_tuition"])
        
        row = {
            "cricos": c["cricos"],
            "title": c["title"],
            "url": found_url,
            "course_duration_per_week": c["duration"],
            "offshore_tuition_fee": fee_val if fee_val != "NULL" else "",
            "onshore_tuition_fee": "",
            "enrolment_fee": nt_val if nt_val != "NULL" else "",
            "materials_fee": "",
            "intake": intake,
            "course_description": "",
            "entry_requirements": entry_req[:500],
            "source": "website" if html else "register",
            "note": "",
        }
        rows.append(row)
    
    # Generate XLSX
    try:
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Courses"
        headers = ["cricos","title","url","course_duration_per_week","offshore_tuition_fee",
                    "onshore_tuition_fee","enrolment_fee","materials_fee","intake",
                    "course_description","entry_requirements","source","note"]
        ws.append(headers)
        for r in rows:
            ws.append([r[h] for h in headers])
        wb.save(xlsx_path)
        print(f"    ✅ XLSX: {xlsx_path.name}")
    except Exception as e:
        print(f"    ❌ XLSX error: {e}")
    
    # Generate SQL
    try:
        with open(sql_path, "w", encoding="utf-8") as f:
            f.write(f"-- {name} ({code}) - Webscrape Update\n")
            f.write(f"UPDATE provider_institution SET intake_date='{intake}', updated_at=NOW() WHERE cricos_provider_code='{code}';\n\n")
            
            emitted = set()
            for r in rows:
                cricos = r["cricos"]
                if not cricos or not re.match(r'^\d{6,7}[A-Za-z]?$', str(cricos)):
                    f.write(f"-- ⚠️ Skipped (no CRICOS): {r['title']} | {r['url']}\n")
                    continue
                if cricos in emitted:
                    f.write(f"-- ⚠️ Skipped (CRICOS {cricos} already emitted): {r['title']}\n")
                    continue
                emitted.add(cricos)
                
                dur = r["course_duration_per_week"] if r["course_duration_per_week"] else "NULL"
                off = r["offshore_tuition_fee"] if r["offshore_tuition_fee"] else "NULL"
                onsh = r["onshore_tuition_fee"] if r["onshore_tuition_fee"] else "NULL"
                enf = r["enrolment_fee"] if r["enrolment_fee"] else "NULL"
                mat = r["materials_fee"] if r["materials_fee"] else "NULL"
                desc = r["course_description"].replace("'", "''")
                er = r["entry_requirements"].replace("'", "''")
                url = r["url"].replace("'", "''")
                
                f.write(f"UPDATE courses SET\n")
                f.write(f"    course_duration_per_week = {dur},\n")
                f.write(f"    offshore_tuition_fee = {off},\n")
                f.write(f"    onshore_tuition_fee = {onsh},\n")
                f.write(f"    enrolment_fee = {enf},\n")
                f.write(f"    materials_fee = {mat},\n")
                f.write(f"    course_description = '{desc}',\n")
                f.write(f"    entry_requirements = '{er}',\n")
                f.write(f"    apply_form = '{url}',\n")
                f.write(f"    updated_at = NOW()\n")
                f.write(f"WHERE cricos_course_code = '{cricos}';\n")
        
        print(f"    ✅ SQL: {sql_path.name} ({len(emitted)} courses)")
    except Exception as e:
        print(f"    ❌ SQL error: {e}")


def main():
    print("="*70)
    print("SA/WA/NT CRICOS Provider Web Scraper")
    print(f"Total providers: {len(PROVIDERS)}")
    print("="*70)
    
    # Check existing folders first
    skipped = 0
    processed = 0
    for prov in PROVIDERS:
        code, name, slug, website, intl_paths, state, ptype = prov
        provider_dir = BASE_DIR / name
        xlsx_path = provider_dir / f"{slug}_webscrape.xlsx"
        sql_path = provider_dir / f"{slug}_webscrape_courses_update.sql"
        
        if xlsx_path.exists() and sql_path.exists():
            print(f"  ⏭️  SKIP: {name} ({code}) - already has webscrape data")
            skipped += 1
            continue
        
        process_provider(prov)
        processed += 1
        time.sleep(1)  # Polite delay
    
    print(f"\n{'='*70}")
    print(f"Done! Processed: {processed}, Skipped (exists): {skipped}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
