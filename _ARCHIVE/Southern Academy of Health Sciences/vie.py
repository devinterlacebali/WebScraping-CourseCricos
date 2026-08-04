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

PROVIDER_CODE = "03778C"

# Accordion (details/summary) sections grouped by destination field
DESCRIPTION_SECTIONS = [
    "Course Overview",
    "Career Prospects",
    "Study Mode",
    "Units of Competency",
    "Pathways Information",
    "Course Credit",
]
REQUIREMENT_SECTIONS = ["Entry Requirements"]
SKIP_SECTIONS = {"Brochure", "Apply Now", "Fees and Charges", "Course Duration"}

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December",
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# === CLEAN HTML ===
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")
    return html.strip()

# === CLEAN NUMERIC FEE ===
def clean_numeric_fee(val: str) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    val_clean = re.sub(r"[^\d\.]", "", str(val))
    if not val_clean:
        return "NULL"
    # Drop a trailing ".00" / ".0" so we store a clean integer where possible
    num = float(val_clean)
    return str(int(num)) if num.is_integer() else str(num)

# === SANITISE A SECTION OF HTML ===
def _sanitise(html: str) -> str:
    frag = BeautifulSoup(html, "html.parser")
    for tag in frag.find_all(["style", "script", "noscript", "form", "iframe", "button"]):
        tag.decompose()
    for tag in frag.find_all(True):
        for attr in ("class", "style", "id", "role", "tabindex"):
            if tag.has_attr(attr):
                del tag[attr]
        for attr in list(tag.attrs):
            if attr.startswith("data-") or attr.startswith("aria-"):
                del tag[attr]
    return str(frag)

# === BUILD {section_title: content_html} FROM THE ELEMENTOR <details> ACCORDION ===
def get_sections(soup):
    sections = {}
    acc = soup.find(class_="elementor-widget-n-accordion")
    if not acc:
        return sections
    for det in acc.find_all("details"):
        summ = det.find("summary")
        if not summ:
            continue
        title = re.sub(r"\s+", " ", summ.get_text(" ", strip=True)).strip()
        clone = BeautifulSoup(str(det), "html.parser")
        s = clone.find("summary")
        if s is not None:
            s.decompose()
        sections.setdefault(title, str(clone))
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
            req += f"<h4>{name}</h4>{html}"
    return clean_html(_sanitise(req)) if req else ""

# === EXTRACT DURATION (e.g. "78 weeks") ===
def extract_duration(full_text) -> str:
    m = re.search(r"Course Duration\s*(\d+\s*weeks?)", full_text, re.IGNORECASE)
    return re.sub(r"\s+", " ", m.group(1)).strip().lower() if m else ""

# === EXTRACT FEES FROM THE COURSE HEADER ===
def extract_fees(full_text):
    def grab(pattern):
        m = re.search(pattern, full_text, re.IGNORECASE)
        return clean_numeric_fee(m.group(1)) if m else "NULL"
    tuition = grab(r"Course Fee\s*(?:AUD)?\s*\$?\s*([\d,\.]+)")
    enrolment = grab(r"Enroll?ment Fee:?\s*\$?\s*([\d,\.]+)")
    materials = grab(r"Material(?:s)? Fee:?\s*\$?\s*([\d,\.]+)")
    return tuition, enrolment, materials

# === EXTRACT INTAKE MONTHS FROM THE COURSE HEADER ===
def extract_intake_months(full_text):
    m = re.search(r"Intake Dates\s*\d{4}(.*?)(?:AQF Level|Note:|Apply Now|Campus Location|$)",
                  full_text, re.IGNORECASE)
    if not m:
        return []
    found = []
    for tok in re.findall(r"[A-Za-z]{3,4}", m.group(1)):
        key = tok.lower()
        if key in MONTHS and MONTHS[key] not in found:
            found.append(MONTHS[key])
    return found

# === EXTRACT CRICOS COURSE CODE (fallback to xlsx) ===
def extract_cricos(full_text) -> str:
    m = re.search(r"CRICOS Course Code:\s*([0-9A-Z]{5,8})", full_text)
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
        "intake_months": [],
    }

    try:
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        full_text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))

        sections = get_sections(soup)
        data["course_description"] = extract_course_description(sections)
        data["entry_requirements"] = extract_entry_requirements(sections)
        data["total_course_duration"] = extract_duration(full_text)
        data["offshore_tuition_fee"], data["enrolment_fee"], data["materials_fee"] = extract_fees(full_text)
        data["intake_months"] = extract_intake_months(full_text)

        page_cricos = extract_cricos(full_text)
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
    excel_path = "Southern Academy of Health Sciences/vie.xlsx"
    sql_path = "Southern Academy of Health Sciences/vie_courses_update.sql"

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

    # Aggregate intake months across all courses (calendar order) for the provider record
    all_months = set()
    for d in results:
        all_months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)

    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '{intake_date}',
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

    print(f"\n✅ Finished! Scraped {len(results)} courses. Intake: {intake_date}")
    print(f"SQL updates saved to {sql_path}")

if __name__ == "__main__":
    asyncio.run(main())
