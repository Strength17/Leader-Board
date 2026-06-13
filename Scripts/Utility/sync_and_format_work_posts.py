import re
import json

def sync_work_posts():
    file_path = 'data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define participants and their specific data points if different from default (+5)
    overrides = {
        "Abongnwi Chrioni-Opal Forba'": {"D10": 10}
    }

    # Extract the PEOPLE array string
    start_marker = 'export const PEOPLE = ['
    end_marker = '];'
    start_idx = content.find(start_marker) + len(start_marker)
    # Finding the closing bracket of the array is tricky due to nested brackets.
    # We'll find the last ]; before WARNINGS
    end_idx = content.rfind(end_marker, 0, content.find('export const WARNINGS'))
    
    people_str = content[start_idx:end_idx].strip()
    
    # We can't easily json.loads it because it's JS, not JSON (multiline strings, no quotes on keys sometimes).
    # But wait, looking at the file, it looks like valid JSON for the objects! 
    # Let's try to wrap it in [] and parse it if possible, but probably not.
    
    # Plan B: Use regex to find each person block and then iterate.
    # Each person block is an object { ... }.
    
    # Find all top-level objects in the PEOPLE array.
    # This regex is simplified and assumes each person starts with { "name":
    person_pattern = r'\{[^{]*?"name":\s*"(.*?)"'
    matches = list(re.finditer(person_pattern, people_str, re.DOTALL))
    
    # Get the start and end positions of each person block
    person_blocks = []
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i+1].start() if i+1 < len(matches) else len(people_str)
        # Refine end to the last closing brace before the next match
        block = people_str[start:end].strip()
        if block.endswith(','):
            block = block[:-1].strip()
        person_blocks.append((matches[i].group(1), block, start, end))

    new_people_blocks = []
    for name, block, s, e in person_blocks:
        new_block = block
        
        # 1. Find all days where workDone is true in the "days" object
        # Example: "D1": { ... "workDone": true ... }
        work_done_days = []
        days_match = re.search(r'"days":\s*\{(.*?)\}\s*,\s*"breakdown"', new_block, re.DOTALL)
        if days_match:
            days_content = days_match.group(1)
            # Find each day entry
            day_entry_matches = re.finditer(r'"(D\d+)":\s*\{[^}]*?"workDone":\s*true', days_content, re.DOTALL)
            for m in day_entry_matches:
                work_done_days.append(m.group(1))
        
        # 2. Find the Work post item and update dayHits and desc
        work_post_pattern = r'(\{\s*"label":\s*"Work post \(image uploaded\)",\s*"pts":\s*(\d+),.*?"dayHits":\s*\[(.*?)\],.*?"desc":\s*"(.*?)"\s*\})'
        
        def item_replacer(match):
            item_full = match.group(1)
            base_pts = int(match.group(2))
            
            if not work_done_days:
                return match.group(0)
            
            # Sort days numerically
            sorted_days = sorted(work_done_days, key=lambda x: int(x[1:]))
            
            # Update dayHits array
            new_day_hits = ", ".join([f'"{d}"' for d in sorted_days])
            
            # Generate new desc
            parts = []
            total = 0
            for day in sorted_days:
                pts = base_pts
                if name in overrides and day in overrides[name]:
                    pts = overrides[name][day]
                parts.append(f"{day}:{pts}")
                total += pts
            
            new_desc = " · ".join(parts) + f". Total: +{total}."
            
            # Update the total points field "pts": 5 is just the base, but some items might have a total?
            # Actually "pts": 5 is fine as a label.
            
            # Reconstruct item
            # Replace dayHits: [...]
            item_updated = re.sub(r'"dayHits":\s*\[.*?\]', f'"dayHits": [\n              {new_day_hits}\n            ]', item_full, flags=re.DOTALL)
            # Replace desc: "..."
            item_updated = re.sub(r'"desc":\s*".*?"', f'"desc": "{new_desc}"', item_updated, flags=re.DOTALL)
            
            return item_updated

        new_block = re.sub(work_post_pattern, item_replacer, new_block, flags=re.DOTALL)
        new_people_blocks.append(new_block)

    # Reconstruct the PEOPLE array
    new_people_str = ",\n  ".join(new_people_blocks)
    
    # Put it back into the file content
    new_content = content[:start_idx] + new_people_str + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    sync_work_posts()
