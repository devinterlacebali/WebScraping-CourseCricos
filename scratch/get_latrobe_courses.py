import asyncio
import re
from playwright.async_api import async_playwright

async def get_sitemap_urls(page, url):
    print(f"Fetching sitemap: {url}")
    try:
        response = await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        content = await page.content()
        text = await page.evaluate("() => document.body.innerText")
        
        urls = re.findall(r"https://www\.latrobe\.edu\.au/[^\s<>\"]+", text)
        if not urls:
            urls = re.findall(r"https://www\.latrobe\.edu\.au/[^\s<>\"]+", content)
        return urls
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        url = "https://www.latrobe.edu.au/courses-sitemap.xml"
        urls = await get_sitemap_urls(page, url)
        print(f"Found {len(urls)} URLs in {url}")
        
        # Let's clean the URLs (remove trailing XML tags etc if regex was sloppy)
        cleaned_urls = set()
        for u in urls:
            # remove trailing tag characters or whitespace
            u_clean = re.sub(r"[<\s\>\&\?\"].*$", "", u)
            u_clean = u_clean.rstrip(".")
            if "/courses/" in u_clean:
                cleaned_urls.add(u_clean)
                
        cleaned_list = sorted(list(cleaned_urls))
        print(f"Total unique course URLs: {len(cleaned_list)}")
        print("First 30 course URLs:")
        for cu in cleaned_list[:30]:
            print(cu)
            
        # Write to a txt file to inspect
        with open("scratch/latrobe_course_urls.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(cleaned_list))
        print("Saved to scratch/latrobe_course_urls.txt")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
