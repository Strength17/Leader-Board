import json
from datetime import datetime

# 1. Load data
with open('data.js', 'r', encoding='utf-8') as f:
    # Extract PEOPLE array (manual extraction for reliability)
    # The file starts with constants, then PEOPLE = [...]
    content = f.read()
    # Find start and end of PEOPLE array
    start = content.find('export const PEOPLE = [') + len('export const PEOPLE = [') - 1
    # Simple brace matching to find the end of the array
    brace_count = 0
    end = -1
    for i in range(start, len(content)):
        if content[i] == '[': brace_count += 1
        elif content[i] == ']': brace_count -= 1
        if brace_count == 0:
            end = i + 1
            break
    people = json.loads(content[start:end])

# 2. Parse Form Data for timestamps
with open('Data/Inputs/Form Data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# Map: (Name, DayNumber) -> TimestampString
submission_map = {}
for line in lines[1:]:
    parts = line.strip().split('\t')
    if len(parts) >= 3:
        timestamp = parts[0]
        name = parts[1].strip()
        day_num = parts[2].strip().replace('Day ', 'D')
        submission_map[(name, day_num)] = timestamp

# 3. Define Correction Logic
def is_before_3pm(timestamp_str):
    try:
        dt = datetime.strptime(timestamp_str, '%m/%d/%Y %H:%M:%S')
        return dt.hour < 15
    except:
        return False

# 4. Audit and Update
for person in people:
    name = person['name']
    
    # Audit daily submissions
    for day_code, day_data in person['days'].items():
        if day_data.get('submitted'):
            timestamp = submission_map.get((name, day_code))
            
            # Check if early bonus exists in breakdown
            breakdown_items = []
            for section in person['breakdown']:
                if section['section'] == 'DAILY CHECK-INS':
                    breakdown_items = section['items']
                    break
            
            has_early_bonus = any(item.get('label') == 'Early submission bonus' for item in breakdown_items)
            
            if timestamp and is_before_3pm(timestamp) and not has_early_bonus:
                # Add Early submission bonus
                breakdown_items.append({
                    "label": "Early submission bonus",
                    "pts": 5,
                    "earned": True,
                    "dayHits": [day_code],
                    "desc": f"Submitted before 3PM on {day_code}."
                })
                # Update points
                person['allTimeTotal'] += 5
                # Update day pts
                day_data['pts'] += 5
                print(f"Corrected {name} for {day_code}: Added early bonus.")

# 5. Save corrected data (just the updated PEOPLE array for now)
with open('data_corrected.json', 'w', encoding='utf-8') as f:
    json.dump(people, f, indent=2)

print("Audit complete. Corrected data saved to data_corrected.json.")
