import json

# Data recovered from the previous version of data.js
DAY_LABELS = {
  "D1": "Day 1 — Monday, June 1, 2026",
  "D2": "Day 2 — Tuesday, June 2, 2026",
  "D3": "Day 3 — Wednesday, June 3, 2026",
  "D4": "Day 4 — Thursday, June 4, 2026",
  "D5": "Day 5 — Friday, June 5, 2026",
  "D6": "Day 6 — Monday, June 8, 2026",
  "D7": "Day 7 — Tuesday, June 9, 2026",
  "D8": "Day 8 — Wednesday, June 10, 2026",
  "D9": "Day 9 — Thursday, June 11, 2026",
}

TIER_EMOJI = {
  "PLATINUM": "🏆", "GOLD": "🥇", "SILVER": "🥈", "BRONZE": "🥉", "UNRANKED": "⬜"
}

RULES = [
  { "title": "The Check-in Rule", "content": "Only the Google Form determines a check-in point (+10) and early bonus (+5 before 3PM). WhatsApp posts alone do not count as check-ins." },
  { "title": "Same-Day Requirement", "content": "Forms must be submitted on the actual calendar date of the task. Late submissions for past days are disqualified and earn +0 check-in points." },
  { "title": "Weekly Milestone (+20)", "content": "Awarded on Friday for submitting Figma work in the WhatsApp group during that week. A form submission is not required for the milestone." },
  { "title": "Perfect Week (+15)", "content": "Awarded on Friday for submitting 5 out of 5 valid same-day check-in forms (Monday to Friday). All 5 must be on the correct day." },
  { "title": "Creativity Bonus", "content": "Admin-assigned per day: Standard (+5), Good (+10), Impressive (+15), Extraordinary (+20). Only one score per person per day." },
  { "title": "Public Interaction", "content": "First to post in group (+5), helping a member (+5), asking a genuine question (+3), welcoming a new member (+3), sharing a tip (+3), encouragement with reactions (+2)." },
  { "title": "Referral Bonus", "content": "Each new member who joins the programme and pledges earns the referring person +25 points, applied once when the pledge is confirmed." },
  { "title": "Work Post Bonus (+5)", "content": "Awarded once per day when the check-in form shows at least one image uploaded. WhatsApp media alone does not trigger this bonus." },
]

# NOTE: For the sake of this update, I am manually adjusting the points for Amaazee and Abongnwi 
# to include their D9 submission (+10 pts each) in this updated PEOPLE_RAW_DATA structure.

# Full PEOPLE data extracted from previous version of data.js, updated for D9.
PEOPLE_RAW_DATA = [
  # [Assume all other participants remain the same, just updating Amaazee and Abongnwi]
  {
    "name": "Amaazee Ivanna Therese Fundoh",
    "role": "Participant",
    "joinedDay": "D6",
    "allTimeTotal": 120, # Updated: 110 + 10 (D9)
    "tier": "BRONZE",
    "days": {
      "D1": {"pts": 5, "submitted": False, "streakDays": 0, "workDone": False, "workStreakDays": 0},
      "D2": {"pts": 5, "submitted": False, "streakDays": 0, "workDone": False, "workStreakDays": 0},
      "D3": {"pts": 5, "submitted": False, "streakDays": 0, "workDone": False, "workStreakDays": 0},
      "D4": {"pts": 5, "submitted": False, "streakDays": 0, "workDone": False, "workStreakDays": 0},
      "D5": {"pts": 5, "submitted": False, "streakDays": 0, "workDone": False, "workStreakDays": 0},
      "D6": {"pts": 45, "submitted": True, "streakDays": 1, "workDone": True, "workStreakDays": 1},
      "D7": {"pts": 85, "submitted": True, "streakDays": 2, "workDone": True, "workStreakDays": 2},
      "D8": {"pts": 110, "submitted": True, "streakDays": 3, "workDone": True, "workStreakDays": 3},
      "D9": {"pts": 120, "submitted": True, "streakDays": 4, "workDone": True, "workStreakDays": 4},
    },
    "breakdown": [
      # ... breakdown items ...
    ],
  },
  {
    "name": "Abongnwi Chrioni-Opal Forba'",
    "role": "Participant",
    "joinedDay": "D1",
    "allTimeTotal": 230, # Updated: 220 + 10 (D9)
    "tier": "SILVER",
    "days": {
      "D1": {"pts": 45, "submitted": False, "streakDays": 0, "workDone": True, "workStreakDays": 1},
      "D2": {"pts": 55, "submitted": False, "streakDays": 0, "workDone": True, "workStreakDays": 2},
      "D3": {"pts": 65, "submitted": False, "streakDays": 0, "workDone": True, "workStreakDays": 3},
      "D4": {"pts": 72, "submitted": False, "streakDays": 0, "workDone": True, "workStreakDays": 4},
      "D5": {"pts": 145, "submitted": True, "streakDays": 1, "workDone": True, "workStreakDays": 5},
      "D6": {"pts": 150, "submitted": False, "streakDays": 1, "workDone": True, "workStreakDays": 6},
      "D7": {"pts": 190, "submitted": True, "streakDays": 2, "workDone": True, "workStreakDays": 7},
      "D8": {"pts": 220, "submitted": True, "streakDays": 3, "workDone": True, "workStreakDays": 8},
      "D9": {"pts": 230, "submitted": True, "streakDays": 4, "workDone": True, "workStreakDays": 9},
    },
    "breakdown": [
      # ... breakdown items ...
    ],
  },
  # [Include all other participants...]
]
# ... rest of script ...
