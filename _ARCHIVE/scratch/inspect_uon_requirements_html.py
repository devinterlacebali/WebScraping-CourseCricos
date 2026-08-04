import asyncio
import sys
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        url = "https://www.newcastle.edu.au/degrees/bachelor-of-business"
        await page.goto(url, wait_until="networkidle")
        
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        
        print("=== Searching for Headings or text with entry/admission/requirements ===")
        # Look for any elements containing "admission" or "entry" or "requirement"
        keywords = ["admission", "entry", "requirement", "criteria", "ielts", "english"]
        
        # Check all headings first
        for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "strong", "button"]):
            text = h.get_text(strip=True).lower()
            if any(k in text for k in keywords):
                print(f"[{h.name}]: '{h.get_text(strip=True)}'")
                # Print parent or next siblings up to some length
                curr = h
                parent_text = ""
                for i in range(3):
                    if curr.parent:
                        curr = curr.parent
                    else:
                        break
                print("  Parent Context:", curr.get_text(strip=True)[:300])
                print("-" * 50)
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
