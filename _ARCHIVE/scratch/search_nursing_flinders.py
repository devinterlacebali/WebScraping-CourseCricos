import json
import urllib.request

ALGOLIA_APP = "EDB1U8JSME"
ALGOLIA_KEY = "5292c8a20c605ac1c7c48baa60e8317e"
ALGOLIA_INDEX = "flinders_main_search"

def main():
    url = f"https://{ALGOLIA_APP}-dsn.algolia.net/1/indexes/{ALGOLIA_INDEX}/query"
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
        print("Total courses:", len(hits))
        
        # Look for nursing
        nursing_hits = []
        for h in hits:
            name = h.get("courseName", "")
            if "nursing" in name.lower():
                nursing_hits.append(h)
                
        print(f"Found {len(nursing_hits)} courses with 'nursing' in Algolia:")
        for h in nursing_hits:
            print(f"- Name: {h.get('courseName')} | Availability: {h.get('availability')} | Link: {h.get('courseLink')}")
            
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
