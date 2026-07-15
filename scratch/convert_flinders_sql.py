import re
from bs4 import BeautifulSoup

def convert_to_table(html_str):
    if not html_str or '<table>' in html_str:
        return html_str
    soup = BeautifulSoup(html_str, 'html.parser')
    parts = []
    current_head = None
    for child in soup.descendants:
        if child.name == 'h5':
            current_head = child.get_text(strip=True)
        elif child.name == 'p' and current_head:
            parts.append((current_head, child.get_text(strip=True)))
            current_head = None
            
    if not parts:
        p_tags = soup.find_all('p')
        if p_tags:
            parts.append(('English Proficiency', ' '.join(p.get_text(strip=True) for p in p_tags)))
            
    if not parts:
        return html_str
        
    out = '<table><tbody>'
    for head, body in parts:
        if body:
            if 'english' in head.lower():
                cat = 'English Proficiency'
            elif 'prerequisite' in head.lower():
                cat = 'Academic Requirements'
            else:
                cat = head
            out += f'<tr><td><strong>{cat}</strong></td><td><ul><li>{body}</li></ul></td></tr>'
    out += '</tbody></table>'
    return out

def main():
    path = 'Flinders University/flinders_courses_update.sql'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(match):
        raw_val = match.group(1)
        unescaped = raw_val.replace("''", "'")
        converted = convert_to_table(unescaped)
        escaped = converted.replace("'", "''")
        return f"entry_requirements = '{escaped}'"

    new_content = re.sub(r"entry_requirements\s*=\s*'((?:''|[^'])*)'", repl, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done converting SQL file successfully.")

if __name__ == '__main__':
    main()
