import subprocess, os, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
VENV_PY = BASE / "venv" / "Scripts" / "python.exe"

# Remaining grammar schools that might not have completed
remaining = [
    ('Christway College', 'christway'),
    ('Caroline Chisholm Catholic College', 'caroline-chisholm'),
    ('Alia College', 'alia'),
    ('Beaconhills College', 'beaconhills'),
    ('Genazzano FCJ College', 'genazzano'),
    ('Oakleigh Grammar', 'oakleigh-grammar'),
    ('Siena College', 'siena'),
    ('Sacre Coeur', 'sacre-coeur'),
    ('The Friends School', 'friends-tas'),
    ('The Hutchins School', 'hutchins'),
    ('St Michael\'s Collegiate School', 'collegiate-tas'),
    ('Ballarat Clarendon College', 'ballarat-clarendon'),
    ('Strathcona Baptist Girls Grammar School', 'strathcona'),
    ('Scotch College', 'scotch-vic'),
    ('Launceston Church Grammar School', 'launceston-grammar'),
    ('Ivanhoe Girls Grammar School', 'ivanhoe-girls'),
    ('Melbourne Grammar School', 'melbourne-grammar'),
    ('Nazareth College', 'nazareth'),
    ('Girton Grammar School', 'girton'),
    ('Mackillop Catholic Regional College', 'mackillop'),
    ('Kardinia International College', 'kardinia'),
]

for name, slug in remaining:
    # Find folder
    folder = None
    for d in os.listdir(BASE):
        if os.path.isdir(BASE / d):
            dlower = d.lower().replace(' ', '').replace("'", '').replace('_', '').replace('-', '')
            name_normalized = name.lower().replace(' ', '').replace("'", '').replace('_', '').replace('-', '')
            if name_normalized in dlower or slug in dlower:
                folder = d
                break
    
    if folder:
        script = BASE / folder / f'{slug}_webscrape.py'
        if script.exists():
            # Check if outputs already exist
            xlsx = BASE / folder / f'{slug}_webscrape.xlsx'
            sql = BASE / folder / f'{slug}_webscrape_courses_update.sql'
            if sql.exists():
                print(f'  OK (exists): {name} ({folder})')
                continue
            
            print(f'  Running: {name} ({folder})')
            try:
                r = subprocess.run([str(VENV_PY), str(script)], capture_output=True, text=True, timeout=120, cwd=str(BASE / folder))
                out = r.stdout[-400:] if r.stdout else '(empty)'
                print(f'    {out[:200]}')
                if r.stderr:
                    err = r.stderr[:200]
                    if 'timeout' not in err.lower():
                        print(f'    ERR: {err}')
                if sql.exists():
                    print(f'    -> SQL OK')
                else:
                    print(f'    -> SQL MISSING')
            except subprocess.TimeoutExpired:
                print(f'    TIMEOUT (120s)')
            except Exception as e:
                print(f'    ERROR: {e}')
        else:
            print(f'  No script: {script}')
    else:
        print(f'  Folder not found: {name}')

print('\nDone!')
