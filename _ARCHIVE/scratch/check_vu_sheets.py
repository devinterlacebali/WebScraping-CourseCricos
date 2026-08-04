import openpyxl

for fn in ["vu.xlsx", "vu_scraped_all.xlsx"]:
    try:
        wb = openpyxl.load_workbook(f"Victoria University/{fn}")
        sheet = wb.active
        print(f"{fn}: {sheet.max_row} rows")
    except Exception as e:
        print(f"Error {fn}: {e}")
