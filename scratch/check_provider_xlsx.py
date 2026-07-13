import pandas as pd

path = "A.RESULT/data_provider.xlsx"
try:
    xl = pd.ExcelFile(path)
    print("Sheets in data_provider.xlsx:", xl.sheet_names)
    df = xl.parse(xl.sheet_names[0])
    print("Columns:", list(df.columns))
    print("First 5 rows:")
    print(df.head())
except Exception as e:
    print("Error:", e)
