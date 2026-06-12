import re
import os

def discover_participants_day9(chat_path, form_path, target_date):
    """
    Dynamically discovers participants who submitted check-ins on the target date
    from WhatsApp chat and Form data without using hardcoded names.
    """
    discovered_participants = set()

    # 1. Discover from WhatsApp (pattern-based discovery)
    # We look for messages on target_date, extract sender.
    if os.path.exists(chat_path):
        with open(chat_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith(target_date):
                    # Match pattern: Date, Time - Sender: Message
                    match = re.match(r'\d{2}/\d{2}/\d{4}, \d{1,2}:\d{2}\s?[ap]m - (.*?):', line)
                    if match:
                        sender = match.group(1).strip()
                        # Exclude admin (manual filter as per protocol/previous context)
                        if 'Strength Awa' not in sender:
                            discovered_participants.add(sender)

    # 2. Discover from Form Data (pattern-based discovery)
    # Looking for lines containing 'D9'
    if os.path.exists(form_path):
        with open(form_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Assuming header is the first line
            for line in lines[1:]:
                if 'D9' in line:
                    # Based on the structure seen earlier: Timestamp\tFull Name\t...
                    parts = line.split('\t')
                    if len(parts) > 1:
                        name = parts[1].strip()
                        discovered_participants.add(name)

    return discovered_participants

# Paths
chat_path = 'Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt'
form_path = 'Data/Inputs/Form Data.txt'
target_date = '11/06/2026'

# Discover
participants = discover_participants_day9(chat_path, form_path, target_date)
print(f"Discovered participants for {target_date}: {list(participants)}")
