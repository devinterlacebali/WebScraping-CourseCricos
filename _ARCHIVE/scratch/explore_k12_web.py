"""
Explore K-12 grammar school websites for international student fee data.
Checks common URL patterns for international student info.
"""
import requests, re, json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

schools = [
    ("00139C", "Fintona Girls School", "www.fintona.vic.edu.au"),
    ("00140K", "Firbank Grammar School", "www.firbank.vic.edu.au"),
    ("00141J", "Camberwell Anglican Girls' Grammar School", "www.cggs.vic.edu.au"),
    ("00142G", "The Geelong College", "www.geelongcollege.vic.edu.au"),
    ("00143G", "Geelong Grammar School", "www.ggs.vic.edu.au"),
    ("00144F", "The Hamilton and Alexandra College", "www.hamiltoncollege.vic.edu.au"),
    ("00145E", "Huntingtower School", "www.huntingtower.vic.edu.au"),
    ("00147C", "The Ivanhoe Grammar School", "www.ivanhoe.com.au"),
    ("00149A", "Kilvington Grammar School", "www.kilvington.vic.edu.au"),
    ("00150G", "Kingswood College", "www.kingswoodcollege.vic.edu.au"),
    ("00151G", "The Knox School", "www.knox.vic.edu.au"),
    ("00152F", "Lauriston Girls' School", "lauriston.vic.edu.au"),
]

# Common paths to try for international fee info
COMMON_PATHS = [
    "/enrolment/international-students",
    "/enrolment/international",
    "/international-students",
    "/international",
    "/admissions/international-students",
    "/admissions/international",
    "/fees/international",
    "/fees",
    "/enrolment/fees",
    "/international/enrolment",
    "/enrolment",
    "/admissions/fees",
]

results = {}
for code, name, domain in schools:
    results[code] = {"name": name, "domain": domain, "pages": {}}
    
    for path in COMMON_PATHS:
        url = f"https://{domain}{path}"
        try:
            r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            has_international = "international" in r.text.lower()
            size = len(r.text)
            results[code]["pages"][path] = {"status": r.status_code, "size": size, "has_intl": has_international}
            print(f"{code} {domain}{path}: {r.status_code} ({size}b) intl={has_international}")
        except Exception as e:
            results[code]["pages"][path] = {"status": str(e)[:60], "size": 0, "has_intl": False}
            print(f"{code} {domain}{path}: ERROR {str(e)[:60]}")

# Print summary
print("\n\n=== SUMMARY ===")
for code, info in results.items():
    working = [p for p, d in info["pages"].items() if d.get("status") == 200]
    print(f"{code} {info['name']}: {len(working)} working paths")
    if working:
        for p in working:
            d = info["pages"][p]
            print(f"  {p} ({d['size']}b, intl={d['has_intl']})")

json.dump(results, open(BASE / "scratch" / "k12_explore_results.json", "w"), indent=2)
print("\nResults saved to scratch/k12_explore_results.json")
