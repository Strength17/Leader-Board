# Technical Handoff: UI Architecture & Visual Logic

This document provides Claude with the definitive blueprint for the UI requirements and logic flow of the Sky Graphics Leaderboard.

---

## 📂 1. Modular Data Architecture
**NOTE TO CLAUDE:** You will **NOT** be provided with the `data.js` file. You must infer its structure entirely from the imports and usage logic within `index.html`. 

### **Inferred Schema from `index.html`:**
*   **`DAY_LABELS`**: Maps keys like `D1`, `D2` to full date strings.
*   **`TIER_EMOJI`**: Standardized rank icons.
*   **`PEOPLE`**: The main array of participant objects. You can see how properties like `p.name`, `p.allTimeTotal`, `p.days`, `p.breakdown`, and `p.roast` are accessed in the `renderBoard` and `openPanel` functions.
*   **`SNAPSHOTS`**: The historical data store. The UI accesses `SNAPSHOTS[currentDay][role]` to render specific leaderboard states.

Your task is to build and enhance the **logic and visuals** in `index.html` to perfectly accommodate this data source.

---

## 🏛️ 2. Program Logic (The 5-Day Rule)
*   **Week Structure:** Each program week consists of exactly **5 days** (Monday–Friday).
*   **Initialization:** Upon load, `index.html` must default to **Week 1** and **Day 5** (the week's milestone finale).
*   **Navigation:** 
    *   Weeks are the primary selector; Days are nested. 
    *   Future weeks (2-6) and future days in the active week must be visually **Locked** (using the `locked` CSS class and 🔒 icon).

---

## ✨ 3. Visual & Functional Requirements
*   **Day 5 "Golden Essence":** When Day 5 is selected (by default or manually), the logic must apply the `essence-golden` class to the `<body>`. This triggers high-end golden gradients, radial glows, and ambient milestone effects across the entire page.
*   **Celebration Engine:** 
    *   **NO Start Animation:** There must be **NO** loading screen, countdown, or automatic animation when the page first loads. The leaderboard must be visible immediately.
    *   **Celebrate Button:** The round 🎉 button at the bottom-right must trigger a 5-second procedural celebration sequence (floating balloons and Achievement Pop Messages) **ONLY** when manually clicked.
*   **Data Source:** `index.html` must correctly import from `./data.js` and render all scores, tiers, and "roasts" dynamically.

---

## 🤖 4. Strategic Instructions for Claude
**To Claude:**
1.  **Direct Entrance:** Ensure the leaderboard is fully rendered and interactive the instant the DOM is ready. Remove all splash screens and initial countdowns.
2.  **Epic Transitions:** While there is no start animation, manual transitions (switching days or opening profiles) should feel premium. Use hardware-accelerated transforms (translate3d/scale) for 60fps smoothness.
3.  **UI Refinement:** While you cannot see `data.js`, you are expected to make `index.html` robust enough to handle any data provided by that module, following the patterns established in the code.
4.  **Parity:** Ensure the mobile experience (max-width: 640px) is just as "epic" as the desktop view.

---

### **Handover Files**
*   `index.html` (Logic & UI)
*   `reply.md` (This explanation)
