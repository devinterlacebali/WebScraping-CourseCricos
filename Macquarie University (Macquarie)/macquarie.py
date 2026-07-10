import os
import re
import sys
import json
import asyncio
import pandas as pd
from playwright.async_api import async_playwright

# Shared AI formatter (repo root) — optional
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
try:
    import ai_formatter
except Exception:
    ai_formatter = None

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROVIDER_CODE = "00002J"
EXCEL_PATH = "Macquarie University (Macquarie)/macquarie.xlsx"
SQL_PATH = "Macquarie University (Macquarie)/macquarie_update.sql"

# Allowed HTML tags for sanitisation
ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5", "table", "thead", "tbody", "tr", "td", "th"}

def safe_print(msg):
    # Safe printing to avoid Windows encoding crashes
    print(str(msg).encode('ascii', 'ignore').decode('ascii'))

# ---------- Helpers ----------
def clean_html(html: str) -> str:
    if not html:
        return ""
    # Replace smart quotes/dashes to be safe and clean spacing
    html = html.replace("’", "'").replace("‘", "'").replace("–", "-")
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

def clean_numeric_fee(val) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def sanitise(html: str) -> str:
    """Flatten wrapper divs/spans and clean HTML tags into minimal semantic HTML."""
    from bs4 import BeautifulSoup
    if not html:
        return ""
    
    frag = BeautifulSoup(html, "html.parser")
    # Drop styling, scripts, images, etc.
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
        
    # Strip attributes except href
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
                
    # Unwrap spans
    for t in frag.find_all("span"):
        t.unwrap()
        
    # Normalise divs
    while True:
        div = frag.find("div")
        if div is None:
            break
        if div.find(["p", "ul", "ol", "li", "div", "table", "h5"]):
            div.unwrap()
        else:
            div.name = "p"
            
    # Bold short label paragraphs ending in ':'
    for p in frag.find_all("p"):
        s = p.get_text(strip=True)
        if s.endswith(":") and len(s) < 60 and not p.find(["strong", "b", "a"]):
            p.string = ""
            strong = frag.new_tag("strong")
            strong.string = s
            p.append(strong)
            
    # Drop unallowed tags
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
            
    # Drop empty elements
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
            
    return str(frag)

# ---------- Scraping Process ----------
async def scrape_all_courses():
    if not os.path.exists(EXCEL_PATH):
        safe_print(f"❌ Driver excel not found: {EXCEL_PATH}")
        return
        
    df = pd.read_excel(EXCEL_PATH)
    all_results = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Navigate to a base page first to establish cookies & Cloudflare validation
        safe_print("Establishing Cloudflare session with base page...")
        await page.goto("https://www.mq.edu.au/study/find-a-course", wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)
        
        for idx, row in df.iterrows():
            url = str(row["url"]).strip()
            orig_title = str(row["title"]).strip()
            
            # Construct Gatsby page-data.json URL
            cleaned_url = url
            if cleaned_url.endswith("/"):
                cleaned_url = cleaned_url[:-1]
                
            slug = cleaned_url.split("/study/find-a-course/courses/")[-1]
            json_url = f"https://www.mq.edu.au/study/page-data/find-a-course/courses/{slug}/page-data.json"
            
            safe_print(f"\n[{idx+1}/{len(df)}] Fetching: {orig_title}")
            
            try:
                # Fetch JSON in browser context
                json_str = await page.evaluate("""async (url) => {
                    const res = await fetch(url);
                    if (!res.ok) throw new Error(`HTTP ${res.status}`);
                    return await res.text();
                }""", json_url)
                
                data = json.loads(json_str)
                res = data.get("result") or {}
                res_data = res.get("data") or {}
                current = res_data.get("current") or {}
                fields = current.get("fields") or {}
                nested_json_str = fields.get("json")
                if not nested_json_str:
                    raise KeyError("fields['json'] is missing or empty")
                
                details = json.loads(nested_json_str)
                
                # 1. Course details
                title = details.get("title") or details.get("search_title") or orig_title
                cricos = details.get("cricos_code", "").strip()
                
                # 2. Duration
                dur_label = details.get("course_duration_in_years", {}).get("label", "")
                
                # 3. Fees
                offshore_fee = "NULL"
                for fee_item in details.get("fees", []):
                    fee_type_val = fee_item.get("fee_type", {}).get("value", "")
                    if "international" in fee_type_val.lower():
                        estimated = fee_item.get("estimated_annual_fee")
                        if estimated:
                            offshore_fee = clean_numeric_fee(estimated)
                            break
                            
                # 4. Description
                desc_html = ""
                marketing_items = details.get("marketing_items")
                descriptions_list = []
                if isinstance(marketing_items, dict):
                    descriptions_list = marketing_items.get("descriptions") or []
                elif isinstance(marketing_items, list):
                    for item in marketing_items:
                        if isinstance(item, dict) and "descriptions" in item:
                            descriptions_list.extend(item.get("descriptions") or [])
                
                # Look specifically for the 'Long Description' object
                for d in descriptions_list:
                    desc_type = d.get("description_type", {}).get("value", "")
                    if "long" in desc_type.lower() and d.get("long_description"):
                        desc_html = d["long_description"]
                        break
                        
                # Fallback: find any item in the list that has a long_description
                if not desc_html:
                    for d in descriptions_list:
                        if d.get("long_description"):
                            desc_html = d["long_description"]
                            break
                            
                # Final fallback
                if not desc_html:
                    desc_html = details.get("overview_and_aims_of_the_course") or ""
                    
                # 5. Entry Requirements
                req_parts = []
                selection_rank = details.get("selection_rank")
                if selection_rank:
                    req_parts.append(f"<p><strong>Minimum Academic Requirements:</strong> Selection Rank of {selection_rank} (or equivalent).</p>")
                
                ielts_overall = details.get("ielts_overall_score")
                if ielts_overall:
                    ielts_sub = (
                        f"Minimum {details.get('ielts_reading_score', '6.0')} in reading, "
                        f"{details.get('ielts_writing_score', '6.0')} in writing, "
                        f"{details.get('ielts_listening_score', '6.0')} in listening, "
                        f"and {details.get('ielts_speaking_score', '6.0')} in speaking."
                    )
                    req_parts.append(f"<p><strong>English Language Requirements:</strong> IELTS overall score of {ielts_overall} ({ielts_sub}).</p>")
                
                assumed = details.get("assumed_knowledge")
                if assumed:
                    req_parts.append(f"<p><strong>Assumed Knowledge:</strong> {assumed.strip()}</p>")
                    
                recommended = details.get("recommended_studies")
                if recommended:
                    req_parts.append(f"<p><strong>Recommended Studies:</strong> {recommended.strip()}</p>")
                    
                other_reqs = details.get("other_requirements")
                if other_reqs:
                    req_parts.append(f"<p><strong>Other Requirements:</strong> {other_reqs.strip()}</p>")
                    
                entry_reqs_html = "\n".join(req_parts)
                
                final_requirements = ""
                if entry_reqs_html:
                    if ai_formatter is not None and ai_formatter.enabled():
                        try:
                            from bs4 import BeautifulSoup
                            plain = re.sub(r"\s+", " ", BeautifulSoup(entry_reqs_html, "html.parser").get_text(" ", strip=True))
                            table = ai_formatter.format_requirements(plain)
                            if table:
                                final_requirements = clean_html(f"<h4>Entry Requirements</h4>{table}")
                        except Exception as e:
                            safe_print(f"  ⚠️ AI Requirements Formatter error: {e}")
                    if not final_requirements:
                        final_requirements = clean_html(sanitise(entry_reqs_html))
                
                # 6. Intakes
                intakes = []
                for offer in details.get("offering", []):
                    cal = offer.get("admission_calendar")
                    if cal:
                        # Map Session X to standard month names if possible
                        if "Session 1" in cal:
                            intakes.append("February")
                        elif "Session 2" in cal:
                            intakes.append("July")
                        else:
                            intakes.append(cal)
                intakes = sorted(list(set(intakes)))
                intake_desc = ", ".join(intakes) if intakes else "February, July"
                
                all_results.append({
                    "cricos": cricos,
                    "title": title,
                    "url": url,
                    "course_description": clean_html(sanitise(desc_html)),
                    "total_course_duration": clean_html(dur_label),
                    "offshore_tuition_fee": offshore_fee,
                    "onshore_tuition_fee": offshore_fee,
                    "enrolment_fee": "NULL",
                    "materials_fee": "NULL",
                    "entry_requirements": final_requirements,
                    "apply_form": url,
                    "intake_desc": intake_desc
                })
                
                safe_print(f"  ✅ Scraped {title} | CRICOS: {cricos} | Fee: {offshore_fee}")
                
            except Exception as e:
                safe_print(f"  ❌ Error: {e}")
                # Append fallback row so we don't lose the record in driver
                all_results.append({
                    "cricos": "",
                    "title": orig_title,
                    "url": url,
                    "course_description": "",
                    "total_course_duration": "",
                    "offshore_tuition_fee": "NULL",
                    "onshore_tuition_fee": "NULL",
                    "enrolment_fee": "NULL",
                    "materials_fee": "NULL",
                    "entry_requirements": "",
                    "apply_form": url,
                    "intake_desc": ""
                })
                
            # Cooperative delay
            await asyncio.sleep(0.05)
            
        await browser.close()
        
    # ---------- Output Generation ----------
    
    # 1. Generate SQL update script
    safe_print(f"\n💾 Generating SQL file: {SQL_PATH}")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution intakes\n"
                "UPDATE provider_institution SET\n"
                "    intake_date = 'February, July',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        for q in all_results:
            if not q["cricos"]:
                f.write(f"-- ⚠️ Skipped (no CRICOS code found or domestic-only): {q['title']} | {q['url']}\n\n")
                continue
                
            f.write(f"UPDATE courses SET\n"
                    f"    course_description = '{q['course_description']}',\n"
                    f"    total_course_duration = '{q['total_course_duration']}',\n"
                    f"    offshore_tuition_fee = {q['offshore_tuition_fee']},\n"
                    f"    onshore_tuition_fee = {q['onshore_tuition_fee']},\n"
                    f"    enrolment_fee = {q['enrolment_fee']},\n"
                    f"    materials_fee = {q['materials_fee']},\n"
                    f"    entry_requirements = '{q['entry_requirements']}',\n"
                    f"    apply_form = '{q['apply_form']}',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{q['cricos']}';\n\n")
                    
    # 2. Enrich driver Excel file
    safe_print(f"💾 Saving Excel file: {EXCEL_PATH}")
    
    def _cell(v):
        # Clean helper for Excel strings
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]
        
    enriched = []
    for q in all_results:
        enriched.append({
            "cricos": q["cricos"],
            "title": q["title"],
            "url": q["url"],
            "total_course_duration": _cell(q["total_course_duration"]),
            "offshore_tuition_fee": _cell(q["offshore_tuition_fee"]),
            "onshore_tuition_fee": _cell(q["onshore_tuition_fee"]),
            "enrolment_fee": _cell(q["enrolment_fee"]),
            "materials_fee": _cell(q["materials_fee"]),
            "intake": _cell(q["intake_desc"]),
            "course_description": _cell(q["course_description"]),
            "entry_requirements": _cell(q["entry_requirements"])
        })
        
    pd.DataFrame(enriched).to_excel(EXCEL_PATH, index=False)
    safe_print("\n🏁 Scrape finished successfully!")

if __name__ == "__main__":
    asyncio.run(scrape_all_courses())
