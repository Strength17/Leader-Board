import re
import json

PHONE_RE = re.compile(r'^\+?[\d\s\-]{7,}$')

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract names from the PEOPLE array
names = re.findall(r'name:\s*\"(.*?)\"', content)
phone_names = [name for name in names if PHONE_RE.match(name.strip())]

print(f'Phone numbers found as names in data.js: {len(phone_names)}')
for p in phone_names:
    print(f" - {p}")
