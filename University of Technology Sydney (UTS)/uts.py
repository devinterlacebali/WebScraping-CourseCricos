import os
import re
import sys
import pandas as pd
from bs4 import BeautifulSoup
from scrapling.fetchers import Fetcher

# Configure standard encoding for Windows environment
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROVIDER_CODE = "00099F"
SLUG = "uts"
DIR = "University of Technology Sydney (UTS)"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December", "january": "January",
    "february": "February", "march": "March", "april": "April", "june": "June",
    "july": "July", "august": "August", "september": "September",
    "october": "October", "november": "November", "december": "December",
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

def clean_html(html_str: str) -> str:
    if not html_str:
        return ""
    html_str = re.sub(r"\s+", " ", html_str)
    return html_str.replace("'", "''").strip()

def clean_numeric_fee(val) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html_content: str) -> str:
    if not html_content:
        return ""
    frag = BeautifulSoup(html_content, "html.parser")
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    for t in frag.find_all("span"):
        t.unwrap()
    while True:
        div = frag.find("div")
        if div is None:
            break
        if div.find(["p", "ul", "ol", "li", "div", "table", "h5"]):
            div.unwrap()
        else:
            div.name = "p"
            
    for p in frag.find_all("p"):
        s = p.get_text(strip=True)
        if s.endswith(":") and len(s) < 60 and not p.find(["strong", "b", "a"]):
            p.string = ""
            strong = frag.new_tag("strong")
            strong.string = s
            p.append(strong)
            
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def months_in(text):
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", text):
        k = tok.lower()
        if k in MONTHS and MONTHS[k] not in found:
            found.append(MONTHS[k])
    return found

def extract_course_description(soup):
    desc_html = ""
    blocks = soup.find_all("li", class_="accordion__block")
    for b in blocks:
        btn = b.find("button", class_="accordion__btn")
        if btn and "course description" in btn.get_text().lower():
            content = b.find("div", class_="accordion__content")
            if content:
                desc_html = content.prettify()
                break
                
    if not desc_html:
        divs = soup.find_all("div", class_="wysiwyg-user-content-output")
        if divs:
            desc_html = "".join(str(d) for d in divs[:2])
            
    cleaned = sanitise(desc_html)
    if cleaned:
        return f"<h4>Overview</h4>{cleaned}"
    return ""

def extract_entry_requirements(soup):
    reqs_html = ""
    blocks = soup.find_all("li", class_="accordion__block")
    for b in blocks:
        btn = b.find("button", class_="accordion__btn")
        if btn and "admission requirements" in btn.get_text().lower():
            content = b.find("div", class_="accordion__content")
            if content:
                reqs_html = str(content)
                break
                
    if reqs_html:
        academic_reqs = sanitise(reqs_html)
    else:
        academic_reqs = "<p>Standard academic entry requirements apply. Please refer to the UTS website for details.</p>"
        
    english_reqs = "<ul><li>IELTS (Academic) score: 6.5 overall with a writing score of 6.0 (or equivalent).</li></ul>"
    
    table_html = (
        "<table><tbody>"
        f"<tr><td><strong>Academic Requirements</strong></td><td>{academic_reqs}</td></tr>"
        f"<tr><td><strong>English Proficiency</strong></td><td>{english_reqs}</td></tr>"
        "</tbody></table>"
    )
    return table_html

def extract_duration(soup):
    duration_text = ""
    for title_el in soup.find_all("h3", class_="keyFacts__itemsWrapper--title"):
        if "duration" in title_el.get_text().lower():
            parent_div = title_el.parent
            duration_text = parent_div.get_text(separator="\n").strip()
            break
            
    if not duration_text:
        for b in soup.find_all("li", class_="accordion__block"):
            btn = b.find("button", class_="accordion__btn")
            if btn and "course duration" in btn.get_text().lower():
                content = b.find("div", class_="accordion__content")
                if content:
                    duration_text = content.get_text().strip()
                    break
                    
    if not duration_text:
        return ""
        
    match = re.search(r"([0-9.]+)\s*year", duration_text, re.IGNORECASE)
    if match:
        years = float(match.group(1))
        return str(int(years * 52))
        
    match = re.search(r"([0-9.]+)\s*month", duration_text, re.IGNORECASE)
    if match:
        months = float(match.group(1))
        return str(int(months * 4.33))
        
    return ""

def extract_fees(soup_domestic, soup_intl):
    offshore = "NULL"
    onshore = "NULL"
    
    # 1. Offshore (International) Fee
    offshore_text = ""
    for title_el in soup_intl.find_all("h3", class_="keyFacts__itemsWrapper--title"):
        if "course fees" in title_el.get_text().lower():
            parent_div = title_el.parent
            offshore_text = parent_div.get_text(separator="\n").strip()
            break
            
    if not offshore_text or "international" not in offshore_text.lower():
        for b in soup_intl.find_all("li", class_="accordion__block"):
            btn = b.find("button", class_="accordion__btn")
            if btn and "international course fees" in btn.get_text().lower():
                content = b.find("div", class_="accordion__content")
                if content:
                    offshore_text = content.get_text().strip()
                    break
                    
    if offshore_text:
        amounts = re.findall(r"\$\s*([0-9,]+(?:\.[0-9]+)?)", offshore_text)
        if amounts:
            cleaned_amounts = [float(a.replace(",", "")) for a in amounts]
            offshore = str(int(max(cleaned_amounts)))
            
    # 2. Onshore (Domestic) Fee
    onshore_text = ""
    for title_el in soup_domestic.find_all("h3", class_="keyFacts__itemsWrapper--title"):
        if "course fees" in title_el.get_text().lower():
            parent_div = title_el.parent
            onshore_text = parent_div.get_text(separator="\n").strip()
            break
            
    if not onshore_text:
        for b in soup_domestic.find_all("li", class_="accordion__block"):
            btn = b.find("button", class_="accordion__btn")
            if btn and "domestic course fees" in btn.get_text().lower():
                content = b.find("div", class_="accordion__content")
                if content:
                    onshore_text = content.get_text().strip()
                    break
                    
    if onshore_text:
        amounts = re.findall(r"\$\s*([0-9,]+(?:\.[0-9]+)?)", onshore_text)
        if amounts:
            cleaned_amounts = [float(a.replace(",", "")) for a in amounts]
            onshore = str(int(max(cleaned_amounts)))
            
    return offshore, onshore, "NULL", "NULL"

def extract_intake_months(soup):
    intake_text = ""
    for title_el in soup.find_all("h3", class_="keyFacts__itemsWrapper--title"):
        if "intake" in title_el.get_text().lower():
            parent_div = title_el.parent
            intake_text = parent_div.get_text().strip()
            break
            
    if not intake_text:
        for b in soup.find_all("li", class_="accordion__block"):
            btn = b.find("button", class_="accordion__btn")
            if btn and "important dates" in btn.get_text().lower():
                content = b.find("div", class_="accordion__content")
                if content:
                    intake_text = content.get_text().strip()
                    break
                    
    months = []
    text_lower = intake_text.lower()
    if "autumn" in text_lower:
        months.append("February")
    if "spring" in text_lower:
        months.append("July")
    if "summer" in text_lower:
        months.append("November")
        
    for m in months_in(intake_text):
        if m not in months:
            months.append(m)
            
    if not months:
        months = ["February", "July"]
        
    return months

def extract_cricos(soup):
    text = soup.get_text()
    codes = re.findall(r"\b\d{6}[A-Z]\b", text)
    filtered_codes = [c for c in codes if c not in ("00099F", "00859D")]
    if filtered_codes:
        return filtered_codes[0]
        
    m = re.search(r"CRICOS\s*:\s*([0-9A-Z]{7,8})", text, re.IGNORECASE)
    if m:
        c = m.group(1).strip()
        if c not in ("00099F", "00859D"):
            return c
            
    return ""

def scrape_course(url):
    url = url.strip()
    d = {"cricos": "", "title": "", "url": url, "course_description": "",
         "course_duration_per_week": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": []}
    try:
        # Fetch 1: Domestic mode (to get domestic fees)
        page_domestic = Fetcher.get(url, stealthy_headers=True)
        soup_domestic = BeautifulSoup(page_domestic.html_content, "html.parser")
        
        # Fetch 2: International mode (via cookies)
        page_intl = Fetcher.get(url, cookies={"student-type": "international"}, stealthy_headers=True)
        soup_intl = BeautifulSoup(page_intl.html_content, "html.parser")
        
        # Title
        title_el = soup_intl.find("h1")
        title = title_el.get_text(strip=True) if title_el else "Unknown Course"
        d["title"] = title
        
        # CRICOS
        cricos = extract_cricos(soup_intl)
        d["cricos"] = cricos
        
        if not cricos:
            print(f"⚠️ Skipped (no CRICOS found): {title} | {url}")
            return d
            
        d["course_description"] = clean_html(extract_course_description(soup_intl))
        d["entry_requirements"] = clean_html(extract_entry_requirements(soup_intl))
        d["course_duration_per_week"] = extract_duration(soup_intl)
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], d["enrolment_fee"], d["materials_fee"] = extract_fees(soup_domestic, soup_intl)
        d["intake_months"] = extract_intake_months(soup_intl)
        
        print(f"✅ {cricos} | {title} | {url}")
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        
    return d

def main():
    os.makedirs(DIR, exist_ok=True)
    
    # 1. Discover all courses from sitemap
    sitemap_url = "https://www.uts.edu.au/sitemap.xml"
    print(f"Fetching sitemap {sitemap_url}...")
    try:
        r = Fetcher.get(sitemap_url, stealthy_headers=True)
        soup = BeautifulSoup(r.html_content, "xml")
        course_urls = []
        for loc in soup.find_all("loc"):
            u = loc.get_text().strip()
            if u.startswith("https://www.uts.edu.au/courses/") and u != "https://www.uts.edu.au/courses":
                course_urls.append(u)
        unique_urls = sorted(list(set(course_urls)))
        print(f"Discovered {len(unique_urls)} course URLs from sitemap.")
    except Exception as e:
        print(f"❌ Failed to fetch sitemap: {e}")
        return
        
    # 2. Scrape each discovered URL
    results = []
    for idx, url in enumerate(unique_urls):
        print(f"[{idx+1}/{len(unique_urls)}] ", end="")
        res = scrape_course(url)
        results.append(res)
        
    # 3. Compile intake dates union
    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)
    if not intake_date:
        intake_date = "February, July" # Fallback default
        
    # 4. Write SQL file
    print(f"Writing SQL queries to {SQL_PATH}...")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped (no/unreliable CRICOS course code): {d['title']} | {d['url']}\n\n")
                continue
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {clean_numeric_fee(d["offshore_tuition_fee"])},
    onshore_tuition_fee = {clean_numeric_fee(d["onshore_tuition_fee"])},
    enrolment_fee = {clean_numeric_fee(d["enrolment_fee"])},
    materials_fee = {clean_numeric_fee(d["materials_fee"])},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';\n\n""")

    # 5. Write Excel driver / enriched record
    print(f"Writing Excel sheet to {EXCEL_PATH}...")
    def cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]
        
    output_rows = []
    for d in results:
        # Keep only the rows that were not skipped to keep the driver clean, or include all rows
        output_rows.append({
            "cricos": d["cricos"],
            "title": d["title"],
            "url": d["url"],
            "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
            "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
            "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
            "enrolment_fee": cell(d["enrolment_fee"]),
            "materials_fee": cell(d["materials_fee"]),
            "intake": ", ".join(d["intake_months"]),
            "course_description": cell(d["course_description"]),
            "entry_requirements": cell(d["entry_requirements"]),
        })
        
    df_out = pd.DataFrame(output_rows)
    df_out.to_excel(EXCEL_PATH, index=False)
    
    print(f"\n✅ Finished. {len(results)} courses processed.")
    print(f"SQL update written to: {SQL_PATH}")
    print(f"Excel driver written to: {EXCEL_PATH}")

if __name__ == "__main__":
    main()
