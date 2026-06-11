
import os

UNRESOLVED_FILE = "Identity_Management/Data/unresolved_names.md"
MAPPINGS_FILE = "Identity_Management/Data/resolved_names.md"
PHONE_RE = __import__('re').compile(r'^\+?[\d\s\-]{7,}$')

def is_phone(raw: str) -> bool:
    return bool(PHONE_RE.match(raw.strip()))

def generate_mappings():
    if not os.path.exists(UNRESOLVED_FILE):
        return

    # Load existing resolved mappings, case-insensitive
    mappings = {}
    if os.path.exists(MAPPINGS_FILE):
        with open(MAPPINGS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    raw, canonical = line.split(":", 1)
                    mappings[raw.strip().lower()] = canonical.strip()

    # Load current unresolved (normalize to lowercase)
    with open(UNRESOLVED_FILE, "r", encoding="utf-8") as f:
        unresolved = set(line.strip().replace("NEEDS MAPPING: ", "").lower() for line in f)

    # Reconcile
    still_unresolved = []
    
    for name_lower in unresolved:
        # Check against mappings (already lowercased keys)
        if name_lower in mappings and mappings[name_lower] != "[MAP_ME]":
            pass
        elif not is_phone(name_lower):
            # Still needs mapping
            still_unresolved.append(name_lower)
            if name_lower not in mappings:
                mappings[name_lower] = "[MAP_ME]"

    # Update unresolved_names.md
    with open(UNRESOLVED_FILE, "w", encoding="utf-8") as f:
        for name in sorted(still_unresolved):
            f.write(f"NEEDS MAPPING: {name}\n")

    # Write resolved_names.md
    with open(MAPPINGS_FILE, "w", encoding="utf-8") as f:
        f.write("# Resolved Name Mappings\n\n")
        for raw, canonical in sorted(mappings.items(), key=lambda x: x[0].lower()):
            if canonical != "[MAP_ME]":
                f.write(f"{raw}: {canonical}\n")

    print(f"Reconciled: {len(still_unresolved)} still unresolved, {len([k for k,v in mappings.items() if v != '[MAP_ME]'])} resolved.")

if __name__ == "__main__":
    generate_mappings()
