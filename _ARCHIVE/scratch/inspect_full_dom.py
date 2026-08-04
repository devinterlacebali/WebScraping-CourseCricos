import asyncio
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Block fonts and media to speed up
        async def block_resources(route):
            if route.request.resource_type in ["image", "media", "font", "stylesheet"]:
                await route.abort()
            else:
                await route.continue_()
        await page.route("**/*", block_resources)
        
        url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        
        # Wait extra time for React/Vue to finish rendering
        await page.wait_for_timeout(5000)
        
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        
        print("\n=== Dumping Headers ===")
        for level in ["h1", "h2", "h3", "h4", "h5"]:
            headers = soup.find_all(level)
            print(f"Total {level}: {len(headers)}")
            for h in headers[:10]:
                print(f"  {h.name}: {h.get_text(strip=True)[:100]}")
                
        print("\n=== Dumping Tables ===")
        tables = soup.find_all("table")
        print(f"Total tables: {len(tables)}")
        for idx, t in enumerate(tables):
            print(f"  Table [{idx}]: text snippet: {t.get_text(strip=True)[:150]}")
            
        print("\n=== Dumping some divs with class names ===")
        divs = soup.find_all("div")
        classes = set()
        for d in divs:
            cls = d.get("class")
            if cls:
                classes.update(cls)
        print("Total unique div classes:", len(classes))
        print("Some classes:", sorted(list(classes))[:50])
        
        # Let's search for "CRICOS" case-insensitive
        cricos_els = soup.find_all(string=re.compile(r"cricos", re.I))
        print(f"\nCRICOS matches found: {len(cricos_els)}")
        for el in cricos_els:
            print(f"  Tag: <{el.parent.name}> Text: {el.strip()[:100]}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
