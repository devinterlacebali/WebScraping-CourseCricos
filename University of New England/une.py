"""
University of New England (UNE) course scraper.

Provider CRICOS code: 00003G.

UNE's course catalogue is served by a Funnelback search backend. A single JSON call
returns every course together with a URL-encoded ``CourseInfo`` blob that already holds
the structured fields we need (fees, duration, intake, entry requirements, summary).
Only the **CRICOS course code** and the richer course description live on the individual
course page, so we fetch each page just for those.

Following the peer public-university convention in this repo (see ANU):
    - offshore_tuition_fee = INTERNATIONAL indicative *annual* fee (as quoted by UNE)
    - onshore_tuition_fee  = '' (domestic students are Commonwealth-supported; left blank)
    - total_course_duration = free text, e.g. "3 years full-time"
Only courses flagged ``fees-international`` are scraped; those without a CRICOS code on the
page (typically research degrees) are skipped with a comment.
"""
import os
import re
import sys
import json
import time
import urllib.parse
import pandas as pd
from bs4 import BeautifulSoup
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

PROVIDER_CODE = "00003G"
DIR = "University of New England"
SLUG = "une"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

# Funnelback course feed: every course + structured CourseInfo, scoped to the Courses tab.
FEED_URL = (
    "https://une-search.funnelback.squiz.cloud/s/search.json"
    "?collection=une~sp-global-search&profile=tab_courses&query=!showall"
    "&num_ranks=500&f.Tabs%7Cune~ds-courses-push=Courses"
)

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

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}


# ---------- helpers ----------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()


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


def months_in(texts):
    found = []
    for text in texts:
        for tok in re.findall(r"[A-Za-z]{3,9}", text or ""):
            k = tok.lower()
            if k in MONTHS and MONTHS[k] not in found:
                found.append(MONTHS[k])
    return found


def fetch_feed():
    """Return the list of course result dicts from the Funnelback feed."""
    p = Fetcher.get(FEED_URL, stealthy_headers=True)
    data = json.loads(p.body.decode("utf-8"))
    results = data["response"]["resultPacket"]["results"]
    return [r for r in results if "/study/courses/" in r.get("liveUrl", "")]


def parse_course_info(result):
    """Decode the URL-encoded CourseInfo JSON blob from a feed result."""
    ci = result.get("listMetadata", {}).get("CourseInfo")
    if not ci:
        return None
    try:
        return json.loads(urllib.parse.unquote(ci[0]))
    except Exception:
        return None


def intl_fee_from(info):
    """Extract the International indicative annual fee (numeric string) or ''."""
    for label, amount in info.get("fee-amounts", []) or []:
        if "international" in label.lower():
            m = re.search(r"([\d,]{3,})", amount)
            if m:
                return m.group(1).replace(",", "")
    return ""


def entry_reqs_from(info):
    """Build entry-requirements HTML from the CourseInfo blob.

    When the AI formatter is enabled (OPENROUTER_API_KEY set), the requirements text is
    reorganised into a categorised table; otherwise we fall back to sanitised HTML.
    """
    parts = []
    for item in info.get("entry-requirements", []) or []:
        if item is None:
            continue
        item = str(item).strip()
        if not item or item.lower() in ("none", "n/a", "na", "not applicable", "null"):
            continue
        if item.lstrip().startswith("<"):
            parts.append(item)
        else:
            parts.append(f"<p>{item}</p>")
    if not parts:
        return ""
    raw_html = "".join(parts)

    if ai_formatter is not None and ai_formatter.enabled():
        try:
            plain = re.sub(r"\s+", " ", BeautifulSoup(raw_html, "html.parser").get_text(" ", strip=True))
            table = ai_formatter.format_requirements(plain)
            if table:
                return clean_html(f"<h4>Entry Requirements</h4>{table}")
        except Exception as e:
            print(f"⚠️ AI Requirements Formatter error: {e}")

    body = sanitise(raw_html)
    return clean_html(f"<h4>Entry Requirements</h4>{body}")


# ---------- per-page scraping ----------
def extract_cricos(soup):
    """Return (valid_cricos, raw_code_found).

    UNE renders the course code in a structured ``<span>CRICOS code</span>`` label
    followed by a ``<ul><li>CODE</li></ul>``. This is more reliable than a loose text
    regex (which could otherwise catch the provider number). A valid course CRICOS is
    6 digits + 1 letter; anything else (e.g. UNE's malformed "0100352") is returned as
    the raw value only, so the course can be flagged rather than silently trusted.
    """
    raw = ""
    for span in soup.find_all("span"):
        if span.get_text(strip=True).lower() == "cricos code":
            div = span.find_parent("div")
            ul = div.find_next_sibling("ul") if div else None
            if not ul:
                continue
            for li in ul.find_all("li"):
                v = li.get_text(strip=True)
                if not v:
                    continue
                # A valid course CRICOS is 6 digits + 1 letter, sometimes followed by a
                # label, e.g. "058149M (Study Abroad Trimester)". Recover the embedded code.
                m = re.search(r"\b([0-9]{6}[A-Z])\b", v)
                if m:
                    return m.group(1), v   # first standard code wins
                raw = raw or v             # remember a non-standard code (e.g. "0100352")
    return "", raw


def scrape_page(url):
    """Return (cricos, raw_code, description_html) from a course page."""
    page = Fetcher.get(url, stealthy_headers=True)
    soup = BeautifulSoup(page.html_content, "html.parser")

    cricos, raw_code = extract_cricos(soup)

    sections = []
    # Main "Course information" block holds the course overview/description.
    info = soup.find("div", class_="info-block__wrapper")
    if info:
        copy = BeautifulSoup(str(info), "html.parser")
        for h in copy.find_all(["h1", "h2", "h3"]):
            h.decompose()
        for a in copy.find_all("a"):
            if "brochure" in a.get_text(strip=True).lower() or "download" in a.get_text(strip=True).lower():
                a.decompose()
        body = sanitise(str(copy))
        if BeautifulSoup(body, "html.parser").get_text(strip=True):
            sections.append(f"<h4>Course Information</h4>{body}")

    # "Your career" / course outcomes section.
    career_h2 = soup.find("h2", id="your-career")
    if career_h2:
        block = career_h2.find_parent("div", class_="block__wrapper") or career_h2.find_parent("div")
        if block:
            copy = BeautifulSoup(str(block), "html.parser")
            for h in copy.find_all(["h1", "h2", "h3"]):
                h.decompose()
            body = sanitise(str(copy))
            if BeautifulSoup(body, "html.parser").get_text(strip=True):
                sections.append(f"<h4>Your Career</h4>{body}")

    return cricos, raw_code, clean_html("".join(sections))


# ---------- main ----------
def main():
    os.makedirs(DIR, exist_ok=True)
    print("🌐 Fetching UNE course feed ...")
    results = fetch_feed()
    print(f"   {len(results)} total courses in feed")

    rows = []
    for r in results:
        info = parse_course_info(r)
        if not info or not info.get("fees-international"):
            continue  # only courses open to international students
        rows.append((r, info))
    print(f"   {len(rows)} international courses to scrape\n")

    all_results = []
    intake_months = set()
    for idx, (r, info) in enumerate(rows, 1):
        title = info.get("name") or r["title"].split(" | ")[0]
        url = r["liveUrl"]
        raw_code = ""
        try:
            cricos, raw_code, description = scrape_page(url)
        except Exception as e:
            cricos, description = "", ""
            print(f"❌ [{idx}/{len(rows)}] {title}: {e}")

        durations = info.get("duration") or []
        duration = durations[0] if durations else ""
        offshore = intl_fee_from(info)
        entry = entry_reqs_from(info)
        course_months = months_in(info.get("start") or [])
        intake_months.update(course_months)

        # Fall back to the CourseInfo summary if the page description came back empty.
        if not description and info.get("summary"):
            description = clean_html(f"<h4>Course Information</h4>{sanitise(info['summary'])}")

        all_results.append({
            "cricos": cricos,
            "raw_code": raw_code,
            "title": title,
            "url": url,
            "course_description": description,
            "total_course_duration": duration,
            "offshore_tuition_fee": offshore,
            "onshore_tuition_fee": "",
            "entry_requirements": entry,
            "apply_form": url,
            "intake": ", ".join(course_months),
        })
        flag = f"CRICOS {cricos}" if cricos else "no CRICOS (skip)"
        print(f"✅ [{idx}/{len(rows)}] {title[:45]} | {flag} | ${offshore or '-'} | {duration}")
        time.sleep(0.3)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in intake_months)

    # ---- SQL ----
    print(f"\n💾 Writing SQL -> {SQL_PATH}")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        written = 0
        for d in all_results:
            if not d["cricos"]:
                reason = (f"unreliable CRICOS '{d['raw_code']}'" if d.get("raw_code")
                          else "no CRICOS course code")
                reason = reason.replace("\n", " ").replace("\r", "")
                f.write(f"-- ⚠️ Skipped ({reason}): {d['title']} | {d['url']}\n\n")
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
                f"WHERE cricos_course_code = '{d['cricos']}';\n\n"
            )

    # ---- xlsx (driver + enriched record) ----
    print(f"💾 Writing xlsx -> {EXCEL_PATH}")

    def cell(v):
        return ("" if v in (None, "NULL") else str(v).replace("''", "'"))[:32000]

    pd.DataFrame([{
        "cricos": d["cricos"],
        "title": d["title"],
        "url": d["url"],
        "total_course_duration": cell(d["total_course_duration"]),
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "intake": cell(d["intake"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in all_results]).to_excel(EXCEL_PATH, index=False)

    skipped = sum(1 for d in all_results if not d["cricos"])
    print(f"\n🏁 Done. {written} course UPDATEs, {skipped} skipped (no CRICOS). "
          f"Provider intake: {intake_date}")


if __name__ == "__main__":
    main()
