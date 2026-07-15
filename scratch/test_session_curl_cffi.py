from curl_cffi import requests
import json

def main():
    # Use session to keep cookies
    s = requests.Session()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
    }
    
    main_url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
    print(f"1. Fetching main page: {main_url}")
    try:
        r = s.get(main_url, headers=headers, impersonate="chrome110", timeout=15)
        print("Main page status:", r.status_code)
        print("Cookies acquired:", s.cookies.get_dict())
    except Exception as e:
        print("Error fetching main page:", e)
        return

    # Now make the AJAX request with the session
    ajax_url = "https://www.latrobe.edu.au/courses/data/2026/international/bu/bachelor-of-business"
    ajax_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": main_url,
    }
    
    print(f"\n2. Fetching AJAX data: {ajax_url}")
    try:
        r2 = s.get(ajax_url, headers=ajax_headers, impersonate="chrome110", timeout=15)
        print("AJAX status code:", r2.status_code)
        if r2.status_code == 200:
            print("SUCCESS! JSON keys:")
            print(r2.json().keys())
            with open("scratch/latrobe_ajax_success.json", "w", encoding="utf-8") as f:
                json.dump(r2.json(), f, indent=2)
            print("Saved to scratch/latrobe_ajax_success.json")
        else:
            print("AJAX content snippet:", r2.text[:500])
    except Exception as e:
        print("Error fetching AJAX:", e)

if __name__ == "__main__":
    main()
