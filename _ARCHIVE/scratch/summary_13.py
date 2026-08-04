"""Quick summary of all 13 providers."""
import sys, csv, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

sites = {
    'EQUALS International': 'equals.edu.au',
    'Menzies Institute': 'menzies.vic.edu.au',
    'ETEA': 'etea.edu.au',
    'alacchealth': 'alacchealth.edu.au',
    'SCEI': 'scei.com.au',
    'Queensford': 'queensford.edu.au',
    'TAFE QLD': 'tafeqld.edu.au',
    'TasTAFE': 'tastafe.tas.edu.au',
    'Stanley College': 'stanleycollege.edu.au',
    'HCI Group': 'hcigroup.com.au',
    'Torrens': 'torrens.edu.au',
    'IHM': 'ihm.edu.au',
    'Strategix': 'strategix.com.au',
}

# Search CSV for each
with open('cricos-courses.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    providers = {}
    for row in reader:
        code = row['CRICOS Provider Code'].strip()
        inst = row['Institution Name'].strip()
        expired = row['Expired'].strip().lower()
        if expired == 'yes': continue
        if code not in providers:
            providers[code] = {'name': inst, 'courses': set()}
        providers[code]['courses'].add(row['CRICOS Course Code'].strip())

keywords = {
    'equals': 'equals',
    'menzies': 'menzies',
    'etea': 'etea',
    'alacchealth': 'alacchealth',
    'scei': 'southern cross education institute',
    'queensford': 'queensford',
    'tafe qld': 'tafe queensland',
    'tastafe': 'tastafe',
    'stanley': 'stanley international college',
    'hci group': 'hci',
    'torrens': 'torrens',
    'ihm': 'health & management',
    'strategix': 'strategix',
}

print(f'{"Name":25} {"Provider":10} {"Courses":8} Site')
print('-'*60)
for name, kw in keywords.items():
    found = [(c, p) for c, p in providers.items() if kw.lower() in p['name'].lower()]
    if found:
        for code, p in found:
            print(f'{name:25} {code:10} {len(p["courses"]):<8} {sites.get(name.title(), "?")}')
    else:
        print(f'{name:25} {"NOT FOUND":10} {"?":8} {sites.get(name.title(), "?")}')
