
MAPPINGS_FILE = "Identity_Management/Data/resolved_names.md"
with open(MAPPINGS_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open(MAPPINGS_FILE, 'w', encoding='utf-8') as f:
    for line in lines:
        if ':' in line:
            raw, canonical = line.split(':', 1)
            f.write(f'{raw.strip().lower()}: {canonical.strip()}\n')
print("Cleaned resolved_names.md")
