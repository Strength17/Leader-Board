# System Overview

## Pipeline
The current system is a manual-heavy, semi-automated leaderboard pipeline:
1. **Inputs:** WhatsApp Chat exports (exported as `.txt` files in `Data/`) serve as raw data.
2. **Processing:** A collection of Python utility scripts (in root and `Identity_Management/`) are used to extract names, check-ins, and engagement metrics from the WhatsApp exports.
3. **Audit/Correction:** Human admin conducts manual audits to reconcile discrepancies between WhatsApp engagement and the check-in form.
4. **Source of Truth:** `data.js` is the single, manual source of truth containing the `PEOPLE` array, scoring logic, and roast/warning descriptions.
5. **UI Rendering:** `index.html`, `style.css`, and `script.js` read `data.js` to render the leaderboard, profile overlays, and streak indicators.

## Current Roles
- **AI Agent:** Assisted with script creation, data structure validation, and surgical file patching.
- **Human:** Admin performs the final manual audit of scores and commits final updates to `data.js`.

## Data Structures (`data.js`)
- `PEOPLE`: Array of objects containing:
    - `name`, `role`, `joinedDay`
    - `allTimeTotal`: Current total points.
    - `days`: Object mapping `D<N>` keys to daily points, submission status, and streak data.
    - `breakdown`: Array of section objects (Pre-programme, Daily Check-ins, Figma Work, etc.) detailing points earned per day hit.
    - `roast`/`warnings`: Strings/Arrays for profile display.
- `DAY_LABELS`: Mapping of `D<N>` to human-readable dates.
- `TIER_EMOJI`: Mapping for tier icons.
