import asyncio
from playwright.async_api import async_playwright
import json
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def main():
    async with async_playwright() as p:
        print("Launching chromium...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        url = "https://www.latrobe.edu.au/courses/data/2026/international/bu/bachelor-of-business"
        print(f"Navigating to {url}...")
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(10000)
            
            text = await page.evaluate("() => document.body.innerText")
            
            # Parse JSON
            data = json.loads(text)
            print("Successfully parsed JSON!")
            
            # Print top level keys
            print("Top level keys:", list(data.keys()))
            
            course_data = data.get("data", {})
            print("Course data keys:", list(course_data.keys()))
            
            # Let's inspect specific fields
            print("\n--- Basic Fields ---")
            print("awardTitle:", course_data.get("awardTitle"))
            print("cricosCourseCode:", course_data.get("cricosCourseCode"))
            print("durationYears:", course_data.get("durationYears"))
            print("durationSemesters:", course_data.get("durationSemesters"))
            print("durationMonths:", course_data.get("durationMonths"))
            print("durationWeeks:", course_data.get("durationWeeks"))
            print("durationDescription:", course_data.get("durationDescription"))
            
            # Let's print some descriptions
            print("\n--- Description Fields ---")
            for k in ["overview", "aims", "courseDescription", "structure", "structureDescription"]:
                if k in course_data:
                    val = course_data[k]
                    snippet = str(val)[:150].replace("\n", " ") if val else "None"
                    print(f"{k}: {snippet}")
                    
            # Let's check entry requirements
            print("\n--- Entry Requirements ---")
            req = course_data.get("entryRequirements")
            if req:
                print("type(entryRequirements):", type(req))
                if isinstance(req, dict):
                    print("entryRequirements keys:", list(req.keys()))
                    for k, v in req.items():
                        print(f"  {k}: {str(v)[:150]}")
                elif isinstance(req, list):
                    print("entryRequirements list length:", len(req))
                    for i, r in enumerate(req[:3]):
                        print(f"  [{i}]: {str(r)[:150]}")
                else:
                    print("entryRequirements value:", str(req)[:200])
            else:
                # search keys for requirements
                req_keys = [k for k in course_data.keys() if "req" in k.lower() or "entry" in k.lower()]
                print("Other potential requirement keys:", req_keys)
                for k in req_keys:
                    print(f"  {k}: {str(course_data[k])[:150]}")
                    
            # Let's check fees
            print("\n--- Fee Fields ---")
            fee_keys = [k for k in course_data.keys() if "fee" in k.lower() or "cost" in k.lower() or "price" in k.lower()]
            print("Fee keys:", fee_keys)
            for k in fee_keys:
                print(f"  {k}: {course_data[k]}")
                
            # Let's check intakes
            print("\n--- Intake / Admission / Semester Fields ---")
            intake_keys = [k for k in course_data.keys() if "intake" in k.lower() or "start" in k.lower() or "semester" in k.lower() or "term" in k.lower() or "session" in k.lower() or "admission" in k.lower()]
            print("Intake keys:", intake_keys)
            for k in intake_keys:
                print(f"  {k}: {str(course_data[k])[:150]}")
                
            # Save the full JSON to a file for backup
            with open("scratch/bachelor_of_business.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print("\nSaved full JSON to scratch/bachelor_of_business.json")
            
        except Exception as e:
            print("Error:", e)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
