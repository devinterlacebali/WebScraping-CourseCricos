import os
import re
import sys
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

PROVIDER_CODE = "03732F"
# Intake months derived from the institution's published academic calendar
INTAKE_DATE = "January, March, April, July, September, November"

# Accordion section titles (Bricks Builder) grouped by destination field
DESCRIPTION_SECTIONS = [
    "Course Rationale",
    "Course Structure",
    "Year 1",
    "Year 2",
    "Year 3",
    "Learning Outcomes",
]
REQUIREMENT_SECTIONS = [
    "Admission",
    "Admission Requirements",
]

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
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    # remove any $, commas, spaces, or /week
    val_clean = re.sub(r"[^\d\.]", "", str(val))
    return val_clean if val_clean else "NULL"

# === SANITISE A SECTION OF HTML ===
def _sanitise(html: str) -> str:
    frag = BeautifulSoup(html, "html.parser")
    for tag in frag.find_all(["style", "script", "noscript"]):
        tag.decompose()
    for tag in frag.find_all(True):
        if tag.has_attr("class"):
            del tag["class"]
        if tag.has_attr("style"):
            del tag["style"]
    return str(frag)

# === BUILD A MAP OF ACCORDION SECTIONS {title: content_html} ===
def get_accordion_sections(soup):
    sections = {}
    acc = soup.find("div", class_="brxe-accordion-nested")
    if not acc:
        return sections
    for title_wrap in acc.find_all("div", class_="accordion-title-wrapper"):
        title = re.sub(r"\s+", " ", title_wrap.get_text(" ", strip=True)).strip()
        content = title_wrap.find_next_sibling("div", class_="accordion-content-wrapper")
        if title and content is not None:
            sections.setdefault(title, str(content))
    return sections

# === EXTRACT COURSE DESCRIPTION ===
def extract_course_description(sections) -> str:
    desc = ""
    for name in DESCRIPTION_SECTIONS:
        html = sections.get(name)
        if html and BeautifulSoup(html, "html.parser").get_text(strip=True):
            desc += f"<h4>{name}</h4>{html}"
    return clean_html(_sanitise(desc)) if desc else ""

# === EXTRACT ENTRY REQUIREMENTS ===
def extract_entry_requirements(sections) -> str:
    req = ""
    for name in REQUIREMENT_SECTIONS:
        html = sections.get(name)
        if html and BeautifulSoup(html, "html.parser").get_text(strip=True):
            heading = "Entry Requirements" if name == "Admission" else name
            req += f"<h4>{heading}</h4>{html}"
    return clean_html(_sanitise(req)) if req else ""

# === EXTRACT DURATION (e.g. "3 years") ===
def extract_duration(soup) -> str:
    text = soup.get_text(" ", strip=True)
    m = re.search(r"(\d+(?:\.\d+)?\s*years?)\s*DURATION", text, re.IGNORECASE)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip().lower()
    m = re.search(r"(\d+)\s*SEMESTERS?", text, re.IGNORECASE)
    if m:
        return f"{m.group(1)} semesters"
    return ""

# === EXTRACT FEES FROM THE "Fees" SECTION ===
def extract_fees(sections):
    fees_html = sections.get("Fees", "")
    text = re.sub(r"\s+", " ", BeautifulSoup(fees_html, "html.parser").get_text(" ", strip=True))
    tuition = "NULL"
    enrolment = "NULL"
    if text:
        # Limit to the International Student Fees block when present
        intl = text
        idx = text.lower().find("international student fees")
        dom = text.lower().find("domestic student fees")
        if idx != -1:
            intl = text[idx:dom] if dom > idx else text[idx:]
        m = re.search(r"Total Course Fees:\s*AUD\s*\$\s*([\d,]+)", intl, re.IGNORECASE)
        if m:
            tuition = clean_numeric_fee(m.group(1))
        m = re.search(r"non-refundable\)\s*:\s*AUD\s*\$\s*([\d,]+)", intl, re.IGNORECASE)
        if m:
            enrolment = clean_numeric_fee(m.group(1))
    return tuition, enrolment

# === EXTRACT CRICOS COURSE CODE FROM PAGE (fallback to xlsx) ===
def extract_cricos(soup) -> str:
    text = soup.get_text(" ", strip=True)
    m = re.search(r"CRICOS Course ID\s*:\s*([0-9A-Z]{5,8})", text)
    return m.group(1) if m else ""

# === SCRAPE PER COURSE ===
async def scrape_course(row, browser):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    if cricos.lower() in ("nan", "none", "null"):
        cricos = ""
    title = str(row["title"]).strip()

    data = {
        "cricos": cricos,
        "title": title,
        "url": url,
        "course_description": "",
        "total_course_duration": "",
        "offshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL",
        "materials_fee": "NULL",
        "entry_requirements": "",
        "apply_form": url,
    }

    try:
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        sections = get_accordion_sections(soup)

        data["course_description"] = extract_course_description(sections)
        data["entry_requirements"] = extract_entry_requirements(sections)
        data["total_course_duration"] = extract_duration(soup)
        data["offshore_tuition_fee"], data["enrolment_fee"] = extract_fees(sections)

        # Prefer CRICOS code from the page; fall back to the value in the xlsx
        page_cricos = extract_cricos(soup)
        if page_cricos:
            data["cricos"] = page_cricos

        await page.close()
        print(f"✅ Scraped successfully: {url}")
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        try:
            await page.close()
        except Exception:
            pass

    return data

# === MAIN ===
async def main():
    excel_path = "Leaders Institute Pty Ltd/leaders.xlsx"
    sql_path = "Leaders Institute Pty Ltd/leaders_courses_update.sql"

    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return

    df = pd.read_excel(excel_path)
    results = []

    async with async_playwright() as p:
        headless_env = os.environ.get("SCRAPER_HEADLESS", "True")
        headless_val = True if headless_env.lower() in ("true", "1") else False

        browser = await p.chromium.launch(headless=headless_val)

        for idx, row in df.iterrows():
            print(f"\n[{idx+1}/{len(df)}] Scraping: {row['url']}")
            course_data = await scrape_course(row, browser)
            results.append(course_data)

        await browser.close()

    # Write SQL updates
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '{INTAKE_DATE}',
    updated_at = NOW()
WHERE cricos_provider_code = '{PROVIDER_CODE}';

""")
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped (no CRICOS course code found): {d['title']} | {d['url']}\n\n")
                continue
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
