import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating to https://www.unisa.edu.au...")
        await page.goto("https://www.unisa.edu.au", timeout=60000)
        print("Loaded page:", page.url)
        print("Title:", await page.title())

        # Let's inspect the page search input elements
        inputs = await page.query_selector_all("input")
        for i, inp in enumerate(inputs):
            name = await inp.get_attribute("name")
            placeholder = await inp.get_attribute("placeholder")
            id_attr = await inp.get_attribute("id")
            print(f"Input {i}: id={id_attr}, name={name}, placeholder={placeholder}")

        # Let's find any search inputs or forms
        try:
            # Type 'Social Work' in search box and submit
            search_input = await page.query_selector("input[type='search']") or await page.query_selector("input[placeholder*='search' i]")
            if search_input:
                await search_input.fill("Social Work")
                await page.keyboard.press("Enter")
                await page.wait_for_timeout(5000)
                print("After search, URL is:", page.url)
                print("After search, Title is:", await page.title())
            else:
                print("No search input found.")
        except Exception as e:
            print("Error during search:", e)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
