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

PROVIDER_CODE = "03763K"
# Intake months derived from the "Intakes" (Study Period) section on the course pages
INTAKE_DATE = "March, July, November"

# Header titles whose content belongs to the course description (kept in order)
DESCRIPTION_SECTIONS = [
    "WHY STUDY",          # matched as a prefix (e.g. "WHY STUDY THE BACHELOR OF BUSINESS?")
    "Course Overview",
    "Subject Outline",
    "Learning Methodology",
]
REQUIREMENT_SECTIONS = ["Entry Requirements"]
# Headers we never want to carry over into a description bucket
STOP_PHRASES = ("apply for admission",)

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
    return val_clean if val_clean else "NULL"

# === SANITISE A SECTION OF HTML ===
def _sanitise(html: str) -> str:
    frag = BeautifulSoup(html, "html.parser")
    for tag in frag.find_all(["style", "script", "noscript", "form", "iframe"]):
        tag.decompose()
    for tag in frag.find_all(True):
        if tag.has_attr("class"):
            del tag["class"]
        if tag.has_attr("style"):
            del tag["style"]
        for attr in ("id", "data-script-id"):
            if tag.has_attr(attr):
                del tag[attr]
    return str(frag)

# === BUILD ORDERED LIST OF (title, content_html) FROM SP PAGE BUILDER ROWS ===
def get_sections(soup):
    rows = [r for r in soup.find_all("div", class_="sppb-row-container")
            if not r.find_parent("div", class_="sppb-row-container")]
    sections = []
    current = None
    buf = []

    def flush():
        if current is not None:
            sections.append((current, "".join(buf)))

    for r in rows:
        hdr = r.find(class_="sppb-addon-header")
        if hdr:
            flush()
            current = re.sub(r"\s+", " ", hdr.get_text(" ", strip=True)).strip()
            buf = []
            # Capture any content sitting in the same row as the header
            clone = BeautifulSoup(str(r), "html.parser")
            h = clone.find(class_="sppb-addon-header")
            if h is not None:
                h.decompose()
            body = clone.get_text(strip=True)
            if body:
                buf.append(str(clone))
        else:
            if current is None:
                continue
            text = re.sub(r"\s+", " ", r.get_text(" ", strip=True)).strip()
            if not text or text.lower().startswith(STOP_PHRASES):
                continue
            buf.append(str(r))
    flush()
    return sections

def _nice_title(title):
    return "Why Study This Course" if title.upper().startswith("WHY STUDY") else title

# === EXTRACT COURSE DESCRIPTION ===
def extract_course_description(sections) -> str:
    desc = ""
    for title, html in sections:
        if any(title.upper().startswith(s.upper()) for s in DESCRIPTION_SECTIONS):
            if BeautifulSoup(html, "html.parser").get_text(strip=True):
                desc += f"<h4>{_nice_title(title)}</h4>{html}"
    return clean_html(_sanitise(desc)) if desc else ""

# === EXTRACT ENTRY REQUIREMENTS ===
def extract_entry_requirements(sections) -> str:
    req = ""
    for title, html in sections:
        if title in REQUIREMENT_SECTIONS:
            if BeautifulSoup(html, "html.parser").get_text(strip=True):
                req += f"<h4>{title}</h4>{html}"
    return clean_html(_sanitise(req)) if req else ""

# === EXTRACT DURATION (e.g. "3 years", "6 months") ===
def extract_duration(full_text) -> str:
    m = re.search(r"Duration\s+(\d+(?:\.\d+)?\s*(?:years?|months?))\s*full-time", full_text, re.IGNORECASE)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip().lower()
    return ""

# === EXTRACT INTERNATIONAL TUITION AS TOTAL COURSE FEE ===
# The site publishes tuition either "per year" or "per Study Period".
# We normalise to the TOTAL course fee using the course duration / structure.
def extract_fees(full_text, duration):
    m = re.search(
        r"International Student Tuition Fee:\s*\$?\s*([\d,]+)\s*(per year|per Study Period)?",
        full_text, re.IGNORECASE)
    if not m:
        return "NULL", ""

    per_value = m.group(1).replace(",", "")
    unit = (m.group(2) or "").strip()
    try:
        per_num = float(per_value)
    except ValueError:
        return "NULL", ""

    if unit.lower() == "per year":
        years = re.search(r"(\d+(?:\.\d+)?)\s*years?", duration or "", re.IGNORECASE)
        n = float(years.group(1)) if years else 1.0
        total = per_num * n
        basis = f"{int(per_num):,}/yr x {years.group(1) if years else '1'} years" if years else f"{int(per_num):,}/yr"
    elif unit.lower() == "per study period":
        # Number of study periods = total subjects / subjects per study period
        cp = re.search(r"Total Course Credit Points\s*(\d+)", full_text, re.IGNORECASE)
        pps = re.search(r"Points per Subject\s*(\d+)", full_text, re.IGNORECASE)
        per_sp = re.search(r"consists of\s*(\d+)\s*subjects?\s*per study period", full_text, re.IGNORECASE)
        sp_count = 1.0
        if cp and pps and per_sp and int(pps.group(1)) and int(per_sp.group(1)):
            subjects = int(cp.group(1)) / int(pps.group(1))
            sp_count = max(1.0, round(subjects / int(per_sp.group(1))))
        total = per_num * sp_count
        basis = f"{int(per_num):,}/study period x {int(sp_count)} SP"
    else:
        total = per_num
        basis = f"{int(per_num):,} (unit unspecified)"

    total_str = str(int(total)) if float(total).is_integer() else str(total)
    return clean_numeric_fee(total_str), basis

# === EXTRACT CRICOS COURSE CODE FROM PAGE (fallback to xlsx) ===
def extract_cricos(full_text) -> str:
    m = re.search(r"CRICOS (?:Course )?Code:\s*([0-9A-Z]{5,8})", full_text)
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
        "fee_unit": "",
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
        full_text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))

        sections = get_sections(soup)
        data["course_description"] = extract_course_description(sections)
        data["entry_requirements"] = extract_entry_requirements(sections)
        data["total_course_duration"] = extract_duration(full_text)
        data["offshore_tuition_fee"], data["fee_unit"] = extract_fees(full_text, data["total_course_duration"])

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
    excel_path = "Adelaide Institute of Higher Education/aihe.xlsx"
    sql_path = "Adelaide Institute of Higher Education/aihe_courses_update.sql"

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
            fee_note = f"  -- AUD total course fee ({d['fee_unit']})" if d["fee_unit"] else ""
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["total_course_duration"]}',
    offshore_tuition_fee = {d["offshore_tuition_fee"]},{fee_note}
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
