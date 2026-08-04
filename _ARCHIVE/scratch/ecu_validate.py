"""Validate ECU output."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

df = pd.read_excel('Edith Cowan University/ecu.xlsx')
print(f'Total courses: {len(df)}')
print(f'With CRICOS: {df.cricos.astype(bool).sum()}')
print(f'With fee: {df.offshore_tuition_fee.astype(bool).sum()}')
print(f'With duration: {df.course_duration_per_week.astype(bool).sum()}')

print('\n=== Nursing courses ===')
nursing = df[df['title'].str.contains('Nursing', case=False, na=False)]
for _, r in nursing.iterrows():
    fee = r['offshore_tuition_fee']
    fee_str = f'${int(float(fee)):,}' if fee and str(fee).strip() not in ('', 'nan', 'NaN') else 'N/A'
    print(f'  {r["title"][:55]} | CRICOS={r["cricos"]} | Fee={fee_str}')

print('\n=== Fee distribution (with fee) ===')
fees = df[df['offshore_tuition_fee'].astype(bool)]['offshore_tuition_fee'].astype(float)
print(f'  Count: {len(fees)}')
print(f'  Min: ${fees.min():,.0f}')
print(f'  Max: ${fees.max():,.0f}')
print(f'  Median: ${fees.median():,.0f}')

suspect = df[(df['offshore_tuition_fee'].astype(bool)) & (df['offshore_tuition_fee'].astype(float) > 200000)]
if len(suspect) > 0:
    print(f'\n⚠️  {len(suspect)} courses with fee > $200,000:')
    for _, r in suspect.iterrows():
        dur = r['course_duration_per_week']
        dur_str = f'{int(dur)}wk ({int(dur)//52}yr)' if dur and str(dur).strip() else '?'
        print(f'  {r["title"][:50]} | Fee=${int(float(r["offshore_tuition_fee"])):,} | Dur={dur_str}')

print('\n=== Duration distribution ===')
durs = df[df['course_duration_per_week'].astype(bool)]['course_duration_per_week'].astype(int)
for w in sorted(durs.unique()):
    cnt = (durs == w).sum()
    print(f'  {w}wk ({w//52}yr): {cnt} courses')

print('\n✅ Validation complete')
