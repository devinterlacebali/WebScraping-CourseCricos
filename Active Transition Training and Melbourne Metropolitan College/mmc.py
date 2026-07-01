import os
import re
import sys
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Force UTF-8 encoding for stdout and stderr on Windows to support emojis in console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# === CLEAN HTML ===
def clean_html(html: str) -> str:
    if not html:
        return ""
    # Replace multiple whitespaces with single space
    html = re.sub(r"\s+", " ", html)
    # Escape single quotes for SQL insertion
    html = html.replace("'", "''")
    return html.strip()

# === CLEAN NUMERIC FEE ===
def clean_numeric_fee(val: str) -> str:
    if not val or val.lower() in ("nan", "null", "n/a", ""):
        return "NULL"
    val_clean = re.sub(r"[^\d\.]", "", val)
    return val_clean if val_clean else "NULL"

# === SCRAPE PER COURSE ===
async def scrape_course(page, row):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    title = str(row["title"]).strip()
    
    print(f"Loading {url}...")
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=40000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        # 1. Parse FAQ Accordions
        desc_parts = []
        req_parts = []
        tuition_fee = "NULL"
        
        faq_accordions = soup.find_all(class_="uael-faq-accordion")
        for accordion in faq_accordions:
            q_el = accordion.find(class_=re.compile(r"uael-accordion-title|uael-question", re.IGNORECASE))
            a_el = accordion.find(class_=re.compile(r"uael-accordion-content|uael-faq-content|uael-answer", re.IGNORECASE))
            
            if not q_el:
                # Fallback if classes differ: first child might be header, second body
                children = list(accordion.find_all(recursive=False))
                if len(children) >= 2:
                    q_el, a_el = children[0], children[1]
                else:
                    continue
                    
            q_text = q_el.get_text().strip()
            if not a_el:
                continue
                
            # Clean attributes from answer element
            for tag in a_el.find_all(True):
                if tag.has_attr("class"):
                    del tag["class"]
                if tag.has_attr("style"):
                    del tag["style"]
            
            a_html = str(a_el)
            
            # Map sections
            q_lower = q_text.lower()
            if any(term in q_lower for term in ["overview", "learn", "units", "structure", "opportunities", "pathway", "mode", "outcome"]):
                desc_parts.append(f"<h4>{q_text}</h4>{a_html}")
            elif "requirement" in q_lower:
                req_parts.append(f"<h4>{q_text}</h4>{a_html}")
            elif "fee" in q_lower:
                # Regex search for tuition fee number
                fee_text = a_el.get_text()
                fee_match = re.search(r"\$?\s*AU?\s*D?\s*[^\d]*(\d+[\d,]*)", fee_text, re.IGNORECASE)
                if fee_match:
                    tuition_fee = fee_match.group(1).replace(",", "")
                    
        # If tuition fee not found in Fees tab, try regex search in full body
        if tuition_fee == "NULL" or not tuition_fee:
            text = soup.body.get_text() if soup.body else soup.get_text()
            fee_match = re.search(r"Tuition\s*Fee\s*=\s*\$?\s*AU?\s*D?\s*[^\d]*(\d+[\d,]*)", text, re.IGNORECASE)
            if fee_match:
                tuition_fee = fee_match.group(1).replace(",", "")
                
        # 2. Append general requirements from prospectus
        # Academic level varies by course level (Diploma/Advanced vs Cert)
        academic_req = "Equivalent to an Australian Year 12 qualification."
        if any(term in title.lower() for term in ["certificate iii", "certificate 3", "certificate iv", "certificate 4"]):
            academic_req = "Equivalent to an Australian Year 10 qualification."
            
        general_reqs_html = f"""
        <h4>General Entry Requirements (from Prospectus)</h4>
        <ul>
            <li><strong>Age:</strong> Must be at least 18 years old.</li>
            <li><strong>Academic:</strong> {academic_req}</li>
            <li><strong>English Test:</strong> IELTS overall 6.5, PTE 50, or equivalent. Please check course specific entry requirements for details.</li>
        </ul>
        """
        req_parts.append(general_reqs_html)
        
        # 3. Combine Description & Requirements
        combined_desc = "".join(desc_parts)
        combined_req = "".join(req_parts)
        
        desc_soup = BeautifulSoup(combined_desc, "html.parser")
        for tag in desc_soup.find_all(["style", "script", "noscript"]):
            tag.decompose()
        cleaned_desc = clean_html(str(desc_soup))
        
        req_soup = BeautifulSoup(combined_req, "html.parser")
        for tag in req_soup.find_all(["style", "script", "noscript"]):
            tag.decompose()
        cleaned_reqs = clean_html(str(req_soup))
        
        return {
            "cricos": cricos,
            "title": title,
            "url": url,
            "course_description": cleaned_desc,
            "total_course_duration": str(row.get("duration", "")),
            "offshore_tuition_fee": clean_numeric_fee(tuition_fee if tuition_fee != "NULL" else str(row.get("fee", ""))),
            "enrolment_fee": clean_numeric_fee(str(row.get("enrolment_fee", "300"))),
            "materials_fee": clean_numeric_fee(str(row.get("materials_fee", "200"))),
            "entry_requirements": cleaned_reqs,
            "apply_form": url
        }
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return {
            "cricos": cricos,
            "title": title,
            "url": url,
            "course_description": "",
            "total_course_duration": str(row.get("duration", "")),
            "offshore_tuition_fee": clean_numeric_fee(str(row.get("fee", ""))),
            "enrolment_fee": clean_numeric_fee(str(row.get("enrolment_fee", "300"))),
            "materials_fee": clean_numeric_fee(str(row.get("materials_fee", "200"))),
            "entry_requirements": "",
            "apply_form": url
        }

# === MAIN ===
async def main():
    excel_path = "Active Transition Training and Melbourne Metropolitan College/mmc.xlsx"
    sql_path = "Active Transition Training and Melbourne Metropolitan College/mmc_courses_update.sql"
    
    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return
        
    df = pd.read_excel(excel_path)
    results = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        for idx, row in df.iterrows():
            print(f"\n[{idx+1}/{len(df)}] Processing: {row['url']}")
            course_data = await scrape_course(page, row)
            results.append(course_data)
            
        await browser.close()
        
    # Write SQL updates
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, March, April, May, July, August, September, October, November',
    updated_at = NOW()
WHERE cricos_provider_code = '03783F';

""")
        for d in results:
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["total_course_duration"]}',
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    materials_fee = {d["materials_fee"]},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")
            
    print(f"\n✅ Finished! Scraped {len(results)} courses. SQL updates saved to {sql_path}")

if __name__ == "__main__":
    asyncio.run(main())
