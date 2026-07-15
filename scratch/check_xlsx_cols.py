import pandas as pd

def main():
    df = pd.read_excel("Deakin University/deakin.xlsx")
    print("Columns in Deakin University/deakin.xlsx:")
    print(df.columns.tolist())
    print("\nFirst 3 rows:")
    print(df.head(3))

if __name__ == "__main__":
    main()
