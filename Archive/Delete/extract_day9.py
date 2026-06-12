
with open('Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

day_9_lines = [line for line in lines if line.startswith('11/06/2026')]

with open('Data/Outputs/whatsapp_day9_raw.txt', 'w', encoding='utf-8') as f:
    f.writelines(day_9_lines)

print(f"Extracted {len(day_9_lines)} lines.")
