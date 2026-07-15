import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import json
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def scrape_course_info(page, course_url):
    print(f"\n1. Navigating to main page: {course_url}")
    # Do not block resources, load page normally
    await page.goto(course_url, wait_until="domcontentloaded", timeout=45000)
    
    # Wait a few seconds for React/Vue selects to render
    await page.wait_for_timeout(5000)
    
    html = await page.content()
    soup = BeautifulSoup(html, "html.parser")
    
    # Extract campus options
    campus_select = soup.find("select", id="courseCampus")
    campus_codes = []
    if campus_select:
        campus_codes = [opt.get("value") for opt in campus_select.find_all("option") if opt.get("value")]
        
    # Extract year options
    year_select = soup.find("select", id="courseYear")
    years = []
    if year_select:
        years = [opt.get("value") for opt in year_select.find_all("option") if opt.get("value")]
        
    print(f"   Parsed campus codes: {campus_codes}")
    print(f"   Parsed years: {years}")
    
    if not campus_codes:
        # Fallback default campus if select not found
        campus_codes = ["BU"]
    if not years:
        # Fallback default year if select not found
        years = ["2026", "2027"]
        
    # We'll use the first year and first campus
    year = years[0]
    campus = campus_codes[0].lower() # e.g. 'ON' -> 'on', 'BU' -> 'bu'
    
    slug = course_url.split("/courses/")[-1]
    
    # Construct API URL
    api_url = f"https://www.latrobe.edu.au/courses/data/{year}/international/{campus}/{slug}"
    print(f"2. Navigating to API URL: {api_url}")
    
    response = await page.goto(api_url, wait_until="domcontentloaded", timeout=45000)
    status = response.status if response else 0
    print(f"   API Response Status: {status}")
    
    if status == 403:
        print("   Cloudflare challenge detected! Waiting 12s for browser solver...")
        await page.wait_for_timeout(12000)
        
    text = await page.evaluate("() => document.body.innerText")
    if "{" in text and "availability" in text:
        data = json.loads(text)
        print("   ✅ SUCCESS: Loaded and parsed JSON!")
        return data
    else:
        print("   ❌ FAILED: Could not parse JSON from page.")
        print("   Page content snippet:", text[:300].strip())
        return None

async def main():
    test_urls = [
        "https://www.latrobe.edu.au/courses/graduate-diploma-in-information-technology",
        "https://www.latrobe.edu.au/courses/master-of-health-administration",
        "https://www.latrobe.edu.au/courses/diploma-of-science"
    ]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        for url in test_urls:
            data = await scrape_course_info(page, url)
            if data:
                c_data = data.get("data", {})
                print(f"      Course Title: {c_data.get('awardTitle')}")
                print(f"      CRICOS Code: {c_data.get('cricosCourseCode')}")
            # Wait 3 seconds between courses
            await asyncio.sleep(3)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
