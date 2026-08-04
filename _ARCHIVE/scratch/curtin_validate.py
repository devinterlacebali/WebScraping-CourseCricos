"""Validate Curtin output."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd, re

df = pd.read_excel('Curtin University/curtin.xlsx')
cricos_pat = re.compile(r'^\d{6,7}[A-Za-z]?$')
real_cricos = sum(1 for c in df['cricos'].astype(str) if isinstance(c, str) and cricos_pat.match(c))
with_fee = sum(1 for f in df['offshore_tuition_fee'].astype(str) if re.match(r'^\d+', str(f)))
print(f'Total: {len(df)}, CRICOS: {real_cricos}, Fee: {with_fee}')

# Nursing
nurs = df[df['title'].str.contains('Nurs|Midwi', case=False, na=False)]
print(f'\n=== Nursing ({len(nurs)}) ===')
for _, r in nurs.iterrows():
    f = r['offshore_tuition_fee']
    fs = 'N/A' if pd.isna(f) or str(f).strip() in ('', 'nan', '0.0') else f'${int(float(f)):,}'
    print(f'  {r["title"][:55]} | CRICOS={r["cricos"]} | Fee={fs}')

# Dedup summary - unique courses by CRICOS
unique = df.drop_duplicates(subset=['cricos'])
print(f'\nUnique by CRICOS: {len(unique)} (of {len(df)} total)')
print(f'Fee range: ${pd.to_numeric(unique["offshore_tuition_fee"], errors="coerce").min():,.0f} - ${pd.to_numeric(unique["offshore_tuition_fee"], errors="coerce").max():,.0f}')
