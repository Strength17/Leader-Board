#!/usr/bin/env python3
"""
SKY GRAPHICS FIGMA EDITION 1 -- Form Data Parser
=================================================

Input:  Data/Form Data.txt  (tab-separated export)
Output: Data/form_report.md

This script implements FILE 2 of SKY_GRAPHICS_PIPELINE_BLUEPRINT.md.

IMPORTANT - ADMIN DECISIONS APPLIED IN THIS SCRIPT
---------------------------------------------------
1. STREAK RULE OVERRIDE: The blueprint's "v4 RESET" rule does NOT apply.
   Per admin decision, missed-day streaks FREEZE (retain previous value)
   instead of resetting to zero. This script does not itself compute
   streaks (that happens in leaderboard_sync.py) -- this comment exists
   purely so the rule is documented consistently across all three
   pipeline scripts.

2. OUTPUT IS A DRAFT FOR ADMIN REVIEW. Disqualifications, "new joiner
   recovery" cases, and duplicate submissions are all FLAGGED in the
   report for the admin to confirm or override -- this script does not
   silently make final calls on edge cases. The blueprint's exception for
   new-joiner recovery forms (submitted on D6+ for an earlier day) is
   honoured: these are flagged separately, NOT auto-disqualified.

3. The pipeline must NEVER rely on what a student wrote about which day
   they're submitting for, except to detect a MISMATCH against the
   timestamp. The timestamp's date is the sole authority for which day a
   submission belongs to.

This script makes NO changes to any other file. It only reads the form
export and writes Data/form_report.md.
"""

import csv
import os
import re
from collections import OrderedDict, defaultdict
from datetime import date, datetime

# ---------------------------------------------------------------------------
# CONFIG / CONSTANTS
# ---------------------------------------------------------------------------

INPUT_FILE = os.path.join("Data", "Form Data.txt")
OUTPUT_FILE = os.path.join("Data", "form_report.md")

# DATE -> DAY mapping (absolute rule, from blueprint). Keys are date objects
# so they can be compared directly against parsed form timestamps.
PROGRAMME_DATES = OrderedDict([
    ("D1", date(2026, 6, 1)),
    ("D2", date(2026, 6, 2)),
    ("D3", date(2026, 6, 3)),
    ("D4", date(2026, 6, 4)),
    ("D5", date(2026, 6, 5)),
    ("D6", date(2026, 6, 8)),
    ("D7", date(2026, 6, 9)),
    ("D8", date(2026, 6, 10)),
    ("D9", date(2026, 6, 11)),
    ("D10", date(2026, 6, 12)),
])
DATE_TO_DAY = {v: k for k, v in PROGRAMME_DATES.items()}

DAY_LABELS = {
    "D1": "Day 1 — June 1, 2026",
    "D2": "Day 2 — June 2, 2026",
    "D3": "Day 3 — June 3, 2026",
    "D4": "Day 4 — June 4, 2026",
    "D5": "Day 5 — June 5, 2026",
    "D6": "Day 6 — June 8, 2026",
    "D7": "Day 7 — June 9, 2026",
    "D8": "Day 8 — June 10, 2026",
    "D9": "Day 9 — June 11, 2026",
    "D10": "Day 10 — June 12, 2026",
}

DAY_ORDER = list(PROGRAMME_DATES.keys())

# Same canonical name mappings used by wa_parser.py
NAME_MAP = {
    "Seun ꧁♛Seun♛꧂": "Oluwasegun Daniel Osawore",
    "Seun": "Oluwasegun Daniel Osawore",
    "+234 806 092 8637": "Faith Emmanuella Busari",
    "Ireneyemi Adedayo 💕Juliet 💕": "Irinyemi Adedayo Juliet",
    "Irinyem Adedayo Juliet": "Irinyemi Adedayo Juliet",
    "Emmanuel Tchouani T²EK": "Emmanuel Karol Tchouani",
    "Chrioni-opal ❤️": "Abongnwi Chrioni-Opal Forba'",
    "Chrioni Opal": "Abongnwi Chrioni-Opal Forba'",
    "Patience Dzekem": "Mbiydzenyuy Patience Dzekem",
    "MBIYDZENYUY PATIENCE DZEKEM": "Mbiydzenyuy Patience Dzekem",
    "Malialia Celine Bride": "Malialia Celine Bride",
    "Christine Choundong": "Christine Choundong",
    "Choundong Christine": "Christine Choundong",
    "Frank Emmanuel ☘❝𝐌𝐫. 𝐅𝐨𝐫€𝐱❞☘": "Frank Emmanuel",
    "Percy Visiy Percy Jr 😎": "Percy Visiy",
    "Mbishitehnyi Ryan": "Mbishitehnyi Ryan",
    "Mopen Bryan": "Open Bryan",
    "Moh Blessing Kebul Boss Ladi(MBK)": "Moh Blessing Kebul",
    "Suilabayu Olga (Suila🫶)": "Suilabayu Olga Simolen",
    "Miss Loise ❤️": "Nkongmi Loise Asonyuy",
    "Mme Assaah N. Nzota": "Assaah Nzota",
    "+237 6 50 00 63 56": "Amaazee Ivanna Therese Fundoh",
    "+237 6 58 75 91 64": "Dorothy Joyce Priscille",
    "+237 6 96 59 27 92": "Nzameyo Mba",
    "Ekanje Hadassah": "Ekanje Hadassah",
    "Strength Awa": "ADMIN",
    "You": "ADMIN",
}

AMBASSADORS = {
    "Christine Choundong",
    "Oluwasegun Daniel Osawore",
    "Mbiydzenyuy Patience Dzekem",
    "Frank Emmanuel",
    "Malialia Celine Bride",
    "Irinyemi Adedayo Juliet",
}

# Expected column order (0-indexed) per blueprint:
COL_TIMESTAMP = 0
COL_NAME = 1
COL_DAY_NUMBER = 2
COL_WATCHED_VIDEO = 3
COL_BUILD = 4
COL_FEEDBACK = 5
COL_POINTS_TODAY = 6
COL_TOTAL_POINTS = 7
COL_STREAK = 8
COL_BONUS_MANUAL = 9
COL_RANK = 10
COL_EXTRA = 11

DAY_NUMBER_RE = re.compile(r'(\d{1,2})')
URL_RE = re.compile(r'https?://\S+')

EARLY_BONUS_HOUR_CUTOFF = 15  # 3 PM, 24h clock


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def safe_get(row, idx):
    return row[idx].strip() if idx < len(row) else ""


def normalize_name(raw_name):
    raw_name = raw_name.strip()
    return NAME_MAP.get(raw_name, raw_name)


def role_for(name):
    return "Ambassador" if name in AMBASSADORS else "Participant"


def parse_timestamp(ts_str):
    """Parse 'M/D/YYYY H:MM:SS' -> datetime, or None if unparseable."""
    ts_str = ts_str.strip()
    if not ts_str:
        return None
    for fmt in ("%m/%d/%Y %H:%M:%S", "%m/%d/%Y %H:%M"):
        try:
            return datetime.strptime(ts_str, fmt)
        except ValueError:
            continue
    return None


def parse_day_number(raw):
    """Extract a day number from a free-text field like 'Day 3' or '3'."""
    m = DAY_NUMBER_RE.search(raw)
    if m:
        return "D" + m.group(1)
    return None


def count_image_links(build_text):
    """Count comma-separated / embedded links in the 'what did you build' field."""
    if not build_text:
        return 0
    return len(URL_RE.findall(build_text))


# ---------------------------------------------------------------------------
# PARSING
# ---------------------------------------------------------------------------

def parse_form(filepath):
    """
    Returns:
      timed_rows: list of dicts for rows WITH a parseable timestamp
      manual_rows: list of dicts for rows with NO timestamp but with a name
                    and at least one points-related field filled in
    """
    timed_rows = []
    manual_rows = []

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        header_skipped = False
        for row in reader:
            if not row or all(not c.strip() for c in row):
                continue

            ts_raw = safe_get(row, COL_TIMESTAMP)
            name_raw = safe_get(row, COL_NAME)

            # Skip header row
            if not header_skipped and ts_raw.lower() == "timestamp":
                header_skipped = True
                continue

            if not name_raw:
                continue

            ts = parse_timestamp(ts_raw)

            if ts is None:
                # No usable timestamp -- could be a manually-added bottom row.
                points_today = safe_get(row, COL_POINTS_TODAY)
                total_points = safe_get(row, COL_TOTAL_POINTS)
                bonus_manual = safe_get(row, COL_BONUS_MANUAL)
                if points_today or total_points or bonus_manual:
                    manual_rows.append({
                        "name": normalize_name(name_raw),
                        "name_raw": name_raw,
                        "points_today": points_today,
                        "total_points": total_points,
                        "bonus_manual": bonus_manual,
                        "raw_row": row,
                    })
                continue

            timed_rows.append({
                "timestamp": ts,
                "name_raw": name_raw,
                "name": normalize_name(name_raw),
                "day_written_raw": safe_get(row, COL_DAY_NUMBER),
                "day_written": parse_day_number(safe_get(row, COL_DAY_NUMBER)),
                "watched_video": safe_get(row, COL_WATCHED_VIDEO),
                "build_text": safe_get(row, COL_BUILD),
                "feedback": safe_get(row, COL_FEEDBACK),
                "bonus_manual": safe_get(row, COL_BONUS_MANUAL),
            })

    # Sort chronologically -- required so "first submission for this person"
    # and "duplicate same-day submission" can be determined correctly.
    timed_rows.sort(key=lambda r: r["timestamp"])
    return timed_rows, manual_rows


# ---------------------------------------------------------------------------
# ANALYSIS
# ---------------------------------------------------------------------------

def analyze_rows(timed_rows):
    """
    Walk submissions in chronological order and classify each one.

    Returns:
      day_data: {day: {person: record}}
      disqualified: list of dicts (late/wrong-day submissions)
      recovery_flags: list of dicts (new-joiner recovery candidates)
      duplicates: list of dicts (2nd+ submission for same person/day)
      outside_programme: list of dicts (timestamp date not in PROGRAMME_DATES)
    """
    day_data = defaultdict(dict)
    disqualified = []
    recovery_flags = []
    duplicates = []
    outside_programme = []

    seen_people = set()          # people who have submitted at least once
    seen_person_days = set()     # (person, day) pairs already recorded

    for row in timed_rows:
        person = row["name"]
        ts = row["timestamp"]
        ts_date = ts.date()
        timestamp_day = DATE_TO_DAY.get(ts_date)
        written_day = row["day_written"]

        if timestamp_day is None:
            outside_programme.append({
                "name": person,
                "timestamp": ts,
                "written_day": written_day,
            })
            continue

        is_first_submission = person not in seen_people
        seen_people.add(person)

        mismatch = (written_day is not None and written_day != timestamp_day)

        submitted = True
        warnings = []

        if mismatch and is_first_submission and timestamp_day != written_day:
            # Possible new-joiner recovery form (blueprint exception):
            # do NOT auto-disqualify, flag for admin decision instead.
            recovery_flags.append({
                "name": person,
                "timestamp": ts,
                "timestamp_day": timestamp_day,
                "written_day": written_day,
            })
            # Default (per blueprint): count as the timestamp day, no
            # retroactive points for the earlier day they claimed.
            submitted = True
            warnings.append(
                f"New joiner recovery form ({written_day} written on "
                f"{timestamp_day}) -- counted as {timestamp_day} pending "
                f"admin decision."
            )
        elif mismatch:
            # Late / wrong-day submission -> disqualified
            submitted = False
            disqualified.append({
                "name": person,
                "timestamp": ts,
                "timestamp_day": timestamp_day,
                "written_day": written_day,
            })
            warnings.append(
                f"Check-in points stripped for {timestamp_day} due to "
                f"late submission (wrote {written_day})."
            )

        # Duplicate same-day submission check
        key = (person, timestamp_day)
        if key in seen_person_days:
            duplicates.append({
                "name": person,
                "timestamp": ts,
                "day": timestamp_day,
            })
            # Per blueprint: keep the first, flag the second. Skip scoring
            # this row entirely.
            continue
        seen_person_days.add(key)

        # Check-in points
        if submitted:
            check_in_pts = 10
            early_bonus = 5 if ts.hour < EARLY_BONUS_HOUR_CUTOFF else 0
        else:
            check_in_pts = 0
            early_bonus = 0

        image_count = count_image_links(row["build_text"])

        day_data[timestamp_day][person] = {
            "timestamp": ts,
            "submitted": submitted,
            "check_in_pts": check_in_pts,
            "early_bonus": early_bonus,
            "image_count": image_count,
            "watched_video": row["watched_video"],
            "build_text": row["build_text"],
            "bonus_manual": row["bonus_manual"],
            "warnings": warnings,
        }

    return day_data, disqualified, recovery_flags, duplicates, outside_programme


def get_all_people(day_data, manual_rows):
    people = set()
    for day, persons in day_data.items():
        people.update(persons.keys())
    for m in manual_rows:
        people.add(m["name"])
    return sorted(people)


# ---------------------------------------------------------------------------
# REPORT GENERATION
# ---------------------------------------------------------------------------

def fmt_ts(ts):
    if not ts:
        return ""
    # Use numeric month/day values to avoid platform-dependent strftime
    # format specifiers (e.g. "%-m") which are invalid on Windows.
    month = ts.month
    day = ts.day
    return f"{month}/{day}/{ts.year} {ts.strftime('%H:%M')}"


def build_report(day_data, disqualified, recovery_flags, duplicates,
                  outside_programme, manual_rows):
    people = get_all_people(day_data, manual_rows)
    lines = []

    lines.append("# SKY GRAPHICS — FORM DATA REPORT")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("> ⚠️ DRAFT FOR ADMIN REVIEW. Disqualifications, recovery-form")
    lines.append("> flags, and duplicate submissions below are FLAGGED, not")
    lines.append("> final. Confirm or override each one before this feeds")
    lines.append("> leaderboard_sync.py.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------
    # SUMMARY TABLE
    # -----------------------------------------------------------------
    lines.append("## SUMMARY TABLE")
    lines.append("")
    header = "| Name | Role | " + " | ".join(DAY_ORDER) + " | Check-in Pts | Early Pts | Images |"
    sep = "|------|------|" + "|".join(["----"] * len(DAY_ORDER)) + "|------|------|------|"
    lines.append(header)
    lines.append(sep)

    for person in people:
        row_cells = [person, role_for(person)]
        total_checkin = 0
        total_early = 0
        total_images = 0
        for day in DAY_ORDER:
            rec = day_data.get(day, {}).get(person)
            if rec is None:
                row_cells.append("—")
            elif rec["submitted"]:
                row_cells.append("✅")
                total_checkin += rec["check_in_pts"]
                total_early += rec["early_bonus"]
                total_images += rec["image_count"]
            else:
                row_cells.append("❌")
        row_cells.append(f"+{total_checkin}")
        row_cells.append(f"+{total_early}")
        row_cells.append(str(total_images))
        lines.append("| " + " | ".join(row_cells) + " |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------
    # DISQUALIFIED SUBMISSIONS
    # -----------------------------------------------------------------
    lines.append("## ⚠️ DISQUALIFIED SUBMISSIONS")
    lines.append("")
    if disqualified:
        lines.append("| Name | Timestamp | Timestamp Day | Student Said | Reason |")
        lines.append("|------|-----------|----------------|---------------|--------|")
        for d in disqualified:
            lines.append(
                f"| {d['name']} | {fmt_ts(d['timestamp'])} | {d['timestamp_day']} "
                f"| {d['written_day'] or '(blank)'} | Form submitted for "
                f"{d['written_day'] or 'an unspecified day'} but timestamp "
                f"maps to {d['timestamp_day']}. Points: +0 |"
            )
    else:
        lines.append("_None detected._")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------
    # NEW JOINER RECOVERY FLAGS
    # -----------------------------------------------------------------
    lines.append("## 🆕 NEW JOINER RECOVERY FORMS (Admin decision required)")
    lines.append("")
    lines.append("> Per blueprint exception: NOT auto-disqualified. Default applied")
    lines.append("> below = counted as the timestamp day, no retroactive points for")
    lines.append("> the earlier day claimed. Confirm or override.")
    lines.append("")
    if recovery_flags:
        lines.append("| Name | Timestamp | Timestamp Day | Student Said | Default Applied |")
        lines.append("|------|-----------|----------------|---------------|------------------|")
        for r in recovery_flags:
            lines.append(
                f"| {r['name']} | {fmt_ts(r['timestamp'])} | {r['timestamp_day']} "
                f"| {r['written_day'] or '(blank)'} | Counted as "
                f"{r['timestamp_day']} submission, joinedDay={r['timestamp_day']} |"
            )
    else:
        lines.append("_None detected._")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------
    # DUPLICATE SUBMISSIONS
    # -----------------------------------------------------------------
    lines.append("## 🔁 DUPLICATE SAME-DAY SUBMISSIONS")
    lines.append("")
    if duplicates:
        lines.append("| Name | Day | Duplicate Timestamp | Action |")
        lines.append("|------|-----|----------------------|--------|")
        for dup in duplicates:
            lines.append(
                f"| {dup['name']} | {dup['day']} | {fmt_ts(dup['timestamp'])} "
                f"| First submission kept, this one ignored |"
            )
    else:
        lines.append("_None detected._")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------
    # OUTSIDE PROGRAMME DATES
    # -----------------------------------------------------------------
    lines.append("## 📅 SUBMISSIONS OUTSIDE PROGRAMME DATES")
    lines.append("")
    if outside_programme:
        lines.append("| Name | Timestamp | Student Said |")
        lines.append("|------|-----------|---------------|")
        for o in outside_programme:
            lines.append(
                f"| {o['name']} | {fmt_ts(o['timestamp'])} | {o['written_day'] or '(blank)'} |"
            )
    else:
        lines.append("_None detected._")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------
    # MANUAL ROWS (no timestamp, pre-existing manual data)
    # -----------------------------------------------------------------
    lines.append("## ✍️ PRE-EXISTING MANUAL ROWS (no timestamp)")
    lines.append("")
    lines.append("> Rows with no timestamp but a name and points already filled in")
    lines.append("> by hand. Carry these into leaderboard_sync.py as existing")
    lines.append("> manual data -- do not overwrite them.")
    lines.append("")
    if manual_rows:
        lines.append("| Name | Points Today | Total Points | Bonus (Manual) |")
        lines.append("|------|---------------|--------------|-----------------|")
        for m in manual_rows:
            lines.append(
                f"| {m['name']} | {m['points_today'] or '—'} "
                f"| {m['total_points'] or '—'} | {m['bonus_manual'] or '—'} |"
            )
    else:
        lines.append("_None detected._")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------
    # FULL BREAKDOWN
    # -----------------------------------------------------------------
    lines.append("## FULL BREAKDOWN")
    lines.append("")
    for person in people:
        lines.append(f"### {person} — {role_for(person)}")
        lines.append("")
        for day in DAY_ORDER:
            rec = day_data.get(day, {}).get(person)
            if rec is None:
                continue
            lines.append(f"#### {day} ({DAY_LABELS[day]} — {fmt_ts(rec['timestamp'])})")
            if rec["submitted"]:
                lines.append("- Submitted: ✅ Valid (same day)")
                if rec["early_bonus"]:
                    lines.append(f"- Early bonus: ✅ (+{rec['early_bonus']}, submitted before 3PM)")
                else:
                    lines.append("- Early bonus: ❌ (submitted at or after 3PM)")
            else:
                lines.append("- Submitted: ❌ DISQUALIFIED")
                lines.append("- Early bonus: ❌ (n/a — disqualified)")
            lines.append(f"- Check-in pts: +{rec['check_in_pts']}")
            lines.append(f"- Watched video: {rec['watched_video'] or '(blank)'}")
            lines.append(f"- Images uploaded: {rec['image_count']}")
            if rec["bonus_manual"]:
                lines.append(f"- Bonus points (manual, from form): {rec['bonus_manual']}")
            for w in rec["warnings"]:
                lines.append(f"- ⚠️ Warning: {w}")
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        print("Place the form export at that path and re-run.")
        return

    timed_rows, manual_rows = parse_form(INPUT_FILE)
    (day_data, disqualified, recovery_flags,
     duplicates, outside_programme) = analyze_rows(timed_rows)

    report = build_report(day_data, disqualified, recovery_flags,
                           duplicates, outside_programme, manual_rows)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Done. Wrote {OUTPUT_FILE}")
    print(f"  Submissions parsed: {len(timed_rows)}")
    print(f"  Manual rows (no timestamp): {len(manual_rows)}")
    print(f"  People detected: {len(get_all_people(day_data, manual_rows))}")
    print(f"  Disqualified: {len(disqualified)}")
    print(f"  New joiner recovery flags: {len(recovery_flags)}")
    print(f"  Duplicates: {len(duplicates)}")
    print(f"  Outside programme dates: {len(outside_programme)}")
    print()
    print("NEXT STEP: open Data/form_report.md and review every flagged")
    print("section (DISQUALIFIED, RECOVERY, DUPLICATES, OUTSIDE PROGRAMME)")
    print("before running leaderboard_sync.py.")


if __name__ == "__main__":
    main()
