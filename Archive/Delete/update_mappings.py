
import os

MAPPINGS_FILE = "Identity_Management/Data/resolved_names.md"
mappings = {
    'Chrioni-opal': 'Abongnwi Chrioni-Opal Forba\'',
    'Seun Seun': 'Oluwasegun Daniel Osawore',
    'Suilabayu Olga (Suila)': 'Suilabayu Olga Simolen',
    'Meghiou Nganka Los Esther': 'Meghiou Nganka Lo',
    'Percy Visiy Percy Jr': 'Percy Visiy',
    'Christine': 'Christine Choundong',
    'Daniel': 'Oluwasegun Daniel Osawore',
    'Emmanuel': 'Emmanuel Karol Tchouani',
    'Faith': 'Faith Emmanuella Busari'
}
with open(MAPPINGS_FILE, "a", encoding="utf-8") as f:
    for raw, canonical in mappings.items():
        f.write(f'{raw}: {canonical}\n')
print("Updated resolved_names.md")
