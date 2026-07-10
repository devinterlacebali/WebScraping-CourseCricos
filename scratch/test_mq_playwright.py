import asyncio
import json
from playwright.async_api import async_playwright

def safe_print(msg):
    print(str(msg).encode('ascii', 'ignore').decode('ascii'))

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Navigate base first
        await page.goto("https://www.mq.edu.au/study/find-a-course", wait_until="domcontentloaded")
        
        json_url = "https://www.mq.edu.au/study/page-data/find-a-course/courses/bachelor-of-chiropractic-science/page-data.json"
        try:
            json_str = await page.evaluate("""async (url) => {
                const res = await fetch(url);
                return await res.text();
            }""", json_url)
            
            data = json.loads(json_str)
            nested = json.loads(data['result']['data']['current']['fields']['json'])
            
            # Print descriptions
            descriptions = nested.get('marketing_items', {}).get('descriptions', [])
            safe_print(f"Descriptions count: {len(descriptions)}")
            for idx, d in enumerate(descriptions):
                safe_print(f"\n--- Object {idx} ({d.get('description_type', {}).get('value')}) ---")
                safe_print(f"Short: {repr(d.get('short_description'))}")
                safe_print(f"Long: {repr(d.get('long_description'))}")
                
            safe_print("\n--- overview_and_aims_of_the_course ---")
            safe_print(repr(nested.get('overview_and_aims_of_the_course')))
                
        except Exception as e:
            safe_print(f"Error: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
