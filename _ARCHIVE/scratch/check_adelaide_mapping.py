import pandas as pd
import os
import re

# 1. Parse adelaide_update.sql to get URL -> CRICOS mapping
sql_mapping = {}
try:
    content = open('The University Of Adelaide/adelaide_update.sql', 'r', encoding='utf-8').read()
    statements = re.findall(
        r"UPDATE\s+courses\s+SET.*?apply_form\s*=\s*'([^'\n]+)'.*?WHERE\s+cricos_course_code\s*=\s*'([^'\n]+)';",
        content,
        re.DOTALL
    )
    for url, cricos in statements:
        sql_mapping[url.strip()] = cricos.strip()
except Exception as e:
    print("Error parsing SQL:", e)

# 2. Parse adelaide.csv to get slug -> Course Name mapping
csv_mapping = {}
try:
    df_csv = pd.read_csv('Adelaide University/adelaide.csv')
    for row in df_csv.values:
        if pd.notna(row[1]):
            slug = os.path.basename(str(row[1])).strip()
            csv_mapping[slug] = str(row[0]).strip()
except Exception as e:
    print("Error parsing CSV:", e)

# 3. Read legacy URLs
urls = [u.strip() for u in open('The University Of Adelaide/adelaide_links.txt').read().splitlines() if u.strip()]

print(f"Total legacy URLs: {len(urls)}")
print(f"Total mapped in SQL: {len(sql_mapping)}")
print(f"Total mapped in CSV: {len(csv_mapping)}")

matched_sql = 0
matched_csv = 0
unmatched = []

for u in urls:
    if u in sql_mapping:
        matched_sql += 1
    else:
        b = os.path.basename(u).replace('.html', '')
        if b in csv_mapping:
            matched_csv += 1
        else:
            unmatched.append(u)

print(f"Matched directly via SQL mapping: {matched_sql}")
print(f"Matched via CSV slug mapping: {matched_csv}")
print(f"Total matched: {matched_sql + matched_csv}")
print(f"Unmatched count: {len(unmatched)}")
if unmatched:
    print("Sample unmatched URLs:", unmatched[:5])
