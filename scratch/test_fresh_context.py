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

async def test_slug_with_fresh_contexts(browser, slug):
    campuses = ["bu", "on", "sy", "be", "al", "sh"]
    years = ["2026", "2027"]
    
    for year in years:
        for campus in campuses:
            # Create a completely fresh context for each attempt to avoid cookie/bot accumulation
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            
            url = f"https://www.latrobe.edu.au/courses/data/{year}/international/{campus}/{slug}"
            print(f"Trying direct navigation on fresh context: {url}...")
            
            try:
                response = await page.goto(url, wait_until="domcontentloaded", timeout=15000)
                status = response.status if response else 0
                print(f"  Status: {status}")
                
                if status == 200:
                    text = await page.evaluate("() => document.body.innerText")
                    if "{" in text and "availability" in text:
                        data = json.loads(text)
                        if data.get("availability") is True:
                            print(f"  ✅ SUCCESS: Found data for {slug} on {campus}/{year}!")
                            await context.close()
                            return data
                elif status == 403:
                    # Cloudflare blocked - let's see if waiting helps or if it's dead
                    print("  Blocked 403. Waiting 5s to see if Turnstile solves...")
                    await page.wait_for_timeout(5000)
                    text = await page.evaluate("() => document.body.innerText")
                    if "{" in text and "availability" in text:
                        data = json.loads(text)
                        print(f"  ✅ SUCCESS after wait on {campus}/{year}!")
                        await context.close()
                        return data
                    
            except Exception as e:
                print(f"  Error: {e}")
            finally:
                await context.close()
                
    return None

async def main():
    slug = "graduate-diploma-in-information-technology"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        data = await test_slug_with_fresh_contexts(browser, slug)
        if data:
            c_data = data.get("data", {})
            print(f"\nFinal Title: {c_data.get('awardTitle')}")
            print(f"Final CRICOS: {c_data.get('cricosCourseCode')}")
        else:
            print("\n❌ Failed to find data.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
