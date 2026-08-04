import csv
import re
import os
import pandas as pd

def clean_slug(s):
    s = s.lower()
    # remove special chars/accents/parentheses/slashes
    s = re.sub(r"\(.*?\)", "", s)
    s = s.replace("/", "-").replace("&", "and")
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s-]+", "-", s)
    return s.strip("-")

def main():
    cricos_file = "cricos-courses.csv"
    sitemap_file = "scratch/latrobe_course_urls.txt"
    
    if not os.path.exists(cricos_file):
        print(f"Error: {cricos_file} not found")
        return
    if not os.path.exists(sitemap_file):
        print(f"Error: {sitemap_file} not found")
        return
        
    # Read sitemap URLs
    with open(sitemap_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]
        
    url_slug_map = {}
    for url in urls:
        # Extract slug
        slug = url.split("/")[-1]
        url_slug_map[slug] = url
        
    print(f"Loaded {len(url_slug_map)} URL slugs from sitemap.")
    
    # Read CRICOS courses for provider 00115M
    cricos_courses = []
    with open(cricos_file, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        # Check header
        # 00115M,La Trobe University (La Trobe),002080A,Bachelor of Arts...
        for row in reader:
            if len(row) < 4:
                continue
            provider_code = row[0].strip()
            if provider_code == "00115M":
                course_code = row[2].strip()
                course_name = row[3].strip()
                cricos_courses.append({
                    "cricos": course_code,
                    "title": course_name
                })
                
    print(f"Loaded {len(cricos_courses)} course records from cricos-courses.csv.")
    
    # Match
    matched_records = []
    unmatched_records = []
    
    # We want a list of unique course titles to avoid duplicates in driver
    unique_titles = {}
    for c in cricos_courses:
        title = c["title"]
        unique_titles.setdefault(title, []).append(c["cricos"])
        
    print(f"Total unique course titles in CRICOS: {len(unique_titles)}")
    
    for title, codes in unique_titles.items():
        slug = clean_slug(title)
        # Try direct slug match
        url = url_slug_map.get(slug)
        
        # If no direct match, try matching with minor variations
        if not url:
            # try suffix/prefix matching
            for u_slug, u_url in url_slug_map.items():
                if u_slug == slug or u_slug.replace("-honours", "") == slug.replace("-honours", ""):
                    url = u_url
                    break
                    
        if url:
            matched_records.append({
                "title": title,
                "url": url,
                "cricos_codes": ",".join(codes)
            })
        else:
            unmatched_records.append({
                "title": title,
                "slug_tried": slug
            })
            
    print(f"Successfully matched: {len(matched_records)}")
    print(f"Unmatched: {len(unmatched_records)}")
    
    # Create the output directory if not exists
    out_dir = "La Trobe University (La Trobe)"
    os.makedirs(out_dir, exist_ok=True)
    
    # Create driver DataFrame
    driver_df = pd.DataFrame(matched_records)[["title", "url"]]
    # Drop duplicates
    driver_df = driver_df.drop_duplicates(subset=["url"])
    
    excel_path = os.path.join(out_dir, "latrobe.xlsx")
    driver_df.to_excel(excel_path, index=False)
    print(f"Saved {len(driver_df)} course URLs to driver file: {excel_path}")
    
    # List a few unmatched ones
    print("\nSome unmatched courses:")
    for um in unmatched_records[:15]:
        print(f"  - Title: {um['title']} (Slug: {um['slug_tried']})")

if __name__ == "__main__":
    main()
