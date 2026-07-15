from bs4 import BeautifulSoup

def main():
    with open("scratch/latrobe_course.html", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    
    wrapper = soup.find("div", class_="ds-main-wrapper")
    if not wrapper:
        print("No ds-main-wrapper found!")
        return
        
    print("Content of ds-main-wrapper (first 2000 chars):")
    print(wrapper.get_text("\n", strip=True)[:2000])
    
    print("\nHTML structure inside ds-main-wrapper:")
    # print all tags and classes down to level 4
    def print_tree(el, depth=0):
        if not el.name:
            return
        print("  " * depth + f"<{el.name}> id={el.get('id')} class={el.get('class')}")
        if depth < 4:
            for child in el.find_all(recursive=False):
                print_tree(child, depth + 1)
                
    print_tree(wrapper)

if __name__ == "__main__":
    main()
