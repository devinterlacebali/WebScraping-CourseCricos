"""Check CSV coverage for 16 new providers."""
import csv

codes = {
    "03733E": "YourLife Health",
    "03741E": "Tred Consultants",
    "00017B": "Bond University",
    "00018A": "Dept for Education SA",
    "00051M": "ELC Career College",
    "00057E": "Alexander Language",
    "00094M": "SA College of English",
    "00098G": "UNSW",
    "00120C": "ANU",
    "00129E": "Ballarat Grammar",
    "00131M": "Billanook College",
    "00132K": "Brighton Grammar",
    "00134G": "Caulfield Grammar (cgs)",
    "00135G": "Carey Baptist Grammar",
    "00136F": "Caulfield Grammar",
    "00138D": "Eltham College",
}

with open("cricos-courses.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    counts = {}
    for row in reader:
        code = row["CRICOS Provider Code"].strip()
        expired = row["Expired"].strip().lower()
        if code in codes and expired != "yes":
            if code not in counts:
                counts[code] = 0
            counts[code] += 1

print(f"{'Code':8} {'Name':30} {'Courses':8}")
print("-"*48)
for code, name in sorted(codes.items()):
    c = counts.get(code, 0)
    print(f"{code:8} {name:30} {c:<8}")
