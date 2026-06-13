import re

def update_leaderboard():
    file_path = 'data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define participants and their specific data points if different from default (+5)
    # Default points per day hit is 5.
    overrides = {
        "Abongnwi Chrioni-Opal Forba'": {"D10": 10}
    }

    # Find every "Work post (image uploaded)" block
    pattern = r'(\{\s*"label":\s*"Work post \(image uploaded\)",\s*"pts":\s*(\d+),.*?"dayHits":\s*\[(.*?)\],.*?"desc":\s*"(.*?)"\s*\})'

    def replacer(match):
        item_block = match.group(1)
        base_pts = int(match.group(2))
        day_hits_raw = match.group(3)
        
        # Extract day hits like "D1", "D2", ...
        days = re.findall(r'D\d+', day_hits_raw)
        if not days:
            return match.group(0)
            
        # Find participant name by looking back
        pos = match.start()
        lookback = content[max(0, pos-4000):pos]
        name_match = re.findall(r'"name":\s*"(.*?)"', lookback)
        name = name_match[-1] if name_match else "Unknown"
        
        parts = []
        total = 0
        for day in days:
            pts = base_pts
            if name in overrides and day in overrides[name]:
                pts = overrides[name][day]
            parts.append(f"{day}:{pts}")
            total += pts
            
        new_desc = " · ".join(parts) + f". Total: +{total}."
        
        # Build the new block
        # Use simple string replacement to avoid regex group issues with large text
        # Find where "desc" starts
        desc_start = item_block.find('"desc"')
        new_block = item_block[:desc_start] + f'"desc": "{new_desc}"\n          }}'
        return new_block

    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    # Also update Abongnwi's allTimeTotal as it might have changed due to the +5 to +10 logic change for D10
    # Current total in file was 250 (calculated with D10:5).
    # Since D10 is now 10 (+5 increase), her total should be 255.
    
    # Find Abongnwi's block and update total and D10 pts in days object
    abong_block_pattern = r'("name":\s*"Abongnwi Chrioni-Opal Forba\'".*?"allTimeTotal":\s*)250(.*?"D10":\s*\{\s*"pts":\s*)250'
    # Actually, the days object pts is as of that day.
    # If she had 220 on D9, and earned +35 on D10 (10 Form + 10 Creativity + 10 Image + 5 late?), total is 255.
    
    # Let's do a simpler replacement for her total
    new_content = new_content.replace('"name": "Abongnwi Chrioni-Opal Forba\'",\n    "role": "Participant",\n    "joinedDay": "D1",\n    "allTimeTotal": 250', 
                                      '"name": "Abongnwi Chrioni-Opal Forba\'",\n    "role": "Participant",\n    "joinedDay": "D1",\n    "allTimeTotal": 255')
    
    # Update her D10 pts entry in the days object as well
    new_content = new_content.replace('"D10": {\n        "pts": 250', '"D10": {\n        "pts": 255')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_leaderboard()
