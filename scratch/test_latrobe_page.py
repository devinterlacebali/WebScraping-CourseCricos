import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        
        # Wait a bit for JS to render facts
        await page.wait_for_timeout(3000)
        
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        
        # Save HTML to scratch for inspection if needed
        with open("scratch/latrobe_course.html", "w", encoding="utf-8") as f:
            f.write(content)
            
        print("Page title:", soup.find("title").get_text(strip=True) if soup.find("title") else "No title")
        
        # Print some parts of the HTML to understand layout
        # Let's find CRICOS, Duration, Fees, Intakes text
        text = soup.get_text(" ", strip=True)
        print("\n--- Search for keywords ---")
        for word in ["CRICOS", "Duration", "Intake", "Fee", "IELTS", "English requirement"]:
            found = [line for line in text.split("\n") if word.lower() in line.lower()]
            print(f"Keyword '{word}' matches:")
            for f_line in found[:5]:
                print(f"  {f_line[:120]}")
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
