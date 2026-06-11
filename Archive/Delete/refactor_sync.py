
import re
import os

with open('leaderboard_sync.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Delete get_all_names_from_legacy
# Match the function body carefully
legacy_pattern = r'def get_all_names_from_legacy\(\).*?return set\(re\.findall\(r\'name:\\s\*\\\"\(.*?\\\)\"\\\', f\.read\(\)\)\)'
content = re.sub(legacy_pattern, '', content, flags=re.DOTALL)

# Replace discover_days_and_people
new_func = '''
def discover_days_and_people(form_per_day, wa_interactions, manual_bonuses, pledges):
    """
    Registry-based: Only use names from the authoritative unique_full_names.md.
    """
    all_days  = set()
    
    # Load authoritative canonical names (registry)
    registry_names = set()
    CANONICAL_PATH = "Identity_Management/Data/unique_full_names.md"
    if os.path.exists(CANONICAL_PATH):
        with open(CANONICAL_PATH, "r", encoding="utf-8") as f:
            registry_names = {line.strip() for line in f if line.strip() and not line.startswith('#')}
    
    # Track names seen in data that are NOT in the registry
    unmapped_names = set()

    # Discover days and validate names against registry
    for name, days in form_per_day.items():
        if name in registry_names:
            all_days.update(days.keys())
        else:
            unmapped_names.add(name)
        
    for name, days in wa_interactions.items():
        if name in registry_names:
            all_days.update(days.keys())
        else:
            unmapped_names.add(name)
        
    for name, data in manual_bonuses.items():
        all_days.update(data.get("creativity", {}).keys())
        all_days.update(data.get("special", {}).keys())
        all_days.update(data.get("wa_interactions", {}).keys())

    # Log unmapped names with activity to a file
    os.makedirs("Data", exist_ok=True)
    with open("Data/inactive_and_unmapped.md", "w", encoding="utf-8") as f:
        f.write("# Inactive Participants & Unmapped Senders\\n\\n")
        for name in sorted(list(unmapped_names)):
            f.write(f"- {name}\\n")

    return sorted(list(all_days), key=day_sort_key), registry_names
'''
# Match the function body carefully
discovery_pattern = r'def discover_days_and_people.*?return sorted\(list\(all_days\), key=day_sort_key\), all_names'
content = re.sub(discovery_pattern, new_func, content, flags=re.DOTALL)

with open('leaderboard_sync.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Pipeline refactored to registry-only.")
