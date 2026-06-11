import re
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    names = set(re.findall(r'name:\s*\"(.*?)\"', content))
    print(f'Total unique participants in data.js: {len(names)}')
