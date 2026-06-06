# WORKFLOW — UI & Data Integrity Recovery

## Phase 1: data.js Integrity & Logic Lockdown
- [x] 1. Apply +5 Standard Work to "Abongnwi Chrioni-Opal Forba'" for Day 1.
- [x] 2. Update Chrioni's allTimeTotal (90 -> 95) and adjust historical SNAPSHOTS (D1-D5).
- [x] 3. Audit all PEOPLE: Ensure Rule "Every form submission (submitted:true) = work done (workDone:true)".
- [x] 4. Recalculate all `workStreakDays` to ensure they include both pure work days and form-submission days.


## Phase 2: index.html Rendering Refactor
- [x] 5. Change Row Filtering logic:
    - **Active (Green):** Anyone with `pts > 0` (Interaction-based).
    - **Inactive (Red):** Only those with `pts === 0` (Zero points for that day).
- [x] 6. Rename "Did Not Submit Yet" label to "No Activity Recorded Today" (or similar professional alternative).
- [x] 7. Ensure UI displays both 📋 Form and ✏️ Work streaks as separate, equal metrics in the row.

## Phase 3: Validation & Cleanup
- [x] 8. Verify data imports: Confirm index.html imports all required variables from data.js.
- [x] 9. Final cross-check of mobile responsiveness (ensuring the new dual-streak columns fit).

---

## Log
2026-06-06: Workflow created.
2026-06-06: Phase 1 Complete - data.js integrity and Chrioni +5 correction applied.
2026-06-06: Phase 2 Complete - Interaction-based rendering and dual-streak UI implemented.
2026-06-06: Phase 3 Complete - Imports verified and responsiveness checked.
2026-06-06: Project successfully recovered and updated.
