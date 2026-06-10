
import re
import json

# Get all unique names in production
with open('data.js', 'r', encoding='utf-8') as f:
    prod_names = set(re.findall(r'name:\s*\"(.*?)\"', f.read()))

# Get known canonical names from wa_parser.py by parsing the NAME_MAP
with open('wa_parser.py', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Extract NAME_MAP
name_map_match = re.search(r'NAME_MAP = \{(.*?)\}', content, re.DOTALL)
if name_map_match:
    # This is a very crude way to get values from the dict in the file
    # But it might be enough to see what's missing
    content_map = name_map_match.group(1)
    canonical_names = set(re.findall(r':\s*\"(.*?)\"', content_map))
else:
    canonical_names = set()

missing = sorted([n for n in prod_names if n not in canonical_names and n != "ADMIN"])

print(f"Total prod names: {len(prod_names)}")
print(f"Known canonical: {len(canonical_names)}")
print(f"Potentially missing from NAME_MAP: {missing}")
