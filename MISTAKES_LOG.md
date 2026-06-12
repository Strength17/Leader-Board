# Mistakes Log

- **Data Integrity:** Never use `allTimeTotal` as a per-day points value — it's the FINAL total. Use carry-forward (`ptsAsOf`) for days with no entry.
- **WhatsApp Parsing:** Emoji matching must strip variation selectors (U+FE0F) and handle both Android and iOS WhatsApp timestamp formats.
- **Day Numbering:** Day 1 = June 1, weekdays only, weekends don't get a Day number.
- **Data Source:** Manual updates to `data.js` are preferred over automated parsing to ensure total accuracy after audit. Always prioritize the manual audit reconciliation over raw parser output.
- **Git Hygiene:** Do not commit `Archive/Delete` files without staging them specifically; do not rely on `git add .` to catch untracked files in complex subdirectories.
