"""
uowc_03_csv_coverage.py — Cek coverage UOWC Ltd di cricos-courses.csv
"""

import csv
import sys

csv_path = r'C:\Users\Dewa(Interlace)\Documents\Interlace Code\WebScraping-CourseCricos\cricos-courses.csv'

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total rows in CSV: {len(rows)}")
print(f"Columns: {list(rows[0].keys())}\n")

# Cari UOWC
uowc_rows = [r for r in rows if 'uowc' in (r.get('Institution Name', '') or '').lower()]
uow_college_rows = [r for r in rows if 'uow college' in (r.get('Institution Name', '') or '').lower()]
uow_pathway_rows = [r for r in rows if 'college' in (r.get('Institution Name', '') or '').lower() and 'uow' in (r.get('Institution Name', '') or '').lower()]

print(f"UOWC Ltd matches: {len(uowc_rows)}")
print(f"UOW College matches: {len(uow_college_rows)}")
print(f"All UOW*College matches: {len(uow_pathway_rows)}")

# Tampilkan semua UOWC rows
print("\n--- UOWC Ltd COURSES IN CSV ---")
all_uowc = [r for r in rows if 'uowc' in (r.get('Institution Name', '') or '').lower()]
for r in all_uowc:
    print(f"  CRICOS: {r['CRICOS Course Code']} | {r['Course Name']} | "
          f"Level: {r['Course Level']} | Duration: {r['Duration (Weeks)']}w | "
          f"Fee: {r.get('Total Course Cost', 'N/A')}")

print(f"\nTotal UOWC courses in CSV: {len(all_uowc)}")

# Cek juga UoW sendiri
uow_rows = [r for r in rows if 'university of wollongong' in (r.get('Institution Name', '') or '').lower() and 'college' not in (r.get('Institution Name', '') or '').lower()]
print(f"\nUniversity of Wollongong (UoW) courses: {len(uow_rows)}")
print(f"UoW CRICOS provider code: {uow_rows[0]['CRICOS Provider Code'] if uow_rows else 'N/A'}")

# Provider codes
providers = set()
for r in rows:
    providers.add((r['CRICOS Provider Code'], r['Institution Name']))
print(f"\nUnique providers: {len(providers)}")
for p in sorted(providers):
    if 'uow' in p[1].lower():
        print(f"  {p[0]} - {p[1]}")
