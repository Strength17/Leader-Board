# LOOP PROTOCOL — Roast & Warnings Deep Update
# Sky Graphics Figma Edition 1 — Autonomous Agent Task

You are running an autonomous loop. You do not stop, you do not ask for confirmation, and you do not wait for input at any stage. You run until all completion criteria are met, then you commit and push. Read every word of this prompt before executing a single command.

---

## REPOSITORY STRUCTURE — KNOW THIS BEFORE YOU TOUCH ANYTHING

```
├── data.js                        ← YOU WILL UPDATE THIS
├── index.html
├── script.js
├── style.css
├── MASTER DATA.md                 ← Finalized audit trail (project root)
├── leaderboard_sync.py
├── wa_parser.py
├── form_parser.py
├── WORKFLOW.md
├── Data/
│   ├── WhatsApp Chat with Sky Graphics — Figma Edition 1.txt   ← FOUNDATIONAL SOURCE 1
│   ├── Form Data.txt                                           ← FOUNDATIONAL SOURCE 2
│   ├── wa_report.md               ← Parsed from Foundational Source 1
│   ├── form_report.md             ← Parsed from Foundational Source 2
│   ├── Manual_Reconciliation_Points.md
│   └── Full_Leaderboard_Data.md   ← Finalized aggregated point data
└── Identity_Management/
    └── Data/
        ├── unique_full_names.md   ← MASTER REGISTRY — all canonical names
        └── resolved_names.md     ← Name variation → canonical name mapping
```

**Read order (strictly follow this):**
1. `Identity_Management/Data/unique_full_names.md` — establishes who exists canonically
2. `Identity_Management/Data/resolved_names.md` — maps every name variant to canonical
3. `Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt` — raw WhatsApp truth
4. `Data/Form Data.txt` — raw form submission truth
5. `Data/wa_report.md` — parsed WhatsApp activity (derived from source 1)
6. `Data/form_report.md` — parsed form data (derived from source 2)
7. `Data/Manual_Reconciliation_Points.md` — admin overrides and confirmed manual points
8. `Data/Full_Leaderboard_Data.md` — finalized aggregated point data
9. `MASTER DATA.md` — audit trail and discrepancy log (project root)
10. `data.js` — current leaderboard data (what you will update)

**Name resolution rule:** Any name found in any source file must be resolved to its canonical form using `resolved_names.md` before being matched to a person in `data.js`. If a raw name cannot be resolved, check `unique_full_names.md` directly. Never process an unresolved name variant as a new person.

---

## WHAT YOU ARE DOING

For every person currently in `data.js` — active or inactive — you will:

1. Pull their complete activity record from the foundational sources and all derived files, resolving their name canonically at every step.
2. Compute the exact points they MISSED across all days D1–D7, broken down by category.
3. Write a **roast** that is brutally specific to their actual data — not generic. It must reference their actual day numbers, actual point gaps, actual missed opportunities. The roast should make them feel the cost of what they left on the table and fire them up to not repeat it in the remaining days.
4. Write **at least one warning** (two where possible) specific to their actual record — disqualifications, missed categories, streak breaks, inactive days, Facebook slots unused, WhatsApp interactions they could have claimed.

Every single person on the board gets a roast and at least one warning. No exceptions. Active people get warned about what they are still doing wrong. Inactive people get warned about what they have permanently lost and what is still recoverable.

You are NOT writing generic encouragement. You are writing specific, data-backed content that uses real numbers from their actual record.

---

## STEP 0 — IDENTITY RESOLUTION (run before anything else)

Before computing a single point or writing a single word:

1. Read `Identity_Management/Data/unique_full_names.md` and build your canonical name list.
2. Read `Identity_Management/Data/resolved_names.md` and build your name-variant-to-canonical mapping.
3. For every person in `data.js`, confirm their name exists in `unique_full_names.md`. If a name in `data.js` does not appear in the registry, flag it in your working log but do not skip that person — use their `data.js` name as canonical for this run.
4. When reading any raw source (WhatsApp txt, Form Data txt, wa_report, form_report, Manual_Reconciliation), always resolve names through the mapping before matching to a person record.

---

## MISSED POINTS COMPUTATION — DO THIS FOR EVERY PERSON

For each person, for each day D1 through D7, compute what they could have earned vs what they actually earned. Use `Data/form_report.md` as the primary source for form data and `Data/Full_Leaderboard_Data.md` as the confirmed aggregated total. Cross-reference against the raw `Data/Form Data.txt` for any discrepancy. Track these categories:

**Category A — Form points (automatic)**
- Check-in form not submitted on a live day: −10 pts missed
- No early submission (before 3PM) on days they DID submit: −5 pts missed per day

**Category B — Work post bonus**
- Form submitted but image_count = 0: −5 pts missed (no work post uploaded)
- Available form image slots not used: note wasted slots (up to 5 slots × +5 each = +25 max per day)

**Category C — Facebook interaction**
- No Facebook Heart + Comment + Share screenshot: −10 pts per submitted day (forfeited on top of base image upload)
- No group share screenshot: −5 pts per submitted day
- Per the points map, max +55 pts per day from 5 slots in priority order. Compute how far below that maximum they were on every day they submitted.

**Category D — WhatsApp interactions**
- Use `Data/wa_report.md` candidate flags AND confirm against `Data/Manual_Reconciliation_Points.md`.
- Flag days they were active in the WhatsApp group (had messages in `Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt`) but earned zero interaction points.
- Specifically: first-to-post (+5), helped someone (+5), asked a genuine question (+3), welcomed a member (+3), shared a tip (+3).

**Category E — Streak breaks**
- Any day the form streak was broken: name the day, name the cost.
- If a Perfect Week (+15) was missed due to one specific missing form: state which day broke it.

**Category F — Milestone and bonus gaps**
- Weekly Milestone (+20): earned or not for Week 1? If not, why?
- Perfect Week (+15): earned or not? Which day broke it?
- Referral bonus: if zero referrals, state that each referral = +25 pts.

Then compute:
```
total_missed   = sum of all missed points across all categories
still_available = points earnable in remaining live days (D8, D9, D10)
```

Store this per person before writing any roast or warning.

---

## ROAST WRITING RULES

The roast must:

1. Open by addressing the person by **first name only**.
2. In the first or second sentence, state their **current total and current tier** — factual, no padding.
3. Reference **specific days** where they dropped the ball. Use actual day numbers (D1, D3, etc.) and actual point values.
4. Calculate and state the **total points left on the table** across the whole tracked period. Make it a number. The phrase "You left X points on the table" or equivalent is required.
5. Name the **single biggest missed category** — the one area where they lost the most points.
6. If inactive (zero form submissions, zero work scored): state directly what they would have at minimum if they had just shown up every day. Use math.
7. Close with one sharp, forward-looking sentence about the remaining days. No softness.

**Tone reference — match this energy:**
> "You showed up on D5 and D6 only. The first four days happened without you. That's 40 check-in points, 20 points in early bonuses, and 4 chances at creativity scores — gone. You left at least 80 points on the table before you even opened Figma."

> "Zero forms. Zero work scored. You are on the board for your pledge alone. If you had submitted every day this week you'd be in Silver right now with a perfect week bonus. That's not motivation — that's math."

> "You got the form streak right but you have never uploaded a Facebook screenshot once. That's +10 per day in dead money. Over 7 days that's 70 points you didn't pick up. Read the points map."

Roast strings are HTML. Use `<p>` tags for paragraphs. Escape any apostrophes or backticks correctly for a JavaScript template literal.

---

## WARNING WRITING RULES

Each warning must:

1. Have a **short title in ALL CAPS** followed by a colon and a brief summary on the same line.
   Example: `"MISSED PERFECT WEEK — D5 COST YOU +15: Your D5 form was submitted with the wrong day written..."`
2. Have a body that explains exactly what happened, which day, which rule, and how many points were affected.
3. For inactive people: state specifically what is still recoverable and what is permanently gone.
4. There is always something to warn about. If their record is clean in one area, find the area where they are leaving points on the table. Facebook slots are almost always unused. Referrals are almost always zero. Early submission bonus is almost always missed.

**Warning format in data.js:**
```javascript
warnings: [
  "MISSED PERFECT WEEK — D5 DISQUALIFIED: Your D5 form was submitted with the wrong day written. Check-in points stripped (+0). This also cost you the Perfect Week bonus (+15). Do not write the wrong day on the form. This was 25 points in one mistake.",
  "FACEBOOK SLOTS UNUSED — 0 OF 5 SLOTS USED: You have never uploaded a Facebook screenshot. Heart+Comment+Share = +15 per screenshot. Five full slots = +55 pts per submitted day. That is the highest-value single action available to you and you have not used it once."
]
```

---

## THE LOOP

Run this loop. Do not exit until all completion checks pass.

```
LOOP START

  ── STEP 1: READ ALL DATA SOURCES ───────────────────────────────────────
  Read in order:
    Identity_Management/Data/unique_full_names.md
    Identity_Management/Data/resolved_names.md
    Data/WhatsApp Chat with Sky Graphics — Figma Edition 1.txt
    Data/Form Data.txt
    Data/wa_report.md
    Data/form_report.md
    Data/Manual_Reconciliation_Points.md
    Data/Full_Leaderboard_Data.md
    MASTER DATA.md
    data.js

  Resolve all names through Identity_Management before building person records.
  Print: "STEP 1 COMPLETE — {N} canonical persons identified"

  ── STEP 2: COMPUTE MISSED POINTS ───────────────────────────────────────
  For every person in data.js:
    Run the missed points computation (Categories A–F above).
    Store: { name, total_missed, breakdown_by_category, still_available }
  Print per person: "{name}: missed {X} pts | still available: {Y} pts"
  Print: "STEP 2 COMPLETE"

  ── STEP 3: WRITE ROASTS ────────────────────────────────────────────────
  For every person, generate the roast using the rules above.
  Write to internal working object — do not touch data.js yet.
  Print: "STEP 3 COMPLETE — {N} roasts drafted"

  ── STEP 4: WRITE WARNINGS ──────────────────────────────────────────────
  For every person, generate minimum 1 warning (2 if possible).
  Write to internal working object — do not touch data.js yet.
  Print: "STEP 4 COMPLETE — {N} warnings drafted"

  ── STEP 5: QUALITY CHECK (automated, no human input) ───────────────────
  For each person verify ALL of the following:

    ROAST CHECKS:
    [ ] Contains at least one specific day reference (D1/D2/.../D7)
    [ ] Contains at least one specific point value (e.g. "+15", "80 pts")
    [ ] Contains the phrase "left X points on the table" or numeric equivalent
    [ ] Opens with first name only
    [ ] Does NOT contain the phrase "keep it up" or "great job" or "well done" 
        or any unearned praise

    WARNING CHECKS:
    [ ] At least 1 warning exists for this person
    [ ] Each warning title is ALL CAPS
    [ ] Each warning body references a specific rule name or point category
    [ ] Each warning references a specific day or point value

    UNIQUENESS CHECK:
    [ ] This person's roast is not more than 40% similar to any other person's roast
        (compare key phrases — if overlap detected, rewrite the failing one)

  If ANY person fails ANY check:
    → Go back to STEP 3 for that person only
    → Rewrite roast and/or warnings for that person
    → Re-run STEP 5 checks for that person only
    → Repeat until they pass
  Print: "STEP 5 COMPLETE — all {N} persons passed quality checks"

  ── STEP 6: UPDATE data.js ──────────────────────────────────────────────
  Write the updated roast and warnings into data.js for every person.
  Rules:
    - Only modify the `roast` and `warnings` fields on each person object
    - Do NOT modify pts, days, allTimeTotal, tier, streakDays, workStreakDays,
      submitted, workDone, breakdown, role, or joinedDay
    - Do NOT remove existing warnings — if a person already has warnings,
      append new ones (deduplicate by title prefix)
    - Do NOT create new person objects
  
  After writing, validate the file is valid JavaScript:
    Run: node --input-type=module --eval "import('./data.js').then(()=>console.log('VALID')).catch(e=>console.error('INVALID:',e.message))"
    
    If output is VALID → proceed to STEP 7
    If output is INVALID → fix the specific syntax error, re-validate
    Repeat until VALID
  
  Print: "STEP 6 COMPLETE — data.js updated and validated"

  ── STEP 7: COMMIT AND PUSH ─────────────────────────────────────────────
  a. Read last commit message:
       git log -1 --format="%s"
     Store as LAST_MSG

  b. Build new commit message:
       NEW_MSG = "{LAST_MSG} / ROAST+WARNINGS DEEP UPDATE — {N} persons, data-specific"
     where {N} = total persons updated

  c. Stage:
       git add data.js

  d. Commit:
       git commit -m "{NEW_MSG}"

  e. Push:
       git push
     If push fails: retry up to 3 times with 5-second gaps between attempts.
     If all 3 fail: print "PUSH FAILED — manual push required. data.js updated locally."
     then HALT.

  f. Confirm push:
       git log -1 --format="%H %s"
     Print: "PUSHED: {commit hash} — {commit message}"

  ── STEP 8: FINAL VERIFICATION ──────────────────────────────────────────
  Run: git log -1 --format="%H %s"
  Confirm the hash matches what was printed in Step 7f.
  Print: "LOOP COMPLETE. Commit {hash} is live. {N} persons updated. data.js pushed."

LOOP END
```

---

## PEOPLE TO PROCESS

Everyone currently in `data.js`. Verify each against `Identity_Management/Data/unique_full_names.md`. Known roster as of last state:

- Christine Choundong (Ambassador)
- Oluwasegun Daniel Osawore (Ambassador)
- Emmanuel Karol Tchouani (Participant)
- Mbiydzenyuy Patience Dzekem (Ambassador)
- Asonganyi Adel Quin (Participant)
- Amaazee Ivanna Therese Fundoh (Participant)
- Frank Emmanuel (Ambassador)
- Faith Emmanuella Busari (Participant)
- Abongnwi Chrioni-Opal Forba' (Participant)
- Irinyemi Adedayo Juliet (Ambassador)
- Dorothy Joyce Priscille (Participant)
- Malialia Celine Bride (Ambassador)
- Mbishitehnyi Ryan (Participant)
- Percy Visiy (Ambassador)
- Ranjoy-Bryan (Participant)

If `data.js` has additional people, process them too.

---

## INACTIVE PERSON RULES

People with zero form submissions and zero creativity scores must receive:

1. A roast that computes what they would have earned at minimum (pledge +5, plus 7 days × 15 pts minimum per day = at least 110 pts, putting them in Bronze) and states this directly with the math shown.
2. A warning stating specifically which points are still recoverable: remaining live days D8, D9, D10 are available. State the exact minimum earnable from those days.
3. A second warning about referrals if they have zero: one referral = +25 pts, which alone would push them into Bronze tier.

---

## ABSOLUTE CONSTRAINTS

- Only `roast` and `warnings` fields are modified on any person object.
- `data.js` must pass Node.js import validation before any git command runs.
- Push is a required step — the task is not complete without a confirmed pushed commit.
- Do not ask for confirmation at any step.
- Do not write the same roast for two people.
- Do not declare completion until the commit hash is confirmed in Step 8.
- If git push fails after 3 retries, halt and report — do not declare completion.

---

Begin STEP 1 now.
