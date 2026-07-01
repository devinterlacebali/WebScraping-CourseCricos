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

PROVIDER_CODE = "03844J"
FEES_URL = "https://aibi.edu.au/fees-and-payments/"
# International application processing fee (per the Fees & Payments page)
ENROLMENT_FEE = "250"

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December",
    "january": "January", "february": "February", "march": "March",
    "april": "April", "june": "June", "july": "July", "august": "August",
    "september": "September", "october": "October", "november": "November",
    "december": "December",
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# Heading buckets to keep for the course description
DESC_HEADING_MATCHERS = [
    ("what is", "Course Overview"),
    ("course learning outcomes", "Course Learning Outcomes"),
    ("career pathways", "Career Pathways"),
    ("course subjects", "Course Subjects"),
    ("year ", None),  # keep original label (e.g. "Year 1 (Level 100)")
]
# Content widgets to drop from description buckets (noise)
DESC_DROP_PREFIXES = ("aqf level", "fees & scholarships", "jump to", "learn more")

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
    num = float(val_clean)
    return str(int(num)) if num.is_integer() else str(num)

# === SANITISE HTML ===
def _sanitise(html: str) -> str:
    frag = BeautifulSoup(html, "html.parser")
    for tag in frag.find_all(["style", "script", "noscript", "form", "iframe", "button", "img", "svg"]):
        tag.decompose()
    # Drop "Read More" summary labels but keep the accordion body
    for s in frag.find_all("summary"):
        if s.get_text(strip=True).lower() in ("read more", "read less"):
            s.decompose()
    for tag in frag.find_all(True):
        for attr in list(tag.attrs):
            if attr in ("href",):
                continue
            del tag[attr]
    return str(frag)

def _norm_title(s):
    s = re.sub(r"\b(in|of|the|and|a)\b", " ", s.lower())
    return re.sub(r"[^a-z0-9]", "", s)

# === BUILD INTERNATIONAL TUITION FEE MAP FROM THE FEES PAGE ===
def build_fee_map(fees_html):
    soup = BeautifulSoup(fees_html, "html.parser")
    tab_titles = {}
    for tab in soup.find_all(attrs={"role": "tab"}):
        key = tab.get("aria-controls") or tab.get("id")
        tab_titles[key] = re.sub(r"\s+", " ", tab.get_text(" ", strip=True))
    fee_map = {}
    for table in soup.find_all("table"):
        panel = table.find_parent(attrs={"role": "tabpanel"})
        label = None
        if panel:
            label = tab_titles.get(panel.get("id")) or tab_titles.get(panel.get("aria-labelledby"))
        if not (label and "International" in label):
            continue
        for tr in table.find_all("tr")[1:]:
            tds = tr.find_all("td")
            if len(tds) >= 2:
                name = _norm_title(tds[0].get_text(" ", strip=True))
                fee_map[name] = clean_numeric_fee(tds[1].get_text())
    return fee_map

# === ORDERED CONTENT WIDGETS OF THE MAIN COURSE BODY ===
def _iter_widgets(soup):
    wanted = ("elementor-widget-heading", "elementor-widget-text-editor",
              "elementor-widget-icon-list", "elementor-widget-n-accordion",
              "elementor-widget-icon-box")
    for w in soup.find_all("div", class_=lambda c: c and any(k in c for k in wanted)):
        # Skip widgets nested inside an accordion body (they duplicate its content)
        if w.find_parent("details") is not None:
            continue
        cls = [c for c in w.get("class", []) if c.startswith("elementor-widget-")
               and c not in ("elementor-widget", "elementor-widget-container")]
        typ = cls[0].replace("elementor-widget-", "") if cls else "?"
        yield typ, w

# === EXTRACT COURSE DESCRIPTION (heading-bucketed) ===
def extract_course_description(soup):
    buckets = []           # (label, [html, ...])
    current_label = None
    started = False
    for typ, w in _iter_widgets(soup):
        text = re.sub(r"\s+", " ", w.get_text(" ", strip=True))
        if typ == "heading":
            low = text.lower()
            if low.startswith("what is") or text:
                started = started or low.startswith("what is")
            # Stop once we reach the tail sections
            if low.startswith(("industry insights", "how to apply", "frequently asked", "about aibi")):
                current_label = None
                continue
            matched = None
            for prefix, label in DESC_HEADING_MATCHERS:
                if low.startswith(prefix):
                    matched = label if label else text
                    break
            if matched:
                current_label = matched
                buckets.append((current_label, []))
            else:
                current_label = None
            continue
        if current_label is None or not text:
            continue
        if text.lower().startswith(DESC_DROP_PREFIXES):
            continue
        buckets[-1][1].append(str(w))

    desc = ""
    for label, parts in buckets:
        body = "".join(parts)
        if body and BeautifulSoup(body, "html.parser").get_text(strip=True):
            desc += f"<h4>{label}</h4>{_sanitise(body)}"
    return clean_html(desc)

# === EXTRACT ENTRY REQUIREMENTS (International tab -> Eligibility Criteria) ===
def extract_entry_requirements(soup):
    tab_titles = {}
    for tab in soup.find_all(attrs={"role": "tab"}):
        key = tab.get("aria-controls") or tab.get("id")
        tab_titles[key] = re.sub(r"\s+", " ", tab.get_text(" ", strip=True))
    for panel in soup.find_all(attrs={"role": "tabpanel"}):
        label = tab_titles.get(panel.get("id")) or tab_titles.get(panel.get("aria-labelledby"))
        if not (label and "International" in label):
            continue
        if "Eligibility" not in panel.get_text():
            continue
        for w in panel.find_all("div", class_=lambda c: c and "elementor-widget-text-editor" in c):
            if "Eligibility Criteria" not in w.get_text():
                continue
            cont = w.find(class_="elementor-widget-container") or w
            # Keep only from the "Eligibility Criteria" heading onward (drop the Fees preamble)
            parts, keep = [], False
            for ch in cont.find_all(recursive=False):
                if not keep and ch.get_text(strip=True).lower().startswith("eligibility criteria"):
                    keep = True
                if keep:
                    parts.append(str(ch))
            body = "".join(parts) if parts else str(cont)
            return clean_html(f"<h4>Entry Requirements</h4>{_sanitise(body)}")
    return ""

# === HEADER FIELD EXTRACTORS ===
def extract_duration(full_text):
    m = re.search(r"Course Duration\s*(.{0,80})", full_text, re.IGNORECASE)
    if not m:
        return ""
    # First "N years / N months" figure in the duration phrase (full-time)
    d = re.search(r"(\d+(?:\.\d+)?)\s*(years?|months?)", m.group(1), re.IGNORECASE)
    return f"{d.group(1)} {d.group(2).lower()}" if d else ""

def extract_intake_months(full_text):
    m = re.search(r"Next Start Date\s*(.*?)(?:Fees|AQF|Study Mode|Campus|Apply|CRICOS|$)",
                  full_text, re.IGNORECASE)
    if not m:
        return []
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", m.group(1)):
        key = tok.lower()
        if key in MONTHS and MONTHS[key] not in found:
            found.append(MONTHS[key])
    return found

# === SCRAPE PER COURSE ===
async def scrape_course(row, browser, fee_map):
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
        "offshore_tuition_fee": fee_map.get(_norm_title(title), "NULL"),
        "enrolment_fee": ENROLMENT_FEE,
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

        data["course_description"] = extract_course_description(soup)
        data["entry_requirements"] = extract_entry_requirements(soup)
        data["total_course_duration"] = extract_duration(full_text)
        data["intake_months"] = extract_intake_months(full_text)

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
    excel_path = "AIBI Higher Education/aibi.xlsx"
    sql_path = "AIBI Higher Education/aibi_courses_update.sql"

    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return

    df = pd.read_excel(excel_path)
    results = []

    async with async_playwright() as p:
        headless_env = os.environ.get("SCRAPER_HEADLESS", "True")
        headless_val = True if headless_env.lower() in ("true", "1") else False

        browser = await p.chromium.launch(headless=headless_val)

        # Build the international tuition-fee map from the central fees page
        fee_map = {}
        try:
            fpage = await browser.new_page()
            await fpage.goto(FEES_URL, wait_until="domcontentloaded", timeout=60000)
            await fpage.wait_for_timeout(2000)
            fee_map = build_fee_map(await fpage.content())
            await fpage.close()
            print(f"Loaded {len(fee_map)} international tuition fees.")
        except Exception as e:
            print(f"⚠️ Could not load fees page: {e}")

        for idx, row in df.iterrows():
            print(f"\n[{idx+1}/{len(df)}] Scraping: {row['url']}")
            course_data = await scrape_course(row, browser, fee_map)
            results.append(course_data)

        await browser.close()

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
                f.write(f"-- ⚠️ Skipped (no/unreliable CRICOS course code): {d['title']} | {d['url']}\n\n")
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
