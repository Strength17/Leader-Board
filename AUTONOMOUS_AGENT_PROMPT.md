# Autonomous Build Loop — Sky Graphics Automation
**Give this whole file to your Gemini CLI agent and say: "Read this file and follow it exactly."**

---

## WHY THIS DOCUMENT EXISTS (read this part yourself, Feli)

A single AI turn cannot run for 5 hours — context windows fill up and the
agent starts looping on "I'm done / I'll stop / I'm done" nonsense. The fix
used by people doing exactly what you described is the **Ralph Wiggum
loop**: a tiny bash script that keeps re-launching the agent with a *fresh*
context, while all real progress lives on disk (files + git commits), not
in the agent's head.

So this document makes the agent do ONE setup pass, then write its own
recurring prompt + a runner script. You start `run_loop.sh` in a terminal
and leave it. It keeps going until YOU press Ctrl+C — no built-in stop
condition. That's the "infinity" you asked for.

---

## PHASE 0 — SESSION MEMORY AUDIT (run once, do this first)

Before touching anything, build your own persistent memory of this project
by reading the actual evidence on disk — not assumptions:

1. Run `git log --oneline -100` and read the last ~50 commits.
2. Read every existing script in the repo (leaderboard `index.html`,
   `data.js`, `script.js`, any `find_emoji_messages.py` / Apps Script /
   Python files).
3. Read any README, notes, or `.md` files already in the repo.
4. From all of this, write **`SYSTEM_OVERVIEW.md`** answering:
   - What is the current end-to-end pipeline? (e.g. WhatsApp export →
     message scan → emoji/points detection → Google Apps Script /
     check-in form → master sheet → `data.js` → `index.html` leaderboard)
   - Which steps are currently done BY A HUMAN, which by AI judgment, and
     which are already scripted/deterministic?
   - What are the exact data structures involved (PEOPLE array shape,
     points rules, day/week numbering, joinedDay logic, etc.)?

5. Write **`MISTAKES_LOG.md`** — scan commit messages, code comments, and
   diffs for every bug that was previously found and fixed. For each one,
   write it as a rule, e.g.:
   - "Never use `allTimeTotal` as a per-day points value — it's the FINAL
     total. Use carry-forward (`ptsAsOf`) for days with no entry."
   - "Emoji matching must strip variation selectors (U+FE0F) and handle
     both Android and iOS WhatsApp timestamp formats."
   - "Day numbering: Day 1 = June 1, weekdays only, weekends don't get a
     Day number."
   - (Add every other one you find — this file is the agent's "don't repeat
     this mistake" memory and MUST be re-read every loop iteration.)

Commit both files: `git commit -am "Phase 0: system overview + mistakes log"`

---

## PHASE 1 — AUTOMATION GAP ANALYSIS

Go through the current pipeline from `SYSTEM_OVERVIEW.md` step by step.
For every step that currently needs a human OR an AI agent to "look at it
and decide," ask: **could a deterministic script do this instead, given the
data that's actually available?**

Examples of the kind of thing to look for:
- Detecting which WhatsApp messages count as a valid check-in (already
  partly scripted — can it be made fully rule-based?)
- Assigning automated points (form submission, early submission, photo
  upload) — fully rule-based from timestamps + emoji presence?
- Updating `data.js` from the master sheet / Apps Script output —
  currently manual? Can it be a script that diffs and writes the file?
- Detecting joined-late participants, streak freezes, milestone days —
  all of these should be pure functions of the data, not judgment calls.

Write **`AUTOMATION_PLAN.md`** as a prioritized TODO list. Each item must
be small enough to be ONE function in ONE script, e.g.:

```markdown
- [ ] detect_checkin_messages(chat_export) -> list of valid check-ins
- [ ] compute_points(checkin, rules) -> points breakdown dict
- [ ] update_data_js(points_by_person, data_js_path) -> writes data.js
- [ ] verify_day_unlock_logic(data_js_path) -> pass/fail report
- [ ] ...
```

Commit: `git commit -am "Phase 1: automation plan"`

---

## PHASE 2 — THE BUILD LOOP (this is what repeats forever)

Each time you (the agent) run, do ONE pass of this:

1. Re-read `MISTAKES_LOG.md`, `SYSTEM_OVERVIEW.md`, and `AUTOMATION_PLAN.md`
   in full. State of the world lives in these files, not your memory.
2. Pick the **highest-priority unfinished item** from `AUTOMATION_PLAN.md`.
3. Write or extend a script containing ONE clearly-named, single-purpose
   function for that item (e.g. `compute_points()` in `points.py`).
4. Write a test for that function using REAL sample data pulled from the
   repo (actual chat export lines, actual `data.js` entries) — not made-up
   toy data.
5. Run the test.
   - **If it fails:** fix the function. Re-run. Keep fixing and re-running
     until it passes. Do not move on while it's failing.
   - **If you hit the exact same failure twice in a row with the same
     fix attempted:** stop trying that approach, write what you tried and
     why it didn't work into `MISTAKES_LOG.md`, and try a fundamentally
     different approach (different library, different data assumption,
     etc.) rather than repeating yourself.
6. Once the test passes:
   - Mark the item `[x]` done in `AUTOMATION_PLAN.md`.
   - Add anything you learned (edge cases, gotchas, format quirks) to
     `MISTAKES_LOG.md` so future loops don't rediscover it.
   - `git add -A && git commit -m "Automate: <short description>"`
7. If `AUTOMATION_PLAN.md` has no unfinished items left, go back to PHASE 1
   logic: re-examine the pipeline (now that more is scripted) for NEW
   automation opportunities, add them to `AUTOMATION_PLAN.md`, and continue.
8. End your turn now (do not try to do a second item in the same turn —
   the loop will restart you with a clean context for the next item).

---

## PHASE 3 — SET UP THE ACTUAL LOOP (do this once, at the end of Phase 0)

Create **`LOOP_PROMPT.md`** containing exactly this text:

```markdown
Read MISTAKES_LOG.md, SYSTEM_OVERVIEW.md, and AUTOMATION_PLAN.md in full.
Then execute exactly ONE pass of PHASE 2 from AUTONOMOUS_AGENT_PROMPT.md
(pick the top unfinished item, build it, test it until it passes, commit
it, log learnings). End your turn after committing — do not start a
second item.
```

Create **`run_loop.sh`**:

```bash
#!/bin/bash
# Ralph-style loop: keeps re-launching the agent with a fresh context.
# Stops ONLY when you press Ctrl+C.
mkdir -p loop_logs
i=0
while :; do
  i=$((i+1))
  echo "=== Iteration $i — $(date) ==="
  cat LOOP_PROMPT.md | gemini -p --yolo 2>&1 | tee "loop_logs/iter_${i}.log"
  echo "=== End iteration $i ==="
  sleep 5
done
```

Make it executable: `chmod +x run_loop.sh`

Commit everything: `git commit -am "Phase 3: loop infrastructure ready"`

**Then tell the user (Feli) exactly this:**

> "Setup is complete. To start the autonomous loop, run `./run_loop.sh` in
> a terminal and leave it running. It will keep working through
> AUTOMATION_PLAN.md, testing and committing as it goes, until you press
> Ctrl+C. Check `loop_logs/` and `git log` to see progress at any time."

---

## GUARDRAILS (non-negotiable, applies to every iteration)

- **Work on a dedicated branch** (e.g. `git checkout -b auto-loop` before
  starting), not directly on `main` — this gives Feli a safe way to review
  or roll back a batch of automated commits without losing manual work.
- **Never commit secrets** (`.env`, API keys, tokens). If you find any in
  the repo, add them to `.gitignore` and flag it in `MISTAKES_LOG.md`
  instead of committing them.
- **Every commit must correspond to a passing test.** No "WIP" or
  "checkpoint" commits with failing code.
- **Don't touch `index.html` / `data.js` rendering logic** unless the
  current `AUTOMATION_PLAN.md` item is specifically about it — stay scoped
  to one function per iteration.

---

## WHEN FELI SAYS "STOP" / "PROGRESS REPORT"

This only happens when Feli presses Ctrl+C on `run_loop.sh` and asks. At
that point, summarize: items completed (from `AUTOMATION_PLAN.md`), what's
still pending, and anything in `MISTAKES_LOG.md` that needs a human
decision. Until then — no summaries, no "I'm done" messages, just keep
working through the loop.
