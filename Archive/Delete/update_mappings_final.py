
import os

MAPPINGS_FILE = "Identity_Management/Data/resolved_names.md"
mappings = {
    'Frank Emmanuel': 'Frank Emmanuel',
    'Oluwasegun Daniel': 'Oluwasegun Daniel Osawore'
}
with open(MAPPINGS_FILE, "a", encoding="utf-8") as f:
    for raw, canonical in mappings.items():
        f.write(f'{raw}: {canonical}\n')
print("Updated resolved_names.md")
