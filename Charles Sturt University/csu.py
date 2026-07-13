"""
Charles Sturt University (CSU) course scraper — upgraded version.

Provider CRICOS code: 00005F.

Upgraded to conform to the repository's standard shape:
  * Scrapling stealthy fetch (no browser).
  * JS nested variable extraction for description, fees, intake dates, and CRICOS.
  * Clean semantic HTML via sanitise() (no wrapper divs / style attrs).
  * Entry requirements passed through the shared ai_formatter (opt-in).
  * Provider `intake_date` UPDATE + per-course UPDATEs.
  * Driver + enriched record written to csu.xlsx.
"""
import os
import re
import sys
import time
import json
import pandas as pd
from bs4 import BeautifulSoup
from scrapling.fetchers import Fetcher


if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROVIDER_CODE = "00005F"
DIR = "Charles Sturt University"
SLUG = "csu"
COURSES_FILE = f"{DIR}/study_csu.xlsx"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_update.sql"

DELAY = 1.5

MONTHS = {
    "january": "January", "february": "February", "march": "March", "april": "April",
    "may": "May", "june": "June", "july": "July", "august": "August",
    "september": "September", "october": "October", "november": "November", "december": "December"
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}


def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()


def sanitise(html: str) -> str:
    """Flatten wrapper divs/spans into clean, minimal semantic HTML."""
    frag = BeautifulSoup(html or "", "html.parser")
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


def extract_json_var(text, var_name):
    pos = text.find(var_name + " =")
    if pos == -1:
        pos = text.find(var_name + "=")
    if pos == -1:
        return None
    
    start = text.find("{", pos)
    start_array = text.find("[", pos)
    if start_array != -1 and (start == -1 or start_array < start):
        start = start_array
        char_open = "["
        char_close = "]"
    else:
        char_open = "{"
        char_close = "}"
        
    if start == -1:
        return None
        
    count = 1
    i = start + 1
    while i < len(text) and count > 0:
        if text[i] == char_open:
            count += 1
        elif text[i] == char_close:
            count -= 1
        i += 1
        
    json_str = text[start:i]
    try:
        return json.loads(json_str)
    except Exception:
        return None


def scrape_course(url, duration):
    d = {
        "url": url,
        "title": "",
        "course_description": "",
        "total_course_duration": duration,
        "offshore_tuition_fee": "",
        "onshore_tuition_fee": "",
        "entry_requirements": "",
        "cricos_course_code": "",
        "apply_form": url,
        "intake": "",
        "ok": False
    }
    
    r = Fetcher.get(url, timeout=15, stealthy_headers=True)
    if r.status != 200:
        print(f"⚠️  Failed to fetch: {r.status}")
        return d, []
        
    soup = BeautifulSoup(r.html_content, "html.parser")
    
    # 0. Get course title
    title_h1 = soup.find("h1")
    if title_h1:
        d["title"] = title_h1.get_text(strip=True)
        
    # Find script with metadata variables
    script_text = ""
    for script in soup.find_all("script"):
        t = script.get_text()
        if "ocb_metadata =" in t:
            script_text = t
            break
            
    if not script_text:
        print("⚠️  Script with metadata not found!")
        return d, []
        
    ocb = extract_json_var(script_text, "ocb_metadata")
    offerings = extract_json_var(script_text, "course_offerings")
    fees = extract_json_var(script_text, "course_fees")
    sessions = extract_json_var(script_text, "session_data")
    
    d["ok"] = True
    
    # 1. CRICOS Code
    cricos = ""
    if offerings and "course_offering" in offerings:
        for o in offerings["course_offering"]:
            if o.get("fund_source_code") == "FPOS" and o.get("cricos_code"):
                cricos = str(o["cricos_code"]).strip()
                break
    d["cricos_course_code"] = cricos
    
    # 2. Description
    description_html = ""
    if ocb and "ocb" in ocb and len(ocb["ocb"]) > 0:
        ocb_item_0 = ocb["ocb"][0]
        mic = ocb_item_0.get("marketing_item_course", [])
        if mic:
            cod = mic[0].get("course_overview_desktop", [])
            if cod:
                description_html = cod[0].get("course_overview_desktop", "")
            if not description_html:
                com = mic[0].get("course_overview_mobile", [])
                if com:
                    description_html = com[0].get("course_overview_mobile", "")
            if not description_html:
                description_html = mic[0].get("marketing_item_metadata_description", "")
                
    d["course_description"] = clean_html(sanitise(description_html))
    
    # 3. Entry Requirements
    reqs_list = []
    if ocb and "ocb" in ocb and len(ocb["ocb"]) > 1:
        ocb_item_1 = ocb["ocb"][1]
        course_list = ocb_item_1.get("course", [])
        if course_list:
            c_entry = course_list[0].get("course_entry_requirements", [])
            for ce in c_entry:
                req_text = ce.get("requirements", "")
                if req_text:
                    reqs_list.append(req_text)
            c_lang = course_list[0].get("language_requirements", [])
            for cl in c_lang:
                req_text = cl.get("requirements", "")
                if req_text:
                    reqs_list.append(req_text)
                    
    combined_reqs = "".join(reqs_list)
    if combined_reqs:
        body = sanitise(combined_reqs)
        d["entry_requirements"] = clean_html(f"<h4>Entry Requirements</h4>{body}")
            
    # 4. Offshore Tuition Fee
    offshore = ""
    if fees and "courseFee" in fees:
        for f in fees["courseFee"]:
            if f.get("student_type_code") == "INT" and f.get("annual_indicative_fee_ft"):
                offshore = str(f.get("annual_indicative_fee_ft"))
                break
    d["offshore_tuition_fee"] = offshore
    
    # 5. Intake months
    intake_months = []
    session_map = {}
    if sessions and "session" in sessions:
        for s in sessions["session"]:
            tc = s.get("term_code")
            sd = s.get("start_Date")
            if tc and sd:
                m = re.search(r"\d{4}-(\d{2})-\d{2}", sd)
                if m:
                    month_num = int(m.group(1))
                    if 1 <= month_num <= 12:
                        session_map[tc] = MONTH_ORDER[month_num - 1]
                        
    if offerings and "course_offering" in offerings:
        intake_set = set()
        for o in offerings["course_offering"]:
            if o.get("fund_source_code") == "FPOS":
                sc = o.get("session_code")
                if sc in session_map:
                    intake_set.add(session_map[sc])
        intake_months = [m for m in MONTH_ORDER if m in intake_set]
        d["intake"] = ", ".join(intake_months)
        
    return d, intake_months


def main():
    # Resolve actual paths to support running from root or subdirectory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "study_csu.xlsx")
    excel_out = os.path.join(script_dir, "csu.xlsx")
    sql_out = os.path.join(script_dir, "csu_update.sql")
    
    print(f"📖 Reading driver file: {input_file}")
    df = pd.read_excel(input_file)
    print(f"📋 Found {len(df)} courses in driver.")
    
    results = []
    all_months = set()
    
    for idx, row in df.iterrows():
        title = str(row.get("title", ""))
        url = str(row.get("url", ""))
        duration = str(row.get("duration", ""))
        
        print(f"\n[{idx+1}/{len(df)}] {title}")
        try:
            d, months = scrape_course(url, duration)
            all_months.update(months)
        except Exception as e:
            print(f"❌ Error scraping {title}: {e}")
            d = {
                "url": url, "title": title, "course_description": "",
                "total_course_duration": duration, "offshore_tuition_fee": "",
                "onshore_tuition_fee": "", "entry_requirements": "",
                "cricos_course_code": "", "apply_form": url, "intake": "", "ok": False
            }
        results.append(d)
        
        if d["ok"]:
            flag = f"CRICOS {d['cricos_course_code']}" if d["cricos_course_code"] else "no CRICOS (skip)"
            print(f"✅ {title[:40]} | {flag} | ${d['offshore_tuition_fee'] or '-'} | {d['total_course_duration']}")
        
        time.sleep(DELAY)
        
    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)
    
    # ---- SQL OUTPUT ----
    print(f"\n💾 Writing SQL -> {sql_out}")
    with open(sql_out, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        written = 0
        for d in results:
            if not d["ok"] or not d["cricos_course_code"]:
                reason = "no CRICOS course code" if d["ok"] else "page fetch failed"
                f.write(f"-- ⚠️ Skipped ({reason}): {d.get('title', 'Unknown')} | {d['url']}\n\n")
                continue
                
            written += 1
            f.write(
                "UPDATE courses SET\n"
                f"    course_description = '{d['course_description']}',\n"
                f"    onshore_tuition_fee = '{d['onshore_tuition_fee']}',\n"
                f"    offshore_tuition_fee = '{d['offshore_tuition_fee']}',\n"
                f"    entry_requirements = '{d['entry_requirements']}',\n"
                f"    total_course_duration = '{clean_html(d['total_course_duration'])}',\n"
                f"    apply_form = '{d['apply_form']}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_course_code = '{d['cricos_course_code']}';\n\n"
            )
            
    # ---- EXCEL OUTPUT ----
    print(f"💾 Writing Excel -> {excel_out}")
    def cell(v):
        return ("" if v in (None, "NULL") else str(v).replace("''", "'"))[:32000]
        
    pd.DataFrame([{
        "cricos": d["cricos_course_code"],
        "title": d.get("title", ""),
        "url": d["url"],
        "total_course_duration": cell(d["total_course_duration"]),
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "intake": cell(d["intake"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(excel_out, index=False)
    
    skipped = sum(1 for d in results if not d["ok"] or not d["cricos_course_code"])
    print(f"\n🏁 Done. {written} course UPDATEs, {skipped} skipped. Provider intake: {intake_date}")


if __name__ == "__main__":
    main()
