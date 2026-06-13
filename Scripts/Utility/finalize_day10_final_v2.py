import re

def finalize_leaderboard():
    file_path = 'data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Christine Choundong (Total 352)
    christine_new = r'''    "name": "Christine Choundong",
    "role": "Ambassador",
    "joinedDay": "D1",
    "allTimeTotal": 352,
    "tier": "GOLD",
    "days": {
      "D1": { "pts": 90, "submitted": true, "streakDays": 1, "workDone": true, "workStreakDays": 1 },
      "D2": { "pts": 136, "submitted": true, "streakDays": 2, "workDone": true, "workStreakDays": 2 },
      "D3": { "pts": 168, "submitted": true, "streakDays": 3, "workDone": true, "workStreakDays": 3 },
      "D4": { "pts": 178, "submitted": false, "streakDays": 3, "workDone": true, "workStreakDays": 4 },
      "D5": { "pts": 223, "submitted": false, "streakDays": 3, "workDone": true, "workStreakDays": 5 },
      "D6": { "pts": 250, "submitted": true, "streakDays": 4, "workDone": true, "workStreakDays": 6 },
      "D7": { "pts": 272, "submitted": true, "streakDays": 5, "workDone": true, "workStreakDays": 7 },
      "D8": { "pts": 287, "submitted": true, "streakDays": 6, "workDone": true, "workStreakDays": 8 },
      "D9": { "pts": 292, "submitted": true, "streakDays": 7, "workDone": true, "workStreakDays": 9 },
      "D10": { "pts": 352, "submitted": true, "streakDays": 8, "workDone": true, "workStreakDays": 10 }
    },
    "breakdown": [
      { "section": "PRE-PROGRAMME", "items": [
          { "label": "Pledge", "pts": 5, "earned": true, "dayHits": null, "desc": "You committed to the programme. +5 for your pledge." },
          { "label": "Referral × 2", "pts": 50, "earned": true, "dayHits": null, "desc": "You brought 2 new members in. +50 pts." }
      ]},
      { "section": "DAILY CHECK-INS", "items": [
          { "label": "Form submission", "pts": 10, "earned": true, "dayHits": ["D1", "D2", "D3", "D6", "D7", "D8", "D9", "D10"], "desc": "8 valid forms submitted. +80 total." }
      ]},
      { "section": "FIGMA WORK", "items": [
          { "label": "Creativity scores", "pts": null, "earned": true, "dayHits": ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D9", "D10"], "desc": "D1:10 · D2:20 · D3:5 · D4:5 · D5:10 · D6:5 · D7:5 · D9:5 · D10:10. Total: +75." }
      ]},
      { "section": "WORK POST", "items": [
          { "label": "Work post (image uploaded)", "pts": 5, "earned": true, "dayHits": ["D1", "D2", "D3", "D5", "D6", "D7", "D8", "D9", "D10"], "desc": "D1:5 · D2:5 · D3:5 · D5:5 · D6:5 · D7:5 · D8:5 · D9:5 · D10:5. Total: +45." }
      ]},
      { "section": "WHATSAPP ENGAGEMENT", "items": [
          { "label": "Asked a genuine question", "pts": 3, "earned": true, "dayHits": ["D2"], "desc": "+3 total." },
          { "label": "First to post check-in in group", "pts": 5, "earned": true, "dayHits": ["D2", "D3", "D4"], "desc": "+15 total." },
          { "label": "Helped another member", "pts": 5, "earned": true, "dayHits": ["D1", "D3"], "desc": "+10 total." },
          { "label": "Posted encouragement that got reactions", "pts": 2, "earned": true, "dayHits": ["D1", "D3", "D6", "D7"], "desc": "+8 total." },
          { "label": "Shared a useful tip or resource", "pts": 3, "earned": true, "dayHits": ["D1"], "desc": "+3 total." },
          { "label": "Welcomed a new member", "pts": 3, "earned": true, "dayHits": ["D2"], "desc": "+3 total." }
      ]},
      { "section": "BONUSES", "items": [
          { "label": "Phase Completion (W1)", "pts": 20, "earned": true, "dayHits": ["D5"], "desc": "5/5 days work completed. +20." },
          { "label": "Special Bonus (D5)", "pts": 10, "earned": true, "dayHits": ["D5"], "desc": "FB interaction bonus confirmed. +10." },
          { "label": "Perfect Week (W2)", "pts": 15, "earned": true, "dayHits": ["D10"], "desc": "5/5 valid same-day forms this week. +15." },
          { "label": "Phase Completion (W2)", "pts": 20, "earned": true, "dayHits": ["D10"], "desc": "5/5 days work completed for final phase. +20." }
      ]}
    ],'''

    # 2. Update Abongnwi (Total 275)
    # User said Chrioni's image upload is 10 for D10. 
    # Current total in previous turn proposal was 270 (with D10 work: 5). 
    # If D10 work is 10, total is 275.
    abongnwi_new = r'''    "name": "Abongnwi Chrioni-Opal Forba'",
    "role": "Participant",
    "joinedDay": "D1",
    "allTimeTotal": 275,
    "tier": "GOLD",
    "days": {
      "D1": { "pts": 45, "submitted": false, "streakDays": 0, "workDone": true, "workStreakDays": 1 },
      "D2": { "pts": 55, "submitted": false, "streakDays": 0, "workDone": true, "workStreakDays": 2 },
      "D3": { "pts": 65, "submitted": false, "streakDays": 0, "workDone": true, "workStreakDays": 3 },
      "D4": { "pts": 72, "submitted": false, "streakDays": 0, "workDone": true, "workStreakDays": 4 },
      "D5": { "pts": 145, "submitted": true, "streakDays": 1, "workDone": true, "workStreakDays": 5 },
      "D6": { "pts": 150, "submitted": false, "streakDays": 1, "workDone": true, "workStreakDays": 6 },
      "D7": { "pts": 190, "submitted": true, "streakDays": 2, "workDone": true, "workStreakDays": 7 },
      "D8": { "pts": 220, "submitted": true, "streakDays": 3, "workDone": true, "workStreakDays": 8 },
      "D9": { "pts": 220, "submitted": false, "streakDays": 3, "workDone": false, "workStreakDays": 8 },
      "D10": { "pts": 275, "submitted": true, "streakDays": 4, "workDone": true, "workStreakDays": 9 }
    },
    "breakdown": [
      { "section": "PRE-PROGRAMME", "items": [
          { "label": "Pledge", "pts": 5, "earned": true, "dayHits": null, "desc": "You committed to the programme. +5 for your pledge." },
          { "label": "Referral × 1", "pts": 25, "earned": true, "dayHits": null, "desc": "You brought 1 new member in. +25 pts." }
      ]},
      { "section": "DAILY CHECK-INS", "items": [
          { "label": "Form submission", "pts": 10, "earned": true, "dayHits": ["D5", "D7", "D8", "D10"], "desc": "4 valid forms submitted. +40 total." }
      ]},
      { "section": "FIGMA WORK", "items": [
          { "label": "Creativity scores", "pts": null, "earned": true, "dayHits": ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D10"], "desc": "D1:5 · D2:10 · D3:10 · D4:5 · D5:5 · D6:5 · D7:5 · D8:5 · D10:10. Total: +60." }
      ]},
      { "section": "WORK POST", "items": [
          { "label": "Work post (image uploaded)", "pts": 5, "earned": true, "dayHits": ["D5", "D7", "D8", "D10"], "desc": "D5:5 · D7:5 · D8:5 · D10:10. Total: +25." }
      ]},
      { "section": "WHATSAPP ENGAGEMENT", "items": [
          { "label": "Asked a genuine question", "pts": 3, "earned": true, "dayHits": ["D1"], "desc": "+3 total." },
          { "label": "Helped another member", "pts": 5, "earned": true, "dayHits": ["D1", "D5"], "desc": "+10 total." },
          { "label": "Posted encouragement that got reactions", "pts": 2, "earned": true, "dayHits": ["D1", "D4", "D5"], "desc": "+6 total." },
          { "label": "Shared a useful tip or resource", "pts": 3, "earned": true, "dayHits": ["D5"], "desc": "+3 total." },
          { "label": "Welcomed a new member", "pts": 3, "earned": true, "dayHits": ["D5"], "desc": "+3 total." }
      ]},
      { "section": "BONUSES", "items": [
          { "label": "Phase Completion (W1)", "pts": 20, "earned": true, "dayHits": ["D5"], "desc": "5/5 days work completed. +20." },
          { "label": "Phase Completion (W2)", "pts": 20, "earned": true, "dayHits": ["D10"], "desc": "5/5 days work completed for final phase. +20." }
      ]}
    ],'''

    # 3. Update Amaazee (Total 190)
    amaazee_new = r'''    "name": "Amaazee Ivanna Therese Fundoh",
    "role": "Participant",
    "joinedDay": "D6",
    "allTimeTotal": 190,
    "tier": "BRONZE",
    "days": {
      "D1": { "pts": 5, "submitted": false, "streakDays": 0, "workDone": false, "workStreakDays": 0 },
      "D2": { "pts": 5, "submitted": false, "streakDays": 0, "workDone": false, "workStreakDays": 0 },
      "D3": { "pts": 5, "submitted": false, "streakDays": 0, "workDone": false, "workStreakDays": 0 },
      "D4": { "pts": 5, "submitted": false, "streakDays": 0, "workDone": false, "workStreakDays": 0 },
      "D5": { "pts": 5, "submitted": false, "streakDays": 0, "workDone": false, "workStreakDays": 0 },
      "D6": { "pts": 45, "submitted": true, "streakDays": 1, "workDone": true, "workStreakDays": 1 },
      "D7": { "pts": 85, "submitted": true, "streakDays": 2, "workDone": true, "workStreakDays": 2 },
      "D8": { "pts": 110, "submitted": true, "streakDays": 3, "workDone": true, "workStreakDays": 3 },
      "D9": { "pts": 130, "submitted": true, "streakDays": 4, "workDone": true, "workStreakDays": 4 },
      "D10": { "pts": 190, "submitted": true, "streakDays": 5, "workDone": true, "workStreakDays": 5 }
    },
    "breakdown": [
      { "section": "PRE-PROGRAMME", "items": [
          { "label": "Pledge", "pts": 5, "earned": true, "dayHits": null, "desc": "You committed to the programme. +5 for your pledge." }
      ]},
      { "section": "DAILY CHECK-INS", "items": [
          { "label": "Form submission", "pts": 10, "earned": true, "dayHits": ["D6", "D7", "D8", "D9", "D10"], "desc": "5 valid forms submitted. +50 total." },
          { "label": "Early submission bonus", "pts": 5, "earned": true, "dayHits": ["D6", "D7"], "desc": "Submitted before 3PM on D6, D7. +10 total." }
      ]},
      { "section": "FIGMA WORK", "items": [
          { "label": "Creativity scores", "pts": null, "earned": true, "dayHits": ["D6", "D7", "D8", "D9", "D10"], "desc": "D6:10 · D7:10 · D8:5 · D9:5 · D10:10. Total: +40." }
      ]},
      { "section": "WORK POST", "items": [
          { "label": "Work post (image uploaded)", "pts": 5, "earned": true, "dayHits": ["D6", "D7", "D8", "D9", "D10"], "desc": "D6:5 · D7:5 · D8:5 · D9:5 · D10:5. Total: +25." }
      ]},
      { "section": "WHATSAPP ENGAGEMENT", "items": [
          { "label": "Helped another member", "pts": 5, "earned": true, "dayHits": ["D7"], "desc": "+5 total." },
          { "label": "Posted encouragement that got reactions", "pts": 2, "earned": true, "dayHits": ["D6", "D7"], "desc": "+4 total." },
          { "label": "Shared a useful tip or resource", "pts": 3, "earned": true, "dayHits": ["D6", "D7"], "desc": "+6 total." }
      ]},
      { "section": "BONUSES", "items": [
          { "label": "Perfect Week (W2)", "pts": 15, "earned": true, "dayHits": ["D10"], "desc": "5/5 valid same-day forms this week. +15." },
          { "label": "Phase Completion (W2)", "pts": 20, "earned": true, "dayHits": ["D10"], "desc": "5/5 days work completed for final phase. +20." }
      ]}
    ],'''

    # Apply surgical replacements for the three participants
    # Escaping the single quote for the regex match
    content = re.sub(r'\{[^{]*?"name": "Christine Choundong".*?\}\s*\],', christine_new + r'\n    ],', content, flags=re.DOTALL)
    content = re.sub(r'\{[^{]*?"name": "Abongnwi Chrioni-Opal Forba\'".*?\}\s*\],', abongnwi_new + r'\n    ],', content, flags=re.DOTALL)
    content = re.sub(r'\{[^{]*?"name": "Amaazee Ivanna Therese Fundoh".*?\}\s*\],', amaazee_new + r'\n    ],', content, flags=re.DOTALL)

    # 4. Explicit Work Post Descriptions for everyone else
    pattern = r'(\{\s*"label":\s*"Work post \(image uploaded\)",\s*"pts":\s*(\d+),.*?"dayHits":\s*\[(.*?)\],.*?"desc":\s*"(.*?)"\s*\})'

    def replacer(match):
        item_block = match.group(1)
        base_pts = int(match.group(2))
        day_hits_raw = match.group(3)
        desc = match.group(4)
        
        if " · " in desc:
            return item_block
            
        days = re.findall(r'D\d+', day_hits_raw)
        if not days:
            return item_block
            
        parts = [f"{d}:{base_pts}" for d in days]
        total = base_pts * len(days)
        new_desc = " · ".join(parts) + f". Total: +{total}."
        
        desc_start = item_block.find('"desc"')
        new_block = item_block[:desc_start] + f'"desc": "{new_desc}"\n          }}'
        return new_block

    content = re.sub(pattern, replacer, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    finalize_leaderboard()
