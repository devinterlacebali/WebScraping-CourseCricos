"""Audit SA/WA/NT providers - comprehensive matching."""
import csv, os
from pathlib import Path

BASE = Path(__file__).resolve().parent
INST_PATH = os.path.expanduser("~/Downloads/cricos-providers-courses-locations/CRICOS Institutions.csv")

# Get course counts
provider_courses = {}
with open(BASE / 'cricos-courses.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        c = r['CRICOS Provider Code'].strip()
        if r['Expired'].strip().lower() in ('no', 'n', ''):
            provider_courses[c] = provider_courses.get(c, 0) + 1

# Get all folders with their data status
all_folders = {}
for d in BASE.iterdir():
    if d.is_dir() and not d.name.startswith('.') and d.name not in ('scratch','venv','A.RESULT'):
        has_data = False
        data_type = ""
        for f in d.iterdir():
            if '_webscrape.xlsx' in f.name:
                has_data = True
                data_type = "webscrape"
                break
            elif f.suffix == '.xlsx' and '_webscrape' not in f.name:
                has_data = True
                data_type = "standard"
                break
        all_folders[d.name.lower()] = {
            'name': d.name, 'has_data': has_data, 'data_type': data_type, 'folder': d
        }

# Load all SA/WA/NT providers
sa_wa_nt = []
with open(INST_PATH, encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        if r.get('Postal Address State','') in ('SA','WA','NT'):
            code = r['CRICOS Provider Code'].strip()
            if code in provider_courses:
                sa_wa_nt.append((code, r['Institution Name'].strip(),
                                r.get('Website','').strip(), r.get('Postal Address State','')))

def match_provider(code, name):
    """Try to match a provider to an existing folder."""
    name_lower = name.lower()
    
    # Direct by code snippet
    for f_lower, info in all_folders.items():
        if code.replace(' ','') in f_lower.replace(' ',''):
            return info
    
    # Name-based
    name_clean = name_lower.replace('(', '').replace(')', '').replace("'", '').replace(',', '').replace('.', '"')
    stopwords = {'the','of','and','for','in','to','a','an','pty','ltd','inc','limited','as','trustee'}
    sig_words = [w for w in name_clean.split() if w not in stopwords and len(w) > 2]
    
    best_score = 0
    best_info = None
    for f_lower, info in all_folders.items():
        f_clean = f_lower.replace('-', ' ').replace('_', ' ').replace("'", '')
        f_words = set(f_clean.split())
        sw_set = set(sig_words)
        overlap = len(sw_set & f_words)
        if overlap > best_score:
            best_score = overlap
            best_info = info
    
    if best_score >= 2:
        return best_info
    return None

# Categorize all
results = []
for code, name, website, state in sa_wa_nt:
    n = provider_courses[code]
    match = match_provider(code, name)
    if match and match['has_data']:
        status = "DONE"
    elif match and not match['has_data']:
        status = "EMPTY"
    else:
        status = "MISS"
    results.append((status, state, code, name, website, n, match['name'] if match else ''))

# Print
print(f"{'Status':<6} {'St':<3} {'Code':<8} {'Crs':<5} {'Folder/Website':<45} {'Name'}")
print("="*125)
for status, state, code, name, website, n, fname in sorted(results, key=lambda x: (x[0], x[1], x[3])):
    if status == "MISS":
        w = website[:40] if website else "N/A"
        print(f"{status:<6} {state:<3} {code:<8} {n:<5} ❌ {w:<40} {name[:55]}")
    elif status == "EMPTY":
        print(f"{status:<6} {state:<3} {code:<8} {n:<5} 📁 {fname[:40]} {name[:55]}")
    else:
        print(f"{status:<6} {state:<3} {code:<8} {n:<5} ✅ {fname[:40]} {name[:55]}")

miss = sum(1 for r in results if r[0] == "MISS")
empty = sum(1 for r in results if r[0] == "EMPTY")
done = sum(1 for r in results if r[0] == "DONE")
print(f"\nDONE: {done} | EMPTY: {empty} | MISS: {miss} | Total: {len(results)}")
