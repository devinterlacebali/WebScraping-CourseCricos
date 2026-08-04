import asyncio
from playwright.async_api import async_playwright
import json
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def main():
    async with async_playwright() as p:
        print("Launching chromium...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Go to the base page to establish the session
        url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        
        # Wait 10 seconds for Cloudflare and assets to load
        print("Waiting 10 seconds...")
        await page.wait_for_timeout(10000)
        
        # Now try to evaluate fetch in browser context
        api_url = "/courses/data/2026/international/bu/bachelor-of-business"
        print(f"Evaluating fetch({api_url}) in page context...")
        try:
            res_text = await page.evaluate("""async (url) => {
                const res = await fetch(url);
                return {
                    status: res.status,
                    statusText: res.statusText,
                    text: await res.text()
                };
            }""", api_url)
            
            print("Status:", res_text["status"])
            print("Status Text:", res_text["statusText"])
            text_len = len(res_text["text"])
            print("Response Length:", text_len)
            
            if res_text["status"] == 200:
                print("SUCCESS! Response snippet:")
                print(res_text["text"][:1000])
                # Save JSON
                try:
                    data = json.loads(res_text["text"])
                    with open("scratch/latrobe_api_success.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2)
                    print("Saved to scratch/latrobe_api_success.json")
                except Exception as je:
                    print("Error parsing JSON:", je)
            else:
                print("Error Response:")
                print(res_text["text"][:1000])
        except Exception as e:
            print("Evaluate fetch failed:", e)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
