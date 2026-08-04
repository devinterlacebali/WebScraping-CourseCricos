"""
USC Cloudflare Detection Check
Uses curl_cffi to try bypass if needed
"""
import requests

def main():
    print("="*60)
    print("CLOUDFLARE / WAF CHECK")
    print("="*60)
    
    url = "https://www.unisc.edu.au/"
    
    # Standard requests
    print(f"\n[1] Standard requests.get()")
    try:
        r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
        print(f"    Status: {r.status_code}")
        print(f"    Server: {r.headers.get('Server', 'N/A')}")
        print(f"    Content length: {len(r.text):,}")
        print(f"    Has Cloudflare headers: {'cf-ray' in r.headers or 'cf-cache-status' in r.headers or 'Server: cloudflare' in str(r.headers)}")
        print(f"    Headers: {dict(r.headers)}")
    except Exception as e:
        print(f"    Error: {e}")
    
    # Check if curl_cffi is available
    print(f"\n[2] curl_cffi available check")
    try:
        import curl_cffi
        from curl_cffi import requests as curly
        print(f"    curl_cffi version: {curl_cffi.__version__}")
        
        print(f"\n[3] curl_cffi requests.get()")
        r2 = curly.get(url, timeout=30, impersonate="chrome110")
        print(f"    Status: {r2.status_code}")
        print(f"    Content length: {len(r2.text):,}")
    except ImportError:
        print(f"    Not installed")
    
    # Final verdict
    print(f"\n[VERDICT]")
    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200 and "cloudflare" in r.headers.get('Server', '').lower():
            print("    Cloudflare detected ✓ (challenge may be needed)")
        elif r.status_code == 200:
            print("    NO Cloudflare issue - direct access works")
            print(f"    Server: {r.headers.get('Server', 'N/A')}")
        elif r.status_code == 503:
            print("    Cloudflare challenge detected (503)")
        else:
            print(f"    Status: {r.status_code} - check manually")
    except Exception as e:
        print(f"    Error reaching website: {e}")

if __name__ == '__main__':
    main()
