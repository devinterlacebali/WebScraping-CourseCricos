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
        
        # 1. Extract course top introduction
        intro_content = ""
        desc_h2 = soup.find("h2", string=lambda t: t and "COURSE DESCRIPTION" in t.upper())
        if desc_h2:
            sibling = desc_h2.next_sibling
            while sibling:
                # Stop if we hit the WPBakery tabs/panels container
                if sibling.name and ("vc_tta-container" in sibling.get("class", []) or "vc_tta" in sibling.name):
                    break
                if sibling.name:
                    intro_content += str(sibling)
                sibling = sibling.next_sibling
                
        # 2. Extract tab panels
        outline_html = ""
        requirements_html = ""
        outcomes_html = ""
        duration_text = ""
        
        # Regex helper for fees
        page_text = soup.body.get_text() if soup.body else soup.get_text()
        
        tuition_fee = "NULL"
        enrolment_fee = "NULL"
        materials_fee = "NULL"
        
        tuition_match = re.search(r"Tuition\s*Fee\s*\$?\s*(\d+[\d,]*)", page_text, re.IGNORECASE)
        if tuition_match:
            tuition_fee = tuition_match.group(1).replace(",", "")
            
        app_match = re.search(r"(?:Application|Enrolment)\s*Fees?\s*\$?\s*(\d+[\d,]*)", page_text, re.IGNORECASE)
        if app_match:
            enrolment_fee = app_match.group(1).replace(",", "")
            
        mat_match = re.search(r"(?:Text\s*Books?\s*&\s*)?Material\s*Fees?\s*\$?\s*(\d+[\d,]*)", page_text, re.IGNORECASE)
        if mat_match:
            materials_fee = mat_match.group(1).replace(",", "")
            
        # Parse panels
        panels = soup.find_all(class_="vc_tta-panel")
        for panel in panels:
            title_el = panel.find(class_="vc_tta-panel-title")
            panel_title = title_el.get_text().strip().lower() if title_el else ""
            body_el = panel.find(class_="vc_tta-panel-body")
            if not body_el:
                continue
                
            # Clean body class and style attributes
            for tag in body_el.find_all(True):
                if tag.has_attr("class"):
                    del tag["class"]
                if tag.has_attr("style"):
                    del tag["style"]
                    
            body_html = str(body_el)
            
            if "outline" in panel_title:
                outline_html = f"<h4>Course Outline</h4>{body_html}"
            elif "requirement" in panel_title:
                requirements_html = f"<h4>Entry Requirements</h4>{body_html}"
            elif "outcome" in panel_title:
                outcomes_html = f"<h4>Learning Outcomes & Career Pathways</h4>{body_html}"
            elif "fee" in panel_title:
                # Find duration from panel content
                duration_match = re.search(r"Duration\s*of\s*Course\s*:\s*([^(\n]+)", body_el.get_text(), re.IGNORECASE)
                if duration_match:
                    duration_text = duration_match.group(1).strip()
                    
        # Fallback duration if not found in Fees tab
        if not duration_text:
            duration_match = re.search(r"Duration\s*of\s*Course\s*:\s*([^(\n]+)", page_text, re.IGNORECASE)
            if duration_match:
                duration_text = duration_match.group(1).strip()
            else:
                duration_text = str(row.get("duration", "")).replace("(including term breaks)", "").strip()
                
        # Combine descriptions
        combined_description = ""
        if intro_content:
            combined_description += f"<h4>Course Intro</h4>{intro_content}"
        if outline_html:
            combined_description += outline_html
        if outcomes_html:
            combined_description += outcomes_html
            
        desc_soup = BeautifulSoup(combined_description, "html.parser")
        for tag in desc_soup.find_all(["style", "script", "noscript"]):
            tag.decompose()
        # Clean attributes
        for tag in desc_soup.find_all(True):
            if tag.has_attr("class"):
                del tag["class"]
            if tag.has_attr("style"):
                del tag["style"]
                
        cleaned_desc = clean_html(str(desc_soup))
        
        # Clean entry requirements
        req_soup = BeautifulSoup(requirements_html, "html.parser")
        for tag in req_soup.find_all(["style", "script", "noscript"]):
            tag.decompose()
        for tag in req_soup.find_all(True):
            if tag.has_attr("class"):
                del tag["class"]
            if tag.has_attr("style"):
                del tag["style"]
        cleaned_reqs = clean_html(str(req_soup))
        
        # Final output
        return {
            "cricos": cricos,
            "title": title,
            "url": url,
            "course_description": cleaned_desc,
            "total_course_duration": duration_text if duration_text else str(row.get("duration", "")),
            "offshore_tuition_fee": clean_numeric_fee(tuition_fee),
            "enrolment_fee": clean_numeric_fee(enrolment_fee),
            "materials_fee": clean_numeric_fee(materials_fee),
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
            "enrolment_fee": clean_numeric_fee(str(row.get("enrolment_fee", "350"))),
            "materials_fee": clean_numeric_fee(str(row.get("materials_fee", "2100"))),
            "entry_requirements": "",
            "apply_form": url
        }

# === MAIN ===
async def main():
    excel_path = "Aspen College/aspen.xlsx"
    sql_path = "Aspen College/aspen_courses_update.sql"
    
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
    intake_date = 'January, February, March, April, May, June, July, August, September, October, November',
    updated_at = NOW()
WHERE cricos_provider_code = '03753A';

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
