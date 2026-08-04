"""CDU - check exact fee text in SSR."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

url = 'https://www.cdu.edu.au/study/course/bachelor-nursing-wnurs1'
r = curl.get(url, impersonate='chrome120', timeout=20, cookies={"CDU_STUDENT_TYPE": "international"})

# Check raw HTML for fee
print('=== "32,760" in raw HTML ===:', '32,760' in r.text)
print('=== "32760" in raw HTML ===:', '32760' in r.text)

# Check raw HTML for International tuition
print('\n=== International tuition in raw HTML ===')
idx = r.text.find('International tuition')
if idx >= 0:
    print(f'  Found at idx {idx}')
    print(f'  Context: {r.text[idx:idx+200]}')
else:
    print('  NOT FOUND in raw HTML')
    # Check if it exists in the whatwg HTML after rendering
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.get_text(separator=' ', strip=True)
    print('\n=== "International tuition" in body ===')
    idx2 = body.find('International tuition')
    if idx2 >= 0:
        print(f'  Found at idx {idx2}: {body[idx2:idx2+200]}')
    else:
        print('  NOT FOUND in body either')
        # Check for any fee text
        for m in re.finditer(r'[Ff]ee.{0,100}', body):
            print(f'  Fee context: {m.group()[:120]}')
            break

# Get ALL text and search for AUD
print('\n=== AUD in body ===')
soup = BeautifulSoup(r.text, 'html.parser')
body = soup.get_text(separator=' ', strip=True)
for m in re.finditer(r'AUD[^0-9]*\$?\s*[0-9,]+', body):
    print(f'  {m.group()}')
    
print('\n=== CRICOS in body ===')
for m in re.finditer(r'CRICOS.{0,100}', body):
    print(f'  {m.group()[:100]}')
