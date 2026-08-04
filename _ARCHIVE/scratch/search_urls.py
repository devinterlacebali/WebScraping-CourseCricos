with open("scratch/latrobe_course_urls.txt", "r", encoding="utf-8") as f:
    urls = f.read().splitlines()
    
business_urls = [u for u in urls if "bachelor-of-business" in u]
print("Bachelor of Business related URLs in sitemap:")
for u in business_urls:
    print(u)
    
accounting_urls = [u for u in urls if "accounting" in u]
print("\nAccounting related URLs in sitemap (first 10):")
for u in accounting_urls[:10]:
    print(u)
