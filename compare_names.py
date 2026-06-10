
import re
import json

def get_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Simple extraction
    return sorted(re.findall(r'name:\s*\"(.*?)\"', content))

names_prod = get_names('data.js')
names_new = get_names('data2.js')

print(f"Names in data.js ({len(names_prod)}): {names_prod}")
print(f"Names in data2.js ({len(names_new)}): {names_new}")

missing = [n for n in names_prod if n not in names_new]
print(f"Missing from data2.js ({len(missing)}): {missing}")
