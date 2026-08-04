"""Register 12 small providers + QC."""
import json, subprocess

small = [
    ("03733E", "YourLife Health and Learning", "yourlife"),
    ("03741E", "Tred Consultants (Tred College)", "tred"),
    ("00018A", "Department for Education SA", "dept-education-sa"),
    ("00051M", "ELC Career College", "elc"),
    ("00057E", "Alexander Language School", "alexander"),
    ("00094M", "SA College of English", "sace"),
    ("00129E", "Ballarat and Queen's Anglican Grammar", "ballarat-grammar"),
    ("00131M", "Billanook College", "billanook"),
    ("00132K", "Brighton Grammar School", "brighton-grammar"),
    ("00135G", "Carey Baptist Grammar School", "carey"),
    ("00136F", "Caulfield Grammar School", "caulfield"),
    ("00138D", "Eltham College", "eltham"),
]

import os
e = json.load(open('scrapers.json'))
for code, name, slug in small:
    dirname = name
    safe = slug
    r = {
        'id': f'{safe}',
        'name': name,
        'scraper': f'{dirname}/{safe}.py',
        'sql': f'{dirname}/{safe}_courses_update.sql',
        'xlsx': f'{dirname}/{safe}.xlsx',
        'dir': dirname,
    }
    e.append(r)
json.dump(e, open('scrapers.json', 'w'), indent=2)
print(f'{len(small)} registered')

for code, name, slug in small:
    subprocess.run(['venv/Scripts/python', 'qc_report.py', slug],
                   capture_output=True, text=True, timeout=15)
    out = subprocess.run(['venv/Scripts/python', 'qc_report.py', slug],
                         capture_output=True, text=True, timeout=15).stdout
    # Show just key lines
    for line in out.splitlines():
        if 'CRICOS matched' in line or 'Rows:' in line or 'SQL format' in line:
            print(f'  {slug}: {line.strip()}')
