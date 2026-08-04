with open("scratch/latrobe_course_urls.txt", "r", encoding="utf-8") as f:
    urls = f.read().splitlines()
    
it_urls = [u for u in urls if "information-technology" in u.lower() or "it" in u.lower() or "tech" in u.lower()]
print("IT/Tech related URLs in sitemap:")
for u in it_urls:
    print(u)
