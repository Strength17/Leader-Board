import json
import re

# Load corrected PEOPLE
with open('data_corrected.json', 'r', encoding='utf-8') as f:
    people = json.load(f)

# Load current data.js to maintain structure
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Define Day 9 Updates
day_9_updates = {
    "Amaazee Ivanna Therese Fundoh": {"pts": 20}, # 10 (base) + 5 (early) + 5 (creativity)
    "Abongnwi Chrioni-Opal Forba'": {"pts": 25}, # 10 (base) + 5 (creativity) + 10 (2 images)
    "Christine Choundong": {"pts": 5} # 5 (creativity)
}

# Apply Day 9 Updates
for person in people:
    name = person["name"]
    if name in day_9_updates:
        pts_today = day_9_updates[name]["pts"]
        person["allTimeTotal"] += pts_today
        person["days"]["D9"] = {
            "pts": person["allTimeTotal"],
            "submitted": True,
            "streakDays": person["days"].get("D8", {}).get("streakDays", 0) + 1,
            "workDone": True,
            "workStreakDays": person["days"].get("D8", {}).get("workStreakDays", 0) + 1
        }
    else:
        last_day = "D8"
        if last_day in person["days"]:
            person["days"]["D9"] = {
                "pts": person["allTimeTotal"],
                "submitted": False,
                "streakDays": person["days"][last_day].get("streakDays", 0),
                "workDone": False,
                "workStreakDays": person["days"][last_day].get("workStreakDays", 0)
            }

# Extract other constants
def extract_json(name, text):
    pattern = rf'export const {name} = (.*?;)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        json_str = match.group(1).replace(';', '')
        return json.loads(json_str)
    return None

rules = extract_json('RULES', content)
day_labels = extract_json('DAY_LABELS', content)
tier_emoji = extract_json('TIER_EMOJI', content)

# Load Warnings from Report
with open('Leaderboard_Detailed_Report.md', 'r', encoding='utf-8') as f:
    report = f.read()
warnings = []
warnings_pattern = r'## SECTION 2: ACTIONABLE WARNINGS & GUIDANCE[\s\S]*'
warnings_section = re.search(warnings_pattern, report).group(0)
for person in people:
    name = person["name"]
    warning_pattern = rf'-\s{re.escape(name)}:\s*(.*)'
    match = re.search(warning_pattern, warnings_section)
    if match:
        warnings.append({"person": name, "title": "Action Required", "details": match.group(1).strip()})

# Write back
new_content = f"""/**
 * SKY GRAPHICS FIGMA EDITION 1 — LEADERBOARD DATA
 * Generated: 2026-06-11
 */

export const DAY_LABELS = {json.dumps(day_labels, indent=2, ensure_ascii=False)};

export const TIER_EMOJI = {json.dumps(tier_emoji, indent=2, ensure_ascii=False)};

export const PEOPLE = {json.dumps(people, indent=2, ensure_ascii=False)};

export const WARNINGS = {json.dumps(warnings, indent=2, ensure_ascii=False)};

export const RULES = {json.dumps(rules, indent=2, ensure_ascii=False)};
"""

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
