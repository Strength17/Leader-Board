# Agent Prompt: Sky Graphics Leaderboard — data.js Schema Update

## Your Mission

You are modifying `data.js` for the Sky Graphics Edition 1 Leaderboard. Your job is to add two new fields to the schema without removing, renaming, or restructuring anything that already exists. You must not break any existing field. You must not guess or invent data values — you derive them from data that is already there using the rules below.

When you start, create a file called `WORKFLOW.md` in the same directory as `data.js`. You will update it as you go. Do not stop until every task in the workflow is ticked.

---

## Step 0 — Create WORKFLOW.md

Create this file immediately before touching anything else:

```md
# WORKFLOW — data.js Schema Update
## Sky Graphics Edition 1 · Dual-Streak System

### STATUS: IN PROGRESS

---

## Tasks

- [ ] 0. WORKFLOW.md created
- [ ] 1. data.js read and parsed in full
- [ ] 2. All PEOPLE entries listed and counted
- [ ] 3. Point classification rules understood (see rules below)
- [ ] 4. Per-day `workDone` derived for every person for every day
- [ ] 5. Per-day `workStreakDays` computed for every person for every day
- [ ] 6. All new fields written into data.js
- [ ] 7. Existing fields verified untouched
- [ ] 8. WORKFLOW.md marked COMPLETE

---

## Log
(append a line here each time you complete a task)
```

Every time you finish a task, open `WORKFLOW.md`, tick that checkbox `[x]`, and append a log line at the bottom. Do not skip ahead. Do not batch-tick. Tick one, do the next.

---

## Step 1 — Read and Understand the Existing Schema

Read `data.js` in full. The file exports:

- `PEOPLE` — array of person objects
- `SNAPSHOTS` — historical data keyed by day (e.g. `SNAPSHOTS['D1']`)
- `DAY_LABELS` — maps day keys like `D1` to full date strings
- `TIER_EMOJI` — maps tier names to emoji
- `PLEDGE_ONLY` — array of names who only pledged

Do not modify any of these exports or their existing structure. You are only adding new fields inside existing objects.

---

## Step 2 — Understand the Existing Per-Day Structure

Each person in `PEOPLE` has a `days` object. Each day entry currently looks like this:

```js
D3: {
  pts: 15,           // total points earned that day
  submitted: true,   // whether they submitted the check-in form
  streakDays: 3      // consecutive days with submitted: true
}
```

You will add two new fields to each day entry:

```js
D3: {
  pts: 15,
  submitted: true,
  streakDays: 3,
  workDone: true,        // NEW — derived from task points (see rules below)
  workStreakDays: 3       // NEW — consecutive days with workDone: true
}
```

---

## Step 3 — Rules for Deriving `workDone`

`workDone` is `true` for a given day if that person earned **any points from manual task-quality awards** on that day. These are the only point values that count as task evidence:

| Points | Meaning |
|--------|---------|
| +5 | Did what the video instructed (baseline task) |
| +10 | Work was more creative than expected |
| +20 | Work was extraordinary |

To find these: look at each person's `breakdown` array. Each breakdown item has a `pts` value, an `earned` boolean, and a `days` array (the days it applies to) and a `dayHits` array (the days it was actually earned).

**A day counts as `workDone: true` if the person has at least one breakdown item where:**
- The item is in the task-quality category (pts is 5, 10, or 20)
- AND that day's key (e.g. `D3`) is present in `item.dayHits`

**Points that do NOT count toward `workDone`:**
- +10 automatic check-in form submission point
- +5 early submission bonus
- +5 pledge point (one-time, not per day)
- +15 perfect week bonus
- +20 phase completion bonus
- Any streak bonuses

If you cannot determine from the breakdown which category a point belongs to, use the item's `label` or `desc` field to identify it. Task-quality items will reference the video, creativity, or quality of work. Auto items will reference the form, submission time, or streak.

**If a person has no breakdown data for a day, set `workDone: false`.**

---

## Step 4 — Rules for Computing `workStreakDays`

Once you have `workDone` for all days for a person, compute `workStreakDays` for each day using this logic:

```
For day D (in order D1, D2, D3, D4, D5):
  if workDone[D] is false:
    workStreakDays[D] = 0
  if workDone[D] is true:
    workStreakDays[D] = workStreakDays[previous day] + 1
    (for D1 there is no previous day, so workStreakDays[D1] = 1 if workDone[D1] is true)
```

Example:
- D1 workDone: true → workStreakDays: 1
- D2 workDone: false → workStreakDays: 0
- D3 workDone: true → workStreakDays: 1
- D4 workDone: true → workStreakDays: 2
- D5 workDone: true → workStreakDays: 3

---



## Step 5 — Writing the Changes

When writing back to `data.js`:

1. **Do not reformat the entire file.** Edit only the fields you are adding.
2. **Do not remove any existing field.**
3. **Do not rename any existing field.**
4. **Do not change any existing value.**
5. **Preserve all existing comments in the file.**
6. **Preserve the export structure exactly** (`export const`, named exports — do not change to default export or CommonJS).
7. Add `workDone` and `workStreakDays` inside each day object, after the existing fields.

---

## Step 6 — Verification Checklist

Before ticking task 8 in WORKFLOW.md, verify the following for every person:

- [ ] Every day object still has `pts`, `submitted`, `streakDays`
- [ ] Every day object now also has `workDone` and `workStreakDays`
- [ ] `workStreakDays` is always 0 on days where `workDone` is false
- [ ] `workStreakDays` increments correctly across consecutive `workDone: true` days
- [ ] No existing field has been removed or changed
- [ ] The file still runs without syntax errors (check for missing commas, brackets)
- [ ] All exports are still present and named correctly

---

## Step 7 — Final WORKFLOW.md Update

When all tasks are done, update the status line at the top of `WORKFLOW.md` to:

```
### STATUS: COMPLETE ✅
```

Then tick task 8 and add a final log line with the timestamp.

---

## Constraints and Rules — Read These Before You Start

- **Never delete existing data.** If you are unsure whether something should be removed, leave it.
- **Never invent values.** If you cannot derive `workDone` from the breakdown data, set it to `false` and log a note in WORKFLOW.md.
- **Never change `SNAPSHOTS`.** Only modify person objects inside the `PEOPLE` array.
- **Never change `PLEDGE_ONLY`.** Those names are handled by the frontend.
- **One task at a time.** Tick each task in WORKFLOW.md before starting the next.
- **If you encounter an ambiguous breakdown item**, use the `label` and `desc` fields to classify it. When in doubt, do not count it as a task-quality point.
- **If you encounter a person with no breakdown array**, set `workDone: false` for all their days.
