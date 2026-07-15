from bs4 import BeautifulSoup

def main():
    with open("scratch/latrobe_course.html", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    
    body = soup.find("body")
    if not body:
        print("No body tag found!")
        return
        
    print("Children of body:")
    for idx, child in enumerate(body.find_all(recursive=False)):
        print(f"[{idx}] Name: <{child.name}>, ID: {child.get('id')}, Class: {child.get('class')}")
        # print first level children of this child
        sub_children = child.find_all(recursive=False)
        print(f"    Sub-children ({len(sub_children)}):")
        for sc in sub_children[:5]:
            print(f"      <{sc.name}> ID: {sc.get('id')} Class: {sc.get('class')}")

if __name__ == "__main__":
    main()
