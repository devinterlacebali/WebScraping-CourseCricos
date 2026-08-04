import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Note: we need a normal context (not blocking resources) to see all API calls
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Array to store requests
        requests_log = []
        
        page.on("request", lambda request: requests_log.append(request.url))
        
        url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        
        print("\n--- Network Requests Logged ---")
        print(f"Total requests: {len(requests_log)}")
        
        # Look for API calls, json files, or search queries
        api_requests = [r for r in requests_log if "json" in r or "api" in r or "query" in r or "data" in r]
        print(f"Found {len(api_requests)} potential data requests:")
        for r in api_requests[:50]:
            print(f"  {r}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
