from curl_cffi import requests
import json

def test_url(url):
    print(f"Fetching: {url}")
    try:
        # Impersonate chrome
        r = requests.get(url, impersonate="chrome110", timeout=15)
        print("Status code:", r.status_code)
        if r.status_code == 200:
            data = r.json()
            print("Successfully parsed JSON! Keys:")
            print(data.keys())
            # Save snippet
            with open("scratch/latrobe_api_response.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print("Saved to scratch/latrobe_api_response.json")
            return True
        else:
            print("Response text snippet:", r.text[:500])
    except Exception as e:
        print("Error:", e)
    return False

def main():
    # Let's try 2026 and 2027, international, campus 'bu'
    urls = [
        "https://www.latrobe.edu.au/courses/data/2026/international/bu/bachelor-of-business",
        "https://www.latrobe.edu.au/courses/data/2027/international/bu/bachelor-of-business",
        "https://www.latrobe.edu.au/courses/data/2026/domestic/bu/bachelor-of-business",
    ]
    for url in urls:
        if test_url(url):
            break

if __name__ == "__main__":
    main()
