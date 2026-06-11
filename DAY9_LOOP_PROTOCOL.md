# DAY 9 LOOP PROTOCOL — Sky Graphics Figma Edition 1
# Agent: Gemini CLI | Model: gemini-2.5-pro (DO NOT use Flash Lite or Flash Preview)

---

## OBJECTIVE
Parse today's WhatsApp chat and form data, compute all points for Day 9, produce a
structured points-mapping file, then — ONLY AFTER explicit human confirmation — update
data.js so the leaderboard is fully current for Day 9.

---

## HARD RULES (never break these)
- Do NOT touch data.js until the human types: **"CONFIRMED — update data.js"**
- Do NOT use Flash Lite or Flash Preview. Model must be gemini-2.5-pro.
- Warnings must only contain genuine problems. Never explain positive points in warnings.
- `workStreakDays` must always be ≥ `streakDays` for every participant.
- Anyone with ≥ 5 cumulative points must appear in data.js.
- Participants do not appear on days before their `joinedDay`.
- Every form submission counts as work done. Any creativity score or photo upload counts as work done.
- Both form streak and work streak use freeze-not-reset logic (a freeze day does not break the streak).

---

## LOOP STRUCTURE
Execute phases in order. Complete each phase fully before moving to the next.
If a phase fails or produces uncertain output, re-attempt it before proceeding.
Log every action taken in `Data/Outputs/agent_run_log.md` as you go.

---

## PHASE 1 — REPO CLEANUP & FILE ARRANGEMENT
**Goal:** Confirm the repo is in a clean, correct state before any data work begins.

1. Run `git log --oneline -5` and confirm HEAD is at the correct Day 8 commit
   ("Day 8 Fully Updated Finally" or "Day 8 Fully Updated!!!"). If it is not, STOP
   and report the current HEAD to the human before proceeding.
2. Ensure the following folder structure exists. Create any missing folders:
   ```
   Data/
     Inputs/          ← all raw source files live here
     Outputs/         ← all agent-generated files live here
   ```
3. Confirm these input files are present in `Data/Inputs/`:
   - WhatsApp chat export (.txt)
   - Form data file (form_report.md or equivalent)
   - master_data.md
   - SkyGraphics_PointsMap_v4.pdf (points reference)
4. Write a one-line status to `Data/Outputs/agent_run_log.md`:
   `[PHASE 1 COMPLETE] Repo clean. Files confirmed.`

---

## PHASE 2 — WHATSAPP PARSE: TODAY'S DAY DATA
**Goal:** Extract only Day 9 activity from the WhatsApp chat.

### How to find today's data:
- WhatsApp exports use timestamps in the format: `DD/MM/YYYY, HH:MM - Sender: Message`
- Find the MOST RECENT date that appears in the chat. That is today (Day 9).
- Read downward from the first message on that date.

### Confirmation check:
- The FIRST message on today's date must be from Strength Awa and must contain:
  `"Good morning Originals"` (or similar greeting)
  followed by a second message containing: `"your task for today drops at 10"`
- If you see this, today's section is correctly identified. Log:
  `[PHASE 2 CONFIRMED] WhatsApp anchor message found. Today = [DATE]`
- If you do NOT see this as the first messages, STOP and report what you found instead.

### What to extract:
- Names of everyone who posted their check-in (shared their work/image) today.
- Note any images shared, links posted, or creativity submissions visible in the chat.
- Note anyone who only reacted or commented but did NOT submit work.
- Save extracted data to: `Data/Outputs/wa_day9_parsed.md`

---

## PHASE 3 — FORM DATA PARSE: DAY 9 SUBMISSIONS
**Goal:** Extract form submissions for Day 9 only.

1. Read the form data file from `Data/Inputs/`.
2. Extract all submissions dated today (Day 9).
3. For each submission record:
   - Participant name (map to known name if needed)
   - Number of images submitted
   - Whether images appear unique or are repetitions of each other
4. Save to: `Data/Outputs/form_day9_parsed.md`

---

## PHASE 4 — POINTS CALCULATION
**Goal:** Compute every point delta for every participant for Day 9.

### Known Day 9 point facts (pre-confirmed by Strength):

**Christine Choundong**
- Creativity score (did the video task): ✅ → +5
- Image submitted: 1 unique image → +5 (photo upload bonus)
- Total Day 9 delta: +10

**Crayoni Opal**
- Creativity score (did the video task): ✅ → +5
- Images submitted: 5 total, but only 2 are unique → +2 × 5 = +10 would be the normal
  full bonus, BUT the form script's automatic assignment must be overridden: only 2 images
  were unique, so only 2 × +5 = +10 is awarded (not 5 × +5 = +25).
  **Agent instruction:** The form script will auto-assign +5 per image (5 images = +25).
  You must reduce this to +10 (2 unique images × +5) and log the override.
- Warning to add: "Submitted 5 images but only 2 were unique. All submitted images must be
  different and show distinct work. Repetition does not earn additional points."
- Total Day 9 delta: +15

### For all other participants:
- Cross-reference WhatsApp parse and form parse.
- If no submission found for today → no points added for Day 9.
- Update their streaks accordingly (freeze-not-reset if applicable).

### Quality note (applies to Christine and Crayoni — goes in `roasts` section of data.js):
> "Following the tutorial is great — but build something REAL. The videos show how to
> design actual applications. Basic shapes are not enough. Your work should look like a
> real-world product, not a practice file."

This is a **roast**, not a warning. It belongs in the `roasts` array for both Christine
and Crayoni in data.js.

### Save full points mapping to: `Data/Outputs/day9_points_map.md`

Format each entry as:
```
## [Participant Name]
- Creativity score: +X
- Photo upload: +X (unique images only — override form auto-assignment if images are not all unique)
- Streak status: [active/frozen/broken]
- workStreakDays: X
- streakDays: X
- Day 9 total delta: +X
- Warnings: [list any, or "none"]
- Roasts: [list any, or "none"]
```

---

## PHASE 5 — HUMAN CONFIRMATION GATE
**Goal:** Present the points map and wait for approval before touching data.js.

1. Print the full contents of `Data/Outputs/day9_points_map.md` to the terminal.
2. Print this message exactly:

```
========================================
PHASE 5 — AWAITING CONFIRMATION

The points map above is ready. Please review it carefully.

When you are satisfied, type exactly:
  CONFIRMED — update data.js

To request changes instead, describe what to fix and the loop will revise and
return to this gate.
========================================
```

3. STOP. Do not proceed to Phase 6 until the human types the confirmation string.

---

## PHASE 6 — UPDATE data.js
**Goal:** Apply the confirmed Day 9 points map to data.js.

This phase only runs after the human has typed: **"CONFIRMED — update data.js"**

1. Read the current `data.js` file fully before making any changes.
2. For each participant in the points map:
   - Increment their `points` by their Day 9 delta.
   - Add Day 9 entry to their `dailyPoints` array.
   - Update `streakDays` and `workStreakDays` using freeze-not-reset logic.
   - Append any new warnings to their `warnings` array (genuine problems only).
   - Append any new roasts to their `roasts` array.
   - Do NOT remove existing warnings or roasts.
3. Verify after writing:
   - `workStreakDays >= streakDays` for every participant.
   - No participant appears on a day before their `joinedDay`.
   - All participants with ≥ 5 cumulative points are present.
4. Save updated `data.js`.
5. Log: `[PHASE 6 COMPLETE] data.js updated for Day 9.`

---

## PHASE 7 — FINAL REPORT
**Goal:** Write a complete summary of everything done this run.

Save to: `Data/Outputs/day9_agent_report.md`

Report must include:
1. **Run summary** — date, day number, model used, phases completed.
2. **WhatsApp parse results** — who was active, what was found.
3. **Form parse results** — who submitted, image counts.
4. **Points map** — full copy of day9_points_map.md.
5. **Changes made to data.js** — list every participant modified and what changed.
6. **Warnings added** — list all new warnings and who they belong to.
7. **Roasts added** — list all new roasts and who they belong to.
8. **Anomalies / flags** — anything unusual found during the run that Strength should know.
9. **Status** — COMPLETE or INCOMPLETE (with reason if incomplete).

Then print to terminal:
```
========================================
DAY 9 LOOP COMPLETE
Full report saved to: Data/Outputs/day9_agent_report.md
========================================
```

---

## ERROR HANDLING
- If any input file is missing → log the missing file, skip that data source, and flag it
  in the report. Do not fabricate data.
- If a participant name in WhatsApp or form data does not match a known name in data.js →
  log it as unresolved in `Data/Outputs/unresolved_names_day9.md` and do not assign points
  until resolved.
- If the WhatsApp anchor message is not found → STOP at Phase 2 and report.
- If data.js fails to parse → STOP at Phase 6 and report the error exactly.

---

## OUTPUT FILES SUMMARY
| File | Purpose |
|------|---------|
| `Data/Outputs/agent_run_log.md` | Live log of every action taken |
| `Data/Outputs/wa_day9_parsed.md` | WhatsApp Day 9 extracted data |
| `Data/Outputs/form_day9_parsed.md` | Form Day 9 extracted data |
| `Data/Outputs/day9_points_map.md` | Full points calculation — shown to human for confirmation |
| `Data/Outputs/day9_agent_report.md` | Final report |
| `Data/Outputs/unresolved_names_day9.md` | Any names that could not be matched (if applicable) |

---

*Protocol written for Sky Graphics Figma Edition 1 — Day 9 update cycle.*
