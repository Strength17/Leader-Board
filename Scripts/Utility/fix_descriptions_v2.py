import re

def fix_descriptions():
    file_path = 'data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the PEOPLE array content
    people_match = re.search(r'export const PEOPLE = \[(.*)\];\s*export const WARNINGS', content, re.DOTALL)
    if not people_match:
        print("Could not find PEOPLE array")
        return
    
    people_content = people_match.group(1)
    
    # We need to process each person individually to handle specific logic (like Abongnwi's D10)
    # Since person objects are separated by }, { (with some variations in whitespace), let's split carefully.
    
    # Actually, a better way is to iterate through the matches of person blocks.
    # Person blocks start with { and have a "name": "..." field.
    
    person_regex = r'(\{\s*"name":\s*"(.*?)",.*?\}\s*\}?\s*\},?)'
    
    def person_replacer(match):
        person_full = match.group(0)
        name = match.group(2)
        
        # Find the Work Post item within this person
        work_post_regex = r'(\{\s*"label":\s*"Work post \(image uploaded\)",\s*"pts":\s*(\d+),.*?"dayHits":\s*\[(.*?)\],.*?"desc":\s*"(.*?)"\s*\})'
        
        def item_replacer(item_match):
            day_hits_raw = item_match.group(3)
            base_pts = int(item_match.group(2))
            
            days = re.findall(r'D\d+', day_hits_raw)
            if not days:
                return item_match.group(0)
            
            parts = []
            total = 0
            for day in days:
                pts = base_pts # Default is 5
                if "Abongnwi" in name and day == "D10":
                    pts = 10
                
                parts.append(f"{day}:{pts}")
                total += pts
            
            new_desc = " · ".join(parts) + f". Total: +{total}."
            
            # Reconstruct the item
            # Using capturing groups to preserve other fields like "earned": true
            item_start = item_match.group(1).split('"desc"')[0]
            item_end = '}'
            
            return f'{item_start}"desc": "{new_desc}"\n          }}'

        new_person = re.sub(work_post_regex, item_replacer, person_full, flags=re.DOTALL)
        return new_person

    # This person_regex is a bit risky for very nested structures.
    # Let's try to just find all Work post items and find the name by looking back.
    
    full_work_post_regex = r'(\{\s*"label":\s*"Work post \(image uploaded\)",\s*"pts":\s*(\d+),.*?"dayHits":\s*\[(.*?)\],.*?"desc":\s*"(.*?)"\s*\})'
    
    def global_item_replacer(match):
        item_full = match.group(1)
        base_pts = int(match.group(2))
        day_hits_raw = match.group(3)
        
        days = re.findall(r'D\d+', day_hits_raw)
        if not days:
            return match.group(0)
        
        # Look back to find the name
        start_pos = match.start()
        lookback = content[max(0, start_pos-2000):start_pos]
        # Find the last "name": "..." before this item
        name_match = re.findall(r'"name":\s*"(.*?)"', lookback)
        name = name_match[-1] if name_match else "Unknown"
        
        parts = []
        total = 0
        for day in days:
            pts = base_pts
            if "Abongnwi" in name and day == "D10":
                pts = 10
            
            parts.append(f"{day}:{pts}")
            total += pts
            
        new_desc = " · ".join(parts) + f". Total: +{total}."
        
        # Preserving the structure
        # Find where "desc" starts in item_full
        desc_start_idx = item_full.find('"desc"')
        new_item = item_full[:desc_start_idx] + f'"desc": "{new_desc}"\n          }}'
        return new_item

    new_content = re.sub(full_work_post_regex, global_item_replacer, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    fix_descriptions()
