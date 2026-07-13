import os
import re
import sys
import asyncio
import fitz  # PyMuPDF
import pandas as pd
from bs4 import BeautifulSoup
from curl_cffi import requests

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- constants -----------------------------------------
PROVIDER_CODE = "00092B"
SLUG = "tafesa"
DIR = "TAFE SA"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
PDF_URL = "https://www.tafesa.edu.au/docs/default-source/international-files/international-course-list.pdf?sfvrsn=72afc14_28"
PDF_PATH = f"{DIR}/international-course-list.pdf"

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

# Mappings for stale URLs in the PDF to their active counterpart pages
URL_OVERRIDES = {
    "https://www.tafesa.edu.au/xml/course/in/in_2026TP01256.aspx": "https://www.tafesa.edu.au/xml/course/in/in_2026TP01556.aspx",
    "https://www.tafesa.edu.au/xml/course/in/in_2022TP01257.aspx": "https://www.tafesa.edu.au/xml/course/in/in_2026TP01557.aspx",
    "https://www.tafesa.edu.au/xml/course/in/in_2026TP01330.aspx": "https://www.tafesa.edu.au/xml/course/in/in_2026TP01469.aspx"
}

# --- shared helpers -----------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

def clean_numeric_fee(val) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    try:
        n = float(v)
        return str(int(n)) if n.is_integer() else str(n)
    except:
        return "NULL"

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html: str) -> str:
    if not html:
        return ""
    frag = BeautifulSoup(html, "html.parser")
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

# --- download PDF --------------------------------------
def download_pdf():
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    if not os.path.exists(PDF_PATH):
        print(f"Downloading PDF from {PDF_URL}...")
        r = requests.get(PDF_URL, impersonate="chrome120")
        if r.status_code == 200:
            with open(PDF_PATH, "wb") as f:
                f.write(r.content)
            print("PDF downloaded successfully.")
        else:
            raise Exception(f"Failed to download PDF, status: {r.status_code}")

# --- discover courses from PDF -------------------------
def discover_courses():
    download_pdf()
    doc = fitz.open(PDF_PATH)
    cricos_pattern = re.compile(r"\b(\d{6}[A-Z]|\d{7})\b")
    
    courses_dict = {}
    
    for page_num in range(1, len(doc)):  # pages 2, 3, 4
        page = doc.load_page(page_num)
        links = page.get_links()
        
        page_urls = []
        for l in links:
            uri = l.get("uri")
            if uri and "/xml/course/" in uri:
                # Apply override if URL is stale
                if uri in URL_OVERRIDES:
                    uri = URL_OVERRIDES[uri]
                rect = l.get("from")
                y_center = (rect.y0 + rect.y1) / 2
                page_urls.append((y_center, uri))
                
        blocks = page.get_text("blocks")
        
        for b in blocks:
            x0, y0, x1, y1, text, block_no, block_type = b
            text_clean = text.strip().replace('\n', ' ')
            if not text_clean or y0 < 60 or y1 > 700:
                continue
            if text_clean.isupper() and not cricos_pattern.search(text_clean):
                continue
                
            cricos_match = cricos_pattern.search(text_clean)
            if cricos_match:
                cricos = cricos_match.group(1)
                y_center = (y0 + y1) / 2
                url = None
                if page_urls:
                    closest = min(page_urls, key=lambda x: abs(x[0] - y_center))
                    if abs(closest[0] - y_center) < 15:
                        url = closest[1]
                
                if not url:
                    continue
                
                # Duration
                duration_match = re.search(r"(\d+)\s*weeks", text_clean, re.IGNORECASE)
                duration = int(duration_match.group(1)) if duration_match else None
                
                # Tuition Fee
                fee_match = re.search(r"\$\s*([\d,]+)", text_clean)
                fee = int(fee_match.group(1).replace(",", "")) if fee_match else None
                
                # Intake raw
                intake_list = []
                for m in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Cont.']:
                    if re.search(rf"\b{m}\b", text_clean, re.IGNORECASE):
                        intake_list.append(m)
                
                intake_months = []
                for m in intake_list:
                    m_lower = m.lower()
                    if m_lower == "cont.":
                        intake_months.append("January")
                    elif m_lower in MONTHS:
                        intake_months.append(MONTHS[m_lower])
                
                title_part = text_clean.split(cricos)[0].strip()
                title_part = re.sub(r"\s+/$", "", title_part).strip()
                
                if url not in courses_dict:
                    courses_dict[url] = {
                        "cricos": cricos,
                        "duration": duration,
                        "fee": fee,
                        "intake_months": intake_months,
                        "draft_title": title_part,
                        "url": url
                    }
                else:
                    curr = courses_dict[url]
                    if not curr["duration"] and duration:
                        curr["duration"] = duration
                    if not curr["fee"] and fee:
                        curr["fee"] = fee
                    if intake_months:
                        curr["intake_months"] = list(set(curr["intake_months"] + intake_months))
                        
    print(f"Discovered {len(courses_dict)} unique courses from PDF.")
    return list(courses_dict.values())

# --- async details fetcher -----------------------------
async def fetch_course_details(sem, client, course):
    url = course["url"]
    
    course_data = {
        "cricos": course["cricos"],
        "title": course["draft_title"],
        "url": url,
        "course_description": "",
        "course_duration_per_week": str(course["duration"]) if course["duration"] else "",
        "offshore_tuition_fee": str(course["fee"]) if course["fee"] else "NULL",
        "onshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL",
        "materials_fee": "NULL",
        "entry_requirements": "",
        "apply_form": url,
        "intake_months": course["intake_months"]
    }
    
    async with sem:
        try:
            r = await client.get(url)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, "html.parser")
                
                # 1. Correct Title
                if soup.title:
                    title_part = soup.title.string.split(" - ")[0].strip()
                    if title_part:
                        course_data["title"] = title_part
                
                # 2. Description
                desc_p = soup.find("p", id="CourseDescription")
                if desc_p:
                    desc_text = desc_p.get_text(strip=True)
                    course_data["course_description"] = f"<h4>Overview</h4><p>{desc_text}</p>"
                
                # 3. Requirements
                req_h2 = None
                for h in soup.find_all("h2"):
                    t_lower = h.get_text().lower()
                    if "admission requirements" in t_lower or "course admission" in t_lower:
                        req_h2 = h
                        break
                if not req_h2:
                    for h in soup.find_all("h2"):
                        t_lower = h.get_text().lower()
                        if "requirements" in t_lower or "admission" in t_lower:
                            req_h2 = h
                            break
                            
                academic_list = []
                english_list = []
                
                if req_h2:
                    for sibling in req_h2.next_siblings:
                        if sibling.name == "h2":
                            break
                        if sibling.name == "ul":
                            for li in sibling.find_all("li"):
                                item_html = "".join(str(c) for c in li.contents)
                                item_cleaned = sanitise(item_html).strip()
                                if not item_cleaned:
                                    continue
                                text_content = li.get_text(strip=True)
                                if any(k in text_content.lower() for k in ["ielts", "english", "toefl", "pearson", "proficiency"]):
                                    english_list.append(item_cleaned)
                                else:
                                    academic_list.append(item_cleaned)
                            break
                            
                if academic_list or english_list:
                    table_html = "<table><tbody>"
                    if academic_list:
                        academic_items = "".join(f"<li>{item}</li>" for item in academic_list)
                        table_html += f"<tr><td><strong>Academic Requirements</strong></td><td><ul>{academic_items}</ul></td></tr>"
                    if english_list:
                        english_items = "".join(f"<li>{item}</li>" for item in english_list)
                        table_html += f"<tr><td><strong>English Proficiency</strong></td><td><ul>{english_items}</ul></td></tr>"
                    table_html += "</tbody></table>"
                    course_data["entry_requirements"] = table_html
                
                # 4. Materials Fee
                fees_table = soup.find("div", class_="cp_feesTable-int")
                if fees_table:
                    subtotal_row = fees_table.find("div", class_=lambda x: x and "cp_feesTable-subTotals" in x)
                    if subtotal_row:
                        cells = subtotal_row.find_all("div", class_="cp_cell")
                        if len(cells) >= 3:
                            inc_text = cells[2].get_text(strip=True)
                            fee_match = re.search(r"AUD\s*\$?(\d+)", inc_text, re.IGNORECASE)
                            if fee_match:
                                course_data["materials_fee"] = clean_numeric_fee(fee_match.group(1))
                                
                print(f"Processed: {course_data['title']} | CRICOS: {course_data['cricos']}")
            else:
                print(f"Failed to fetch: {url} (status: {r.status_code})")
        except Exception as e:
            print(f"Error scraping: {url} -> {e}")
            
    return course_data

async def fetch_all_details(courses):
    sem = asyncio.Semaphore(15)
    client = requests.AsyncSession(impersonate="chrome120")
    tasks = [fetch_course_details(sem, client, c) for c in courses]
    results = await asyncio.gather(*tasks)
    return results

# --- main ----------------------------------------------
def main():
    discovered = discover_courses()
    if not discovered:
        print("No courses discovered. Exiting.")
        return
        
    results = asyncio.run(fetch_all_details(discovered))
    
    # Process intakes
    all_months = set()
    for r in results:
        all_months.update(r["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)
    if not intake_date:
        intake_date = "January, July"  # default TAFE SA intake
        
    # Write SQL
    print(f"Writing SQL update queries to {SQL_PATH}...")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        for r in results:
            if not r["cricos"]:
                f.write(f"-- ⚠️ Skipped (no/unreliable CRICOS course code): {r['title']} | {r['url']}\n\n")
                continue
                
            clean_desc = clean_html(r["course_description"])
            clean_reqs = clean_html(r["entry_requirements"])
            
            f.write(f"UPDATE courses SET\n"
                    f"    course_description = '{clean_desc}',\n"
                    f"    course_duration_per_week = {r['course_duration_per_week'] or 'NULL'},\n"
                    f"    offshore_tuition_fee = {r['offshore_tuition_fee']},\n"
                    f"    onshore_tuition_fee = {r['onshore_tuition_fee']},\n"
                    f"    enrolment_fee = {r['enrolment_fee']},\n"
                    f"    materials_fee = {r['materials_fee']},\n"
                    f"    entry_requirements = '{clean_reqs}',\n"
                    f"    apply_form = '{r['apply_form']}',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
                    
    # Write Excel
    print(f"Writing Excel sheet to {EXCEL_PATH}...")
    def cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]
        
    pd.DataFrame([{
        "cricos": r["cricos"],
        "title": r["title"],
        "url": r["url"],
        "course_duration_per_week": int(r["course_duration_per_week"]) if str(r["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(r["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(r["onshore_tuition_fee"]),
        "enrolment_fee": cell(r["enrolment_fee"]),
        "materials_fee": cell(r["materials_fee"]),
        "intake": ", ".join(r["intake_months"]),
        "course_description": cell(r["course_description"]),
        "entry_requirements": cell(r["entry_requirements"]),
    } for r in results]).to_excel(EXCEL_PATH, index=False)
    
    print(f"\n✅ Finished. {len(results)} courses processed.")
    print(f"SQL update written to: {SQL_PATH}")
    print(f"Excel driver written to: {EXCEL_PATH}")

if __name__ == "__main__":
    main()
