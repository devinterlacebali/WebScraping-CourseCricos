import json
import urllib.request
import time

ALGOLIA_APP = "EDB1U8JSME"
ALGOLIA_KEY = "5292c8a20c605ac1c7c48baa60e8317e"
ALGOLIA_INDEX = "flinders_main_search"

def main():
    url = f"https://{ALGOLIA_APP}-dsn.algolia.net/1/indexes/{ALGOLIA_INDEX}/query"
    # Query 1000 hits with no filters (or filtering to courses)
    body = json.dumps({"params": "query=&hitsPerPage=1000&filters=dir2:courses"}).encode()
    headers = {
        "X-Algolia-Application-Id": ALGOLIA_APP,
        "X-Algolia-API-Key": ALGOLIA_KEY,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    
    try:
        req = urllib.request.Request(url, data=body, method="POST", headers=headers)
        resp = json.loads(urllib.request.urlopen(req, timeout=40).read().decode())
        hits = resp.get("hits", [])
        print("Total courses in Algolia index (all):", len(hits))
        
        # Check a few specific course names
        search_names = ["Speech Pathology", "Education", "Nutrition", "Social Work", "Study Abroad"]
        found = {name: [] for name in search_names}
        for h in hits:
            name = h.get("courseName", "")
            avail = h.get("availability", [])
            link = h.get("courseLink", "")
            for sn in search_names:
                if sn.lower() in name.lower():
                    found[sn].append((name, avail, link))
                    
        for sn in search_names:
            print(f"\n--- Matches for '{sn}': ---")
            for name, avail, link in found[sn][:10]:
                print(f"  * {name} | Availability: {avail} | Link: {link}")
                
    except Exception as e:
        print("Error fetching from Algolia:", e)

if __name__ == '__main__':
    main()
