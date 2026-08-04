import pandas as pd
import os
import re

# 1. Parse adelaide_update.sql to get URL -> CRICOS mapping
url_to_cricos = {}
try:
    content = open('The University Of Adelaide/adelaide_update.sql', 'r', encoding='utf-8').read()
    statements = re.findall(
        r"UPDATE\s+courses\s+SET.*?apply_form\s*=\s*'([^'\n]+)'.*?WHERE\s+cricos_course_code\s*=\s*'([^'\n]+)';",
        content,
        re.DOTALL
    )
    for url, cricos in statements:
        url_to_cricos[url.strip()] = cricos.strip()
except Exception as e:
    print("Error parsing SQL:", e)

# 2. Parse adelaide.csv to get Course Name -> Legacy URL mapping
name_to_url = {}
try:
    df_csv = pd.read_csv('Adelaide University/adelaide.csv')
    for row in df_csv.values:
        if pd.notna(row[1]):
            url = str(row[1]).strip()
            name = str(row[0]).strip()
            name_to_url[name] = url
except Exception as e:
    print("Error parsing CSV:", e)

# 3. Read cricos-courses.csv for provider 00123M
cricos_db = {}
try:
    df_c = pd.read_csv('cricos-courses.csv', dtype=str)
    uofa_courses = df_c[df_c['CRICOS Provider Code'] == '00123M'][['CRICOS Course Code', 'Course Name']].dropna()
    for row in uofa_courses.values:
        code = str(row[0]).strip()
        name = str(row[1]).strip()
        norm_name = re.sub(r'[^a-z0-9]', '', name.lower())
        cricos_db[norm_name] = code
except Exception as e:
    print("Error parsing cricos-courses.csv:", e)

# 4. Combine them
name_to_cricos = {}
fallback_count = 0
not_found = []

for name, url in name_to_url.items():
    slug = os.path.basename(url)
    df_url = f"https://www.adelaide.edu.au/degree-finder/2025/{slug}.html"
    
    cricos_code = None
    if df_url in url_to_cricos:
        cricos_code = url_to_cricos[df_url]
    elif url in url_to_cricos:
        cricos_code = url_to_cricos[url]
        
    if cricos_code:
        name_to_cricos[name] = cricos_code
    else:
        # Fallback to cricos-courses.csv name match
        norm = re.sub(r'[^a-z0-9]', '', name.lower())
        if norm in cricos_db:
            name_to_cricos[name] = cricos_db[norm]
            fallback_count += 1
        else:
            not_found.append((name, url))

print(f"Total Course Names in CSV: {len(name_to_url)}")
print(f"Mapped directly via legacy URL: {len(name_to_cricos) - fallback_count}")
print(f"Mapped via cricos-courses name fallback: {fallback_count}")
print(f"Total mapped: {len(name_to_cricos)}")
print(f"Not found: {len(not_found)}")
if not_found:
    print("Samples of Not Found:")
    for n, u in not_found[:10]:
        print(f"  '{n}' -> '{u}'")
