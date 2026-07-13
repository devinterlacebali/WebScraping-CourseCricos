import os
import re
import sys
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from curl_cffi import requests

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- constants -----------------------------------------
PROVIDER_CODE = "00026A"
SLUG = "usyd"
DIR = "The University of Sydney"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- shared helpers -----------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

def clean_numeric_fee(val) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    try:
        n = float(v)
        return str(int(n)) if n.is_integer() else str(n)
    except:
        return "NULL"

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html: str) -> str:
    if not html:
        return ""
    frag = BeautifulSoup(html, "html.parser")
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

# --- parsing helpers ----------------------------------
def compile_description(explorer_data):
    content = explorer_data.get("content", {})
    overview = ""
    o_comp = content.get("course-overview", {})
    if o_comp and isinstance(o_comp, dict):
        overview = o_comp.get("summary", "")
    if not overview:
        about = content.get("nd-about-this-course", {})
        if about and isinstance(about, dict):
            overview = about.get("description", "") or about.get("subDescriptionRemove", "")
    
    structure = ""
    wys = content.get("course-what-will-you-study", {})
    if wys and isinstance(wys, dict):
        structure = wys.get("summary", "")
        
    opp = content.get("course-opportunities-rte", {})
    opp_text = ""
    if opp and isinstance(opp, dict):
        opp_text = opp.get("summary", "")
        
    desc = ""
    if overview:
        desc += f"<h4>Overview</h4>{sanitise(overview)}"
    if structure:
        desc += f"<h4>Structure</h4>{sanitise(structure)}"
    if opp_text:
        desc += f"<h4>Opportunities</h4>{sanitise(opp_text)}"
    return desc

def compile_requirements(core_data, explorer_data):
    content = explorer_data.get("content", {})
    admission_summary = ""
    adm = content.get("course-admission-requirement-rte", {})
    if adm and isinstance(adm, dict):
        admission_summary = adm.get("summary", "")
    
    int_scores = content.get("intEntryScores", {})
    atar = ""
    ib = ""
    gaokao = ""
    sat = ""
    if isinstance(int_scores, dict) and "collections" in int_scores:
        for item in int_scores.get("collections", []):
            code = item.get("code")
            score_2026 = item.get("2026") or item.get("2025")
            if code == "ATAR-INDICATOR":
                atar = score_2026
            elif code == "IB-INDICATOR":
                ib = score_2026
            elif code == "GAOKAO":
                gaokao = score_2026
            elif code == "USA-SAT":
                sat = score_2026
    
    academic_html = ""
    if admission_summary:
        academic_html += sanitise(admission_summary)
    
    scores_list = []
    if atar:
        scores_list.append(f"<li>ATAR: {atar}</li>")
    if ib:
        scores_list.append(f"<li>International Baccalaureate (IB): {ib}</li>")
    if gaokao and gaokao != "The selected qualification is not applicable for this course.":
        scores_list.append(f"<li>Gaokao: {gaokao}</li>")
    if sat:
        scores_list.append(f"<li>USA SAT: {sat}</li>")
        
    if scores_list:
        academic_html += "<p><strong>Commencing Indicative Scores:</strong></p><ul>" + "".join(scores_list) + "</ul>"
        
    attrs = core_data.get("attributes", {})
    entry_reqs = attrs.get("entryRequirements", {})
    english_list = []
    for year_req in entry_reqs.get("entryRequirementsByYear", []):
        if year_req.get("year") in (2026, 2027):
            for req in year_req.get("entryRequirements", []):
                desc = req.get("description")
                code_desc = req.get("codeDesc")
                if desc and code_desc:
                    english_list.append(f"<li>{code_desc}: {desc}</li>")
            if english_list:
                break
    
    english_html = ""
    if english_list:
        english_html = "<ul>" + "".join(english_list) + "</ul>"
    else:
        english_html = "<p>Please refer to the English language requirements page for details.</p>"
        
    table_html = "<table><tbody>"
    if academic_html:
        table_html += f"<tr><td><strong>Academic Requirements</strong></td><td>{academic_html}</td></tr>"
    if english_html:
        table_html += f"<tr><td><strong>English Proficiency</strong></td><td>{english_html}</td></tr>"
    table_html += "</tbody></table>"
    return table_html

def extract_commencing_fees(core_data):
    attrs = core_data.get("attributes", {})
    fee_summary = attrs.get("feeSummary", {})
    int_fee = "NULL"
    dom_fee = "NULL"
    for fby in fee_summary.get("feesByYear", []):
        if fby.get("year") in (2026, 2027):
            for fee in fby.get("fees", []):
                if fee.get("type") == "INTFEE" and fee.get("amount"):
                    int_fee = clean_numeric_fee(fee.get("amount"))
                elif fee.get("type") == "DOMCSP" and fee.get("amount"):
                    dom_fee = clean_numeric_fee(fee.get("amount"))
            if int_fee != "NULL" or dom_fee != "NULL":
                break
    return int_fee, dom_fee

def extract_intake_months(explorer_data):
    content = explorer_data.get("content", {})
    panel = content.get("nd-key-information-panel", {})
    months = []
    if isinstance(panel, dict):
        if panel.get("intSem1") or panel.get("domSem1"):
            months.append("February")
        if panel.get("intSem2") or panel.get("domSem2"):
            months.append("August")
    return months

def extract_duration(core_data):
    attrs = core_data.get("attributes", {})
    years = attrs.get("lengthInYear")
    if years:
        try:
            return str(int(float(years) * 52))
        except:
            pass
    return ""

# --- discover all courses via Coveo API ----------------
def discover_courses():
    print("Discovering courses via Coveo API...")
    url = "https://platform-ap-southeast-2.cloud.coveo.com/rest/search/v2"
    params = {
        "organizationId": "universityofsydneyproduction10somjans"
    }
    headers = {
        "Authorization": "Bearer xx3124d44f-146e-43cd-a3d5-af6a42a52f55",
        "Content-Type": "application/json"
    }
    
    courses = []
    first = 0
    step = 100
    
    while True:
        payload = {
            "searchHub": "courses-search",
            "q": "",
            "numberOfResults": step,
            "firstResult": first
        }
        try:
            r = requests.post(url, params=params, json=payload, headers=headers, impersonate="chrome120")
            if r.status_code != 200:
                print(f"Error fetching search results: {r.status_code} {r.text}")
                break
            data = r.json()
            results = data.get("results", [])
            if not results:
                break
            for item in results:
                title = item.get("title")
                click_uri = item.get("clickUri")
                courses.append({
                    "title": title,
                    "url": click_uri
                })
            print(f"  Fetched {len(courses)} courses...")
            if len(results) < step:
                break
            first += step
        except Exception as e:
            print("Error discovering courses:", e)
            break
            
    print(f"Total discovered courses: {len(courses)}")
    return courses

# --- async details fetcher -----------------------------
async def fetch_course_details(sem, client, course):
    url = course["url"]
    # Construct coredata and explorer paths
    base_path = url.replace(".html", "")
    core_url = base_path + ".coredata.json"
    exp_url = base_path + ".explorer.json"
    
    course_data = {
        "cricos": "",
        "title": course["title"],
        "url": url,
        "course_description": "",
        "course_duration_per_week": "",
        "offshore_tuition_fee": "NULL",
        "onshore_tuition_fee": "NULL",
        "enrolment_fee": "NULL",
        "materials_fee": "NULL",
        "entry_requirements": "",
        "apply_form": url,
        "intake_months": []
    }
    
    async with sem:
        # Fetch Coredata
        core_data = {}
        try:
            r = await client.get(core_url)
            if r.status_code == 200:
                core_data = r.json()
        except Exception as e:
            pass
            
        # Fetch Explorer
        explorer_data = {}
        try:
            r = await client.get(exp_url)
            if r.status_code == 200:
                explorer_data = r.json()
        except Exception as e:
            pass
            
        if core_data or explorer_data:
            attrs = core_data.get("attributes", {})
            cricos = attrs.get("cricosCode") or ""
            if cricos:
                course_data["cricos"] = str(cricos).strip()
            
            course_data["course_description"] = compile_description(explorer_data)
            course_data["entry_requirements"] = compile_requirements(core_data, explorer_data)
            course_data["course_duration_per_week"] = extract_duration(core_data)
            
            int_fee, dom_fee = extract_commencing_fees(core_data)
            course_data["offshore_tuition_fee"] = int_fee
            # onshore fee set to DOMCSP or NULL
            course_data["onshore_tuition_fee"] = dom_fee
            
            course_data["intake_months"] = extract_intake_months(explorer_data)
            print(f"Processed: {course['title']} | CRICOS: {course_data['cricos']}")
        else:
            print(f"Failed to fetch JSONs for: {course['title']}")
            
    return course_data

async def fetch_all_details(courses):
    sem = asyncio.Semaphore(15) # safe concurrency limit
    client = requests.AsyncSession(impersonate="chrome120")
    tasks = [fetch_course_details(sem, client, c) for c in courses]
    results = await asyncio.gather(*tasks)
    return results

# --- main ----------------------------------------------
def main():
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        
    discovered = discover_courses()
    if not discovered:
        print("No courses discovered. Exiting.")
        return
        
    results = asyncio.run(fetch_all_details(discovered))
    
    # Process intakes
    all_months = set()
    for r in results:
        all_months.update(r["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)
    if not intake_date:
        intake_date = "February, August" # USyd default semesters
        
    # Write SQL
    print(f"Writing SQL update queries to {SQL_PATH}...")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        for r in results:
            if not r["cricos"]:
                f.write(f"-- ⚠️ Skipped (no/unreliable CRICOS course code): {r['title']} | {r['url']}\n\n")
                continue
                
            clean_desc = clean_html(r["course_description"])
            clean_reqs = clean_html(r["entry_requirements"])
            
            f.write(f"UPDATE courses SET\n"
                    f"    course_description = '{clean_desc}',\n"
                    f"    course_duration_per_week = {r['course_duration_per_week'] or 'NULL'},\n"
                    f"    offshore_tuition_fee = {r['offshore_tuition_fee']},\n"
                    f"    onshore_tuition_fee = {r['onshore_tuition_fee']},\n"
                    f"    enrolment_fee = {r['enrolment_fee']},\n"
                    f"    materials_fee = {r['materials_fee']},\n"
                    f"    entry_requirements = '{clean_reqs}',\n"
                    f"    apply_form = '{r['apply_form']}',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
                    
    # Write Excel
    print(f"Writing Excel sheet to {EXCEL_PATH}...")
    def cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]
        
    pd.DataFrame([{
        "cricos": r["cricos"],
        "title": r["title"],
        "url": r["url"],
        "course_duration_per_week": int(r["course_duration_per_week"]) if str(r["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(r["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(r["onshore_tuition_fee"]),
        "enrolment_fee": cell(r["enrolment_fee"]),
        "materials_fee": cell(r["materials_fee"]),
        "intake": ", ".join(r["intake_months"]),
        "course_description": cell(r["course_description"]),
        "entry_requirements": cell(r["entry_requirements"]),
    } for r in results]).to_excel(EXCEL_PATH, index=False)
    
    print(f"\n✅ Finished. {len(results)} courses processed.")
    print(f"SQL update written to: {SQL_PATH}")
    print(f"Excel driver written to: {EXCEL_PATH}")

if __name__ == "__main__":
    main()
