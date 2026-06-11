import re
import sys

# Set stdout to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Define the log file path
log_file = r'Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt'

# Keywords identifying potential check-ins
checkin_keywords = ['i have', 'done', 'today', 'today i learned', 'i learnt', 'today i']

# Regex to capture messages: Date, Time, Sender, Message
log_pattern = re.compile(r'(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}\s?[ap]m) - ([^:]+): (.*)')

print(f"{'Sender':<30} | {'Date':<10} | {'Message'}")
print("-" * 120)

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = log_pattern.match(line)
        if match:
            date_str, time_str, sender, message = match.groups()
            
            # Exclude admin (Strength Awa)
            if 'Strength Awa' in sender:
                continue

            # Check if any check-in keyword exists in the message
            # Use 'word boundary' or simple substring check. 
            # Substring check is broader and safer for these phrases.
            if any(keyword in message.lower() for keyword in checkin_keywords):
                print(f"{sender.strip():<30} | {date_str:<10} | {message.strip()}")
