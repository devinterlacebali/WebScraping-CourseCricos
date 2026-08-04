"""Debug UC accordion structure."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 ...'}
url = 'https://www.canberra.edu.au/course/364JA/2/2027'
r = requests.get(url, headers=H, timeout=20)
soup = BeautifulSoup(r.text, 'html.parser')

# Find accordion with "About this course"
accs = soup.find_all('div', class_=re.compile(r'bs-accordion|accordion', re.I))
print(f'Total accordions: {len(accs)}')
for acc in accs:
    # Find any heading/button/label
    label = acc.find(['h3', 'h4', 'button', 'a', 'span'], string=re.compile(r'About this course', re.I))
    if label:
        print(f'Found label: {label.name}, text: {label.get_text(strip=True)}')
        print(f'  label tag: {label.name}')
        print(f'  label class: {label.get("class", "")}')
        # Find content after label
        course_details = acc.find('div', class_=re.compile(r'course-details|tab-content'))
        if course_details:
            txt = course_details.get_text(strip=True)
            print(f'  content: {txt[:300]}')
        else:
            print(f'  NO course-details in accordion')
            print(f'  accordion HTML: {str(acc)[:500]}')
        break
else:
    # Maybe it's not wrapped in an accordion parent
    print('No accordion with About this course found')
    # Look for any element containing that text
    for el in soup.find_all(string=re.compile(r'About this course', re.I)):
        print(f'  Found text in: {el.parent.name if el.parent else "none"}')
        if el.parent:
            print(f'  classes: {el.parent.get("class", "")}')
            print(f'  parent HTML: {str(el.parent)[:300]}')
