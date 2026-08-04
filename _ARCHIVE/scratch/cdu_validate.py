"""Validate CDU output."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import re, pandas as pd

df = pd.read_excel('Charles Darwin University/cdu.xlsx')
cricos_pat = re.compile(r'^\d{6,7}[A-Za-z]?$')
real_cricos = sum(1 for c in df['cricos'].astype(str) if isinstance(c, str) and cricos_pat.match(c))
with_fee = sum(1 for f in df['offshore_tuition_fee'].astype(str) if re.match(r'^\d+$', str(f)))
with_dur = sum(1 for d in df['course_duration_per_week'].astype(str) if re.match(r'^\d+$', str(d)))
print(f'Total: {len(df)}, CRICOS: {real_cricos}, Fee: {with_fee}, Dur: {with_dur}')

nurs = df[df['title'].str.contains('Nurs|Midwi', case=False, na=False)]
print(f'\n=== Nursing ({len(nurs)}) ===')
for _, r in nurs.iterrows():
    f = r['offshore_tuition_fee']
    fs = 'N/A'
    if pd.notna(f):
        try: fs = f'${int(float(f)):,}'
        except: pass
    print(f'  {r["title"][:55]} | CRICOS={r["cricos"]} | Fee={fs}')

fees = pd.to_numeric(df['offshore_tuition_fee'], errors='coerce').dropna()
print(f'\nFee range: ${fees.min():,.0f} - ${fees.max():,.0f} (median ${fees.median():,.0f})')
durs = pd.to_numeric(df['course_duration_per_week'], errors='coerce').dropna()
for w in sorted(durs.unique()):
    print(f'  {int(w)}wk ({int(w)//52}yr): {int((durs==w).sum())} courses')
