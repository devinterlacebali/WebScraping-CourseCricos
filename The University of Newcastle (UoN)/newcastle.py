import os
import re
import sys
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Configure standard encoding for Windows environment
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Append parent directory to sys.path to import ai_formatter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from ai_formatter import format_requirements
except ImportError:
    def format_requirements(text):
        return ""

PROVIDER_CODE = "00109J"
SLUG = "newcastle"
DIR = "The University of Newcastle (UoN)"
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

def extract_course_description(soup):
    desc_html = []
    for h2 in soup.find_all("h2"):
        h2_text = h2.get_text(strip=True)
        if any(x in h2_text.lower() for x in ["overview", "career", "placement"]):
            desc_html.append(f"<h4>{h2_text}</h4>")
            curr = h2.next_sibling
            section_elements = []
            while curr:
                if curr.name == "h2":
                    break
                if curr.name in ["p", "div", "ul", "ol"]:
                    section_elements.append(str(curr))
                curr = curr.next_sibling
            if section_elements:
                desc_html.append(sanitise("".join(section_elements)))
    return "".join(desc_html)

def extract_duration(soup):
    ft_el = soup.find("span", class_="degree-full-time-duration")
    if ft_el:
        txt = ft_el.get_text(strip=True)
        match = re.search(r"([0-9.]+)\s*year", txt, re.IGNORECASE)
        if match:
            years = float(match.group(1))
            return str(int(years * 52))
        match = re.search(r"([0-9.]+)\s*month", txt, re.IGNORECASE)
        if match:
            months = float(match.group(1))
            return str(int(months * 4.33))
    return ""

def extract_fees(soup, duration_weeks):
    offshore = "NULL"
    fee_el = soup.find("span", class_="degree-international-fee")
    if fee_el:
        fee_text = fee_el.get_text(strip=True)
        m = re.search(r"([0-9,]+)", fee_text)
        if m:
            annual_fee = float(m.group(1).replace(",", ""))
            if duration_weeks:
                years = int(duration_weeks) / 52.0
                total_fee = annual_fee * years
                offshore = str(int(total_fee))
            else:
                offshore = str(int(annual_fee))
    return offshore, "NULL", "NULL", "NULL"

def extract_intake_months(soup):
    intake_text = ""
    for tag in soup.find_all(True):
        classes = tag.get("class") or []
        classes_str = " ".join(classes)
        if any(x in classes_str.lower() for x in ["start-date", "offerings", "additional-dates"]):
            intake_text += " " + tag.get_text()
            
    months = []
    for token in re.findall(r"\b[A-Za-z]{3,9}\b", intake_text):
        k = token.lower()
        if k in MONTHS and MONTHS[k] not in months:
            months.append(MONTHS[k])
            
    if not months:
        months = ["February", "July"]
        
    return months

def extract_entry_requirements(soup):
    tab_intl = soup.find(id="tab-international")
    academic_text = ""
    english_text = ""
    
    if tab_intl:
        for h4 in tab_intl.find_all("h4"):
            h4_text = h4.get_text().strip()
            if "entry requirements" in h4_text.lower():
                siblings = []
                s = h4.next_sibling
                while s:
                    if s.name == "h4":
                        break
                    if s.name in ["p", "ul", "ol", "div"]:
                        siblings.append(s.get_text(strip=True))
                    s = s.next_sibling
                academic_text = " ".join(siblings)
            elif "english proficiency" in h4_text.lower():
                siblings = []
                s = h4.next_sibling
                while s:
                    if s.name == "h4":
                        break
                    if s.name in ["p", "ul", "ol", "div"]:
                        siblings.append(s.get_text(strip=True))
                    s = s.next_sibling
                english_text = " ".join(siblings)
                
    if not english_text:
        eng_el = soup.find(class_="admission-info-mid")
        if eng_el:
            english_text = eng_el.get_text(strip=True)
            
    if not academic_text:
        academic_text = "Admission to our undergraduate/postgraduate degree programs usually requires successful completion of a senior secondary school qualification or bachelor degree at the required level."
        
    raw_text = (
        f"Entry requirements: {academic_text}\n\n"
        f"English proficiency requirements: {english_text}"
    )
    
    # Try AI formatting
    try:
        formatted_html = format_requirements(raw_text)
        if formatted_html and formatted_html.strip():
            return formatted_html
    except Exception as e:
        print(f"AI Formatting failed: {e}")
        
    # Manual Fallback
    table_html = (
        "<table><tbody>"
        f"<tr><td><strong>Academic Requirements</strong></td><td><p>{academic_text}</p></td></tr>"
        f"<tr><td><strong>English Proficiency</strong></td><td><p>{english_text}</p></td></tr>"
        "</tbody></table>"
    )
    return table_html

async def block_resources(route):
    if route.request.resource_type in ["image", "media", "font", "stylesheet"]:
        await route.abort()
    else:
        await route.continue_()

async def scrape_course(page, url):
    url = url.strip()
    d = {"cricos": "", "title": "", "url": url, "course_description": "",
         "course_duration_per_week": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": []}
    try:
        # Load page content (resolve at DOMContentLoaded)
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        
        # Click view all start dates if present to expand
        try:
            buttons = await page.locator("button.additional-dates").all()
            for btn in buttons:
                if await btn.is_visible():
                    await btn.click()
                    await page.wait_for_timeout(200)
        except Exception:
            pass
            
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        
        # Title
        title_el = soup.find("h1")
        title = title_el.get_text(strip=True) if title_el else "Unknown Course"
        d["title"] = title
        
        # CRICOS Code
        cricos_el = soup.find("span", class_="degree-cricos-code")
        cricos = cricos_el.get_text(strip=True) if cricos_el else ""
        # Strip any trailing symbols/spaces
        cricos = re.sub(r"[^0-9A-Z]", "", cricos).strip()
        d["cricos"] = cricos
        
        if not cricos:
            print(f"⚠️ Skipped (no CRICOS found): {title} | {url}")
            return d
            
        d["course_description"] = clean_html(extract_course_description(soup))
        d["course_duration_per_week"] = extract_duration(soup)
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], d["enrolment_fee"], d["materials_fee"] = extract_fees(soup, d["course_duration_per_week"])
        d["entry_requirements"] = clean_html(extract_entry_requirements(soup))
        d["intake_months"] = extract_intake_months(soup)
        
        print(f"✅ {cricos} | {title} | {url}")
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        
    return d

async def run_scraper():
    os.makedirs(DIR, exist_ok=True)
    
    print("Launching Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        await page.route("**/*", block_resources)
        
        # 1. Discover all courses from sitemap
        sitemap_url = "https://www.newcastle.edu.au/designs/uon-2016/sitemaps/degrees-sitemap"
        print(f"Fetching sitemap {sitemap_url}...")
        try:
            await page.goto(sitemap_url, wait_until="domcontentloaded")
            sitemap_content = await page.content()
            soup = BeautifulSoup(sitemap_content, "xml")
            course_urls = []
            for loc in soup.find_all("loc"):
                u = loc.get_text().strip()
                if u.startswith("https://www.newcastle.edu.au/degrees") and u != "https://www.newcastle.edu.au/degrees":
                    course_urls.append(u)
            unique_urls = sorted(list(set(course_urls)))
            print(f"Discovered {len(unique_urls)} course URLs from sitemap.")
        except Exception as e:
            print(f"❌ Failed to fetch sitemap: {e}")
            await browser.close()
            return
            
        # 2. Scrape each discovered URL
        results = []
        for idx, url in enumerate(unique_urls):
            print(f"[{idx+1}/{len(unique_urls)}] ", end="")
            res = await scrape_course(page, url)
            results.append(res)
            
        await browser.close()
        
    # 3. Compile intake dates union
    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)
    if not intake_date:
        intake_date = "February, July"
        
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

def main():
    asyncio.run(run_scraper())

if __name__ == "__main__":
    main()
