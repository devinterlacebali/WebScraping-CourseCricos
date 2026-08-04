"""UWA Playwright - find and click the right element."""
import asyncio, re
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})

        print("Navigating...")
        await page.goto('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours',
                        timeout=60000, wait_until='domcontentloaded')
        await page.wait_for_timeout(3000)

        # Scroll down to trigger the sticky navigation
        await page.evaluate('window.scrollTo(0, window.innerHeight)')
        await page.wait_for_timeout(1000)

        # Dump the full innerText BEFORE clicking
        text_before = await page.inner_text('body')
        print("International before click:", 'International' in text_before)
        print("Fee before click:", 'Fee' in text_before)
        print("$ before click:", '$' in text_before)

        # Look for sticky nav section with tab buttons
        # The page has a sticky nav with buttons for different sections
        # Try various selectors
        fee_button = None

        # Method 1: button with text FEES
        fee_button = await page.query_selector('button:has-text("FEES")')
        if fee_button:
            print("Method 1: Found FEES button")
            await fee_button.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await fee_button.click(force=True)
            await page.wait_for_timeout(3000)
            print("Clicked via force")

        text_after = await page.inner_text('body')
        print("\nInternational after click:", 'International Student Fees' in text_after)

        if 'International Student Fees' in text_after:
            idx = text_after.index('International Student Fees')
            print(text_after[idx:idx+2000])
        else:
            # Try method 2 - look for a elements with href to #fees
            fee_link = await page.query_selector('a[href*="fee" i]')
            if fee_link:
                print("Method 2: Found fee link")
                href = await fee_link.get_attribute('href')
                print(f"  href: {href}")
                await fee_link.click()
                await page.wait_for_timeout(3000)

            text_after2 = await page.inner_text('body')
            if 'International Student Fees' in text_after2:
                idx = text_after2.index('International Student Fees')
                print(text_after2[idx:idx+2000])
            else:
                # Method 3 - find the nav list and try each item
                nav_items = await page.query_selector_all('nav a, [role="tablist"] button, .sticky-nav button')
                for item in nav_items:
                    txt = await item.inner_text()
                    print(f"  Nav: {txt.strip()}")
                    if 'fee' in txt.lower():
                        print(f"  -> Clicking {txt.strip()}")
                        await item.click(force=True)
                        await page.wait_for_timeout(2000)

                text_after3 = await page.inner_text('body')
                if 'International Student Fees' in text_after3:
                    idx = text_after3.index('International Student Fees')
                    print(text_after3[idx:idx+2000])
                else:
                    print("STILL NOT FOUND")
                    # Method 4 - XPath all text nodes around "Fees & Scholarships"
                    fee_els = await page.query_selector_all('text=FEES & SCHOLARSHIPS')
                    for el in fee_els:
                        print(f"Class: {await el.evaluate('e => e.className')}")
                        tag = await el.evaluate('e => e.tagName')
                        print(f"Tag: {tag}")
                        parent_tag = await el.evaluate('e => e.parentElement.tagName')
                        print(f"Parent: {parent_tag}")
                        can_click = await el.evaluate('e => typeof e.click === \"function\"')
                        print(f"Can click: {can_click}")

        await browser.close()

asyncio.run(main())
