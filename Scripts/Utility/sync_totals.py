import re

def sync_totals():
    file_path = 'data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract PEOPLE array
    start_marker = 'export const PEOPLE = ['
    end_marker = '];'
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.rfind(end_marker, 0, content.find('export const WARNINGS'))
    people_str = content[start_idx:end_idx].strip()

    # Regex to find each person block
    # Person blocks start with { and have a "name"
    person_pattern = r'(\{[^{]*?"name":\s*"(.*?)"(.*?)\}\s*\]\s*\},?)'
    
    # We'll iterate through matches
    # Since person blocks have nested objects, we'll use a better approach:
    # Find { "name": "..." and then find the closing brace that matches the first one.
    
    new_people_blocks = []
    current_pos = 0
    while True:
        match = re.search(r'\{[^{]*?"name":\s*"(.*?)"', people_str[current_pos:])
        if not match:
            break
        
        name = match.group(1)
        start_idx_in_people = current_pos + match.start()
        
        # Find matching closing brace
        brace_count = 0
        end_idx_in_people = -1
        for i in range(start_idx_in_people, len(people_str)):
            if people_str[i] == '{':
                brace_count += 1
            elif people_str[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx_in_people = i + 1
                    break
        
        if end_idx_in_people == -1:
            break
            
        block = people_str[start_idx_in_people:end_idx_in_people]
        current_pos = end_idx_in_people
        
        # Calculate total from breakdown
        total = 0
        # Find all "pts": numbers in the breakdown sections
        # But skip the "pts" in the daily entries of "days" object.
        # Breakdown items look like: { "label": "...", "pts": 10, ... } or { "label": "...", "pts": null, ... "desc": "... Total: +75." }
        
        # Extract breakdown content
        breakdown_match = re.search(r'"breakdown":\s*\[(.*?)\]\s*,\s*"warnings"', block + ',"warnings"', re.DOTALL)
        if breakdown_match:
            breakdown_str = breakdown_match.group(1)
            # Find all items
            items = re.finditer(r'\{\s*"label":\s*"(.*?)",\s*"pts":\s*(null|\d+),.*?"desc":\s*"(.*?)"', breakdown_str, re.DOTALL)
            for item in items:
                label = item.group(1)
                pts_val = item.group(2)
                desc = item.group(3)
                
                if pts_val != "null":
                    # If it's a fixed points item (Pledge, Referral, etc.)
                    # Check for "Total: +X" in desc if it's a recurring item
                    total_match = re.search(r'Total:\s*\+(\d+)', desc)
                    if total_match:
                        total += int(total_match.group(1))
                    else:
                        total += int(pts_val)
                else:
                    # If it's a null points item (Creativity), look for "Total: +X" in desc
                    total_match = re.search(r'Total:\s*\+(\d+)', desc)
                    if total_match:
                        total += int(total_match.group(1))
        
        print(f"Calculated total for {name}: {total}")
        
        # Update block with new total
        new_block = re.sub(r'"allTimeTotal":\s*\d+', f'"allTimeTotal": {total}', block)
        # Also update D10 pts if it exists
        new_block = re.sub(r'"D10":\s*\{\s*"pts":\s*\d+', f'"D10": {{\n        "pts": {total}', new_block)
        
        new_people_blocks.append(new_block)

    # Reconstruct
    new_people_str = ",\n  ".join(new_people_blocks)
    new_content = content[:start_idx] + new_people_str + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    sync_totals()
