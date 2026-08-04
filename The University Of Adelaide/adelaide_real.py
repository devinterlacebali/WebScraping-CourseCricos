import os
import re
import sys
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Ensure correct terminal output encoding for Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- Paths & Constants ---
_ROOT = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(_ROOT, "Book1.xlsx")
OUTPUT_SQL = os.path.join(_ROOT, "adelaide_update.sql")
OUTPUT_EXCEL = os.path.join(_ROOT, "adelaide_scraped_all.xlsx")

# Import ai_formatter if available
sys.path.append(os.path.dirname(_ROOT))
try:
    from ai_formatter import format_requirements
except ImportError:
    def format_requirements(text):
        return ""

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- Helper Functions ---
def clean_html(html: str) -> str:
    if not html:
        return ""
    # Replaces single quotes with double single quotes for SQL insertion
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

def num_fee(val):
    if not val:
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v:
        return "NULL"
    try:
        n = float(v)
        return str(int(n)) if n > 0 else "NULL"
    except ValueError:
        return "NULL"

def parse_weeks_from_duration(duration_text):
    if not duration_text:
        return "NULL"
    # Search for years (e.g. 3 years, 3 year(s), 1.5 years)
    m = re.search(r"([\d.]+)\s*year", duration_text, re.I)
    if m:
        try:
            years = float(m.group(1))
            return str(int(round(years * 52)))
        except ValueError:
            pass
    # Search for months (e.g. 18 months, 6 month)
    m = re.search(r"([\d.]+)\s*month", duration_text, re.I)
    if m:
        try:
            months = float(m.group(1))
            return str(int(round((months / 12) * 52)))
        except ValueError:
            pass
    return "NULL"

def build_legacy_mapping():
    """Build a mapping of course titles to legacy UofA CRICOS codes."""
    print("🔍 Building legacy UofA mapping...")
    url_to_cricos = {}
    sql_path = os.path.join(_ROOT, "adelaide_update.sql")
    if os.path.exists(sql_path):
        try:
            with open(sql_path, "r", encoding="utf-8") as f:
                content = f.read()
            statements = re.findall(
                r"UPDATE\s+courses\s+SET.*?apply_form\s*=\s*'([^'\n]+)'.*?WHERE\s+cricos_course_code\s*=\s*'([^'\n]+)';",
                content,
                re.DOTALL
            )
            for url, cricos in statements:
                url_to_cricos[url.strip()] = cricos.strip()
            print(f"  Loaded {len(url_to_cricos)} entries from existing SQL update file.")
        except Exception as e:
            print(f"  ⚠️ Error parsing SQL mapping: {e}")

    name_to_url = {}
    csv_path = os.path.join(os.path.dirname(_ROOT), "Adelaide University", "adelaide.csv")
    if os.path.exists(csv_path):
        try:
            df_csv = pd.read_csv(csv_path)
            for row in df_csv.values:
                if pd.notna(row[1]):
                    url = str(row[1]).strip()
                    name = str(row[0]).strip()
                    name_to_url[name] = url
            print(f"  Loaded {len(name_to_url)} entries from adelaide.csv.")
        except Exception as e:
            print(f"  ⚠️ Error parsing CSV mapping: {e}")

    cricos_db = {}
    cricos_path = os.path.join(os.path.dirname(_ROOT), "cricos-courses.csv")
    if os.path.exists(cricos_path):
        try:
            df_c = pd.read_csv(cricos_path, dtype=str)
            uofa_courses = df_c[df_c['CRICOS Provider Code'] == '00123M'][['CRICOS Course Code', 'Course Name']].dropna()
            for row in uofa_courses.values:
                code = str(row[0]).strip()
                name = str(row[1]).strip()
                norm_name = re.sub(r'[^a-z0-9]', '', name.lower())
                cricos_db[norm_name] = code
            print(f"  Loaded {len(cricos_db)} legacy UofA courses from cricos-courses.csv.")
        except Exception as e:
            print(f"  ⚠️ Error parsing cricos-courses.csv: {e}")

    name_to_cricos = {}
    for name, url in name_to_url.items():
        slug = os.path.basename(url)
        df_url = f"https://www.adelaide.edu.au/degree-finder/2025/{slug}.html"
        
        cricos_code = None
        if df_url in url_to_cricos:
            cricos_code = url_to_cricos[df_url]
        elif url in url_to_cricos:
            cricos_code = url_to_cricos[url]
            
        if cricos_code:
            name_to_cricos[name] = cricos_code
        else:
            norm = re.sub(r'[^a-z0-9]', '', name.lower())
            if norm in cricos_db:
                name_to_cricos[name] = cricos_db[norm]

    # Add all remaining cricos-courses.csv mappings
    for norm_name, code in cricos_db.items():
        if norm_name not in name_to_cricos:
            name_to_cricos[norm_name] = code

    pretty_to_cricos = {name: code for name, code in name_to_cricos.items() if not name.islower()}
    print(f"  Successfully compiled mapping. Total unique pretty courses: {len(pretty_to_cricos)}")
    return pretty_to_cricos, cricos_db

def find_legacy_cricos(scraped_title, pretty_to_cricos, cricos_db):
    if not scraped_title:
        return None
    
    # 1. Normalize scraped title
    scraped_norm = re.sub(r'[^a-z0-9]', '', scraped_title.lower())
    
    # 2. Try exact match on pretty names normalized
    for pretty_name, code in pretty_to_cricos.items():
        if re.sub(r'[^a-z0-9]', '', pretty_name.lower()) == scraped_norm:
            return code
            
    # 3. Try match on cricos_db directly
    if scraped_norm in cricos_db:
        return cricos_db[scraped_norm]
        
    # 4. Fuzzy match: Check if names without "(Honours)" or "Honours" or "Honors" match
    clean_scraped = re.sub(r'\b(honours|honors|advanced)\b', '', scraped_title.lower())
    clean_scraped_norm = re.sub(r'[^a-z0-9]', '', clean_scraped)
    
    for pretty_name, code in pretty_to_cricos.items():
        clean_pretty = re.sub(r'\b(honours|honors|advanced)\b', '', pretty_name.lower())
        if re.sub(r'[^a-z0-9]', '', clean_pretty) == clean_scraped_norm:
            return code
            
    for norm_name, code in cricos_db.items():
        clean_norm = re.sub(r'\b(honours|honors|advanced)\b', '', norm_name)
        if clean_norm == clean_scraped_norm:
            return code
            
    # 5. Word set match (for ordering differences: e.g. "Engineering (Chemical)" vs "Chemical Engineering")
    scraped_words = set(re.findall(r'\b[a-z]{3,}\b', scraped_title.lower()))
    scraped_words.discard("honours")
    scraped_words.discard("honors")
    scraped_words.discard("advanced")
    
    if len(scraped_words) >= 2:
        for pretty_name, code in pretty_to_cricos.items():
            pretty_words = set(re.findall(r'\b[a-z]{3,}\b', pretty_name.lower()))
            pretty_words.discard("honours")
            pretty_words.discard("honors")
            pretty_words.discard("advanced")
            if scraped_words == pretty_words:
                return code
                
    return None

def slug_matches_legacy(url, pretty_to_cricos, cricos_db):
    """Fuzzy check on URL slug to avoid fetching non-UofA pages."""
    slug = os.path.basename(url.rstrip("/"))
    slug_norm = re.sub(r'[^a-z0-9]', '', slug.lower())
    
    # Check exact match
    if slug_norm in cricos_db:
        return True
        
    for pretty_name in pretty_to_cricos.keys():
        if re.sub(r'[^a-z0-9]', '', pretty_name.lower()) == slug_norm:
            return True
            
    # Check fuzzy match
    clean_slug = re.sub(r'\b(honours|honors|advanced)\b', '', slug.lower())
    clean_slug_norm = re.sub(r'[^a-z0-9]', '', clean_slug)
    
    for pretty_name in pretty_to_cricos.keys():
        clean_pretty = re.sub(r'\b(honours|honors|advanced)\b', '', pretty_name.lower())
        if re.sub(r'[^a-z0-9]', '', clean_pretty) == clean_slug_norm:
            return True
            
    # Word set match
    slug_words = set(re.findall(r'\b[a-z]{3,}\b', slug.lower()))
    slug_words.discard("honours")
    slug_words.discard("honors")
    slug_words.discard("advanced")
    
    if len(slug_words) >= 2:
        for pretty_name in pretty_to_cricos.keys():
            pretty_words = set(re.findall(r'\b[a-z]{3,}\b', pretty_name.lower()))
            pretty_words.discard("honours")
            pretty_words.discard("honors")
            pretty_words.discard("advanced")
            if slug_words == pretty_words:
                return True
                
    return False

def scrape_course_page(url):
    """Scrape course details from the given URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    int_url = url.rstrip("/") + "/int/"
    html = ""
    target_url = int_url
    
    try:
        r = requests.get(int_url, headers=headers, timeout=20)
        if r.status_code == 200:
            html = r.text
        else:
            # Fallback to domestic
            dom_url = url.rstrip("/") + "/dom/"
            target_url = dom_url
            r = requests.get(dom_url, headers=headers, timeout=20)
            if r.status_code == 200:
                html = r.text
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None

    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")
    
    # --- 1. Course Title ---
    title = ""
    title_el = soup.find("h1")
    if title_el:
        title = title_el.get_text(strip=True)

    # --- 2. Overview / Description ---
    course_description = ""
    overview = soup.find("h3", string=re.compile(r"^\s*Overview\s*$", re.I))
    if overview:
        paragraphs = []
        for tag in overview.find_all_next():
            if tag.name == "h3" and tag.get_text(strip=True).lower() != "overview":
                break
            if tag.name == "p":
                paragraphs.append(str(tag))
        course_description = clean_html("".join(paragraphs))

    # --- 3. Entry Requirements ---
    entry_requirements = ""
    block = soup.select_one("div.block-content-wrapper")
    if not block:
        block = soup.select_one("div.entryrequirements")
    
    if block:
        raw_reqs = str(block)
        plain_text = block.get_text("\n").strip()
        ai_table = format_requirements(plain_text)
        entry_requirements = clean_html(ai_table if ai_table else raw_reqs)

    # --- 4. Duration ---
    total_course_duration = ""
    dur_span = soup.find("span", string=re.compile("year", re.I))
    if dur_span:
        total_course_duration = dur_span.get_text(strip=True)
    weeks = parse_weeks_from_duration(total_course_duration)

    # --- 5. Offshore Tuition Fee ---
    offshore_fee_str = ""
    fee_span = soup.select_one("div.degree-details-content-section-subtitle span")
    if fee_span and "$" in fee_span.get_text():
        offshore_fee_str = fee_span.get_text(strip=True)
    else:
        text_with_dollar = soup.find(string=re.compile(r"\$[0-9,]+"))
        if text_with_dollar:
            offshore_fee_str = text_with_dollar.strip()
    
    offshore_tuition_fee = num_fee(offshore_fee_str)

    # --- 6. Intake Months ---
    intake_months = []
    text_content = soup.get_text()
    for month in MONTH_ORDER:
        if re.search(rf"\b{month}\b", text_content, re.I):
            intake_months.append(month)

    return {
        "title": title,
        "course_description": course_description,
        "entry_requirements": entry_requirements,
        "total_course_duration": total_course_duration,
        "course_duration_per_week": weeks,
        "offshore_tuition_fee": offshore_tuition_fee,
        "apply_form": url,
        "intake_months": intake_months
    }

def main():
    pretty_to_cricos, cricos_db = build_legacy_mapping()

    print(f"📖 Reading driver file: {INPUT_FILE}")
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: driver spreadsheet {INPUT_FILE} not found!")
        sys.exit(1)
        
    df = pd.read_excel(INPUT_FILE)
    if "link" not in df.columns:
        print("❌ Error: 'link' column not found in spreadsheet!")
        sys.exit(1)

    urls = df["link"].dropna().unique().tolist()
    print(f"Loaded {len(urls)} URLs from driver file.")

    # Apply pre-filtering to avoid unnecessary requests
    filtered_urls = []
    print("🔍 Filtering URLs by legacy slug/name matching...")
    for url in urls:
        if slug_matches_legacy(url, pretty_to_cricos, cricos_db):
            filtered_urls.append(url)
    
    print(f"Filtered {len(urls)} URLs down to {len(filtered_urls)} relevant UofA legacy courses.")

    results = []
    emitted = set()

    for idx, url in enumerate(filtered_urls, 1):
        print(f"[{idx}/{len(filtered_urls)}] Scraping: {url}")
        res = scrape_course_page(url)
        if not res:
            print("  ⚠️ Scrape failed")
            continue

        title = res["title"]
        legacy_cricos = find_legacy_cricos(title, pretty_to_cricos, cricos_db)
        
        if not legacy_cricos:
            print(f"  ℹ️ Course '{title}' does not map to legacy UofA. Skipped.")
            continue

        res["legacy_cricos"] = legacy_cricos
        results.append(res)
        print(f"  ✅ Mapped: '{title}' -> Legacy CRICOS: {legacy_cricos} | Fee: {res['offshore_tuition_fee']} | Duration: {res['total_course_duration']}")
        
        # Polite delay to not overload server
        time.sleep(0.5)

    if not results:
        print("❌ No legacy UofA course data could be matched/scraped!")
        sys.exit(1)

    # --- Write SQL Updates ---
    print(f"💾 Writing SQL update queries: {OUTPUT_SQL}")
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write("-- The University Of Adelaide (UofA) legacy course updates\n\n")
        for r in results:
            cricos = r["legacy_cricos"]
            if cricos in emitted:
                continue
            emitted.add(cricos)
            
            f.write(f"-- Course: {r['title']} ({cricos})\n")
            f.write("UPDATE courses SET\n")
            f.write(f"    course_description = '{r['course_description']}',\n")
            
            weeks_val = r['course_duration_per_week']
            f.write(f"    course_duration_per_week = {weeks_val},\n")
            f.write(f"    total_course_duration = '{r['total_course_duration']}',\n")
            
            fee_val = r['offshore_tuition_fee']
            f.write(f"    offshore_tuition_fee = {fee_val},\n")
            f.write("    onshore_tuition_fee = NULL,\n")
            f.write(f"    entry_requirements = '{r['entry_requirements']}',\n")
            f.write(f"    apply_form = '{r['apply_form']}',\n")
            f.write("    updated_at = NOW()\n")
            f.write(f"WHERE cricos_course_code = '{cricos}';\n\n")

    # --- Write Excel Output ---
    print(f"💾 Saving enriched results: {OUTPUT_EXCEL}")
    excel_rows = []
    for r in results:
        excel_rows.append({
            "cricos": r["legacy_cricos"],
            "title": r["title"],
            "url": r["apply_form"],
            "course_duration_per_week": r["course_duration_per_week"] if r["course_duration_per_week"] != "NULL" else "",
            "offshore_tuition_fee": r["offshore_tuition_fee"] if r["offshore_tuition_fee"] != "NULL" else "",
            "intake": ", ".join(r["intake_months"]),
            "course_description": r["course_description"].replace("''", "'"),
            "entry_requirements": r["entry_requirements"].replace("''", "'"),
            "note": "Scraped from Adelaide Uni merged portal for legacy UofA mapping"
        })
    df_out = pd.DataFrame(excel_rows)
    df_out.to_excel(OUTPUT_EXCEL, index=False)

    print(f"\n🎉 Scrape finished successfully!")
    print(f"   - Total courses processed: {len(emitted)}")
    print(f"   - SQL Update Script: {OUTPUT_SQL}")
    print(f"   - Excel Spreadsheet: {OUTPUT_EXCEL}")

if __name__ == "__main__":
    main()
