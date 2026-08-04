"""Check key fees in Acknowledge output."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

df = pd.read_excel('Acknowledge Education/acknowledgeeducation.xlsx')
for _, r in df.iterrows():
    title = str(r.get('title', ''))
    fee = r.get('offshore_tuition_fee', '')
    if 'nursing' in title.lower() or 'social work' in title.lower():
        print(f'{title}: fee={fee}')
