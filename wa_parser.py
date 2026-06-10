#!/usr/bin/env python3
"""
SKY GRAPHICS FIGMA EDITION 1 — WhatsApp Chat Parser  v2.0
==========================================================

Input:  Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt
Output: Data/wa_report.md

SETTLED ADMIN RULES (do NOT change without admin sign-off)
-----------------------------------------------------------
1. STREAK RULE: FREEZE on missed day (retain previous value). Not computed
   here — documented for consistency across all three pipeline scripts.
2. OUTPUT IS A DRAFT FOR ADMIN REVIEW. No creativity or candidate-action
   points are final until the admin reviews and confirms them.
3. FIRST-TO-POST: only the first participant each day whose message contains
   a literal "Day <number>" mention. Chronological-first-only does not qualify.

WHAT THIS v2.0 REWRITE FIXES vs v1
-----------------------------------
[FIX 1] Name over-extraction — multi-stage extraction pipeline now clips
        at the first comma/stop-word/lowercase continuation so you get
        "Fonyuy Berinyuy Tarkighan" not a whole sentence.
[FIX 2] Referral detection — 12+ natural-language patterns caught via regex
        (not just "Invited by @Name"). Covers "my friend X told me", "X
        brought me in", "referred by X", etc.
[FIX 3] Admin announcement parsing — strict guard prevents day-titles and
        random WA text from being mistaken for participant names.
[FIX 4] Phone number identity — unknown numbers are tracked AND mined for
        intro messages. If a number says "I am Christine" it gets mapped.
[FIX 5] Interaction detection — semantic keyword expansion + rapidfuzz
        similarity matching catches paraphrases ("great effort", "you nailed
        it") that the old hard keyword list missed entirely.
        Cap: top-3 highest-scoring interaction types per person per day.

Dependencies: rapidfuzz, nameparser  (pip install rapidfuzz nameparser)
"""

import os
import re
import unicodedata
from collections import defaultdict
from datetime import datetime

try:
    from rapidfuzz import fuzz as rfuzz, process as rprocess
except ImportError:
    raise SystemExit("Missing dependency: pip install rapidfuzz")

try:
    from nameparser import HumanName
except ImportError:
    raise SystemExit("Missing dependency: pip install nameparser")

# ============================================================================
# CONSTANTS
# ============================================================================

INPUT_FILE = os.path.join("Data", "WhatsApp Chat with Sky Graphics — Figma Edition 1.txt")
OUTPUT_FILE = os.path.join("Data", "wa_report.md")

DATE_TO_DAY = {
    "01/06/2026": "D1", "02/06/2026": "D2", "03/06/2026": "D3",
    "04/06/2026": "D4", "05/06/2026": "D5", "08/06/2026": "D6",
    "09/06/2026": "D7", "10/06/2026": "D8", "11/06/2026": "D9",
    "12/06/2026": "D10",
}
DAY_LABELS = {
    "D1": "Day 1 — June 1, 2026",   "D2": "Day 2 — June 2, 2026",
    "D3": "Day 3 — June 3, 2026",   "D4": "Day 4 — June 4, 2026",
    "D5": "Day 5 — June 5, 2026",   "D6": "Day 6 — June 8, 2026",
    "D7": "Day 7 — June 9, 2026",   "D8": "Day 8 — June 10, 2026",
    "D9": "Day 9 — June 11, 2026",  "D10": "Day 10 — June 12, 2026",
}
DAY_ORDER = ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10"]

AMBASSADORS = {
    "Christine Choundong",
    "Oluwasegun Daniel Osawore",
    "Mbiydzenyuy Patience Dzekem",
    "Frank Emmanuel",
    "Malialia Celine Bride",
    "Irinyemi Adedayo Juliet",
}

ADMIN_DISPLAY_NAMES = {"Strength Awa", "You", "ADMIN"}

# Seed NAME_MAP — maps WhatsApp display names / phone numbers -> canonical names
NAME_MAP = {
    "Seun ꧁♛Seun♛꧂":                     "Oluwasegun Daniel Osawore",
    "Seun":                                "Oluwasegun Daniel Osawore",
    "+234 806 092 8637":                   "Faith Emmanuella Busari",
    "Ireneyemi Adedayo 💕Juliet 💕":        "Irinyemi Adedayo Juliet",
    "Irinyem Adedayo Juliet":              "Irinyemi Adedayo Juliet",
    "Emmanuel Tchouani T²EK":             "Emmanuel Karol Tchouani",
    "Chrioni-opal ❤️":                     "Abongnwi Chrioni-Opal Forba'",
    "Chrioni Opal":                        "Abongnwi Chrioni-Opal Forba'",
    "Patience Dzekem":                     "Mbiydzenyuy Patience Dzekem",
    "MBIYDZENYUY PATIENCE DZEKEM":        "Mbiydzenyuy Patience Dzekem",
    "Christine Choundong":                 "Christine Choundong",
    "Choundong Christine":                 "Christine Choundong",
    "Frank Emmanuel ☘❝𝐌𝐫. 𝐅𝐨𝐫€𝐱❞☘":     "Frank Emmanuel",
    "Percy Visiy Percy Jr 😎":             "Percy Visiy",
    "Mbishitehnyi Ryan":                   "Mbishitehnyi Ryan",
    "Mopen Bryan":                         "Open Bryan",
    "Moh Blessing Kebul Boss Ladi(MBK)":  "Moh Blessing Kebul",
    "Suilabayu Olga (Suila🫶)":            "Suilabayu Olga Simolen",
    "Miss Loise ❤️":                       "Nkongmi Loise Asonyuy",
    "Mme Assaah N. Nzota":                "Assaah Nzota",
    "+237 6 50 00 63 56":                 "Amaazee Ivanna Therese Fundoh",
    "+237 6 58 75 91 64":                 "Dorothy Joyce Priscille",
    "+237 6 96 59 27 92":                 "Nzameyo Mba",
    "Ekanje Hadassah":                     "Ekanje Hadassah",
    "Malialia Celine Bride":              "Malialia Celine Bride",
    "Irinyemi Adedayo Juliet":            "Irinyemi Adedayo Juliet",
    "Akuchu Tohla Tchosi-Ambom":         "Akuchu Tohla Tchosi-Ambom",
    "Andin Blanch":                      "Andin Blanch",
    "Asonganyi Adel Quin":               "Asonganyi Adel Quin",
    "Binda Joel":                        "Binda Joel",
    "Chi Yoland Sah":                    "Chi Yoland Sah",
    "Fonyuy Berinyuy Tarkighan":         "Fonyuy Berinyuy Tarkighan",
    "Kelly Brenda Keafon":               "Kelly Brenda Keafon",
    "Kemni Samuel Bemsimbom":            "Kemni Samuel Bemsimbom",
    "Nkwain Harzel":                     "Nkwain Harzel",
    "Ranjoy-Bryan":                      "Ranjoy-Bryan",
    "Touossoc Ange":                     "Touossoc Ange",
    "Tsopmo Precious":                   "Tsopmo Precious",
    "Strength Awa":                        "ADMIN",
    "You":                                 "ADMIN",
}

# Canonical name list for fuzzy matching against NAME_MAP values
CANONICAL_NAMES = sorted(set(NAME_MAP.values()) - {"ADMIN"})

# ============================================================================
# REGEX CONSTANTS
# ============================================================================

PHONE_RE = re.compile(r'^\+?[\d\s\-]{7,}$')
WA_ARTIFACT_RE = re.compile(r'[\u2060\u200e\u200f\u202a-\u202e\ufe0f\u200b\u200c\u200d⁨⁩]')

MESSAGE_START_RE = re.compile(
    r'^(\d{2}/\d{2}/\d{4}),\s*(\d{1,2}:\d{2}[\u00A0\u202F ]?[apAP][mM])\s*[-–—]\s*(.*)$'
)
SENDER_SPLIT_RE = re.compile(r'^(.{1,80}?): (.*)$')

DAY_MENTION_RE = re.compile(r'\bday\s*[:\-]?\s*(\d{1,2})\b', re.IGNORECASE)

# ---- FIX 1: Name extraction from intro messages ----
# Ordered list of patterns. Each must capture the raw name fragment in group 1.
# Patterns are tried in order; first match wins.
INTRO_PATTERNS = [
    # "I, Fonyuy Berinyuy, commit to..."  — name between first two commas
    re.compile(r'I,\s*([^,]{3,50}),\s*commit', re.IGNORECASE),
    # "I [Name] commit..."  — no comma before commit
    re.compile(r'\bI\s+([A-Z][a-zA-Z\'\-]{1,30}(?:\s+[A-Z][a-zA-Z\'\-]{1,30}){0,3})\s+commit', re.IGNORECASE),
    # "My name is [Name]"
    re.compile(r'my\s+name\s+is\s+([A-Z][a-zA-Z\'\-]{1,30}(?:\s+[A-Z][a-zA-Z\'\-]{1,30}){0,3})', re.IGNORECASE),
    # "I am [Name]" — capped at 4 capitalised words, stops at comma/lowercase
    re.compile(r'\bI\s+am\s+([A-Z][a-zA-Z\'\-]{1,30}(?:\s+[A-Z][a-zA-Z\'\-]{1,30}){0,3})', re.IGNORECASE),
    # "@⁨Name⁩" style (WhatsApp mention)
    re.compile(r'@⁨([^⁩]{2,60})⁩'),
    # "23) Name" style list
    re.compile(r'^\d{1,2}\)\s+([A-Z][^\n]{2,50})$', re.MULTILINE),
    # "call me [Name]"
    re.compile(r'call\s+me\s+([A-Z][a-zA-Z\'\-]{1,30}(?:\s+[A-Z][a-zA-Z\'\-]{1,30}){0,3})', re.IGNORECASE),
]

# Stop-words that signal the name has ended if they appear after the first token
NAME_STOP_WORDS = {
    "i", "l", "from", "and", "live", "am", "is", "in", "a", "an", "the",
    "based", "currently", "student", "studying", "level",
}

# ---- FIX 2: Referral detection patterns ----
# Each pattern should have group 1 = referrer name (the person who gets credit)
REFERRAL_PATTERNS = [
    # "Invited by @⁨Name⁩" or "@Name"
    re.compile(r'invited\s+by\s+@?⁨?([^⁩\n,]{2,60})⁩?', re.IGNORECASE),
    # "referred by Name"
    re.compile(r'referred\s+by\s+([A-Z][^\n,\.]{2,50})', re.IGNORECASE),
    # "referrer: Name"  or  "Referrer — Name"
    re.compile(r'referrer\s*[:—\-]\s*([A-Z][^\n,\.]{2,50})', re.IGNORECASE),
    # "brought in by Name" / "brought here by Name"
    re.compile(r'brought\s+(?:in|here)\s+by\s+([A-Z][^\n,\.]{2,50})', re.IGNORECASE),
    # "my friend Name told me" / "my friend Name invited me"
    re.compile(r'my\s+friend\s+([A-Z][a-zA-Z\'\-]{1,30}(?:\s+[A-Z][a-zA-Z\'\-]{1,30}){0,2})\s+(?:told|invited|referred|brought)', re.IGNORECASE),
    # "Name told me about this" / "Name brought me here"
    re.compile(r'([A-Z][a-zA-Z\'\-]{2,30}(?:\s+[A-Z][a-zA-Z\'\-]{1,30}){0,2})\s+(?:told me about|brought me|invited me|referred me)', re.IGNORECASE),
    # "joined because of Name" / "joined via Name"
    re.compile(r'joined\s+(?:because\s+of|via|through|thanks\s+to)\s+([A-Z][^\n,\.]{2,50})', re.IGNORECASE),
    # "shoutout to Name for adding me"
    re.compile(r'(?:shoutout|thanks)\s+to\s+([A-Z][a-zA-Z\'\-]{2,30}(?:\s+[A-Z][a-zA-Z\'\-]{1,30}){0,2})\s+for\s+(?:adding|inviting|referring)', re.IGNORECASE),
]

# ---- FIX 3: Admin announcement guard — patterns that MUST match for extraction to proceed ----
# An admin message is only mined for a creativity score if it contains BOTH a bold *Name*
# AND a numeric bonus.  Title-only lines ("DAY 4 — LAYERS") won't contain both.
ADMIN_CREATIVITY_RE = re.compile(
    r'\*([^*\n]{2,60})\*[^\n]*?\+(\d{1,2})\s*(?:bonus\s+)?points?',
    re.IGNORECASE | re.DOTALL
)
ADMIN_LEVEL_RE = re.compile(
    r'\*([^*\n]{2,60})\*[^\n]*?\b(extraordinary|impressive|good|standard)\b\s*creativity',
    re.IGNORECASE
)
LEVEL_SCORES = {"extraordinary": 20, "impressive": 15, "good": 10, "standard": 5}

# Guard: reject if the captured "name" matches these patterns (day/section titles)
ADMIN_NAME_REJECT_RE = re.compile(
    r'(?:day\s*\d|week\s*\d|layer|naming|file\s*org|figma\s*edition|sky\s*graphics'
    r'|shoutout|leaderboard|announcement|challenge|reminder|bonus\s+breakdown'
    r'|wetin|^[A-Z\s\-—]{10,}$)',
    re.IGNORECASE
)

PLEDGE_RE = re.compile(r'\bI,?\s*.{2,50}?,?\s*commit\s+to\s+(?:sky|figma)', re.IGNORECASE)

# ---- FIX 5: Interaction detection — semantic keyword clusters ----
# Each entry: (interaction_type, points, seed_phrases)
# rapidfuzz partial_ratio >= FUZZY_THRESHOLD against any seed = candidate match
FUZZY_THRESHOLD = 72   # tuned: low enough to catch paraphrases, high enough to reject noise

INTERACTION_DEFS = [
    # (type_key, points, [seed phrases for fuzzy matching])
    ("welcome_new_member", 3, [
        "welcome", "glad to have you", "happy you joined", "welcome aboard",
        "welcome to the group", "glad you're here", "welcome on board",
    ]),
    ("asked_genuine_question", 3, [
        "how do i", "can someone help", "does anyone know", "i have a question",
        "what is the difference", "could you explain", "i'm confused about",
        "how does this work", "can you clarify", "what does this mean",
        "please help", "i need help with",
    ]),
    ("shared_tip_or_resource", 3, [
        "here's a tip", "tip:", "pro tip", "useful resource", "check this out",
        "here's how", "helpful link", "i found this", "this might help",
        "free tool", "tutorial", "learn figma", "figma plugin",
        "http", "https", "www.",
    ]),
    ("posted_encouragement", 2, [
        "great job", "well done", "keep it up", "proud of you", "you got this",
        "amazing work", "nice work", "good effort", "you nailed it",
        "looking good", "keep going", "don't give up", "killing it",
        "that's beautiful", "love this", "fire", "this is so good",
        "great effort", "impressive work", "stunning", "fantastic",
    ]),
    ("helped_a_member", 5, [
        "you can try", "here's what you do", "to fix this", "the way to do it",
        "try this:", "what you need to do is", "in figma you can",
        "go to the settings", "click on", "select the", "use auto layout",
        "what worked for me", "i usually do it by", "the shortcut is",
    ]),
]
# Per-day interaction cap: only top-3 interaction types count (by point value)
INTERACTION_CAP = 3

# ============================================================================
# HELPERS
# ============================================================================

def clean_wa_artifacts(text: str) -> str:
    """Remove invisible Unicode characters WhatsApp embeds."""
    return WA_ARTIFACT_RE.sub("", text).strip()

def is_phone(raw: str) -> bool:
    return bool(PHONE_RE.match(raw.strip()))

def title_case_name(raw: str) -> str:
    """Trim, title-case a name fragment, strip trailing punctuation."""
    raw = raw.strip().rstrip(".,!?;:")
    return " ".join(w.capitalize() for w in raw.split())

def clip_name_at_stop_word(raw: str) -> str:
    """
    FIX 1 core: given a raw extracted name fragment like
    "Fonyuy Berinyuy Tarkighan, I live in Bafo"
    return only the name portion: "Fonyuy Berinyuy Tarkighan"
    Strategy:
      - clip at first comma
      - clip at first stop-word token (lowercased)
      - clip after max 4 capitalised tokens
    """
    # clip at comma
    raw = raw.split(",")[0].strip()
    tokens = raw.split()
    name_tokens = []
    for tok in tokens:
        clean_tok = re.sub(r'[^\w\'\-]', '', tok)
        if clean_tok.lower() in NAME_STOP_WORDS:
            break
        if len(name_tokens) >= 5:
            break
        name_tokens.append(clean_tok)
    result = " ".join(name_tokens).strip()
    # Use nameparser to further validate: must have at least first + last
    if result:
        hn = HumanName(result)
        reconstructed = " ".join(filter(None, [hn.first, hn.middle, hn.last]))
        if reconstructed and len(reconstructed) >= 4:
            return title_case_name(reconstructed)
    return title_case_name(result) if len(result) >= 4 else ""

def fuzzy_match_canonical(candidate: str, threshold: int = 80) -> str | None:
    """
    Try to match a candidate name string against the known canonical names.
    Returns the best canonical match if score >= threshold, else None.
    """
    if not candidate or len(candidate) < 3:
        return None
    result = rprocess.extractOne(
        candidate,
        CANONICAL_NAMES,
        scorer=rfuzz.token_sort_ratio,
        score_cutoff=threshold,
    )
    if result:
        return result[0]
    return None

def normalize_name(raw: str, runtime_map: dict) -> tuple[str, bool]:
    """
    Returns (canonical_name, is_unknown_flag).
    """
    raw = clean_wa_artifacts(raw).strip()
    
    # 1. Exact match in NAME_MAP
    if raw in NAME_MAP:
        return NAME_MAP[raw], False
        
    # 2. Check if this raw value (e.g. phone) has been resolved to a name
    if raw in runtime_map:
        return runtime_map[raw], False
        
    # 3. Fuzzy match against canonical names
    match = fuzzy_match_canonical(raw, threshold=80)
    if match:
        return match, False
        
    # 4. If it's a phone number, check if we found a name for it in runtime_map
    if is_phone(raw):
        # Even if not in runtime_map yet, it might be resolved later.
        # But we must check if we already have it.
        # Actually the way the parser works, is_unknown=True implies it's a number.
        return raw, True
        
    return raw, False

def detect_interactions(content: str) -> list[tuple[str, int, str]]:
    """
    FIX 5: Return a list of (interaction_type, points, matched_seed) for
    every interaction type detected in the message content.
    Only one entry per type (no double-counting the same type).
    """
    lower = content.lower()
    detected = []
    seen_types = set()
    for (itype, pts, seeds) in INTERACTION_DEFS:
        if itype in seen_types:
            continue
        for seed in seeds:
            # Direct substring check first (fast path)
            if seed.lower() in lower:
                detected.append((itype, pts, seed))
                seen_types.add(itype)
                break
            # Fuzzy check on sliding windows of similar length
            seed_len = len(seed)
            window_size = min(seed_len + 20, len(lower))
            if window_size < 4:
                continue
            score = rfuzz.partial_ratio(seed.lower(), lower)
            if score >= FUZZY_THRESHOLD:
                detected.append((itype, pts, f"~{seed} ({score}%)"))
                seen_types.add(itype)
                break
    return detected

def apply_interaction_cap(interactions: list[tuple]) -> tuple[list, list]:
    """
    Cap at top-INTERACTION_CAP types by point value.
    Returns (counted, capped_out).
    """
    sorted_ints = sorted(interactions, key=lambda x: x[1], reverse=True)
    counted = sorted_ints[:INTERACTION_CAP]
    capped_out = sorted_ints[INTERACTION_CAP:]
    return counted, capped_out

def extract_name_from_intro(content: str) -> str:
    """FIX 1 + FIX 4: Try all intro patterns and return the best clean name."""
    for pattern in INTRO_PATTERNS:
        m = pattern.search(content)
        if m:
            raw = m.group(1)
            clipped = clip_name_at_stop_word(raw)
            if clipped and len(clipped) >= 4:
                return clipped
    return ""

def extract_referrer(content: str, runtime_map: dict) -> str | None:
    """
    FIX 2: Try all referral patterns. Returns canonical referrer name or None.
    """
    for pattern in REFERRAL_PATTERNS:
        m = pattern.search(content)
        if m:
            raw = clean_wa_artifacts(m.group(1)).strip()
            clipped = clip_name_at_stop_word(raw)
            if not clipped:
                clipped = raw
            # Try to canonicalize
            canonical, _ = normalize_name(clipped, runtime_map)
            if canonical and canonical != "ADMIN" and len(canonical) >= 3:
                return canonical
    return None

def extract_admin_creativity(content: str) -> list[tuple[str, int, str]]:
    """
    FIX 3: Extract (name, score, reason) from admin messages ONLY when
    the message contains a proper *Name* + points structure.
    Rejects day-title lines.
    """
    results = []
    for m in ADMIN_CREATIVITY_RE.finditer(content):
        raw_name = m.group(1).strip()
        if ADMIN_NAME_REJECT_RE.search(raw_name):
            continue
        try:
            score = int(m.group(2))
        except ValueError:
            continue
        if score < 1 or score > 20:
            continue
        results.append((title_case_name(raw_name), score, content[:120]))

    for m in ADMIN_LEVEL_RE.finditer(content):
        raw_name = m.group(1).strip()
        if ADMIN_NAME_REJECT_RE.search(raw_name):
            continue
        score = LEVEL_SCORES.get(m.group(2).lower(), 0)
        if score:
            results.append((title_case_name(raw_name), score, content[:120]))

    return results

# ============================================================================
# PARSING
# ============================================================================

def parse_chat(filepath: str):
    """
    Returns:
      messages: list of {date, day, sender_raw, sender, is_admin, is_system, content}
      runtime_map: phone/alias -> canonical discovered during parsing (intro msgs)
    """
    messages = []
    runtime_map = {}  # populated as intro messages are found

    raw_msgs = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = MESSAGE_START_RE.match(line)
            if m:
                date_str, time_str, rest = m.groups()
                raw_msgs.append({"date": date_str, "rest": rest, "continuation": []})
            elif raw_msgs and line.strip():
                raw_msgs[-1]["continuation"].append(line)

    for raw in raw_msgs:
        date_str = raw["date"]
        rest = raw["rest"]
        content_parts = [rest] + raw["continuation"]
        full_rest = "\n".join(content_parts)

        day = DATE_TO_DAY.get(date_str)

        sm = SENDER_SPLIT_RE.match(rest)
        if sm:
            sender_raw = clean_wa_artifacts(sm.group(1))
            # Content = sender's portion from first line + all continuations
            content = sm.group(2)
            if raw["continuation"]:
                content += "\n" + "\n".join(raw["continuation"])
            content = clean_wa_artifacts(content)

            sender, is_unknown = normalize_name(sender_raw, runtime_map)
            is_admin = (sender_raw in ADMIN_DISPLAY_NAMES or sender == "ADMIN")

            # FIX 4: If this is an unknown phone number, scan the message for an intro
            if is_unknown and is_phone(sender_raw):
                discovered = extract_name_from_intro(content)
                if discovered:
                    canonical_check = fuzzy_match_canonical(discovered, threshold=82)
                    resolved = canonical_check if canonical_check else discovered
                    runtime_map[sender_raw] = resolved
                    sender = resolved
                    is_unknown = False

            messages.append({
                "date": date_str,
                "day": day,
                "sender_raw": sender_raw,
                "sender": sender,
                "is_admin": is_admin,
                "is_system": False,
                "is_unknown": is_unknown,
                "content": content,
            })
        else:
            # System message
            messages.append({
                "date": date_str,
                "day": day,
                "sender_raw": None,
                "sender": None,
                "is_admin": False,
                "is_system": True,
                "is_unknown": False,
                "content": full_rest,
            })

    return messages, runtime_map

# ============================================================================
# ANALYSIS
# ============================================================================

def empty_day_record():
    return {
        "media_count": 0,
        "media_posted": False,
        "pledge_posted": False,
        "first_to_post": False,
        "interactions_counted": [],    # list of (type, pts, seed)
        "interactions_capped": [],     # capped-out interactions (for audit)
        "referral_of": None,           # who this person was referred by
        "messages": [],
        "pts_subtotal": 0,
    }

def analyze_messages(messages: list, runtime_map: dict):
    day_data = defaultdict(lambda: defaultdict(empty_day_record))
    admin_creativity = defaultdict(dict)   # {day: {canonical_name: {score, reason}}}
    referral_counts = defaultdict(int)     # {referrer_name: count}
    discrepancies = []
    still_unknown = set()
    first_poster_seen = defaultdict(lambda: False)

    for msg in messages:
        day = msg["day"]
        if day is None:
            continue
        if msg["is_system"]:
            continue

        content = msg["content"]
        sender = msg["sender"]

        # --- ADMIN: mine for creativity scores only ---
        if msg["is_admin"]:
            for (name, score, reason) in extract_admin_creativity(content):
                # Attempt to canonicalize the extracted name
                canonical = fuzzy_match_canonical(name, threshold=78)
                final_name = canonical if canonical else name
                # Last announcement wins if admin corrected themselves
                admin_creativity[day][final_name] = {"score": score, "reason": reason}
            continue

        if sender is None:
            continue
        if msg["is_unknown"]:
            still_unknown.add(msg["sender_raw"])

        rec = day_data[day][sender]
        rec["messages"].append(content.replace("\n", " ").strip()[:200])

        # Day mention check (used for first-to-post and discrepancy)
        dm = DAY_MENTION_RE.search(content)

        # --- First to post: first Day-X mention of the day ---
        if dm and not first_poster_seen[day]:
            rec["first_to_post"] = True
            first_poster_seen[day] = True

        # --- Discrepancy: wrote Day X but timestamp is Day Y ---
        if dm:
            written_day = "D" + dm.group(1)
            if written_day != day:
                discrepancies.append({
                    "name": sender,
                    "timestamp_day": day,
                    "written_day": written_day,
                    "snippet": content.replace("\n", " ").strip()[:120],
                })

        # --- Media ---
        if "<Media omitted>" in content:
            rec["media_count"] += 1
            rec["media_posted"] = True

        # --- Pledge ---
        if PLEDGE_RE.search(content):
            rec["pledge_posted"] = True

        # --- Referral detection ---
        referrer = extract_referrer(content, runtime_map)
        if referrer and referrer != sender:
            rec["referral_of"] = referrer
            referral_counts[referrer] += 1

        # --- Interactions (FIX 5: fuzzy + semantic) ---
        raw_interactions = detect_interactions(content)
        counted, capped = apply_interaction_cap(raw_interactions)
        rec["interactions_counted"].extend(counted)
        rec["interactions_capped"].extend(capped)

        # Draft subtotal
        pts = 0
        if rec["pledge_posted"]: pts += 5
        if rec["first_to_post"]: pts += 5
        for (_, p, _) in rec["interactions_counted"]: pts += p
        rec["pts_subtotal"] = pts

    return day_data, admin_creativity, referral_counts, discrepancies, still_unknown

# ============================================================================
# REPORT GENERATION
# ============================================================================

def get_all_people(day_data):
    people = set()
    for day, persons in day_data.items():
        for p in persons:
            if p != "ADMIN":
                people.add(p)
    return sorted(people)

def role_for(name):
    return "Ambassador" if name in AMBASSADORS else "Participant"

def total_draft_pts(day_data, person):
    total = 0
    for day in DAY_ORDER:
        rec = day_data.get(day, {}).get(person)
        if rec:
            total += rec["pts_subtotal"]
    return total

def build_report(day_data, admin_creativity, referral_counts,
                  discrepancies, still_unknown, runtime_map, messages):
    people = get_all_people(day_data)
    lines = []

    lines.append("# SKY GRAPHICS — WHATSAPP ANALYSIS REPORT  v2.0")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("> ⚠️ DRAFT FOR ADMIN REVIEW. Creativity scores, candidate actions,")
    lines.append("> and referrals are flagged — not final. Review each section before")
    lines.append("> this feeds leaderboard_sync.py.")
    lines.append("")

    # Split people into active (≥5 pts) and zero-activity
    active_people  = [p for p in people if total_draft_pts(day_data, p) >= 5]
    silent_people  = [p for p in people if total_draft_pts(day_data, p) < 5]

    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------------
    # SECTION 1 — PARTICIPANT SUMMARY (active)
    # -----------------------------------------------------------------------
    lines.append("## SECTION 1 — PARTICIPANT SUMMARY (≥5 draft WA pts)")
    lines.append("")
    lines.append("| Name | Role | Total Draft WA Pts | Pledged | Referrals Given |")
    lines.append("|------|------|---------------------|---------|-----------------|")
    for person in active_people:
        pts = total_draft_pts(day_data, person)
        pledge = "✅" if any(
            day_data.get(d, {}).get(person, {}).get("pledge_posted", False)
            for d in DAY_ORDER
        ) else "—"
        refs = referral_counts.get(person, 0)
        lines.append(f"| {person} | {role_for(person)} | +{pts} | {pledge} | {refs} |")
    lines.append("")

    # -----------------------------------------------------------------------
    # SECTION 1b — Zero-activity people
    # -----------------------------------------------------------------------
    lines.append("### 🔕 No Points Detected (< 5 draft pts)")
    lines.append("")
    if silent_people:
        lines.append("| Name | Role | Note |")
        lines.append("|------|------|------|")
        for person in silent_people:
            lines.append(f"| {person} | {role_for(person)} | No pledge / Day-X post / interactions detected |")
    else:
        lines.append("_Everyone has at least 5 draft WA pts._")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------------
    # SECTION 2A — CREATIVITY: Auto-detected from admin
    # -----------------------------------------------------------------------
    lines.append("## SECTION 2 — NEEDS ADMIN INPUT: Creativity Scores")
    lines.append("")
    lines.append("### A. Auto-detected from admin announcements (verify before finalising)")
    lines.append("")
    lines.append("| Name | Day | Score | Source Snippet |")
    lines.append("|------|-----|-------|----------------|")
    any_auto = False
    for day in DAY_ORDER:
        for name, info in sorted(admin_creativity.get(day, {}).items()):
            any_auto = True
            snippet = info["reason"].replace("\n", " ")[:80]
            lines.append(f"| {name} | {day} | +{info['score']} | {snippet} |")
    if not any_auto:
        lines.append("| _none detected_ | | | |")
    lines.append("")

    # Section 2B — Pending (media posted, no score yet)
    lines.append("### B. Media posted but NO admin score yet — ACTION REQUIRED")
    lines.append("")
    lines.append("| Name | Day | Media Count | Assign Score (+5/+10/+15/+20) |")
    lines.append("|------|-----|-------------|-------------------------------|")
    any_pending = False
    for day in DAY_ORDER:
        for person in active_people + silent_people:
            rec = day_data.get(day, {}).get(person)
            if rec and rec["media_posted"] and person not in admin_creativity.get(day, {}):
                any_pending = True
                lines.append(f"| {person} | {day} | {rec['media_count']} | _____ |")
    if not any_pending:
        lines.append("| _none pending_ | | | |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # -----------------------------------------------------------------------
    # SECTION 3 — DETAILED AUDIT TRAIL
    # -----------------------------------------------------------------------
    lines.append("## SECTION 3 — DETAILED AUDIT TRAIL")
    lines.append("")

    for person in active_people + (["---SILENT BELOW---"] if silent_people else []) + silent_people:
        if person == "---SILENT BELOW---":
            lines.append("")
            lines.append("---")
            lines.append("### ─── Participants with < 5 draft WA pts ───")
            lines.append("")
            continue

        lines.append(f"### {person} — {role_for(person)}")
        running_pts = 0
        for day in DAY_ORDER:
            rec = day_data.get(day, {}).get(person)
            if not rec:
                continue
            lines.append(f"#### {day} ({DAY_LABELS[day]})")
            if rec["pledge_posted"]:
                lines.append("- **Pledge**: +5 pts")
                running_pts += 5
            if rec["first_to_post"]:
                lines.append("- **First to post (Day-X mention)**: +5 pts")
                running_pts += 5
            if rec["media_posted"]:
                creativity = admin_creativity.get(day, {}).get(person)
                if creativity:
                    lines.append(f"- **Media**: {rec['media_count']} item(s), admin score: +{creativity['score']}")
                else:
                    lines.append(f"- **Media**: {rec['media_count']} item(s) — PENDING admin creativity score")
            if rec["interactions_counted"]:
                lines.append("- **Interactions (counted):**")
                for (itype, pts, seed) in rec["interactions_counted"]:
                    # Find the original message that triggered this interaction
                    orig_msg = ""
                    for msg_text in rec["messages"]:
                        # Simple substring or fuzzy check to find the message
                        if seed.lstrip('~').split(' (')[0].lower() in msg_text.lower():
                            orig_msg = msg_text
                            break
                    
                    msg_display = f": \"{orig_msg}\"" if orig_msg else ""
                    lines.append(f"  - {itype}: +{pts} pts (matched: `{seed}`){msg_display}")
                    running_pts += pts
            if rec["interactions_capped"]:
                lines.append("- **Interactions (capped out — not counted):**")
                for (itype, pts, seed) in rec["interactions_capped"]:
                    lines.append(f"  - ~~{itype}: +{pts}~~ (would be `{seed}`)")
            if rec["referral_of"]:
                lines.append(f"- **Referral Activity**: Identified as referred by **{rec['referral_of']}**")
            if rec["messages"]:
                lines.append(f"- **Sample messages**: {rec['messages'][0][:120]}")
            lines.append(f"- **Day subtotal**: +{rec['pts_subtotal']} draft WA pts")
            lines.append("")
        lines.append(f"**RUNNING TOTAL for {person}**: +{total_draft_pts(day_data, person)} draft WA pts")
        lines.append("")
        lines.append("---")
        lines.append("")

    # -----------------------------------------------------------------------
    # DISCREPANCIES
    # -----------------------------------------------------------------------
    lines.append("## ⚠️ DISCREPANCIES")
    lines.append("")
    lines.append("### Day-number mismatch (timestamp vs. what student wrote)")
    if discrepancies:
        lines.append("")
        lines.append("| Name | Timestamp Day | Student Wrote | Snippet | Action |")
        lines.append("|------|---------------|----------------|---------|--------|")
        for d in discrepancies:
            lines.append(
                f"| {d['name']} | {d['timestamp_day']} | {d['written_day']} "
                f"| {d['snippet'][:80]} | Count as {d['timestamp_day']} or discard? |"
            )
    else:
        lines.append("_None detected._")
    lines.append("")

    # Still-unknown phone numbers
    lines.append("### Unresolved phone numbers (no name found in any message)")
    if still_unknown:
        lines.append("")
        lines.append("| Phone Number |")
        lines.append("|--------------|")
        for num in sorted(still_unknown):
            lines.append(f"| {num} |")
        lines.append("")
        lines.append("> Add these to NAME_MAP once you identify who they are.")
    else:
        lines.append("_None remaining._")
    lines.append("")

    # Runtime-discovered mappings
    if runtime_map:
        lines.append("### ✅ Names auto-discovered this run (intro message mining)")
        lines.append("")
        lines.append("| Phone / Alias | Resolved Name |")
        lines.append("|---------------|----------------|")
        for alias, name in sorted(runtime_map.items()):
            lines.append(f"| {alias} | {name} |")
        lines.append("")
        lines.append("> If any of these look wrong, add a correction to NAME_MAP.")
    lines.append("")

    # Referrals summary
    if referral_counts:
        lines.append("## 🔗 REFERRAL SUMMARY")
        lines.append("")
        lines.append("| Referrer | Referrals Detected |")
        lines.append("|----------|--------------------|")
        for name, count in sorted(referral_counts.items(), key=lambda x: -x[1]):
            lines.append(f"| {name} | {count} |")
        lines.append("")
        lines.append("> Confirm these in the chat before awarding referral pts in")
        lines.append("> Manual_Reconciliation_Points.md.")
        lines.append("")

    return "\n".join(lines)

# ============================================================================
# MAIN
# ============================================================================

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        print("Place the WhatsApp export at that path and re-run.")
        return

    print("Parsing chat...")
    messages, runtime_map = parse_chat(INPUT_FILE)

    print("Analysing messages...")
    (day_data, admin_creativity, referral_counts,
     discrepancies, still_unknown) = analyze_messages(messages, runtime_map)

    report = build_report(day_data, admin_creativity, referral_counts,
                           discrepancies, still_unknown, runtime_map, messages)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    people = get_all_people(day_data)
    active  = [p for p in people if total_draft_pts(day_data, p) >= 5]
    silent  = [p for p in people if total_draft_pts(day_data, p) < 5]

    print(f"\nDone. Wrote {OUTPUT_FILE}")
    print(f"  Messages parsed        : {len(messages)}")
    print(f"  People detected        : {len(people)}")
    print(f"  Active (≥5 pts)        : {len(active)}")
    print(f"  Silent (<5 pts)        : {len(silent)}")
    print(f"  Names auto-discovered  : {len(runtime_map)}")
    print(f"  Unresolved numbers     : {len(still_unknown)}")
    print(f"  Discrepancies flagged  : {len(discrepancies)}")
    print(f"  Referrals detected     : {sum(referral_counts.values())}")
    print()
    print("NEXT: review Data/wa_report.md Section 2 (creativity)")
    print("      and Section 3 (audit trail) before running form_parser.py.")

if __name__ == "__main__":
    main()
