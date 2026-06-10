
import json
import re

def get_pts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    data = {}
    # Split into person blocks by looking for opening brace of object inside array
    person_blocks = re.split(r'\}\s*,\s*\{', content)
    for block in person_blocks:
        name_match = re.search(r'name:\s*\"(.*?)\"', block)
        if not name_match: continue
        name = name_match.group(1)
        
        days_pts = {}
        for d in ['D1', 'D2', 'D3', 'D4', 'D5']:
            pts_match = re.search(rf'{d}:\s*\{{.*?pts:\s*(\d+)', block)
            days_pts[d] = int(pts_match.group(1)) if pts_match else 0
        data[name] = days_pts
    return data

data_prod = get_pts('data.js')
data_new  = get_pts('data2.js')

print(f'Comparing {len(data_prod)} prod participants with {len(data_new)} new participants.')

mismatches = 0
for name, days in data_prod.items():
    if name not in data_new:
        print(f'MISSING: {name} in data2.js')
        mismatches += 1
        continue
    for d in ['D1', 'D2', 'D3', 'D4', 'D5']:
        if data_prod[name].get(d, 0) != data_new[name].get(d, 0):
            print(f'MISMATCH: {name} {d} (Prod: {data_prod[name].get(d, 0)}, New: {data_new[name].get(d, 0)})')
            mismatches += 1

if mismatches == 0:
    print('All data matches for D1-D5.')
else:
    print(f'Found {mismatches} mismatches.')
