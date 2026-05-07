"""Convert single-line $$ formulas to multi-line format matching Ch10/Ch12 standard."""
import re
import sys

filepath = sys.argv[1]

with open(filepath, encoding='utf-8') as f:
    content = f.read()

def to_multiline(m):
    formula = m.group(1).strip()
    parts = formula.rsplit(r'\tag{', 1)
    if len(parts) == 2:
        body = parts[0].strip()
        tag = r'\tag{' + parts[1]
        return '$$\n' + body + '\n' + tag + '\n$$'
    return '$$\n' + formula + '\n$$'

# Match single-line $$ blocks
content = re.sub(r'\$\$([^\n]+?)\$\$', to_multiline, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

tags = re.findall(r'\\tag\{', content)
multiline = re.findall(r'\$\$\n', content)
print(f'Tags: {len(tags)}, Multi-line blocks: {len(multiline)}')
