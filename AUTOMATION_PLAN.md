# Automation Plan

Prioritized TODO list for automating the leaderboard pipeline:

- [ ] `compute_points(engagement_data, form_data, rules) -> points_breakdown_dict`: Centralize scoring logic to ensure consistency across participants.
- [ ] `update_data_js(points_by_person, data_js_path) -> bool`: Script to safely diff and update `data.js` without manual file editing.
- [ ] `audit_reconciliation(whatsapp_data, form_data) -> discrepancies_report`: Automate the detection of differences between WhatsApp engagement and form entries.
- [ ] `verify_day_unlock_logic(data_js_path) -> pass/fail report`: Ensure daily points/day unlocking logic complies with the established program rules.
