import re
import json
import sys

# Paths
CANONICAL_NAMES_FILE = "Identity_Management/Data/unique_full_names.md"
DATA_JS = "data.js"

def run_verification():
    # Load canonical names
    with open(CANONICAL_NAMES_FILE, "r", encoding="utf-8") as f:
        canonical_names = {line.strip() for line in f if line.strip() and not line.startswith('#')}

    # Load data.js names
    with open(DATA_JS, "r", encoding="utf-8") as f:
        content = f.read()
        # Find names in the PEOPLE array
        data_names = set(re.findall(r'name:\s*\"(.*?)\"', content))

    # Verification
    invalid_names = [name for name in data_names if name not in canonical_names and name != "ADMIN"]
    
    if invalid_names:
        print(f"VERIFICATION FAILED: {len(invalid_names)} names in data.js are NOT in unique_full_names.md:")
        for name in invalid_names:
            print(f" - {name}")
        sys.exit(1)
    else:
        print("VERIFICATION PASSED: All names in data.js are canonical.")

if __name__ == "__main__":
    run_verification()
