
import re
with open('leaderboard_sync.py', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Remove get_all_names_from_legacy
content = re.sub(r'def get_all_names_from_legacy\(\).*?return set\(re\.findall\(r\'name:\\s\*\\\"\(.*?\\\)\"\\\', f\.read\(\)\)\)', '', content, flags=re.DOTALL)

with open('leaderboard_sync.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed legacy name discovery.")
