import re
import os

GLOBAL_NAMES = "Data/Global_names.md"
RESOLVED_NAMES = "Data/resolved_names.md"
UNIQUE_FULL_NAMES = "Data/unique_full_names.md"
DATA_JS = "data.js"
AUDIT_REPORT = "Data/name_integrity_audit.md"

def load_canonical_names():
    names = set()
    if os.path.exists(GLOBAL_NAMES):
        with open(GLOBAL_NAMES, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    names.add(line.strip())
    if os.path.exists(RESOLVED_NAMES):
        with open(RESOLVED_NAMES, "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    _, canonical = line.split(":", 1)
                    names.add(canonical.strip())
    return sorted(list(names))

def get_data_js_names():
    if not os.path.exists(DATA_JS):
        return set()
    with open(DATA_JS, "r", encoding="utf-8") as f:
        return set(re.findall(r'name:\s*\"(.*?)\"', f.read()))

def run_audit():
    canonical_list = load_canonical_names()
    
    # Write unique_full_names.md
    with open(UNIQUE_FULL_NAMES, "w", encoding="utf-8") as f:
        f.write("\n".join(canonical_list))
    
    # Audit against data.js
    data_js_names = get_data_js_names()
    
    with open(AUDIT_REPORT, "w", encoding="utf-8") as f:
        f.write("# Name Integrity Audit\n\n")
        
        # Flag missing in ground truth
        missing_in_ground_truth = [n for n in data_js_names if n not in canonical_list and n != "ADMIN"]
        if missing_in_ground_truth:
            f.write("## Missing in Ground Truth (Data/Global_names.md or Data/resolved_names.md)\n")
            for name in missing_in_ground_truth:
                f.write(f"- {name}: Missing from our canonical lists. Likely reason: Needs to be added to Global_names.md or resolved in Data/resolved_names.md.\n")
        
        # Flag useless/repetitive (not directly visible in a name list, but we can list canonical names)
        f.write("\n## Authoritative Canonical List\n")
        for name in canonical_list:
            f.write(f"- {name}\n")
            
    print(f"Audit complete. Unique names saved to {UNIQUE_FULL_NAMES}, audit report to {AUDIT_REPORT}")

if __name__ == "__main__":
    run_audit()
