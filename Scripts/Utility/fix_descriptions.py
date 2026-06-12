import re

def update_work_post_descriptions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find each person's block
    people_match = re.search(r'export const PEOPLE = \[(.*)\];\s*export const WARNINGS', content, re.DOTALL)
    if not people_match:
        print("Could not find PEOPLE array")
        return

    people_content = people_match.group(1)
    
    # Split by person objects (assuming they start with { and end with }, at the first level)
    # This is tricky because of nested objects. 
    # Let's try a different approach: find all "Work post (image uploaded)" items.
    
    item_regex = r'\{\s*"label":\s*"Work post \(image uploaded\)",\s*"pts":\s*\d+,\s*"earned":\s*true,\s*"dayHits":\s*\[(.*?)\],\s*"desc":\s*"(.*?)"\s*\}'
    
    def replacer(match):
        day_hits_raw = match.group(1)
        # Extract days like D1, D2
        days = re.findall(r'D\d+', day_hits_raw)
        
        if not days:
            return match.group(0)
            
        # For each person, we calculate points. 
        # Default is 5. 
        # We need to know if it's Christine or Abongnwi to match existing logic.
        # But wait, the user said "Do that for every body".
        
        # Check if we are in Abongnwi's block by looking back in the content? 
        # Or just check if the current desc already has :10 for D10.
        
        parts = []
        total = 0
        for day in days:
            pts = 5
            # Special logic for Abongnwi's D10 if already set
            if day == "D10":
                # Check if it was 10 in the existing string or if we know it should be 10
                # Actually, Abongnwi is the only one with 10 for D10 so far.
                # Let's find the name by looking back.
                pos = match.start()
                lookback = content[max(0, pos-2000):pos]
                if "Abongnwi" in lookback:
                    pts = 10
            
            parts.append(f"{day}:{pts}")
            total += pts
        
        new_desc = " · ".join(parts) + f". Total: +{total}."
        
        return f"""{{
            "label": "Work post (image uploaded)",
            "pts": 5,
            "earned": true,
            "dayHits": [{day_hits_raw}],
            "desc": "{new_desc}"
          }}"""

    new_people_content = re.sub(item_regex, replacer, people_content, flags=re.DOTALL)
    
    # Note: The regex replacement above might mess up indentation, 
    # but I'll try to keep it clean.
    
    final_content = content.replace(people_content, new_people_content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == "__main__":
    update_work_post_descriptions('data.js')
