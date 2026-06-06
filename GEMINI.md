# Project-Specific Instructions (Sky Graphics Leaderboard)

## Data Management
- **Modularity:** Keep all data (PEOPLE, SNAPSHOTS, DAY_LABELS, TIER_EMOJI) in `data.js`. Use ES6 exports.
- **Integrity:** Ensure that `allTimeTotal` in the `PEOPLE` array matches the sum of individual day points and bonuses.
- **Snapshots:** The `SNAPSHOTS` object must be synchronized with the `PEOPLE` array for historical accuracy.

## UI/UX Standards
- **Golden Essence:** Day 5 must always trigger the `essence-golden` class on the `<body>`.
- **Locking Logic:** Future weeks and days must be visually locked and non-functional.
- **Celebration:** The 5-second countdown must be the first thing a user sees on page load, followed by the balloon animation.

## Code Style
- **Vanilla JS:** Avoid external libraries unless explicitly requested.
- **Surgical Edits:** When updating `index.html`, use precise `replace` calls. Avoid rewriting the entire file to prevent truncation.
- **Responsiveness:** Ensure all UI upgrades are tested for mobile view (max-width: 640px).

## Cleanup Workflow
- **Transient Files:** Always delete `message.txt` and `reply.md` before finalizing a milestone.
- **Master Data:** Maintain `SkyGraphics_E1_MasterData.xlsx` as the ultimate source of truth for all manual corrections.
