"""Debug UC description extraction."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 ...'}
url = 'https://www.canberra.edu.au/course/364JA/2/2027'
r = requests.get(url, headers=H, timeout=20)
soup = BeautifulSoup(r.text, 'html.parser')

# 1. Find "About this course"
about = soup.find(['h3', 'h4'], string=re.compile(r'About this course', re.I))
print(f'About heading: {about}')
if about:
    print(f'  tag: {about.name}, text: {about.get_text(strip=True)}')
    print(f'  parent: {about.parent.name}, class: {about.parent.get("class", "")}')

    # Find accordion body
    parent = about.find_parent(['div', 'section'])
    print(f'  parent tag: {parent.name if parent else "none"}')
    if parent:
        content = parent.find('div', class_=re.compile(r'course-details|tab-content'))
        print(f'  content div: {content}')
        if content:
            print(f'  content text: {content.get_text(strip=True)[:200]}')
        else:
            # What's inside parent?
            for c in parent.children:
                print(f'  child: {c.name if hasattr(c,"name") else repr(c)[:100]}')

    # Try siblings approach
    parts = []
    for sib in about.find_all_next():
        if sib.name in ['h3', 'h4'] and 'About' not in sib.get_text(strip=True):
            break
        if sib.name == 'p' and sib.get_text(strip=True):
            parts.append(str(sib))
    print(f'  p-sibling approach: {len(parts)} paragraphs')
    if parts:
        print(f'  first: {parts[0][:200]}')

# 2. Check all h3/h4 content
print('\n=== ALL CONTENT HEADINGS ===')
for h in soup.find_all(['h3', 'h4']):
    txt = h.get_text(strip=True)
    # Find content after heading until next heading
    content = []
    for sib in h.find_next_siblings():
        if sib.name in ['h2', 'h3', 'h4']:
            break
        if sib.name == 'p' and sib.get_text(strip=True):
            content.append(sib.get_text(strip=True)[:100])
    if content:
        print(f'  {h.name} "{txt}": {content[:3]}')
