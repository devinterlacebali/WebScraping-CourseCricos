import pandas as pd
import numpy as np

df = pd.read_excel("The University Of Adelaide/adelaide.xlsx")

print("--- Total rows:", len(df))

# 1. Check duplicate CRICOS codes
duplicates = df[df.duplicated(subset=['cricos'], keep=False) & df['cricos'].notna()]
print(f"\n--- Duplicated CRICOS codes ({len(duplicates)} rows):")
for cricos, g in duplicates.groupby('cricos'):
    print(f"CRICOS: {cricos} (occurs {len(g)} times)")
    for idx, row in g.iterrows():
        print(f"  - Title: {row['title']}")
        print(f"    URL: {row['url']}")
        print(f"    Fee: {row['offshore_tuition_fee']}, Duration: {row['course_duration_per_week']}")

# 2. Check low fees (< 1000)
low_fees = df[(df['offshore_tuition_fee'] < 1000) & df['offshore_tuition_fee'].notna()]
print(f"\n--- Low fees (< 1000) ({len(low_fees)} rows):")
for idx, row in low_fees.iterrows():
    print(f"Title: {row['title']} | CRICOS: {row['cricos']}")
    print(f"  URL: {row['url']}")
    print(f"  Fee: {row['offshore_tuition_fee']}, Duration: {row['course_duration_per_week']}")

# 3. Check high durations (> 520 weeks)
long_duration = df[(df['course_duration_per_week'] > 520) & df['course_duration_per_week'].notna()]
print(f"\n--- Long durations (> 520 weeks) ({len(long_duration)} rows):")
for idx, row in long_duration.iterrows():
    print(f"Title: {row['title']} | CRICOS: {row['cricos']}")
    print(f"  URL: {row['url']}")
    print(f"  Fee: {row['offshore_tuition_fee']}, Duration: {row['course_duration_per_week']}")

# 4. Check annual fee anomalies (annual fee < 5000 or > 100000)
df['implied_annual_fee'] = df['offshore_tuition_fee'] / df['course_duration_per_week'] * 52
annual_anomalies = df[((df['implied_annual_fee'] < 5000) | (df['implied_annual_fee'] > 100000)) & df['implied_annual_fee'].notna()]
print(f"\n--- Implied annual fee anomalies ({len(annual_anomalies)} rows):")
for idx, row in annual_anomalies.iterrows():
    print(f"Title: {row['title']} | CRICOS: {row['cricos']}")
    print(f"  URL: {row['url']}")
    print(f"  Fee: {row['offshore_tuition_fee']}, Duration: {row['course_duration_per_week']}, Implied Annual: {row['implied_annual_fee']:.2f}")
