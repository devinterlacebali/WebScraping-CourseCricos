#!/usr/bin/env python3
"""
qc_report.py — Unified QC report for any scraped provider.

Usage:
    venv/Scripts/python qc_report.py <provider_slug>

Examples:
    venv/Scripts/python qc_report.py edith-cowan-university
    venv/Scripts/python qc_report.py curtin-university
    venv/Scripts/python qc_report.py charles-darwin-university

Reads provider info from scrapers.json, runs all QC checks,
and prints a clean PASS/FAIL report.
"""
import sys, json, csv, re
from pathlib import Path

# Fix numpy ABI conflict
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

import pandas as pd

MONTHS = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']

CRICOS_RE = re.compile(r'^\d{6,7}[A-Za-z]?$')

# Load scrapers registry
ROOT = Path(__file__).resolve().parent
REGISTRY = json.loads((ROOT / 'scrapers.json').read_text(encoding='utf-8'))

# Known provider code verification
PROVIDER_CODES = {
    '00279B': 'ECU', '00300K': 'CDU', '00301J': 'Curtin',
    '00125J': 'Murdoch', '00126G': 'UWA', '00244B': 'UniSQ',
    '02225M': 'UniSQ', '00123M': 'UofA (legacy)', '00124K': 'Victoria',
    '00197D': 'Acknowledge', '00213J': 'QUT', '00212K': 'UC',
    '00219C': 'CQU', '00233E': 'Griffith', '00246M': 'Think',
    '04249J': 'Adelaide (new)', '00114A': 'SCU', '01595D': 'USC',
}

# ==== Helper functions ====

def cell(v):
    """Safely get cell value as string."""
    if pd.isna(v) or v is None: return ""
    s = str(v).strip()
    return "" if s in ('nan', 'NULL', 'None') else s

def fmt_dollar(val):
    """Format a number as $x,xxx."""
    try: return f"${float(val):,.0f}"
    except: return str(val)

def fmt_annual(fee, weeks):
    """Compute implied annual fee from total fee and duration weeks."""
    try:
        f = float(fee)
        w = float(weeks)
        if w <= 0: return None
        return f / w * 52
    except: return None


# ==== Main QC ====

def run_qc(slug):
    # Find entry in registry — prefer one with xlsx key
    entry = None
    candidates = [e for e in REGISTRY if e['id'] == slug and 'xlsx' in e]
    if candidates:
        entry = candidates[0]
    else:
        for e in REGISTRY:
            if e['id'] == slug:
                entry = e
                break
    if not entry:
        print(f"\n❌ Provider '{slug}' not found in scrapers.json")
        print(f"   Available: {[e['id'] for e in REGISTRY if 'scraper' in e][-20:]}")
        sys.exit(1)

    name = entry['name']
    xlsx_path = ROOT / entry['xlsx']
    sql_path_rel = entry.get('sql', '')
    sql_path = ROOT / sql_path_rel if sql_path_rel else None

    # === File existence ===
    checks = []

    xlsx_ok = xlsx_path.exists()
    sql_ok = sql_path.exists() if sql_path else False

    checks.append(('📁 XLSX exists', '✅' if xlsx_ok else '❌'))
    checks.append(('📁 SQL exists', '✅' if sql_ok else '❌'))

    if not xlsx_ok:
        print(f"\n{'='*60}")
        print(f"  QC REPORT: {name}")
        print(f"{'='*60}")
        print()
        for label, status in checks: print(f"  {status} {label}")
        print(f"\n  ❌ QC FAILED — XLSX not found at: {xlsx_path}")
        return

    # === Load data ===
    df = pd.read_excel(xlsx_path)
    n_total = len(df)

    # Derive provider code from SQL file
    provider_code = ""
    if sql_ok:
        sql_text = sql_path.read_text(encoding='utf-8')
        m = re.search(r"cricos_provider_code\s*=\s*'(\w+)'", sql_text)
        if m: provider_code = m.group(1)

    # CSV count
    csv_count = 0
    csv_entries = []
    try:
        with open(ROOT / 'cricos-courses.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                if row and len(row) >= 3 and row[0].strip() == provider_code:
                    csv_count += 1
                    csv_entries.append({
                        'cricos': row[2].strip(),
                        'name': row[3].strip() if len(row) > 3 else "",
                        'fee': row[20].strip().replace('$','').replace(',','') if len(row) > 20 else "",
                        'duration': row[19].strip() if len(row) > 19 else "",
                    })
    except FileNotFoundError:
        pass

    # === CRICOS ===
    cricos_series = df['cricos'].astype(str)
    real_cricos = sum(1 for c in cricos_series if isinstance(c, str) and CRICOS_RE.match(c))
    cricos_rate = real_cricos / csv_count * 100 if csv_count > 0 else 0
    cricos_pass = cricos_rate >= 50
    checks.append((f'🆔 CRICOS matched {real_cricos}/{csv_count} ({cricos_rate:.0f}%)',
                   '✅' if cricos_pass else '❌'))

    # === Fee sanity ===
    fees = pd.to_numeric(df['offshore_tuition_fee'], errors='coerce')
    valid_fees = fees.dropna()
    durs = pd.to_numeric(df['course_duration_per_week'], errors='coerce')

    total_fee_pass = True
    annual_fee_pass = True
    fee_issues = []
    annual_fees = []

    if len(valid_fees) > 0:
        # Total fee range check
        below = valid_fees[(valid_fees > 0) & (valid_fees < 1000)]
        above_mil = valid_fees[valid_fees > 1_000_000]
        zero = valid_fees[valid_fees == 0]

        if len(below) > 0:
            total_fee_pass = False
            fee_issues.append(f'{len(below)} fees < $1K (may be CSP domestic)')
        if len(above_mil) > 0:
            total_fee_pass = False
            fee_issues.append(f'{len(above_mil)} fees > $1M (duration bug!)')
        if len(zero) > 0:
            fee_issues.append(f'{len(zero)} fees = $0')

        # Annual fee check (reverse-engineer)
        for i in range(len(df)):
            f = df['offshore_tuition_fee'].iloc[i]
            d = df['course_duration_per_week'].iloc[i]
            try:
                f_val = float(f) if pd.notna(f) else None
                d_val = float(d) if pd.notna(d) else None
            except ValueError:
                continue
            if f_val is not None and d_val is not None and d_val > 0:
                ann = fmt_annual(f_val, d_val)
                if ann is not None and ann > 0:
                    annual_fees.append(ann)

        if annual_fees:
            min_ann = min(annual_fees)
            max_ann = max(annual_fees)
            bad_ann = [a for a in annual_fees if a < 5000 or a > 100_000]
            if bad_ann:
                annual_fee_pass = False
                fee_issues.append(f'{len(bad_ann)} implied annual fees outside $5K-$100K range')

    fee_status = '✅' if (total_fee_pass and annual_fee_pass) else '⚠️'
    checks.append((f'💰 Fee total ${valid_fees.min():,.0f}–${valid_fees.max():,.0f}'
                   if len(valid_fees) > 0 else '💰 Fee: none', fee_status))

    if fee_issues:
        for issue in fee_issues:
            checks.append((f'   ⚠️ {issue}', ''))

    # === Duration sanity ===
    valid_durs = durs.dropna()
    dur_pass = True
    dur_issues = []
    if len(valid_durs) > 0:
        extreme = valid_durs[valid_durs > 520]  # > 10 years
        if len(extreme) > 0:
            dur_pass = False
            dur_issues.append(f'{len(extreme)} durations > 10 years ({int(extreme.max())}w max)')
        single = valid_durs[valid_durs == 1]
        if len(single) > 0:
            dur_issues.append(f'{len(single)} durations = 1 week')
    checks.append((f'📅 Duration range {int(valid_durs.min())}w–{int(valid_durs.max())}w'
                   if len(valid_durs) > 0 else '📅 Duration: none',
                   '✅' if dur_pass else '⚠️'))
    for issue in dur_issues:
        checks.append((f'   ⚠️ {issue}', ''))

    # === Intake check ===
    all_intakes = set()
    intake_noise = set()
    for v in df['intake'].dropna():
        parts = str(v).split(',')
        for p in parts:
            p = p.strip()
            if p:
                all_intakes.add(p)
                if p not in MONTHS and len(p) > 2:
                    intake_noise.add(p)

    real_intakes = [m for m in MONTHS if m in all_intakes]
    intake_pass = len(intake_noise) == 0
    intake_label = ', '.join(real_intakes) if real_intakes else '(none)'
    intake_status = '✅' if intake_pass else '⚠️'
    if len(all_intakes) == 0:
        intake_status = '❌'
        intake_label = 'EMPTY'
    checks.append((f'📆 Intake: {intake_label}', intake_status))
    if intake_noise:
        checks.append((f'   ⚠️ Non-month values: {", ".join(intake_noise)}', ''))

    # === Nursing spot-check ===
    nurs_mask = df['title'].str.contains('Nurs|Midwi', case=False, na=False)
    nursing = df[nurs_mask & cricos_series.str.match(CRICOS_RE.pattern, na=False)]
    nursing_all = df[nurs_mask]
    nursing_pass = True
    nursing_issues = []
    no_cricos_nurs = nursing_all[nursing_all['cricos'].astype(str).str.match(CRICOS_RE.pattern, na=False) == False]

    if len(nursing_all) > 0 and len(no_cricos_nurs) == len(nursing_all):
        nursing_pass = False
        nursing_issues.append('All nursing courses lack CRICOS')

    if len(nursing) > 0:
        for _, r in nursing.iterrows():
            f = pd.to_numeric(r['offshore_tuition_fee'], errors='coerce')
            d = pd.to_numeric(r['course_duration_per_week'], errors='coerce')
            if pd.notna(f) and float(f) < 10000:
                nursing_issues.append(f'{r["title"][:40]} fee ${float(f):,.0f} too low')
                nursing_pass = False
            if pd.isna(r['intake']) or str(r['intake']).strip() == '':
                nursing_issues.append(f'{r["title"][:40]} no intake')
                # Not a fail, just a warning

    checks.append((f'🩺 Nursing with CRICOS: {len(nursing)} / {len(nursing_all)} total',
                   '✅' if nursing_pass else '⚠️'))
    for issue in nursing_issues[:5]:
        checks.append((f'   ⚠️ {issue}', ''))
    if len(nursing_issues) > 5:
        checks.append((f'   ... and {len(nursing_issues)-5} more', ''))

    # === Provider code check ===
    pc_label = PROVIDER_CODES.get(provider_code, provider_code or '?')
    code_known = provider_code in PROVIDER_CODES
    checks.append((f'🏷️ Provider: {provider_code} ({pc_label})',
                   '✅' if code_known else 'ℹ️'))

    # === Deduplication ===
    unique_cricos = df.drop_duplicates(subset=['cricos'])
    dedup_rate = len(unique_cricos) / n_total * 100 if n_total > 0 else 0
    checks.append((f'📊 Unique CRICOS: {len(unique_cricos)}/{n_total} ({dedup_rate:.0f}%)', ''))

    # === SQL Format Check ===
    sql_format_pass = True
    sql_format_issues = []
    if sql_ok:
        sql_text = sql_path.read_text(encoding='utf-8')
        # Check header: provider_institution UPDATE with intake_date
        has_header = bool(re.search(r'UPDATE provider_institution\s+SET\s+intake_date\s*=', sql_text, re.I))
        if not has_header:
            sql_format_pass = False
            sql_format_issues.append('Missing provider_institution header')
        
        # Check columns in course UPDATE (main full course entries)
        course_blocks = re.findall(r'UPDATE courses SET(.*?);\s*$', sql_text, re.I | re.S | re.M)
        has_main = False
        has_register = False
        for block in course_blocks:
            if 'course_description' in block:
                has_main = True
            if 'Register-only' in sql_text:
                has_register = True
        
        has_onshore = bool(re.search(r'onshore_tuition_fee\s*=', sql_text, re.I))
        has_enrolment = bool(re.search(r'enrolment_fee\s*=', sql_text, re.I))
        has_materials = bool(re.search(r'materials_fee\s*=', sql_text, re.I))
        has_apply_form = bool(re.search(r'apply_form\s*=', sql_text, re.I))
        has_updated_at = bool(re.search(r'updated_at\s*=\s*NOW\(\)', sql_text, re.I))
        has_skipped = bool(re.search(r'--\s*⚠️\s*Skipped', sql_text))
        
        if not has_onshore:
            sql_format_issues.append('Missing onshore_tuition_fee')
            sql_format_pass = False
        if not has_enrolment:
            sql_format_issues.append('Missing enrolment_fee')
            sql_format_pass = False
        if not has_materials:
            sql_format_issues.append('Missing materials_fee')
            sql_format_pass = False
        if not has_apply_form:
            sql_format_issues.append('Missing apply_form')
            sql_format_pass = False
        if not has_updated_at:
            sql_format_issues.append('Missing updated_at=NOW()')
            sql_format_pass = False
        
        # Check no course_name or cricos_provider_code in course UPDATE
        if re.search(r'(?<!provider_institution\s)SET.*course_name\s*=', sql_text, re.I | re.S):
            sql_format_issues.append('Has deprecated course_name column in courses UPDATE')
            sql_format_pass = False
        if re.search(r'(?<!provider_institution\s)SET.*cricos_provider_code\s*=', sql_text, re.I | re.S):
            sql_format_issues.append('Has deprecated cricos_provider_code in courses UPDATE')
            sql_format_pass = False
        
        # Check description has HTML content
        descs = re.findall(r"course_description\s*=\s*'([^']*)'", sql_text, re.I)
        if descs:
            empty_descs = sum(1 for d in descs if not d.strip())
            html_descs = sum(1 for d in descs if '<' in d and '>' in d)
            if html_descs == 0 and empty_descs < len(descs):
                sql_format_issues.append(f'Description values are plain text, not HTML')
                # Not a fail, just a note
        
        checks.append((f'📝 SQL format correct', '✅' if sql_format_pass else '⚠️'))
        for issue in sql_format_issues[:5]:
            checks.append((f'   ⚠️ {issue}', ''))
        if len(sql_format_issues) > 5:
            checks.append((f'   ... and {len(sql_format_issues)-5} more', ''))
    else:
        checks.append((f'📝 SQL format check', '⚠️ (no SQL file)'))

    # === Overall PASS/FAIL ===
    all_pass = all(
        s == '✅' for label, s in checks
        if s in ('✅', '❌', '⚠️') and not label.startswith('   ')
    )

    # === Print report ===
    print(f"\n{'='*60}")
    print(f"  QC REPORT: {name}")
    print(f"{'='*60}")
    print()
    for label, status in checks:
        if status:
            print(f"  {status} {label}")
        else:
            print(f"     {label}")

    print()
    print(f"  Rows: {n_total} | CSV matched: {csv_count}")
    print(f"  Fee (total): ${valid_fees.min():,.0f} – ${valid_fees.max():,.0f}" if len(valid_fees) > 0 else "  Fee: NONE")
    
    if annual_fees:
        print(f"  Fee (annual): ${min(annual_fees):,.0f} – ${max(annual_fees):,.0f}/yr")
    
    print(f"  Duration: {int(valid_durs.min())}w – {int(valid_durs.max())}w" if len(valid_durs) > 0 else "  Duration: NONE")
    print()
    print(f"{'='*60}")
    if all_pass:
        print(f"  ✅ ALL CHECKS PASSED — Ready to register! 🚀")
    else:
        print(f"  ⚠️  SOME CHECKS FAILED — Review issues above")
    print(f"{'='*60}")
    print()
    print(f"  Files: {xlsx_path.name} | {sql_path.name}")
    print()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: qc_report.py <provider_slug>  or  qc_report.py --all")
        print()
        print("Available providers:")
        for e in REGISTRY:
            if 'xlsx' in e:
                print(f"  {e['id']}  — {e['name']}")
        sys.exit(1)

    if sys.argv[1] == '--all':
        passed = 0
        failed = 0
        for e in REGISTRY:
            if 'xlsx' not in e: continue
            print(f"\n{'─'*60}")
            print(f"  ▶ {e['name']}")
            print(f"{'─'*60}")
            # Run QC, capture result via return value
            import io, contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                run_qc(e['id'])
            output = buf.getvalue()
            # Show full output
            print(output.strip()[-200:])
            if '✅ ALL CHECKS PASSED' in output:
                passed += 1
            else:
                failed += 1
        print(f"\n{'='*60}")
        print(f"  ✅ PASS: {passed} | ⚠️  FAIL: {failed}")
        print(f"{'='*60}")
    else:
        run_qc(sys.argv[1])
