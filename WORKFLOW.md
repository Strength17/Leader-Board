# Workflow: Leaderboard Data Integrity Loop

## Goal
Produce a `data2.js` that contains absolute data, reconciling all inputs (WhatsApp, Google Forms, Manual Admin Overrides) to match the ground truth in `MASTER DATA.md`.

## Protocol (The Loop)
For each iteration (1 to 10):
1.  **Reset/Clean:** Ensure all previous outputs are cleared (if necessary).
2.  **Execute Pipeline:**
    *   Run `wa_parser.py` -> Updates `Data/wa_report.md`.
    *   Run `form_parser.py` -> Updates `Data/form_report.md`.
    *   Run `leaderboard_sync.py` -> Reads all reports + `Data/Manual_Reconciliation_Points.md`.
        *   Produces `Data/master_data.md` (audit trail).
        *   Produces `data.js` (UI output).
    *   Run `generate_audit.py` -> Updates `Data/WA_Interaction_Audit.md`.
3.  **Validate:**
    *   Compare `Data/master_data.md` (Audit) against `data2.js` (UI Data).
    *   Compare `Data/master_data.md` against `MASTER DATA.md` (Ground Truth).
    *   Log any discrepancies in `reply.md`.
4.  **Log Results:** Append run #, status, and discrepancies found to `reply.md`.
5.  **Iterate:** If discrepancies exist, fix code/data, then loop back to step 1.

## Progress Tracking
- [x] Run 1
- [x] Run 2
- [x] Run 3
- [x] Run 4
- [x] Run 5
- [x] Run 6
- [x] Run 7
- [x] Run 8
- [x] Run 9
- [x] Run 10
