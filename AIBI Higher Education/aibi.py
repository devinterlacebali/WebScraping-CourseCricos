"""
AIBI Higher Education scraper (Scrapling).

  * No browser / no asyncio — pages are fetched over plain HTTP with
    Scrapling's Fetcher (TLS-fingerprint + stealth headers). All the AIBI
    content lives in the server HTML, so a headless browser is unnecessary.
  * Parsing uses Scrapling's Adaptor (css / xpath / children / attrib /
    html_content) instead of BeautifulSoup navigation. `adaptive=True` is
    used on the section headings so the scraper self-heals if AIBI reshuffles
    its Elementor widgets.

Output: aibi_courses_update.sql
"""
import os
import re
import sys
import pandas as pd
from bs4 import BeautifulSoup            # only used to sanitise small HTML fragments
from scrapling.fetchers import Fetcher

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROVIDER_CODE = "03844J"
FEES_URL = "https://aibi.edu.au/fees-and-payments/"
ENROLMENT_FEE = "250"

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December", "january": "January",
    "february": "February", "march": "March", "april": "April", "june": "June",
    "july": "July", "august": "August", "september": "September",
    "october": "October", "november": "November", "december": "December",
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

DESC_HEADING_MATCHERS = [
    ("what is", "Course Overview"),
    ("course learning outcomes", "Course Learning Outcomes"),
    ("career pathways", "Career Pathways"),
    ("course subjects", "Course Subjects"),
    ("year ", None),
]
DESC_DROP_PREFIXES = ("aqf level", "fees & scholarships", "jump to", "learn more")

WIDGET_XPATH = (
    "//div[contains(@class,'elementor-widget-heading') "
    "or contains(@class,'elementor-widget-text-editor') "
    "or contains(@class,'elementor-widget-icon-list') "
    "or contains(@class,'elementor-widget-n-accordion') "
    "or contains(@class,'elementor-widget-icon-box')][not(ancestor::details)]"
)

# ---------- helpers ----------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

def clean_numeric_fee(val: str) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    val_clean = re.sub(r"[^\d\.]", "", str(val))
    if not val_clean:
        return "NULL"
    num = float(val_clean)
    return str(int(num)) if num.is_integer() else str(num)

def _sanitise(html: str) -> str:
    frag = BeautifulSoup(html, "html.parser")
    for tag in frag.find_all(["style", "script", "noscript", "form", "iframe", "button", "img", "svg"]):
        tag.decompose()
    for s in frag.find_all("summary"):
        if s.get_text(strip=True).lower() in ("read more", "read less"):
            s.decompose()
    for tag in frag.find_all(True):
        for attr in list(tag.attrs):
            if attr != "href":
                del tag[attr]
    return str(frag)

def _norm_title(s):
    s = re.sub(r"\b(in|of|the|and|a)\b", " ", s.lower())
    return re.sub(r"[^a-z0-9]", "", s)

def _txt(el):
    return re.sub(r"\s+", " ", el.get_all_text()).strip()

def _classes(el):
    return el.attrib.get("class") or ""

# ---------- fee maps (International -> offshore, Domestic -> onshore) ----------
def build_fee_maps(page):
    tabs = page.css("[role=tab]")
    def label_for(panel):
        lab = panel.attrib.get("aria-labelledby")
        pid = panel.attrib.get("id")
        for t in tabs:
            if t.attrib.get("id") == lab or t.attrib.get("aria-controls") == pid:
                return _txt(t)
        return ""
    offshore, onshore = {}, {}
    for panel in page.css("[role=tabpanel]"):
        label = label_for(panel)
        if "International" in label:
            target = offshore
        elif "Domestic" in label:
            target = onshore
        else:
            continue
        for table in panel.css("table"):
            for tr in table.css("tr")[1:]:
                tds = tr.css("td")
                if len(tds) >= 2:
                    target[_norm_title(_txt(tds[0]))] = clean_numeric_fee(_txt(tds[1]))
    return offshore, onshore

# ---------- description (heading-bucketed) ----------
def extract_course_description(page):
    widgets = page.xpath(WIDGET_XPATH, adaptive=True)
    buckets = []
    current = None
    for w in widgets:
        cls = _classes(w)
        text = _txt(w)
        if "elementor-widget-heading" in cls:
            low = text.lower()
            if low.startswith(("industry insights", "how to apply", "frequently asked", "about aibi")):
                current = None
                continue
            matched = None
            for prefix, label in DESC_HEADING_MATCHERS:
                if low.startswith(prefix):
                    matched = label if label else text
                    break
            if matched:
                current = matched
                buckets.append((current, []))
            else:
                current = None
            continue
        if current is None or not text:
            continue
        if text.lower().startswith(DESC_DROP_PREFIXES):
            continue
        buckets[-1][1].append(w.html_content)

    desc = ""
    for label, parts in buckets:
        body = "".join(parts)
        if body and BeautifulSoup(body, "html.parser").get_text(strip=True):
            desc += f"<h4>{label}</h4>{_sanitise(body)}"
    return clean_html(desc)

# ---------- entry requirements (International tab -> Eligibility Criteria) ----------
def extract_entry_requirements(page):
    tabs = page.css("[role=tab]")
    def label_for(panel):
        lab = panel.attrib.get("aria-labelledby")
        pid = panel.attrib.get("id")
        for t in tabs:
            if t.attrib.get("id") == lab or t.attrib.get("aria-controls") == pid:
                return _txt(t)
        return ""
    for panel in page.css("[role=tabpanel]"):
        if "International" not in label_for(panel) or "Eligibility" not in panel.get_all_text():
            continue
        for w in panel.css("div.elementor-widget-text-editor"):
            if "Eligibility Criteria" not in w.get_all_text():
                continue
            cont = w.css(".elementor-widget-container")
            cont = cont[0] if cont else w
            parts, keep = [], False
            for ch in cont.children:
                if not keep and _txt(ch).lower().startswith("eligibility criteria"):
                    keep = True
                if keep:
                    parts.append(ch.html_content)
            body = "".join(parts) if parts else cont.html_content
            return clean_html(f"<h4>Entry Requirements</h4>{_sanitise(body)}")
    return ""

# ---------- header fields ----------
def extract_duration(full_text):
    m = re.search(r"Course Duration\s*(.{0,80})", full_text, re.IGNORECASE)
    if not m:
        return ""
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

# ---------- per-course ----------
def scrape_course(row, offshore_map, onshore_map):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    if cricos.lower() in ("nan", "none", "null"):
        cricos = ""
    title = str(row["title"]).strip()

    data = {
        "cricos": cricos, "title": title, "url": url,
        "course_description": "", "total_course_duration": "",
        "offshore_tuition_fee": offshore_map.get(_norm_title(title), "NULL"),
        "onshore_tuition_fee": onshore_map.get(_norm_title(title), "NULL"),
        "enrolment_fee": ENROLMENT_FEE, "materials_fee": "NULL",
        "entry_requirements": "", "apply_form": url, "intake_months": [],
    }
    try:
        page = Fetcher.get(url, stealthy_headers=True)
        full_text = re.sub(r"\s+", " ", page.get_all_text())
        data["course_description"] = extract_course_description(page)
        data["entry_requirements"] = extract_entry_requirements(page)
        data["total_course_duration"] = extract_duration(full_text)
        data["intake_months"] = extract_intake_months(full_text)
        print(f"✅ Scraped successfully: {url}")
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
    return data

# ---------- main ----------
def main():
    excel_path = "AIBI Higher Education/aibi.xlsx"
    sql_path = "AIBI Higher Education/aibi_courses_update.sql"

    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return

    df = pd.read_excel(excel_path)

    offshore_map, onshore_map = {}, {}
    try:
        offshore_map, onshore_map = build_fee_maps(Fetcher.get(FEES_URL, stealthy_headers=True))
        print(f"Loaded {len(offshore_map)} offshore + {len(onshore_map)} onshore tuition fees.")
    except Exception as e:
        print(f"⚠️ Could not load fees page: {e}")

    results = []
    for idx, row in df.iterrows():
        print(f"\n[{idx+1}/{len(df)}] Scraping: {row['url']}")
        results.append(scrape_course(row, offshore_map, onshore_map))

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
    onshore_tuition_fee = {d["onshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    materials_fee = {d["materials_fee"]},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")

    # Write the full scraped record back to the Excel (keeps cricos/title/url as the driver)
    def _cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]  # Excel hard-caps cells at 32,767 chars
    enriched = [{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "total_course_duration": d["total_course_duration"],
        "offshore_tuition_fee": _cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": _cell(d["onshore_tuition_fee"]),
        "enrolment_fee": _cell(d["enrolment_fee"]),
        "materials_fee": _cell(d["materials_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": _cell(d["course_description"]),
        "entry_requirements": _cell(d["entry_requirements"]),
    } for d in results]
    pd.DataFrame(enriched).to_excel(excel_path, index=False)

    print(f"\n✅ Finished! Scraped {len(results)} courses. Intake: {intake_date}")
    print(f"SQL updates saved to {sql_path}")
    print(f"Excel record updated at {excel_path}")

if __name__ == "__main__":
    main()
