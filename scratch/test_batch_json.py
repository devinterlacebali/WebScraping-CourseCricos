import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import json
import random
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def fetch_json(page, slug):
    campuses = ["bu", "on", "sy", "be", "al", "sh"]
    years = ["2026", "2027"]
    
    for year in years:
        for campus in campuses:
            url = f"https://www.latrobe.edu.au/courses/data/{year}/international/{campus}/{slug}"
            print(f"  Trying: year={year}, campus={campus}...")
            try:
                # Direct navigation to solve Cloudflare
                response = await page.goto(url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(3000)
                
                text = await page.evaluate("() => document.body.innerText")
                if "Just a moment..." not in text and "{" in text:
                    data = json.loads(text)
                    if data.get("availability") is True:
                        print(f"  ✅ SUCCESS: Found data for {slug} (year={year}, campus={campus})")
                        return data
            except Exception as e:
                pass
    print(f"  ❌ FAILED: Could not find JSON data for {slug}")
    return None

async def main():
    df = pd.read_excel("La Trobe University (La Trobe)/latrobe.xlsx")
    urls = df["url"].tolist()
    
    # Pick 5 random URLs
    sample_urls = random.sample(urls, min(5, len(urls)))
    print("Testing 5 sample course URLs:")
    for su in sample_urls:
        print(" -", su)
        
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        for url in sample_urls:
            slug = url.split("/courses/")[-1]
            print(f"\nFetching data for slug: {slug}...")
            data = await fetch_json(page, slug)
            if data:
                c_data = data.get("data", {})
                print(f"    Title: {c_data.get('awardTitle')}")
                print(f"    CRICOS: {c_data.get('cricosCourseCode')}")
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
