import re

def analyze_cricos(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.finditer(r"UPDATE courses SET(.*?)WHERE cricos_course_code = '([^']+)';", content, re.DOTALL | re.IGNORECASE)
    res = {}
    for m in matches:
        block = m.group(1)
        cricos = m.group(2)
        
        apply_match = re.search(r"apply_form\s*=\s*'([^']+)'", block)
        url = apply_match.group(1) if apply_match else "unknown"
        
        desc_match = re.search(r"course_description\s*=\s*'(.*?)',", block, re.DOTALL)
        desc = desc_match.group(1) if desc_match else ""
        
        if cricos not in res:
            res[cricos] = []
        res[cricos].append((url, desc))
    return res

orig = analyze_cricos("The University Of Adelaide/adelaide_courses_update.sql")
fixed = analyze_cricos("The University Of Adelaide/adelaide_courses_update_fixed.sql")

# Let's look at 115677K
print("115677K in Original:", len(orig.get("115677K", [])))
print("115677K in Fixed:", len(fixed.get("115677K", [])))

if fixed.get("115677K"):
    url, desc = fixed["115677K"][0]
    print(f"Fixed URL: {url}")
    print(f"Fixed Desc (first 300 chars): {desc[:300]}")
    
# Let's list some other duplicate codes in Fixed to see if they exist
for k, v in fixed.items():
    if len(orig.get(k, [])) > 1:
        print(f"CRICOS {k} was updated {len(orig[k])} times in original, now {len(v)} times in fixed. URL: {v[0][0]}")
