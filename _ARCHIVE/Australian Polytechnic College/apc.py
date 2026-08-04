import os
import re
import sys
import json
import urllib.request
import urllib.parse
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Force UTF-8 encoding for stdout and stderr on Windows
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

# === EXTRACT COURSE DESCRIPTION ===
def extract_course_description(course) -> str:
    desc = ""
    # Course Intro
    intro = course.get("course_intro")
    if intro:
         desc += f"<h4>Course Intro</h4>{intro}"
         
    # Outcome / Career Opportunities
    outcome = course.get("outcome")
    if outcome:
         desc += f"<h4>Career Outcomes</h4>{outcome}"
         
    # Course Structure / Units
    struct = course.get("course_structure")
    if struct:
         desc += f"<h4>Course Structure</h4>{struct}"
         
    # Pathway
    pathway = course.get("pathway")
    if pathway:
         desc += f"<h4>Pathway</h4>{pathway}"
         
    if desc:
        desc_soup = BeautifulSoup(desc, "html.parser")
        for tag in desc_soup.find_all(["style", "script", "noscript"]):
            tag.decompose()
        # Clean class and style attributes
        for tag in desc_soup.find_all(True):
            if tag.has_attr("class"):
                del tag["class"]
            if tag.has_attr("style"):
                del tag["style"]
        return clean_html(str(desc_soup))
    return ""

# === EXTRACT ENTRY REQUIREMENTS ===
def extract_entry_requirements(course) -> str:
    req = ""
    entry = course.get("entry_requirement")
    if entry:
        req += f"<h4>Entry Requirements</h4>{entry}"
        
    resource = course.get("resource_requirement")
    if resource:
        req += f"<h4>Resource Requirements</h4>{resource}"
        
    if req:
        req_soup = BeautifulSoup(req, "html.parser")
        for tag in req_soup.find_all(["style", "script", "noscript"]):
            tag.decompose()
        for tag in req_soup.find_all(True):
            if tag.has_attr("class"):
                del tag["class"]
            if tag.has_attr("style"):
                del tag["style"]
        return clean_html(str(req_soup))
    return ""

# === SCRAPE PER COURSE ===
async def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    duration = str(row["duration"]).strip()
    fee = clean_numeric_fee(str(row["fee"]))
    enrolment_fee = clean_numeric_fee(str(row.get("enrolment_fee", "250")))
    materials_fee = clean_numeric_fee(str(row.get("materials_fee", "1000")))
    title = str(row["title"]).strip()
    
    # Extract slug from URL
    # URL format: https://australianpolytechnic.edu.au/courses/{slug}
    parsed = urllib.parse.urlparse(url)
    slug = parsed.path.strip("/").replace("courses/", "").strip()
    
    # slug needs to be unquoted for file/url fetching
    slug_unquoted = urllib.parse.unquote(slug)
    
    api_url = f"https://admin.australianpolytechnic.edu.au/api/courses/{urllib.parse.quote(slug_unquoted)}"
    
    data = {
        "cricos": cricos,
        "title": title,
        "url": url,
        "course_description": "",
        "total_course_duration": duration,
        "offshore_tuition_fee": fee,
        "enrolment_fee": enrolment_fee,
        "materials_fee": materials_fee,
        "entry_requirements": "",
        "apply_form": url,
    }
    
    # If the course is Solid Plastering and doesn't have an API entry, use boilerplate
    if "solid-plastering" in slug.lower():
        data["course_description"] = clean_html(
            "<h4>Course Intro</h4><p>This qualification reflects the role of solid plasterers who apply, maintain and restore plaster in residential and commercial buildings.</p>"
        )
        data["entry_requirements"] = clean_html(
            "<h4>Entry Requirements</h4><p>Applicants must be at least 18 years old and have completed Australian Year 12 or equivalent, and have IELTS overall 5.5 or equivalent.</p>"
        )
        print(f"ℹ️ Used boilerplate for Solid Plastering: {url}")
        return data
        
    try:
        print(f"Fetching API: {api_url}")
        req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as response:
            res = json.loads(response.read().decode("utf-8"))
            course = res.get("data", {}).get("course")
            if course:
                data["course_description"] = extract_course_description(course)
                data["entry_requirements"] = extract_entry_requirements(course)
                print(f"✅ API Scraped successfully: {url}")
            else:
                print(f"⚠️ Empty API response for slug: {slug_unquoted}")
    except Exception as e:
        print(f"❌ Error API scraping {url}: {e}")
        
    return data

# === MAIN ===
async def main():
    excel_path = "Australian Polytechnic College/apc.xlsx"
    sql_path = "Australian Polytechnic College/apc_courses_update.sql"
    
    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return
        
    df = pd.read_excel(excel_path)
    results = []
    
    for idx, row in df.iterrows():
        print(f"\n[{idx+1}/{len(df)}] Processing: {row['url']}")
        course_data = await scrape_course(row)
        results.append(course_data)
        
    # Write SQL updates
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, February, March, April, May, June, July, August, September, October, November, December',
    updated_at = NOW()
WHERE cricos_provider_code = '03724F';

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
