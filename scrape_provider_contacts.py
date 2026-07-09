import os
import sys
import re
import time
import csv
import urllib3
import requests
import pandas as pd
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from urllib.parse import urljoin, urlparse

# Force UTF-8 encoding for stdout and stderr on Windows to support emojis in console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Suppress urllib3 warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Config
INPUT_FILE = "provider_institution.csv"
CRICOS_CACHE_FILE = "A.RESULT/provider_contacts.csv"
OUTPUT_DIR = "A.RESULT"
CSV_OUTPUT = os.path.join(OUTPUT_DIR, "provider_contacts_from_websites.csv")
EXCEL_OUTPUT = os.path.join(OUTPUT_DIR, "provider_contacts_from_websites.xlsx")

MAX_WORKERS = 10  # Speed up since we fetch different servers, reduces local bottleneck
RETRY_ATTEMPTS = 2
TIMEOUT = 10  # Keep timeout low so blocked/offline sites don't stall the executor

# Thread safety lock for CSV writing
csv_write_lock = Lock()

# Request headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}

# Regexes for email and phone numbers
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}")
PHONE_REGEX = re.compile(r"(?:\+61|0)[2-478](?:\s?\d){8}|1[38]00(?:\s?\d){6}")

# System or dummy emails to ignore if we have better candidates
EXCLUDE_EMAIL_KEYWORDS = ["sentry", "wp-admin", "webmaster", "noreply", "no-reply", "example", "domain"]

def clean_value(val):
    if val is None or pd.isna(val):
        return ""
    val = str(val).strip()
    val = re.sub(r"\s+", " ", val)
    return val

def clean_phone(phone):
    # Keep only digits and '+'
    cleaned = re.sub(r"[^\d+]", "", phone)
    # Remove leading/trailing + if it's double
    cleaned = re.sub(r"^\++", "+", cleaned)
    return cleaned

def is_same_domain(url1, url2):
    try:
        return urlparse(url1).netloc.replace("www.", "") == urlparse(url2).netloc.replace("www.", "")
    except Exception:
        return False

def extract_contacts_from_html(html, current_url):
    soup = BeautifulSoup(html, "html.parser")
    emails = []
    phones = []
    contact_links = []
    
    # 1. Parse anchors for mailto:, tel:, and contact links
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        href_lower = href.lower()
        
        # Email mailto link
        if href_lower.startswith("mailto:"):
            email_val = href[7:].split("?")[0].strip()
            if EMAIL_REGEX.match(email_val):
                emails.append(email_val)
        
        # Phone tel link
        elif href_lower.startswith("tel:"):
            phone_val = href[4:].split("?")[0].strip()
            phones.append(phone_val)
            
        # Contact page link
        else:
            text = a.get_text().lower()
            if any(kw in text or kw in href_lower for kw in ["contact", "about", "support", "enquiry", "touch"]):
                abs_url = urljoin(current_url, href)
                # Keep only internal contact links
                if is_same_domain(current_url, abs_url):
                    contact_links.append(abs_url)
                    
    # 2. Parse text content using regex
    text_content = soup.get_text(" ")
    
    for match in EMAIL_REGEX.finditer(text_content):
        emails.append(match.group(0))
        
    for match in PHONE_REGEX.finditer(text_content):
        phones.append(match.group(0))
        
    # Clean phone numbers
    cleaned_phones = []
    for p in phones:
        cp = clean_phone(p)
        if len(cp) >= 8:  # Validate min digits length for Australian numbers
            cleaned_phones.append(cp)
            
    # Filter and clean emails
    cleaned_emails = []
    for e in emails:
        e_clean = e.strip().lower()
        if not any(kw in e_clean for kw in EXCLUDE_EMAIL_KEYWORDS):
            cleaned_emails.append(e)
            
    # Fallback to general list if all filtered
    if not cleaned_emails and emails:
        cleaned_emails = emails

    # Deduplicate while preserving order
    final_emails = list(dict.fromkeys(cleaned_emails))
    final_phones = list(dict.fromkeys(cleaned_phones))
    final_links = list(dict.fromkeys(contact_links))
    
    return final_emails, final_phones, final_links

def scrape_website(website_url):
    """Crawls a website homepage and optionally a contact page to get email/phone."""
    if not website_url.startswith("http://") and not website_url.startswith("https://"):
        website_url = "http://" + website_url
        
    emails = []
    phones = []
    
    try:
        # Request homepage
        r = requests.get(website_url, headers=HEADERS, timeout=TIMEOUT, verify=False, allow_redirects=True)
        if r.status_code == 200:
            h_emails, h_phones, contact_links = extract_contacts_from_html(r.text, r.url)
            emails.extend(h_emails)
            phones.extend(h_phones)
            
            # Follow the first contact page link for deeper search
            if contact_links:
                contact_url = contact_links[0]
                try:
                    cr = requests.get(contact_url, headers=HEADERS, timeout=TIMEOUT, verify=False, allow_redirects=True)
                    if cr.status_code == 200:
                        c_emails, c_phones, _ = extract_contacts_from_html(cr.text, cr.url)
                        emails.extend(c_emails)
                        phones.extend(c_phones)
                except Exception:
                    pass  # Ignore failure to fetch subpage
            
            return {
                "emails": list(dict.fromkeys(emails)),
                "phones": list(dict.fromkeys(phones)),
                "source": "Website"
            }
        else:
            return None
    except Exception:
        return None

def process_provider(code, default_name, default_website, fallback_data):
    """Executes website-first scrape with CRICOS cache fallback."""
    # Determine the website to visit
    website = default_website
    if not website or website.lower() in ("null", "n/a"):
        website = fallback_data.get("website_url", "")
        
    website = clean_value(website)
    
    web_emails = []
    web_phones = []
    source = "CRICOS Fallback"
    
    # Attempt to crawl website if available
    if website:
        web_res = scrape_website(website)
        if web_res:
            web_emails = web_res["emails"]
            web_phones = web_res["phones"]
            source = "Website"
            
    # Resolve Email
    final_email = ""
    if web_emails:
        final_email = web_emails[0]
    else:
        final_email = fallback_data.get("email", "")
        
    # Resolve Phone
    final_phone = ""
    if web_phones:
        final_phone = web_phones[0]
    else:
        final_phone = fallback_data.get("phone_number", "")
        
    # Resolve Institution Name
    final_name = clean_value(fallback_data.get("institution_name")) or clean_value(default_name)
    final_website = website or clean_value(fallback_data.get("website_url"))
    
    return {
        "cricos_code": code,
        "institution_name": final_name,
        "website_url": final_website,
        "phone_number": clean_value(final_phone),
        "email": clean_value(final_email),
        "status": f"Success ({source})"
    }

def main():
    print("🚀 Starting AusCourseMiner Provider Contacts Website Scraper")
    
    # 1. Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 2. Load CRICOS fallback cache database
    cricos_fallback_db = {}
    if os.path.exists(CRICOS_CACHE_FILE):
        try:
            with open(CRICOS_CACHE_FILE, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    code = clean_value(row.get("cricos_code"))
                    if code:
                        cricos_fallback_db[code] = {
                            "phone_number": clean_value(row.get("phone_number")),
                            "email": clean_value(row.get("email")),
                            "website_url": clean_value(row.get("website_url")),
                            "institution_name": clean_value(row.get("institution_name"))
                        }
            print(f"💾 Loaded CRICOS fallback cache: {len(cricos_fallback_db)} providers cached.")
        except Exception as e:
            print(f"⚠️ Error reading CRICOS cache file {CRICOS_CACHE_FILE}: {e}")
    else:
        print(f"⚠️ Warning: CRICOS cache file {CRICOS_CACHE_FILE} not found. Running without fallback database.")
        
    # 3. Check resume state
    scraped_codes = set()
    file_exists = os.path.exists(CSV_OUTPUT)
    
    if file_exists:
        try:
            with open(CSV_OUTPUT, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames and "cricos_code" in reader.fieldnames:
                    for row in reader:
                        if row["cricos_code"]:
                            scraped_codes.add(row["cricos_code"])
            print(f"🔄 Resuming scraper: found {len(scraped_codes)} already scraped providers in {CSV_OUTPUT}.")
        except Exception as e:
            print(f"⚠️ Error reading existing CSV output: {e}. Starting fresh.")
            file_exists = False
            scraped_codes = set()

    # 4. Read dataset
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file {INPUT_FILE} not found!")
        sys.exit(1)
        
    df_input = pd.read_csv(INPUT_FILE)
    df_input.columns = [c.strip() for c in df_input.columns]
    
    providers_list = []
    for _, row in df_input.iterrows():
        code = clean_value(row.get("cricos_provider_code"))
        if not code:
            continue
        
        inst_name = row.get("institution_name")
        if pd.isna(inst_name) or clean_value(inst_name) == "NULL":
            inst_name = row.get("trading_name")
        inst_name = clean_value(inst_name)
        
        website = row.get("website")
        website = clean_value(website)
        
        providers_list.append((code, inst_name, website))
        
    total_providers = len(providers_list)
    print(f"📋 Total providers in dataset: {total_providers}")
    
    # Filter remaining
    remaining_providers = [p for p in providers_list if p[0] not in scraped_codes]
    to_scrape_count = len(remaining_providers)
    print(f"⚡ Remaining providers to scrape: {to_scrape_count}")
    
    if to_scrape_count == 0:
        print("🎉 All providers have already been scraped! Generating final Excel report...")
        generate_excel_output()
        print("✅ Excel report created successfully.")
        return

    # 5. Open CSV in append or write mode
    write_header = not file_exists
    
    csv_file = open(CSV_OUTPUT, mode="a" if file_exists else "w", newline="", encoding="utf-8")
    fieldnames = ["cricos_code", "institution_name", "website_url", "phone_number", "email", "status"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    if write_header:
        writer.writeheader()
        csv_file.flush()

    completed_count = len(scraped_codes)
    success_count = 0
    fallback_count = 0

    print(f"🌐 Scraping with {MAX_WORKERS} concurrent threads. Please wait...\n")

    # 6. Multi-threaded execution
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(
                process_provider, 
                code, 
                name, 
                web, 
                cricos_fallback_db.get(code, {})
            ): code 
            for code, name, web in remaining_providers
        }
        
        for future in as_completed(futures):
            code = futures[future]
            try:
                result = future.result()
                
                # Write thread-safely to CSV
                with csv_write_lock:
                    writer.writerow(result)
                    csv_file.flush()
                
                completed_count += 1
                if "Website" in result["status"]:
                    success_count += 1
                    status_emoji = "🌐"
                else:
                    fallback_count += 1
                    status_emoji = "💾"
                
                # Console logs
                print(f"[{completed_count}/{total_providers}] {status_emoji} Code: {result['cricos_code']} | "
                      f"Name: {result['institution_name'][:40]}... | "
                      f"Phone: {result['phone_number'] or 'N/A'} | "
                      f"Email: {result['email'] or 'N/A'}")
                sys.stdout.flush()
                
            except Exception as e:
                print(f"❌ Unhandled thread exception for provider {code}: {e}")
                sys.stdout.flush()

    csv_file.close()
    
    print("\n🏁 Scraping phase completed.")
    print(f"📊 Results: Scraped from Web={success_count}, Fallback to CRICOS={fallback_count}")
    
    # 7. Generate final sorted Excel report and clean CSV
    generate_excel_output()
    print("✅ All processes completed successfully!")

def generate_excel_output():
    # Load all results from CSV, clean, sort by cricos_code, and save both CSV and Excel
    if os.path.exists(CSV_OUTPUT):
        df = pd.read_csv(CSV_OUTPUT)
        # Drop duplicates based on cricos_code, keeping first
        df = df.drop_duplicates(subset=["cricos_code"], keep="first")
        # Sort by CRICOS code
        df = df.sort_values(by="cricos_code")
        
        # Save cleaned CSV (keeping the status column to maintain consistency)
        df.to_csv(CSV_OUTPUT, index=False)
        
        # Drop status column only for final Excel output
        if "status" in df.columns:
            df_cleaned = df.drop(columns=["status"])
        else:
            df_cleaned = df
            
        # Check if pi (1).csv exists to split the sheets
        pi_file = "pi (1).csv"
        if os.path.exists(pi_file):
            try:
                df_pi = pd.read_csv(pi_file)
                df_pi.columns = [c.strip() for c in df_pi.columns]
                urgent_codes = set(df_pi["cricos_provider_code"].dropna().astype(str).str.strip().tolist())
                
                # Split df_cleaned based on cricos_code
                df_urgent = df_cleaned[df_cleaned["cricos_code"].astype(str).str.strip().isin(urgent_codes)]
                df_others = df_cleaned[~df_cleaned["cricos_code"].astype(str).str.strip().isin(urgent_codes)]
                
                # Sort both by cricos_code
                df_urgent = df_urgent.sort_values(by="cricos_code")
                df_others = df_others.sort_values(by="cricos_code")
                
                with pd.ExcelWriter(EXCEL_OUTPUT, engine="openpyxl") as writer:
                    df_urgent.to_excel(writer, index=False, sheet_name="URGENT NURSING")
                    df_others.to_excel(writer, index=False, sheet_name="Provider Institution")
                print(f"📁 Excel report created with URGENT NURSING ({len(df_urgent)} rows) and Provider Institution ({len(df_others)} rows) sheets.")
            except Exception as e:
                print(f"⚠️ Error splitting Excel sheets: {e}. Saving all to a single sheet.")
                with pd.ExcelWriter(EXCEL_OUTPUT, engine="openpyxl") as writer:
                    df_cleaned.to_excel(writer, index=False, sheet_name="Provider Institution")
        else:
            print(f"⚠️ {pi_file} not found. Saving all to a single sheet.")
            with pd.ExcelWriter(EXCEL_OUTPUT, engine="openpyxl") as writer:
                df_cleaned.to_excel(writer, index=False, sheet_name="Provider Institution")
                
        print(f"📁 Cleaned CSV saved to {CSV_OUTPUT}")
        print(f"📁 Sorted Excel report saved to {EXCEL_OUTPUT}")

if __name__ == "__main__":
    main()
