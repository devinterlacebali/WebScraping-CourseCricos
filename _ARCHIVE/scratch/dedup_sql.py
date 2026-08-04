import re
import sys
import os

def dedup_sql(input_path, output_path):
    print(f"Reading {input_path}...")
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all UPDATE courses SET ... WHERE cricos_course_code = '...';
    pattern = re.compile(
        r"(UPDATE\s+courses\s+SET.*?WHERE\s+cricos_course_code\s*=\s*'([^']+)';)", 
        re.DOTALL | re.IGNORECASE
    )

    matches = list(pattern.finditer(content))
    print(f"Found {len(matches)} total course updates.")

    # Group matches by CRICOS code
    cricos_groups = {}
    for idx, m in enumerate(matches):
        statement = m.group(1)
        cricos = m.group(2)
        # Extract URL
        url_match = re.search(r"apply_form\s*=\s*'([^']+)'", statement)
        url = url_match.group(1) if url_match else ""
        cricos_groups.setdefault(cricos, []).append({
            'index': idx,
            'start': m.start(),
            'end': m.end(),
            'statement': statement,
            'url': url,
            'url_len': len(url)
        })

    # For each group, select the one with the shortest URL
    chosen_indices = set()
    for cricos, group in cricos_groups.items():
        # Sort by URL length, then by index to ensure deterministic order
        sorted_group = sorted(group, key=lambda x: (x['url_len'], x['index']))
        chosen = sorted_group[0]
        chosen_indices.add(chosen['index'])
        if len(group) > 1:
            print(f"CRICOS {cricos}: keeping {chosen['url']} ({chosen['url_len']})")
            for discarded in sorted_group[1:]:
                print(f"  Discarding: {discarded['url']} ({discarded['url_len']})")

    # Reconstruct the file content
    # We will replace each update match: if it is chosen, we keep it, otherwise we replace with empty or skipped comment
    new_content_parts = []
    last_end = 0
    for idx, m in enumerate(matches):
        # Add the text between the last match and this match
        new_content_parts.append(content[last_end:m.start()])
        if idx in chosen_indices:
            # Keep the statement
            new_content_parts.append(m.group(1))
        else:
            # Discard (we can write a comment or just skip it)
            # Let's write a skipped comment to show what was skipped
            url_match = re.search(r"apply_form\s*=\s*'([^']+)'", m.group(1))
            url = url_match.group(1) if url_match else "unknown"
            new_content_parts.append(f"-- ⚠️ Skipped (duplicate CRICOS): {url}")
        last_end = m.end()

    # Add the remaining text at the end of the file
    new_content_parts.append(content[last_end:])

    # Join and clean up excessive newlines
    result = "".join(new_content_parts)
    
    # Save the output
    print(f"Writing to {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    print("Done!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python dedup_sql.py <input_sql> <output_sql>")
    else:
        dedup_sql(sys.argv[1], sys.argv[2])
