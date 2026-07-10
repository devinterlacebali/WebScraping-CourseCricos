import os
import re
import sys
import pandas as pd
from bs4 import BeautifulSoup, Comment
from scrapling.fetchers import Fetcher

# Shared AI formatter (repo root) — optional, opt-in via OPENROUTER_API_KEY
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

PROVIDER_CODE = "00001K"
EXCEL_PATH = "Canberra Institute of Technology/cit.xlsx"
SQL_PATH = "Canberra Institute of Technology/cit_courses_update.sql"

# Allowed tags for HTML sanitisation
ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5", "table", "thead", "tbody", "tr", "td", "th"}

# ---------- helpers ----------
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
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def sanitise(html: str) -> str:
    """Flatten wrapper divs/spans into clean, minimal semantic HTML."""
    frag = BeautifulSoup(html, "html.parser")
    # Drop non-content tags outright
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
    # Strip every attribute except href
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    # Unwrap inline wrappers
    for t in frag.find_all("span"):
        t.unwrap()
    # Normalise <div>: wrapper (has block children) -> unwrap; text-only -> <p>
    while True:
        div = frag.find("div")
        if div is None:
            break
        if div.find(["p", "ul", "ol", "li", "div", "table", "h5"]):
            div.unwrap()
        else:
            div.name = "p"
    # Bold short label paragraphs ending in ':' (e.g. "Academic requirement:")
    for p in frag.find_all("p"):
        s = p.get_text(strip=True)
        if s.endswith(":") and len(s) < 60 and not p.find(["strong", "b", "a"]):
            p.string = ""
            strong = frag.new_tag("strong")
            strong.string = s
            p.append(strong)
    # Drop leftover unknown tags (keep their text) and empty elements
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def extract_fee(tuition_html, qual_name):
    """Smart parser to match fee description with qualification name and extract total qualification fee."""
    if not tuition_html:
        return "NULL"
    
    # Normalise qual_name to compare keywords
    q_tokens = set(re.findall(r"[a-z0-9]+", qual_name.lower()))
    # Remove generic keywords to focus on core qualification level/subject
    q_tokens -= {"of", "in", "and", "management", "hospitality", "science", "arts", "support", "services", "health"}
    
    soup = BeautifulSoup(tuition_html, "html.parser")
    # Extract blocks of texts
    paragraphs = []
    for tag in soup.find_all(["p", "div", "li", "strong"]):
        text = tag.get_text(" ", strip=True)
        if text and text not in paragraphs:
            paragraphs.append(text)
            
    # Find paragraphs that match the qualification name best
    best_match_idx = -1
    max_overlap = 0
    for idx, p in enumerate(paragraphs):
        p_tokens = set(re.findall(r"[a-z0-9]+", p.lower()))
        overlap = len(q_tokens.intersection(p_tokens))
        if overlap > max_overlap:
            max_overlap = overlap
            best_match_idx = idx
            
    # Search from matching index onwards
    search_range = paragraphs[best_match_idx:] if best_match_idx != -1 else paragraphs
    
    # 1. Look for total qualification fee
    for p_text in search_range[:3]:
        m_total = re.search(r"total.*?fee.*?\$\s*([\d,]+)", p_text, re.I)
        if m_total:
            return clean_numeric_fee(m_total.group(1))
            
    # 2. Look for any price in the format $XX,XXX
    for p_text in search_range[:3]:
        m_any = re.search(r"\$\s*([\d,]{3,7})", p_text)
        if m_any:
            return clean_numeric_fee(m_any.group(1))
            
    return "NULL"

def extract_materials_fee(extra_html):
    """Extracts materials fee from the extra fees block."""
    if not extra_html:
        return "NULL"
    soup = BeautifulSoup(extra_html, "html.parser")
    text = soup.get_text(" ", strip=True)
    m = re.search(r"material.*?fee[s]*.*?\$\s*([\d,]+)", text, re.I) or \
        re.search(r"material.*?\$\s*([\d,]+)", text, re.I) or \
        re.search(r"equipment.*?\$\s*([\d,]+)", text, re.I)
    return clean_numeric_fee(m.group(1)) if m else "NULL"

# ---------- scraping single page ----------
def scrape_cit_page(url):
    print(f"🌐 Fetching page: {url}")
    qualifications = []
    
    try:
        page = Fetcher.get(url, stealthy_headers=True)
        html = page.html_content
        soup = BeautifulSoup(html, "html.parser")
        
        # 1. Extract Main Title and Course Description parent container
        title_elem = soup.find("h1", class_="fz-38") or soup.find("h1")
        main_title = title_elem.get_text(strip=True) if title_elem else "Course Page"
        
        desc_container = soup.find("div", class_="pr-md-5")
        description_html = ""
        if desc_container:
            # Clone desc_container to prevent modifying main page DOM
            desc_copy = BeautifulSoup(str(desc_container), "html.parser")
            # Remove title
            for h in desc_copy.find_all("h1"):
                h.decompose()
            # Remove flyers or figures
            for fig in desc_copy.find_all(["figure", "figcaption", "a"]):
                if "flyer" in fig.get_text(strip=True).lower() or fig.name == "figure":
                    fig.decompose()
            description_html = sanitise(str(desc_copy))
            
        # 2. Parse accordion lists for Duration, Intake, Fees, Entry Requirements
        info_list = soup.find("ul", class_="info-list")
        
        duration_desc = ""
        intake_desc = ""
        tuition_fees_html = ""
        extra_fees_html = ""
        
        if info_list:
            for li in info_list.find_all("li", recursive=False):
                caption = li.find("strong", class_="title")
                desc_div = li.find("div", class_="description")
                if not caption or not desc_div:
                    continue
                
                cap_text = caption.get_text(strip=True).lower()
                desc_html = str(desc_div)
                
                if "duration" in cap_text:
                    duration_desc = sanitise(desc_html)
                elif "intake" in cap_text:
                    intake_desc = desc_div.get_text(" ", strip=True)
                elif "fees" in cap_text:
                    # Separate tuition and extra fees inside the desc_div
                    rows = desc_div.find_all("div", class_="text-row")
                    for r in rows:
                        t = r.get_text(" ", strip=True).lower()
                        if "tuition fee" in t:
                            tuition_fees_html = str(r)
                        elif "extra fee" in t:
                            extra_fees_html = str(r)
                    if not tuition_fees_html:
                        tuition_fees_html = desc_html
                        
        # 3. Entry Requirements
        entry_reqs_html = ""
        accordion = soup.find("ul", class_="accordion")
        if accordion:
            for li in accordion.find_all("li", recursive=False):
                opener = li.find("a", class_="opener")
                if opener and "entry requirements" in opener.get_text(strip=True).lower():
                    slide = li.find("div", class_="slide")
                    if slide:
                        entry_reqs_html = str(slide)
                        break
                        
        # 4. Formulate requirements
        final_requirements = ""
        if entry_reqs_html:
            if ai_formatter is not None and ai_formatter.enabled():
                try:
                    plain = re.sub(r"\s+", " ", BeautifulSoup(entry_reqs_html, "html.parser").get_text(" ", strip=True))
                    plain = re.sub(r"^\s*Entry Requirements\s*", "", plain, flags=re.IGNORECASE)
                    table = ai_formatter.format_requirements(plain)
                    if table:
                        final_requirements = clean_html(f"<h4>Entry Requirements</h4>{table}")
                except Exception as e:
                    print(f"⚠️ AI Requirements Formatter error: {e}")
            if not final_requirements:
                body = sanitise(entry_reqs_html)
                body = re.sub(r"^\s*<p>\s*Entry Requirements\s*</p>", "", body, flags=re.IGNORECASE)
                final_requirements = clean_html(f"<h4>Entry Requirements</h4>{body}")
                
        # 5. Extract Qualifications from Course/s block
        quals_found = []
        if info_list:
            for li in info_list.find_all("li", recursive=False):
                caption = li.find("strong", class_="title")
                desc_div = li.find("div", class_="description")
                if caption and "course/s" in caption.get_text(strip=True).lower() and desc_div:
                    # Qualifications are usually separated by hr or tag blocks
                    # Let's divide by hr first
                    desc_str = str(desc_div)
                    segments = desc_str.split("<hr")
                    for seg in segments:
                        seg_soup = BeautifulSoup(seg, "html.parser")
                        # Look for title and CRICOS code in this qualification segment
                        text = seg_soup.get_text(" ", strip=True)
                        cricos_match = re.search(r"CRICOS\s*:\s*([0-9A-Za-z\-]+)", text, re.I) or \
                                       re.search(r"CRICOS\s*Code\s*:\s*([0-9A-Za-z\-]+)", text, re.I)
                        if cricos_match:
                            cricos_code = cricos_match.group(1).strip()
                            # Title is usually the text before |
                            qual_title = text.split("|")[0].strip()
                            # If no | exists, clean the text around CRICOS
                            if not qual_title or len(qual_title) < 5:
                                qual_title = main_title
                            quals_found.append((qual_title, cricos_code))
                            
        # If no quals found in the list, try regex on the entire page
        if not quals_found:
            text = soup.get_text(" ", strip=True)
            cricos_matches = re.findall(r"CRICOS\s*(?:Course)?\s*(?:Code)?\s*:\s*([0-9A-Za-z]+)", text, re.I)
            if cricos_matches:
                for c in set(cricos_matches):
                    quals_found.append((main_title, c))
                    
        # Make sure they are unique
        quals_found = list(dict.fromkeys(quals_found))
        
        # 6. Format qualifications data
        for q_title, q_cricos in quals_found:
            # Extract qualification specific fee
            q_fee = extract_fee(tuition_fees_html, q_title)
            q_materials = extract_materials_fee(extra_fees_html)
            
            qualifications.append({
                "cricos": q_cricos,
                "title": q_title,
                "url": url,
                "course_description": clean_html(description_html),
                "total_course_duration": clean_html(duration_desc),
                "offshore_tuition_fee": q_fee,
                "onshore_tuition_fee": q_fee,
                "enrolment_fee": "NULL",
                "materials_fee": q_materials,
                "entry_requirements": final_requirements,
                "apply_form": url,
                "intake_desc": intake_desc
            })
            
            print(f"✅ Found Qualification: {q_title} | CRICOS: {q_cricos} | Fee: {q_fee}")
            
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        
    return qualifications

# ---------- main execution ----------
def main():
    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Driver excel not found: {EXCEL_PATH}")
        return
        
    df = pd.read_excel(EXCEL_PATH)
    all_results = []
    
    for idx, row in df.iterrows():
        url = str(row["url"]).strip()
        title = str(row["title"]).strip()
        print(f"\n[{idx+1}/{len(df)}] Processing Category: {title} | {url}")
        
        quals = scrape_cit_page(url)
        if quals:
            all_results.extend(quals)
        else:
            # Keep placeholder if scrape failed or returned no qualifications
            all_results.append({
                "cricos": "",
                "title": title,
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
            
    # Process intake dates from all scraped courses
    # CIT has main intake semesters: Semester 1 (February) and Semester 2 (July)
    # Plus April/October options for specific courses
    intake_date = "February, April, July, October"
    
    # 1. Write SQL file
    print(f"\n💾 Saving SQL file to: {SQL_PATH}")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
                
        for q in all_results:
            if not q["cricos"]:
                f.write(f"-- ⚠️ Skipped (no CRICOS code found): {q['title']} | {q['url']}\n\n")
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
                    
    # 2. Write Excel file
    print(f"💾 Saving Excel file to: {EXCEL_PATH}")
    
    def _cell(v):
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
    print("\n🏁 Process Completed successfully!")

if __name__ == "__main__":
    main()
