import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def test_hash(hash_query):
    async with async_playwright() as p:
        print(f"\n--- Testing with hash: {hash_query} ---")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Listen to console errors and log messages
        page.on("console", lambda msg: print(f"CONSOLE: [{msg.type}] {msg.text}") if msg.type in ("error", "log") else None)
        
        url = f"https://www.latrobe.edu.au/courses/bachelor-of-business{hash_query}"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        
        # Wait 8 seconds for React to fetch and render
        await page.wait_for_timeout(8000)
        
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        
        # Check text
        text = soup.get_text(" ", strip=True)
        if "trouble loading" in text.lower():
            print("❌ Result: Still failed with 'trouble loading'.")
        else:
            print("✅ Result: SUCCESS! Course details loaded.")
            # Print a small snippet of the loaded content
            print("Snippet:", text[:500])
            
        await browser.close()

async def main():
    # Let's test a few variations of international/domestic studentType and year
    hashes = [
        "#/overview?location=BU&studentType=intl&year=2026",
        "#/overview?location=BU&studentType=intl&year=2027",
        "#/overview?location=BU&studentType=intl",
        "#/overview?location=BU&studentType=int&year=2026",
    ]
    for h in hashes:
        await test_hash(h)

if __name__ == "__main__":
    asyncio.run(main())
