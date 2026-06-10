"""
SKY GRAPHICS FIGMA EDITION 1 -- Leaderboard Sync  (DYNAMIC REFACTOR)
======================================================================

Input:  Data/wa_report.md               (output of wa_parser.py)
        Data/form_report.md             (output of form_parser.py)
        Data/Manual_Reconciliation_Points.md   (admin manual points)
Output: Data/master_data.md            (human-readable audit trail)
        data.js                        (leaderboard UI — goes in project root)

ZERO-MAINTENANCE DESIGN
-----------------------
* No hardcoded DAY_ORDER or DAY_LABELS  — discovered from the two reports.
* No hardcoded participant roster      — discovered from the two reports.
* No hardcoded MANUAL_BONUSES dict     — parsed from Manual_Reconciliation_Points.md.

ADMIN DECISIONS
---------------
1. STREAK RULE: FREEZE (not reset) on missed days.
2. WORK POST (+5): Triggered ONLY when form_report.md shows image_count > 0.
   WhatsApp media is NOT used for the base +5.
3. INTERACTIONS (+3 each): welcome, help, tip flags from wa_report.md.
4. MANUAL POINTS: Creativity scores, referral bonuses, milestones read from
   Data/Manual_Reconciliation_Points.md.

FORMULA (per day)
-----------------
  ptsToday = (CheckIn * 10) + (EarlyBonus * 5) + (WorkPost * 5)
           + (Interactions * 3) + ManualPoints(creativity + specials)

  Referrals (+25 each) and milestones are pre-programme / week-close bonuses.
"""

import os
import re
import json
from collections import defaultdict
from datetime import datetime

# ===========================================================================
# FILE PATHS
# ===========================================================================

WA_REPORT      = os.path.join("Data", "wa_report.md")
FORM_REPORT    = os.path.join("Data", "form_report.md")
MANUAL_REPORT  = os.path.join("Data", "Manual_Reconciliation_Points.md")
MASTER_OUT     = os.path.join("Data", "master_data.md")
DATA_JS_OUT    = "data2.js"

# ===========================================================================
# PROGRAMME CONSTANTS  (only things that cannot be derived from reports)
# ===========================================================================

# Canonical day ordering used to sort any days found in reports
_CANONICAL_DAY_ORDER = ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10"]

# Canonical labels for every possible programme day
_CANONICAL_DAY_LABELS = {
    "D1":  "Day 1 — Monday, June 1, 2026",
    "D2":  "Day 2 — Tuesday, June 2, 2026",
    "D3":  "Day 3 — Wednesday, June 3, 2026",
    "D4":  "Day 4 — Thursday, June 4, 2026",
    "D5":  "Day 5 — Friday, June 5, 2026",
    "D6":  "Day 6 — Monday, June 8, 2026",
    "D7":  "Day 7 — Tuesday, June 9, 2026",
    "D8":  "Day 8 — Wednesday, June 10, 2026",
    "D9":  "Day 9 — Thursday, June 11, 2026",
    "D10": "Day 10 — Friday, June 12, 2026",
}

# The last day of each week (used for milestone / perfect-week awards)
# Key = day label (e.g. "D5"), value = week tag (e.g. "W1")
WEEK_MILESTONE_DAYS = {"D5": "W1", "D10": "W2"}

TIER_THRESHOLDS = [
    (350, "PLATINUM"),
    (250, "GOLD"),
    (150, "SILVER"),
    (50,  "BRONZE"),
    (0,   "UNRANKED"),
]

# Keep ambassadors as the only hardcoded constant per spec
AMBASSADORS = {
    "Christine Choundong",
    "Oluwasegun Daniel Osawore",
    "Mbiydzenyuy Patience Dzekem",
    "Frank Emmanuel",
    "Malialia Celine Bride",
    "Irinyemi Adedayo Juliet",
}

FREEZE_STREAKS_ON_MISS = True   # admin override: freeze, not reset

# WhatsApp interaction flag → (points, display label)
WA_INTERACTION_META = {
    "first_to_post":  (5,  "First to post check-in in group"),
    "question":       (3,  "Asked a genuine question"),
    "helped":         (5,  "Helped another member"),
    "welcomed":       (3,  "Welcomed a new member"),
    "tip":            (3,  "Shared a useful tip or resource"),
    "encouragement":  (2,  "Posted encouragement that got reactions"),
}

RULES = [
    {"title": "The Check-in Rule",
     "content": "Only the Google Form determines a check-in point (+10) and early bonus (+5 before 3PM). WhatsApp posts alone do not count as check-ins."},
    {"title": "Same-Day Requirement",
     "content": "Forms must be submitted on the actual calendar date of the task. Late submissions for past days are disqualified and earn +0 check-in points."},
    {"title": "Weekly Milestone (+20)",
     "content": "Awarded on Friday for submitting Figma work in the WhatsApp group during that week. A form submission is not required for the milestone."},
    {"title": "Perfect Week (+15)",
     "content": "Awarded on Friday for submitting 5 out of 5 valid same-day check-in forms (Monday to Friday). All 5 must be on the correct day."},
    {"title": "Creativity Bonus",
     "content": "Admin-assigned per day: Standard (+5), Good (+10), Impressive (+15), Extraordinary (+20). Only one score per person per day."},
    {"title": "Public Interaction",
     "content": "First to post in group (+5), helping a member (+5), asking a genuine question (+3), welcoming a new member (+3), sharing a tip (+3), encouragement with reactions (+2)."},
    {"title": "Referral Bonus",
     "content": "Each new member who joins the programme and pledges earns the referring person +25 points, applied once when the pledge is confirmed."},
    {"title": "Work Post Bonus (+5)",
     "content": "Awarded once per day when the check-in form shows at least one image uploaded. WhatsApp media alone does not trigger this bonus."},
]

# ===========================================================================
# HELPERS
# ===========================================================================

def day_sort_key(d):
    """Sort key so D1 < D2 ... < D10 regardless of string sort."""
    try:
        return _CANONICAL_DAY_ORDER.index(d)
    except ValueError:
        # Unknown day: put at the end, ordered numerically
        m = re.match(r'D(\d+)', d)
        return int(m.group(1)) + 100 if m else 999

def sort_days(day_iterable):
    return sorted(day_iterable, key=day_sort_key)

def get_tier(pts):
    for threshold, tier in TIER_THRESHOLDS:
        if pts >= threshold:
            return tier
    return "UNRANKED"

def role_for(name):
    return "Ambassador" if name in AMBASSADORS else "Participant"

def wa_interaction_pts(flags: dict) -> int:
    """Sum WA interaction points from a flags dict."""
    total = 0
    for key, (pts, _label) in WA_INTERACTION_META.items():
        if flags.get(key):
            total += pts
    return total

# ===========================================================================
# PARSER — Manual_Reconciliation_Points.md
# ===========================================================================

def parse_manual_report(filepath):
    """
    Parse Data/Manual_Reconciliation_Points.md and return a nested dict:

    {
      name: {
        "creativity":       {day: int},   # admin creativity scores per day
        "referral_pts":     int,          # total referral points
        "milestone_weeks":  ["W1", ...],  # weeks with milestone (+20)
        "perfect_weeks":    ["W1", ...],  # weeks with perfect-week (+15)
        "special":          {day: {"pts": int, "reason": str}},
        "wa_interactions":  {day: {flag: bool}},
      }
    }

    Parsing strategy
    ----------------
    Section 1 — "Creativity Scores Assigned":
        Lines like:  **Name**: D1: +10, D2: +20, ...
        Also:        **Name**: Day 1: +10, ...

    Section 2 — "Interaction & Referral Points":
        Lines like:  **Name**: Referral bonus (+75), First-to-post (D1, D5 = +10), ...
        Also:        **Name**: ... Welcome/Help (+3), Welcomed members (+3), ...

    Section 3 — "Milestone Points":
        Lines like:  **Weekly Milestone (+20 pts)**: Awarded to Name1, Name2, ...
    """
    result = defaultdict(lambda: {
        "creativity":      {},
        "referral_pts":    0,
        "milestone_weeks": [],
        "perfect_weeks":   [],
        "special":         {},
        "wa_interactions": {},
    })

    if not os.path.exists(filepath):
        print(f"  [WARN] {filepath} not found — manual points will be empty.")
        return dict(result)

    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    section = None

    # Regex patterns
    name_re      = re.compile(r'^\s*\*\s*\*\*(.+?)\*\*\s*[:\-]\s*(.*)$')
    day_pts_re   = re.compile(r'\b(D\d{1,2})\s*[:\-=]\s*\+?(\d+)\s*(?:pts?)?', re.IGNORECASE)
    ref_re       = re.compile(r'Referral bonus\s*\(\+(\d+)\)', re.IGNORECASE)
    milestone_re = re.compile(r'\*\*Weekly Milestone[^*]*\*\*\s*[:\-]\s*Awarded to\s*(.+)', re.IGNORECASE)
    fb_bonus_re  = re.compile(r'FB Interaction\s*\(\+(\d+)\)', re.IGNORECASE)
    first_post_re = re.compile(r'First-to-post\s*\([^)]+\)\s*=?\s*\+?(\d+)', re.IGNORECASE)
    # first-to-post day list: "First-to-post (D2, D3, D4 = +15)"
    first_post_days_re = re.compile(r'First-to-post\s*\(([^)]+)\)', re.IGNORECASE)
    tech_help_re = re.compile(r'Technical Help\s+(D\d{1,2})\s*\(\+(\d+)\)', re.IGNORECASE)
    first_form_re = re.compile(r'First Form\s*\(\+(\d+)\)', re.IGNORECASE)
    perfect_re   = re.compile(r'Perfect Week\s*\(\+\d+\)', re.IGNORECASE)
    milestone_week_re = re.compile(r'Weekly Milestone\s*\(\+\d+\)', re.IGNORECASE)
    welcome_help_re = re.compile(r'Welcome(?:d members|/Help)\s*\(\+(\d+)\)', re.IGNORECASE)
    ambassador_ms_re = re.compile(r'Ambassador Milestone\s*\(\+(\d+)\)', re.IGNORECASE)

    # Pre-process lines to handle wrapped lines (lines not starting with * or #)
    processed_lines = []
    for line in text.splitlines():
        line = line.rstrip()
        if not line: continue
        if line.lstrip().startswith(('*', '#')):
            processed_lines.append(line)
        else:
            if processed_lines:
                processed_lines[-1] += " " + line.lstrip()
            else:
                processed_lines.append(line)

    for line in processed_lines:
        line = line.strip()
        # Detect section header
        if re.search(r'^\s*#+\s*.*Creativity Scores Assigned', line, re.IGNORECASE):
            section = "creativity"
            continue
        if re.search(r'^\s*#+\s*.*Interaction.*Referral', line, re.IGNORECASE):
            section = "interaction"
            continue
        if re.search(r'^\s*#+\s*.*Milestone Points', line, re.IGNORECASE):
            section = "milestone"
            continue

        # --- SECTION: Creativity Scores ---
        if section == "creativity":
            m = name_re.search(line)
            if m:
                name  = m.group(1).strip()
                rest  = m.group(2)
                for dm in day_pts_re.finditer(rest):
                    day = dm.group(1).upper()
                    pts = int(dm.group(2))
                    # Keep highest score if duplicated (e.g. "D6: +5, D6: +5")
                    existing = result[name]["creativity"].get(day, 0)
                    result[name]["creativity"][day] = existing + pts

    # --- SECTION: Interaction & Referral ---
    for line in processed_lines:
        line = line.strip()
        # Detect section header
        if re.search(r'^\s*#+\s*.*Creativity Scores Assigned', line, re.IGNORECASE):
            section = "creativity"
            continue
        if re.search(r'^\s*#+\s*.*Interaction.*Referral', line, re.IGNORECASE):
            section = "interaction"
            continue
        if re.search(r'^\s*#+\s*.*Milestone Points', line, re.IGNORECASE):
            section = "milestone"
            continue

        if section == "interaction":
            m = name_re.search(line)
            if m:
                raw_name = m.group(1).strip()
                rest = m.group(2)

                # Canonicalize name

                name = get_canonical_name(raw_name)
                # ... [rest of logic] ...
            else:
                pass

            # Referral bonus
            for rm in ref_re.finditer(rest):
                result[name]["referral_pts"] += int(rm.group(1))

            # Perfect week
            if perfect_re.search(rest):
                if "W1" not in result[name]["perfect_weeks"]:
                    result[name]["perfect_weeks"].append("W1")

            # Weekly milestone
            if milestone_week_re.search(rest):
                if "W1" not in result[name]["milestone_weeks"]:
                    result[name]["milestone_weeks"].append("W1")
            
            # FB interaction bonus → special on D5
            fbm = fb_bonus_re.search(rest)
            if fbm:
                fb_pts = int(fbm.group(1))
                day_key = "D5"
                existing = result[name]["special"].get(day_key, {})
                result[name]["special"][day_key] = {
                    "pts":    existing.get("pts", 0) + fb_pts,
                    "reason": "FB interaction bonus confirmed",
                }
            
            # First-to-post: award wa_interaction flag per day
            fpdm = first_post_days_re.search(rest)
            if fpdm:
                days_str = fpdm.group(1)
                for fd in re.findall(r'D\d{1,2}', days_str, re.IGNORECASE):
                    fd = fd.upper()
                    if fd not in result[name]["wa_interactions"]:
                        result[name]["wa_interactions"][fd] = {}
                    result[name]["wa_interactions"][fd]["first_to_post"] = True

            # Welcome/Help interaction flag
            whm = welcome_help_re.search(rest)
            if whm:
                wh_pts = int(whm.group(1))
                flag = "helped" if wh_pts >= 5 else "welcomed"
                # Apply generically to D1 unless a specific day was named
                day_m = re.search(r'\bD\d{1,2}\b', rest)
                day_key = day_m.group(0).upper() if day_m else "D1"
                if day_key not in result[name]["wa_interactions"]:
                    result[name]["wa_interactions"][day_key] = {}
                result[name]["wa_interactions"][day_key][flag] = True

                # Weekly milestone
                if milestone_week_re.search(rest):
                    if "W1" not in result[name]["milestone_weeks"]:
                        result[name]["milestone_weeks"].append("W1")

                # Technical help day
                for thm in tech_help_re.finditer(rest):
                    th_day = thm.group(1).upper()
                    th_pts = int(thm.group(2))
                    existing = result[name]["special"].get(th_day, {})
                    result[name]["special"][th_day] = {
                        "pts":    existing.get("pts", 0) + th_pts,
                        "reason": f"Technical Help {th_day}",
                    }

                # First form bonus → special on D1
                ffm = first_form_re.search(rest)
                if ffm:
                    ff_pts = int(ffm.group(1))
                    existing = result[name]["special"].get("D1", {})
                    result[name]["special"]["D1"] = {
                        "pts":    existing.get("pts", 0) + ff_pts,
                        "reason": "First to submit check-in form",
                    }

                # Ambassador milestone → special
                amm = ambassador_ms_re.search(rest)
                if amm:
                    am_pts = int(amm.group(1))
                    existing = result[name]["special"].get("D1", {})
                    result[name]["special"]["D1"] = {
                        "pts":    existing.get("pts", 0) + am_pts,
                        "reason": "Ambassador milestone bonus",
                    }

        # --- SECTION: Milestone Points ---
        if section == "milestone":
            mm = milestone_re.search(line)
            if mm:
                names_str = mm.group(1)
                # Split on comma, "and", strip punctuation
                names_list = re.split(r',\s*|\s+and\s+', names_str)
                for n in names_list:
                    n = n.strip().rstrip(".").replace("and ", "")
                    if n:
                        if "W1" not in result[n]["milestone_weeks"]:
                            result[n]["milestone_weeks"].append("W1")

    return dict(result)

# ===========================================================================
# PARSER — form_report.md
# ===========================================================================

def parse_form_report(filepath):
    """
    Parse form_report.md and return:

    form_per_day: {name: {day: {"submitted": bool, "check_in_pts": int,
                                "early_bonus": int, "image_count": int,
                                "warnings": [str]}}}
    joined_days:  {name: first_day_string}
    """
    if not os.path.exists(filepath):
        print(f"  [WARN] {filepath} not found — form data will be empty.")
        return {}, {}

    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    form_per_day  = defaultdict(lambda: defaultdict(dict))
    joined_days   = {}

    person_re  = re.compile(r'^### (.+?) — (Ambassador|Participant)$')
    day_re     = re.compile(r'^#### (D\d{1,2})\b')
    submit_re  = re.compile(r'- Submitted:\s*(✅|❌)')
    early_re   = re.compile(r'- Early bonus:\s*(✅|❌)')
    checkin_re = re.compile(r'- Check-in pts:\s*\+(\d+)')
    images_re  = re.compile(r'- Images uploaded:\s*(\d+)')
    warn_re    = re.compile(r'- ⚠️ Warning:\s*(.+)')

    current_person = None
    current_day    = None

    for line in text.splitlines():
        line = line.rstrip()

        m = person_re.match(line)
        if m:
            current_person = m.group(1).strip()
            current_day    = None
            continue

        m = day_re.match(line)
        if m and current_person:
            current_day = m.group(1)
            form_per_day[current_person][current_day] = {
                "submitted":    False,
                "check_in_pts": 0,
                "early_bonus":  0,
                "image_count":  0,
                "warnings":     [],
            }
            if current_person not in joined_days:
                joined_days[current_person] = current_day
            continue

        if current_person and current_day:
            rec = form_per_day[current_person][current_day]
            m = submit_re.search(line)
            if m:
                rec["submitted"] = (m.group(1) == "✅")
                continue
            m = early_re.search(line)
            if m:
                rec["early_bonus"] = 5 if m.group(1) == "✅" else 0
                continue
            m = checkin_re.search(line)
            if m:
                rec["check_in_pts"] = int(m.group(1))
                continue
            m = images_re.search(line)
            if m:
                rec["image_count"] = int(m.group(1))
                continue
            m = warn_re.search(line)
            if m:
                rec["warnings"].append(m.group(1))

    return dict(form_per_day), joined_days

# ===========================================================================
# PARSER — wa_report.md
# ===========================================================================

def parse_wa_report(filepath):
    """
    Parse wa_report.md and return:
    wa_interactions: {name: {day: {flag: bool}}}
    pledges:         set of names with a Pledge entry
    """
    if not os.path.exists(filepath):
        print(f"  [WARN] {filepath} not found — WA data will be empty.")
        return {}, set()

    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    wa_interactions = defaultdict(lambda: defaultdict(dict))
    pledges = set()

    person_re = re.compile(r'^### (.+?) — (Ambassador|Participant)$')
    day_re    = re.compile(r'^#### (D\d{1,2})\b')

    # Map report labels to our internal interaction flags
    label_map = {
        "first_to_post":        "first_to_post",
        "welcome_new_member":   "welcomed",
        "helped_a_member":      "helped",
        "shared_tip_or_resource": "tip",
        "asked_genuine_question": "question",
        "posted_encouragement": "encouragement",
    }

    current_person = None
    current_day    = None

    for line in text.splitlines():
        line = line.strip()
        if not line: continue

        m = person_re.match(line)
        if m:
            current_person = m.group(1).strip()
            current_day    = None
            continue

        m = day_re.match(line)
        if m and current_person:
            current_day = m.group(1)
            continue

        # Look for interactions: "- label: +X pts"
        if current_person and current_day and line.startswith("- "):
            for label, flag in label_map.items():
                if f"- {label}:" in line:
                    wa_interactions[current_person][current_day][flag] = True

        # Look for pledge: "- **Pledge:** +5 pts"
        if current_person and "**Pledge:**" in line and "+5 pts" in line:
            pledges.add(current_person)

    return dict(wa_interactions), pledges


# Import Name Mapping from wa_parser
# We need to ensure we map names consistently.
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from wa_parser import NAME_MAP, CANONICAL_NAMES

def get_canonical_name(name):
    """Fuzzy match or map name to canonical."""
    name = name.strip()
    if name in NAME_MAP:
        return NAME_MAP[name]
    # Check if it's already canonical
    if name in CANONICAL_NAMES:
        return name
    # Fuzzy match
    from rapidfuzz import process as rprocess, fuzz as rfuzz
    match = rprocess.extractOne(name, CANONICAL_NAMES, scorer=rfuzz.token_sort_ratio, score_cutoff=85)
    return match[0] if match else name

def get_all_names_from_legacy():
    """Extract all names from the existing production data.js."""
    if not os.path.exists("data.js"):
        return set()
    with open("data.js", "r", encoding="utf-8") as f:
        return set(re.findall(r'name:\s*\"(.*?)\"', f.read()))

def discover_days_and_people(form_per_day, wa_interactions, manual_bonuses, pledges):
    """
    Collect every day key (D1..D10) and every person name seen across
    all three data sources.

    Returns:
        day_order:  list of day keys sorted canonically
        all_names:  set of participant name strings
    """
    all_days  = set()
    all_names = get_all_names_from_legacy()

    for name, days in form_per_day.items():
        all_names.add(name)
        all_days.update(days.keys())

    for name, days in wa_interactions.items():
        all_names.add(name)
        all_days.update(days.keys())

    for name, data in manual_bonuses.items():
        all_names.add(name)
        all_days.update(data.get("creativity", {}).keys())
        all_days.update(data.get("special", {}).keys())
        all_days.update(data.get("wa_interactions", {}).keys())
    
    for name in pledges:
        all_names.add(name)

    # Remove admin artefacts
    all_names.discard("ADMIN")
    all_names.discard("")

    return sort_days(all_days), all_names

# ===========================================================================
# POINTS CALCULATION
# ===========================================================================

def calc_day_points(name, day, form_rec, manual_bonuses, wa_interactions):
    """
    Compute all point components for one person on one day.

    Formula:
      ptsToday = (CheckIn * 10) + (EarlyBonus * 5) + (WorkPost * 5)
               + (Interactions * 3 each, per WA flag)
               + creativity_score + special_pts + milestone_pts + perfect_pts
    """
    mb = manual_bonuses.get(name, {})

    # --- Form data ---
    if form_rec:
        check_in_pts = form_rec.get("check_in_pts", 0)
        early_bonus  = form_rec.get("early_bonus",  0)
        submitted    = form_rec.get("submitted",     False)
        image_count  = form_rec.get("image_count",  0)
        warnings     = form_rec.get("warnings",     [])
    else:
        check_in_pts = 0
        early_bonus  = 0
        submitted    = False
        image_count  = 0
        warnings     = []

    # Work Post bonus: +5 flat if image_count > 0 (form only)
    work_post_pts = 5 if image_count > 0 else 0

    # --- Creativity score (from manual report) ---
    creativity_score = mb.get("creativity", {}).get(day, 0)

    # workDone: either submitted a form OR has creativity score
    workDone = submitted or creativity_score > 0

    # --- WhatsApp interactions ---
    # Merge: manual report flags take precedence over wa_report flags
    # (admin may have overridden in the manual report)
    wa_day_manual = mb.get("wa_interactions", {}).get(day, {})
    wa_day_report = wa_interactions.get(name, {}).get(day, {})
    # Merge: manual overrides
    wa_flags = {**wa_day_report, **wa_day_manual}

    wa_pts    = wa_interaction_pts(wa_flags)
    wa_detail = []
    for flag, (pts, label) in WA_INTERACTION_META.items():
        if wa_flags.get(flag):
            wa_detail.append((label, pts))

    # --- Special one-off bonus ---
    special_rec = mb.get("special", {}).get(day, {})
    special_pts = special_rec.get("pts", 0)

    # --- Milestone (+20) — only on the day the week closes ---
    milestone_pts = 0
    if day in WEEK_MILESTONE_DAYS:
        week_tag = WEEK_MILESTONE_DAYS[day]
        if week_tag in mb.get("milestone_weeks", []):
            milestone_pts = 20

    # --- Perfect week (+15) ---
    perfect_pts = 0
    if day in WEEK_MILESTONE_DAYS:
        week_tag = WEEK_MILESTONE_DAYS[day]
        if week_tag in mb.get("perfect_weeks", []):
            perfect_pts = 15

    delta = (check_in_pts + early_bonus + work_post_pts
             + creativity_score + wa_pts + special_pts
             + milestone_pts + perfect_pts)

    return {
        "delta":            delta,
        "submitted":        submitted,
        "workDone":         workDone,
        "check_in_pts":     check_in_pts,
        "early_bonus":      early_bonus,
        "image_count":      image_count,
        "work_post_pts":    work_post_pts,
        "creativity_score": creativity_score,
        "wa_pts":           wa_pts,
        "wa_detail":        wa_detail,
        "special_pts":      special_pts,
        "special_reason":   special_rec.get("reason", ""),
        "milestone_pts":    milestone_pts,
        "perfect_pts":      perfect_pts,
        "warnings":         warnings,
    }

def calc_pre_programme(name, manual_bonuses):
    """Pledge (5) + referral points. Awarded before D1."""
    mb = manual_bonuses.get(name, {})
    pledge_pts   = 5
    referral_pts = mb.get("referral_pts", 0)
    return pledge_pts, referral_pts

def calc_streaks(days_computed):
    """
    Apply FREEZE_STREAKS_ON_MISS streak logic.
    Mutates each result dict in place, adding streakDays and workStreakDays.
    """
    form_streak = 0
    work_streak = 0
    for _day, result in days_computed:
        if result["submitted"]:
            form_streak += 1
        elif not FREEZE_STREAKS_ON_MISS:
            form_streak = 0
        # else: freeze — form_streak unchanged

        if result["workDone"]:
            work_streak += 1
        elif not FREEZE_STREAKS_ON_MISS:
            work_streak = 0

        result["streakDays"]     = form_streak
        result["workStreakDays"] = work_streak

# ===========================================================================
# BUILD BREAKDOWN
# ===========================================================================

def build_breakdown(name, days_results, manual_bonuses, pledge_pts, referral_pts):
    """
    Build the breakdown sections list for the profile panel.
    """
    mb = manual_bonuses.get(name, {})
    sections = []

    # PRE-PROGRAMME
    pre_items = [{
        "label":   "Pledge",
        "pts":     5,
        "earned":  True,
        "dayHits": None,
        "desc":    "You committed to the programme. +5 for your pledge.",
    }]
    refs = mb.get("referral_pts", 0)
    if refs > 0:
        ref_count = refs // 25
        pre_items.append({
            "label":   f"Referral × {ref_count}",
            "pts":     refs,
            "earned":  True,
            "dayHits": None,
            "desc":    f"You brought {ref_count} new member{'s' if ref_count != 1 else ''} in. +{refs} pts.",
        })
    sections.append({"section": "PRE-PROGRAMME", "items": pre_items})

    # DAILY CHECK-INS
    checkin_hits  = [d for d, r in days_results if r["submitted"]]
    early_hits    = [d for d, r in days_results if r["early_bonus"] > 0]
    checkin_total = sum(r["check_in_pts"] for _, r in days_results)
    early_total   = sum(r["early_bonus"]  for _, r in days_results)

    ci_items = [{
        "label":   "Form submission",
        "pts":     10,
        "earned":  bool(checkin_hits),
        "dayHits": checkin_hits or None,
        "desc":    (f"{len(checkin_hits)} valid form{'s' if len(checkin_hits) != 1 else ''} submitted. "
                    f"+{checkin_total} total.") if checkin_hits else "No valid form submissions yet.",
    }]
    if early_hits:
        ci_items.append({
            "label":   "Early submission bonus",
            "pts":     5,
            "earned":  True,
            "dayHits": early_hits,
            "desc":    f"Submitted before 3PM on {', '.join(early_hits)}. +{early_total} total.",
        })
    sections.append({"section": "DAILY CHECK-INS", "items": ci_items})

    # FIGMA WORK (creativity scores)
    creativity_by_day = {d: r["creativity_score"] for d, r in days_results if r["creativity_score"] > 0}
    if creativity_by_day:
        score_desc = " · ".join(f"{d}:{s}" for d, s in sorted(creativity_by_day.items(), key=lambda x: day_sort_key(x[0])))
        cre_items = [{
            "label":   "Creativity scores",
            "pts":     None,
            "earned":  True,
            "dayHits": sort_days(creativity_by_day.keys()),
            "desc":    score_desc + f". Total: +{sum(creativity_by_day.values())}.",
        }]
    else:
        cre_items = [{
            "label":   "Creativity scores",
            "pts":     None,
            "earned":  False,
            "dayHits": None,
            "desc":    "No creativity scores awarded yet.",
        }]
    sections.append({"section": "FIGMA WORK", "items": cre_items})

    # WORK POST (image uploads → +5 flat)
    work_post_hits  = [d for d, r in days_results if r["work_post_pts"] > 0]
    work_post_total = sum(r["work_post_pts"] for _, r in days_results)
    if work_post_hits:
        sections.append({"section": "WORK POST", "items": [{
            "label":   "Work post (image uploaded)",
            "pts":     5,
            "earned":  True,
            "dayHits": work_post_hits,
            "desc":    f"Image uploaded on {', '.join(work_post_hits)}. +{work_post_total} total.",
        }]})

    # WHATSAPP ENGAGEMENT
    wa_total = sum(r["wa_pts"] for _, r in days_results)
    if wa_total > 0:
        wa_by_action = defaultdict(list)
        for d, r in days_results:
            for label, pts in r["wa_detail"]:
                wa_by_action[label].append(d)
        wa_items = []
        for label, day_list in sorted(wa_by_action.items()):
            pts_each = next(p for flag, (p, l) in WA_INTERACTION_META.items() if l == label)
            wa_items.append({
                "label":   label,
                "pts":     pts_each,
                "earned":  True,
                "dayHits": day_list,
                "desc":    f"+{pts_each * len(day_list)} total.",
            })
        sections.append({"section": "WHATSAPP ENGAGEMENT", "items": wa_items})

    # BONUSES
    bonus_items = []
    for d, r in days_results:
        if r["milestone_pts"] > 0:
            bonus_items.append({
                "label":   f"Week Milestone ({WEEK_MILESTONE_DAYS.get(d, d)})",
                "pts":     r["milestone_pts"],
                "earned":  True,
                "dayHits": [d],
                "desc":    "Figma work submitted for the week. +20.",
            })
        if r["perfect_pts"] > 0:
            bonus_items.append({
                "label":   f"Perfect Week ({WEEK_MILESTONE_DAYS.get(d, d)})",
                "pts":     r["perfect_pts"],
                "earned":  True,
                "dayHits": [d],
                "desc":    "5/5 valid same-day forms. +15.",
            })
        if r["special_pts"] > 0:
            bonus_items.append({
                "label":   f"Special Bonus ({d})",
                "pts":     r["special_pts"],
                "earned":  True,
                "dayHits": [d],
                "desc":    r["special_reason"] + f". +{r['special_pts']}.",
            })
    if bonus_items:
        sections.append({"section": "BONUSES", "items": bonus_items})

    return sections

# ===========================================================================
# ROAST GENERATOR
# ===========================================================================

def generate_roast(name, days_results, tier, warnings):
    total_days  = len(days_results)
    active_days = sum(1 for _, r in days_results if r["delta"] > 0)
    form_days   = sum(1 for _, r in days_results if r["submitted"])
    work_days   = sum(1 for _, r in days_results if r["workDone"])
    streak      = max((r["streakDays"]     for _, r in days_results), default=0)
    attendance  = round(100 * active_days / total_days) if total_days else 0
    gap         = work_days - form_days
    first_name  = name.split()[0]

    parts = [f"<p><strong>{first_name}.</strong> "]

    if tier in ("PLATINUM", "GOLD"):
        parts.append("You are at the top of this board. Every day you show up, you pull further ahead.")
        if gap > 2:
            parts.append(f" But you are posting work without submitting the form on {gap} days. "
                         "That is free points you are giving away. Fix it.")
        elif attendance == 100:
            parts.append(" 100% attendance. That is the standard. Hold it.")
        parts.append("</p>")
    elif tier == "SILVER":
        parts.append("You are in the upper half. Close to Gold.")
        if streak >= 3:
            parts.append(f" {streak}-day streak — keep that going.")
        if gap > 0:
            parts.append(f" You are leaving points on the table: {gap} day(s) with work but no form.")
        parts.append("</p>")
    elif tier == "BRONZE":
        parts.append("You have made it onto the board. But barely.")
        if active_days < total_days // 2:
            parts.append(f" You have only shown up {active_days} of {total_days} days. "
                         "Consistency is the whole game here.")
        parts.append("</p>")
    else:
        parts.append("You are on this board because you pledged.")
        if active_days == 0:
            parts.append(" But pledging was the easy part. You have not submitted a single day yet.")
        parts.append(" Every day you sit this out, someone else is climbing past you.</p>")

    return "".join(parts)

# ===========================================================================
# BUILD PERSON
# ===========================================================================

def build_person(name, day_order, form_per_day, manual_bonuses, wa_interactions):
    """
    Build a full person dict for a single participant.
    """
    mb = manual_bonuses.get(name, {})

    # Pre-programme points
    pledge_pts, referral_pts = calc_pre_programme(name, manual_bonuses)
    pre_total = pledge_pts + referral_pts

    # Determine which days this person has any data on
    form_days     = set(form_per_day.get(name, {}).keys())
    wa_days       = set(wa_interactions.get(name, {}).keys())
    cre_days      = set(mb.get("creativity", {}).keys())
    special_days  = set(mb.get("special", {}).keys())
    manual_wa_days = set(mb.get("wa_interactions", {}).keys())
    milestone_days = {d for d in WEEK_MILESTONE_DAYS if WEEK_MILESTONE_DAYS[d] in mb.get("milestone_weeks", [])}
    perfect_days   = {d for d in WEEK_MILESTONE_DAYS if WEEK_MILESTONE_DAYS[d] in mb.get("perfect_weeks", [])}

    active_days = (form_days | wa_days | cre_days | special_days
                   | manual_wa_days | milestone_days | perfect_days)

    # Build per-day results in discovered programme order
    days_computed = []
    
    # Track streaks here
    form_streak = 0
    work_streak = 0
    
    cumulative = pre_total
    days_out   = {}
    
    for day in day_order:
        form_rec = form_per_day.get(name, {}).get(day, None)
        
        # Calculate points for this day (active or empty)
        result = calc_day_points(name, day, form_rec, manual_bonuses, wa_interactions)
        
        # Apply streak logic per day
        if result["submitted"]:
            form_streak += 1
        elif not FREEZE_STREAKS_ON_MISS:
            form_streak = 0
        if result["workDone"]:
            work_streak += 1
        elif not FREEZE_STREAKS_ON_MISS:
            work_streak = 0
            
        result["streakDays"]     = form_streak
        result["workStreakDays"] = work_streak
        
        days_computed.append((day, result))
        cumulative += result["delta"]
        
        days_out[day] = {
            "pts":            cumulative,
            "submitted":      result["submitted"],
            "streakDays":     result["streakDays"],
            "workDone":       result["workDone"],
            "workStreakDays": result["workStreakDays"],
        }

    joined_day = next(iter(days_out), "D1")
    all_time   = cumulative
    tier       = get_tier(all_time)

    all_warnings = []
    for _, result in days_computed:
        all_warnings.extend(result.get("warnings", []))

    breakdown = build_breakdown(name, days_computed, manual_bonuses, pledge_pts, referral_pts)
    roast     = generate_roast(name, days_computed, tier, all_warnings)

    return {
        "name":          name,
        "role":          role_for(name),
        "joinedDay":     joined_day,
        "allTimeTotal":  all_time,
        "tier":          tier,
        "warnings":      all_warnings,
        "days":          days_out,
        "breakdown":     breakdown,
        "roast":         roast,
        "_days_detail":  days_computed,   # for master_data.md only
        "_pre_total":    pre_total,
    }

# ===========================================================================
# MASTER DATA MARKDOWN
# ===========================================================================

def write_master_data(all_people, day_order, filepath):
    lines = []
    lines.append("# SKY GRAPHICS FIGMA EDITION 1 — MASTER DATA AUDIT TRAIL")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("> Generated by leaderboard_sync.py (dynamic refactor).")
    lines.append("> Primary source of truth: form_report.md, wa_report.md,")
    lines.append("> Manual_Reconciliation_Points.md.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Summary table
    lines.append("## SUMMARY")
    lines.append("")
    header = "| Name | Role | Total | Tier | " + " | ".join(day_order) + " |"
    sep    = "|------|------|-------|------|" + "|".join(["----"] * len(day_order)) + "|"
    lines.append(header)
    lines.append(sep)
    for p in sorted(all_people, key=lambda x: -x["allTimeTotal"]):
        day_cells = []
        for d in day_order:
            if d in p["days"]:
                day_cells.append(str(p["days"][d]["pts"]))
            else:
                day_cells.append("—")
        lines.append(f"| {p['name']} | {p['role']} | {p['allTimeTotal']} | {p['tier']} | "
                     + " | ".join(day_cells) + " |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-person detail
    for p in sorted(all_people, key=lambda x: -x["allTimeTotal"]):
        lines.append(f"## {p['name']} — {p['role']}")
        lines.append(f"**All-time total:** {p['allTimeTotal']} pts  |  **Tier:** {p['tier']}  |  "
                     f"**Joined:** {p['joinedDay']}")
        lines.append("")
        if p["warnings"]:
            for w in p["warnings"]:
                lines.append(f"⚠️  {w}")
            lines.append("")

        for day, result in p.get("_days_detail", []):
            delta      = result["delta"]
            cumulative = p["days"][day]["pts"]
            lines.append(f"### {day} — delta +{delta} → cumulative {cumulative}")
            lines.append(f"- Form: {'✅' if result['submitted'] else '❌'}  "
                         f"check-in +{result['check_in_pts']}  "
                         f"early +{result['early_bonus']}")
            lines.append(f"- Images: {result['image_count']}  "
                         f"work post +{result['work_post_pts']}")
            lines.append(f"- Creativity: +{result['creativity_score']}")
            lines.append(f"- WA pts: +{result['wa_pts']}" +
                         (f"  ({', '.join(l for l, _ in result['wa_detail'])})"
                          if result["wa_detail"] else ""))
            if result["special_pts"]:
                lines.append(f"- Special: +{result['special_pts']}  ({result['special_reason']})")
            if result["milestone_pts"]:
                lines.append(f"- Milestone: +{result['milestone_pts']}")
            if result["perfect_pts"]:
                lines.append(f"- Perfect week: +{result['perfect_pts']}")
            lines.append(f"- Streaks: form={result['streakDays']}  work={result['workStreakDays']}")
            lines.append("")

        lines.append("---")
        lines.append("")

    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

# ===========================================================================
# DATA.JS WRITER
# ===========================================================================

def js_str(s):
    """Escape a string for use inside a JS template literal."""
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

def write_data_js(all_people, day_order, day_labels, filepath):
    """
    Write the final data.js file in the exact structure expected by the UI.
    day_order and day_labels are derived dynamically from the reports.
    """
    lines = []

    lines.append("/**")
    lines.append(" * SKY GRAPHICS FIGMA EDITION 1 — LEADERBOARD DATA")
    lines.append(f" * Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(" *")
    lines.append(" * STREAK RULES (admin override — FREEZE on miss):")
    lines.append(" *   Form streak: freezes (does not reset) on missed form days")
    lines.append(" *   Work streak: freezes (does not reset) on days without scored work")
    lines.append(" *   submitted:true always implies workDone:true")
    lines.append(" *")
    lines.append(" * pts in days[D] = CUMULATIVE total as of that day")
    lines.append(" * ptsToday (delta) is NOT stored here — UI derives it as pts - prevDay.pts")
    lines.append(" */")
    lines.append("")

    # DAY_LABELS — dynamically built from discovered days
    lines.append("export const DAY_LABELS = {")
    for d in day_order:
        label = day_labels.get(d, d)
        lines.append(f"  {d}: '{label}',")
    lines.append("};")
    lines.append("")

    # TIER_EMOJI
    lines.append("export const TIER_EMOJI = {")
    lines.append("  PLATINUM: '🏆', GOLD: '🥇', SILVER: '🥈', BRONZE: '🥉', UNRANKED: '⬜'")
    lines.append("};")
    lines.append("")

    # PEOPLE
    lines.append("export const PEOPLE = [")
    for p in all_people:
        lines.append("  {")
        lines.append(f"    name: {json.dumps(p['name'])},")
        lines.append(f"    role: {json.dumps(p['role'])},")
        lines.append(f"    joinedDay: {json.dumps(p['joinedDay'])},")
        lines.append(f"    allTimeTotal: {p['allTimeTotal']},")
        lines.append(f"    tier: {json.dumps(p['tier'])},")

        # warnings
        if p["warnings"]:
            warn_js = ", ".join(json.dumps(w) for w in p["warnings"])
            lines.append(f"    warnings: [{warn_js}],")
        else:
            lines.append("    warnings: [],")

        # days — write only days that exist
        if p["days"]:
            lines.append("    days: {")
            for d in day_order:
                if d not in p["days"]:
                    continue
                rec = p["days"][d]
                lines.append(
                    f"      {d}: {{ pts: {rec['pts']}, submitted: {'true' if rec['submitted'] else 'false'}, "
                    f"streakDays: {rec['streakDays']}, workDone: {'true' if rec['workDone'] else 'false'}, "
                    f"workStreakDays: {rec['workStreakDays']} }},"
                )
            lines.append("    },")
        else:
            lines.append("    days: {},")

        # breakdown
        lines.append("    breakdown: [")
        for sec in p["breakdown"]:
            lines.append(f"      {{ section: {json.dumps(sec['section'])}, items: [")
            for item in sec["items"]:
                pts_js    = str(item["pts"]) if item["pts"] is not None else "null"
                earned_js = "true" if item["earned"] else "false"
                hits_js   = json.dumps(item["dayHits"]) if item["dayHits"] else "null"
                desc_js   = json.dumps(item["desc"])
                label_js  = json.dumps(item["label"])
                lines.append(
                    f"        {{ label: {label_js}, pts: {pts_js}, "
                    f"earned: {earned_js}, dayHits: {hits_js}, desc: {desc_js} }},"
                )
            lines.append("      ]},")
        lines.append("    ],")

        # roast (template literal to preserve HTML)
        safe_roast = js_str(p["roast"])
        lines.append(f"    roast: `{safe_roast}`,")

        lines.append("  },")

    lines.append("];")
    lines.append("")

    # RULES
    lines.append("export const RULES = [")
    for rule in RULES:
        lines.append(f"  {{ title: {json.dumps(rule['title'])}, content: {json.dumps(rule['content'])} }},")
    lines.append("];")
    lines.append("")

    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

# ===========================================================================
# MAIN
# ===========================================================================

def main():
    print("Sky Graphics — Leaderboard Sync  (Dynamic Refactor)")
    print("=" * 52)

    # ── Step 1: Parse all three data sources ─────────────────────────────────
    print(f"\n[1/4] Parsing {FORM_REPORT} ...")
    form_per_day, joined_days = parse_form_report(FORM_REPORT)
    # Canonicalize form data
    new_form_per_day = {}
    for name, days in form_per_day.items():
        new_form_per_day[get_canonical_name(name)] = days
    form_per_day = new_form_per_day
    print(f"      People with form data: {len(form_per_day)}")

    print(f"\n[2/4] Parsing {WA_REPORT} ...")
    wa_interactions, pledges = parse_wa_report(WA_REPORT)
    # Canonicalize WA data
    new_wa_interactions = {}
    for name, days in wa_interactions.items():
        new_wa_interactions[get_canonical_name(name)] = days
    wa_interactions = new_wa_interactions
    pledges = {get_canonical_name(p) for p in pledges}
    print(f"      People with WA interaction data: {len(wa_interactions)}")

    print(f"\n[3/4] Parsing {MANUAL_REPORT} ...")
    manual_bonuses = parse_manual_report(MANUAL_REPORT)
    # Canonicalize Manual data
    new_manual_bonuses = {}
    for name, data in manual_bonuses.items():
        new_manual_bonuses[get_canonical_name(name)] = data
    manual_bonuses = new_manual_bonuses
    print(f"      People in manual report: {len(manual_bonuses)}")

    # ── Step 2: Dynamic day + roster discovery ────────────────────────────────
    day_order, all_names = discover_days_and_people(form_per_day, wa_interactions, manual_bonuses, pledges)
    print(f"\n      Discovered days:  {day_order}")
    print(f"      Discovered names: {len(all_names)}")

    # Build DAY_LABELS dynamically (fallback to generic label if not in canonical map)
    day_labels = {d: _CANONICAL_DAY_LABELS.get(d, f"{d} — Programme Day") for d in day_order}

    # ── Step 3: Build PEOPLE records ─────────────────────────────────────────
    print(f"\n[4/4] Building PEOPLE records for {len(all_names)} participants ...")
    all_people = []
    for name in sorted(all_names):
        p = build_person(name, day_order, form_per_day, manual_bonuses, wa_interactions)
        all_people.append(p)

    # Sort by all-time total descending, then name
    all_people.sort(key=lambda x: (-x["allTimeTotal"], x["name"]))

    # ── Step 4: Write outputs ─────────────────────────────────────────────────
    print(f"\n[5/5] Writing outputs ...")

    write_master_data(all_people, day_order, MASTER_OUT)
    print(f"  ✓ {MASTER_OUT}")

    # Strip internal debug keys before exporting to data.js
    export_people = []
    for p in all_people:
        ep = {k: v for k, v in p.items() if not k.startswith("_")}
        export_people.append(ep)

    write_data_js(export_people, day_order, day_labels, DATA_JS_OUT)
    print(f"  ✓ {DATA_JS_OUT}")

    print(f"\nDone.")
    print(f"  {len(all_people)} people in PEOPLE array")
    print(f"  {len(day_order)} days discovered: {', '.join(day_order)}")
    tiers = {}
    for p in all_people:
        tiers[p["tier"]] = tiers.get(p["tier"], 0) + 1
    for tier in ["PLATINUM", "GOLD", "SILVER", "BRONZE", "UNRANKED"]:
        if tier in tiers:
            print(f"  {tier}: {tiers[tier]}")

    print(f"\nNEXT STEP: review {MASTER_OUT} for accuracy,")
    print(f"then push data.js to your GitHub repository.")


if __name__ == "__main__":
    main()
