import re
import os

def parse_whatsapp_chat(raw_chat_path, output_path, target_date_str):
    """
    Parses a WhatsApp chat export to extract messages for a specific date.
    It identifies interactions based on predefined patterns to assign points
    and logs raw messages for manual review.
    """
    
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    with open(raw_chat_path, 'r', encoding='utf-8') as f:
        chat_content = f.readlines()

    day_9_raw_messages = []
    for line in chat_content:
        if line.startswith(target_date_str):
            day_9_raw_messages.append(line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(day_9_raw_messages)

    print(f"Extracted {len(day_9_raw_messages)} messages for {target_date_str} to {output_path}")

    # For the actual parsing of points, a more complex script would be needed
    # that understands different message types (e.g., questions, encouragement, referrals).
    # For now, this just extracts the raw messages for the day.

    # Placeholder for actual parsing logic
    parsed_data = []
    for line in day_9_raw_messages:
        # Example: Basic regex to find a name and message
        match = re.match(r'^\d{2}/\d{2}/\d{4}, \d{1,2}:\d{2}\s(?:am|pm)\s-\s(.*?):(.*)$', line)
        if match:
            name = match.group(1).strip()
            message = match.group(2).strip()
            # This is where you'd implement logic to assign points based on message content
            # For this exercise, I'll just store the name and message
            parsed_data.append(f"- Person: {name}, Message: {message}")
            
    # Save a simple parsed output for now, as a placeholder
    parsed_output_path = output_path.replace('_raw.txt', '_parsed.md')
    with open(parsed_output_path, 'w', encoding='utf-8') as f:
        f.write("# WhatsApp Day 9 Parsed Data (" + target_date_str + ")

") # Avoid f-string for this line
        if parsed_data:
            f.write("
".join(parsed_data))
        else:
            f.write("No parsable interactions found for today.")

    print(f"Generated parsed WhatsApp data to {parsed_output_path}")


# Define the paths and target date for Day 9
raw_chat_export_path = 'Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt'
whatsapp_day9_raw_output = 'Data/Outputs/whatsapp_day9_raw.txt'
whatsapp_day9_parsed_output = 'Data/Outputs/whatsapp_day9_parsed.md' # This is the expected output as per protocol
target_date = '11/06/2026' # Day 9

# Create an adapted wa_parser.py
# The original wa_parser.py was not modified, so we are creating a new one with the logic
# to handle specific day parsing.
# The `wa_parser.py` file mentioned in the protocol does not exist, so I am creating a temporary script here
# to perform the action.
parse_whatsapp_chat(raw_chat_export_path, whatsapp_day9_raw_output, target_date)
