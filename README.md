# Leader-Board

A live, real-time leaderboard system built for **Sky Graphics Figma Edition 1**, a structured 6-week Figma design programme with ~49 participants and an ambassador tier.

## What it does
- Renders a live HTML leaderboard with countdown animations, day-specific filtering, tab switching, and celebration animations on milestone days
- Displays participant profile panels and tier status (e.g. Gold, Ambassador)
- Auto-refreshes from a data pipeline that ingests WhatsApp exports and Google Form submissions

## Stack
- **Frontend:** JavaScript, HTML/CSS (deployed as a static site)
- **Data pipeline:** Python scripts (`wa_parser.py`, `form_parser.py`, `leaderboard_sync.py`) that process raw WhatsApp chat exports and form data into a structured `data.js` file consumed by the frontend
- **Deployment:** Vercel, connected to GitHub for continuous deployment

## Live demo
https://leader-board-lake.vercel.app

## Status
Actively maintained — in production use for a live cohort as of July 2026.
