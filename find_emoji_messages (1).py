#!/usr/bin/env python3
"""
find_emoji_messages.py

Scan an exported WhatsApp chat (.txt) for messages that contain ALL FOUR
target emojis: ✅ 👤 🛠️ 📷  (a message must have every one of them)

For each match it:
  - Pulls the WhatsApp timestamp (date + time) the message was sent.
  - Works out which programme "Day" that date falls on.
        Day 1  = June 1
        Day 5  = June 5
        Weekends (Sat/Sun) are NOT counted, so:
        Day 6  = June 8  (the next weekday after June 5)
  - Flags a discrepancy if the message was sent on a date that doesn't
    fall on a programme day (i.e. a weekend / outside the schedule).
  - Writes the timestamp, the computed Day, any discrepancy note, and
    the FULL original message (all lines) to a log file.

Usage:
    python find_emoji_messages.py <chat_export.txt> [output_log.txt] [--mdy]

By default dates are parsed as DD/MM/YYYY (common WhatsApp format outside
the US). Pass --mdy if your export uses MM/DD/YYYY instead.

If no output file is given, the log is written next to the input file as
"<input-name>_emoji_matches.log".
"""

import re
import sys
from datetime import date, timedelta
from pathlib import Path

# ── The emojis we're looking for — ALL must be present in a message ──
# Using '🛠' (U+1F6E0) and '📸' (U+1F4F8) as identified in the logs.
TARGET_EMOJIS = ["✅", "👤", "🛠", "📸"]

# Variation Selector-16 (U+FE0F) is an invisible character some phones
# attach to emojis (e.g. "🛠️" = U+1F6E0 + U+FE0F) and others omit. Strip
# it from both the target emojis and the message text so "🛠️" and "🛠"
# are treated as the same emoji.
VARIATION_SELECTOR_RE = re.compile("\ufe0f")


def normalize(text):
    return VARIATION_SELECTOR_RE.sub("", text)


TARGET_EMOJIS_NORMALIZED = [normalize(e) for e in TARGET_EMOJIS]

# Programme Day 1 = June 1 (year is taken from whatever year appears in
# the chat export's timestamps).
PROGRAM_START_MONTH = 6
PROGRAM_START_DAY = 1

WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Standard WhatsApp export line format:
#   12/03/2026, 14:05 - Sender Name: message text
MESSAGE_START_RE = re.compile(
    r"^(\d{1,2})/(\d{1,2})/(\d{2,4}),?\s+(\d{1,2}):(\d{2})(?:\s?([APap][Mm]))?\s*-\s*(.*)$"
)


def read_lines(path):
    """Read the chat export, auto-detecting common WhatsApp export
    encodings (UTF-8, UTF-8 with BOM, UTF-16)."""
    raw = path.read_bytes()

    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        encoding = "utf-16"
    elif raw.startswith(b"\xef\xbb\xbf"):
        encoding = "utf-8-sig"
    else:
        encoding = "utf-8"

    text = raw.decode(encoding, errors="replace")
    return text.splitlines(keepends=True)


def parse_messages(lines):
    """
    Group raw lines into individual messages, since WhatsApp exports
    multi-line messages as plain continuation lines (no timestamp).
    Yields (header_match, body_lines) tuples.
    """
    current_match = None
    current_body = []

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        match = MESSAGE_START_RE.match(line)

        if match:
            if current_match is not None:
                yield current_match, current_body
            current_match = match
            current_body = [line]
        else:
            if current_match is not None:
                current_body.append(line)

    if current_match is not None:
        yield current_match, current_body


def message_contains_all_emojis(body_lines):
    full_text = normalize("\n".join(body_lines))
    # Ensure every target emoji is present in the normalized full message text
    return all(emoji in full_text for emoji in TARGET_EMOJIS_NORMALIZED)


def parse_date_from_match(match, mdy=False):
    """Return a date object from the regex match, handling DD/MM vs MM/DD
    and 2- vs 4-digit years."""
    a, b, year_str = match.group(1), match.group(2), match.group(3)
    if len(year_str) == 2:
        year = 2000 + int(year_str)
    else:
        year = int(year_str)

    if mdy:
        month, day = int(a), int(b)
    else:
        day, month = int(a), int(b)

    return date(year, month, day)


def format_time(match):
    hour, minute, ampm = match.group(4), match.group(5), match.group(6)
    if ampm:
        return f"{hour}:{minute} {ampm.upper()}"
    return f"{hour}:{minute}"


def compute_day_number(d, program_start):
    """
    Programme Day numbering: Day 1 = program_start (a weekday).
    Each subsequent weekday (Mon-Fri) increments the Day count.
    Weekends don't get a Day number -> returns None.
    """
    if d.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        return None
    if d < program_start:
        return None

    day_num = 0
    cur = program_start
    while cur <= d:
        if cur.weekday() < 5:
            day_num += 1
        cur += timedelta(days=1)
    return day_num


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    mdy = "--mdy" in sys.argv

    if len(args) < 1:
        print("Usage: python find_emoji_messages.py <chat_export.txt> [output_log.txt] [--mdy]")
        sys.exit(1)

    input_path = Path(args[0])
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}")
        sys.exit(1)

    output_path = Path(args[1]) if len(args) >= 2 else input_path.with_name(
        f"{input_path.stem}_emoji_matches.log"
    )

    lines = read_lines(input_path)

    matches = []
    program_year = None
    for match, body_lines in parse_messages(lines):
        if not message_contains_all_emojis(body_lines):
            continue
        msg_date = parse_date_from_match(match, mdy=mdy)
        if program_year is None:
            program_year = msg_date.year
        matches.append((match, msg_date, body_lines))

    program_start = date(program_year or date.today().year, PROGRAM_START_MONTH, PROGRAM_START_DAY)

    # Sort chronologically so messages line up under their timestamps in order
    matches.sort(key=lambda m: (m[1], m[0].group(4), m[0].group(5)))

    with output_path.open("w", encoding="utf-8") as out:
        out.write(f"Searched: {input_path}\n")
        out.write(f"Required emojis (ALL must be present): {' '.join(TARGET_EMOJIS)}\n")
        out.write(f"Programme Day 1 = {program_start.strftime('%d/%m/%Y')}\n")
        out.write(f"Matches found: {len(matches)}\n")
        out.write("=" * 60 + "\n\n")

        for match, msg_date, body_lines in matches:
            time_str = format_time(match)
            weekday_name = WEEKDAY_NAMES[msg_date.weekday()]
            day_num = compute_day_number(msg_date, program_start)

            if day_num is not None:
                day_label = f"Day {day_num}"
                discrepancy = "None"
            elif msg_date < program_start:
                day_label = "N/A (before programme start)"
                discrepancy = f"Message dated before Day 1 ({program_start.strftime('%d/%m/%Y')})"
            else:
                day_label = "N/A (weekend)"
                discrepancy = f"Submitted on a {weekday_name} - not a programme day"

            out.write(f"[Timestamp] {msg_date.strftime('%d/%m/%Y')} ({weekday_name}), {time_str}\n")
            out.write(f"[Day]       {day_label}\n")
            out.write(f"[Discrepancy] {discrepancy}\n")
            out.write("----- Full message -----\n")
            out.write("\n".join(body_lines))
            out.write("\n-------------------------\n\n")

    print(f"Done. {len(matches)} message(s) contain all four emojis.")
    print(f"Log written to: {output_path}")


if __name__ == "__main__":
    main()
