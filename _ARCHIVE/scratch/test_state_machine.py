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

async def fetch_course_json(page, slug):
    campuses = ["bu", "on", "sy", "be", "al", "sh"]
    years = ["2026", "2027"]
    
    for year in years:
        for campus in campuses:
            url = f"https://www.latrobe.edu.au/courses/data/{year}/international/{campus}/{slug}"
            print(f"  Trying: year={year}, campus={campus}...")
            try:
                response = await page.goto(url, wait_until="domcontentloaded", timeout=20000)
                status = response.status if response else 0
                
                if status == 404:
                    # Instant fallback, no sleep
                    continue
                    
                if status == 403:
                    # Cloudflare challenge - wait for solving
                    print("    Cloudflare challenge detected, waiting 10s for solver...")
                    await page.wait_for_timeout(10000)
                    
                # Check page text for JSON
                text = await page.evaluate("() => document.body.innerText")
                if "{" in text and "availability" in text:
                    data = json.loads(text)
                    if data.get("availability") is True:
                        print(f"    ✅ Found data for {slug} (year={year}, campus={campus})")
                        return data
            except Exception as e:
                print(f"    Error on {campus}/{year}: {e}")
                
    return None

async def main():
    test_slugs = [
        "graduate-diploma-in-information-technology",
        "diploma-of-teacher-education",
        "master-of-health-administration",
        "diploma-of-science",
        "associate-degree-of-teacher-education"
    ]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        for slug in test_slugs:
            print(f"\nFetching slug: {slug}...")
            data = await fetch_course_json(page, slug)
            if data:
                c_data = data.get("data", {})
                print(f"    Title: {c_data.get('awardTitle')}")
                print(f"    CRICOS: {c_data.get('cricosCourseCode')}")
            else:
                print(f"    ❌ Could not fetch data for {slug}")
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
