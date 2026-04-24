# 验证清单

本项目当前主要验证 Markdown 可维护性和引用完整性。

## 必跑检查

1. Markdown 文件必须能按 UTF-8 读取。
2. 本地 Markdown 链接和图片引用必须存在。
3. `#term-...` 术语锚点必须存在。
4. `translation.md` 和 `commentary.md` 正文中不应出现行内 `$...$` 数学写法；块级 `$$...$$` 可保留。

## 当前 PowerShell 检查脚本

以下脚本可在仓库根目录运行。

```powershell
$env:PYTHONIOENCODING='utf-8'; @'
from pathlib import Path
import re

root = Path.cwd()

for p in root.rglob('*.md'):
    p.read_text(encoding='utf-8')
print('All markdown files read as UTF-8')

missing = []
for md in root.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)|\[[^\]]+\]\(([^)]+)\)', text):
        target = m.group(1) or m.group(2)
        if target.startswith(('http://', 'https://', 'mailto:')) or target.startswith('#'):
            continue
        file_target = target.split('#', 1)[0]
        if file_target.startswith('D:') or not file_target:
            continue
        if not (md.parent / file_target).resolve().exists():
            missing.append((str(md.relative_to(root)), target))
if missing:
    print('MISSING')
    for item in missing:
        print(item)
    raise SystemExit(1)
print('All local markdown links/images exist')

missing_terms = []
for md in root.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    for m in re.finditer(r'\[[^\]]+\]\(([^)]+#term-[^)]+)\)', text):
        target = m.group(1)
        file_target, anchor = target.split('#', 1)
        target_file = (md.parent / file_target).resolve()
        target_text = target_file.read_text(encoding='utf-8')
        if f'id="{anchor}"' not in target_text and f"id='{anchor}'" not in target_text:
            missing_terms.append((str(md.relative_to(root)), target))
if missing_terms:
    print('MISSING TERMS')
    for item in missing_terms:
        print(item)
    raise SystemExit(1)
print('All glossary term anchors exist')

inline_math = []
for md in root.rglob('*.md'):
    if md.name not in {'translation.md', 'commentary.md'} and 'glossary' not in md.parts:
        continue
    for i, line in enumerate(md.read_text(encoding='utf-8').splitlines(), 1):
        stripped = line.strip()
        if '$' in line and stripped != '$$':
            inline_math.append((str(md.relative_to(root)), i, line[:160]))
if inline_math:
    print('INLINE MATH FOUND')
    for item in inline_math:
        print(item)
    raise SystemExit(1)
print('No inline math found in prose files')
'@ | python -
```
