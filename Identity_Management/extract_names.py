import re
import os

WA_FILE = "Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt"
OUTPUT_FILE = "Data/discovered_names.md"

def extract_sender_names():
    if not os.path.exists(WA_FILE):
        print(f"Error: {WA_FILE} not found.")
        return

    # Pattern for WhatsApp message: "DD/MM/YYYY, HH:MM - SenderName: Message"
    # We want to capture SenderName
    # WhatsApp sender names are usually followed by ": "
    
    sender_re = re.compile(r'^\d{2}/\d{2}/\d{4},\s*\d{1,2}:\d{2}\s*[apAP][mM]\s*-\s*(.*?):', re.MULTILINE)
    
    unique_senders = set()
    
    with open(WA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            match = sender_re.match(line)
            if match:
                name = match.group(1).strip()
                # Exclude obvious non-names or system messages if possible, 
                # but keep it broad per instructions (just extract everything).
                if name:
                    unique_senders.add(name)
    
    # Sort alphabetically
    sorted_senders = sorted(list(unique_senders))
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted_senders))
    
    print(f"Extracted {len(sorted_senders)} unique sender names to {OUTPUT_FILE}")

if __name__ == "__main__":
    extract_sender_names()
