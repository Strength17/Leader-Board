/**
 * SKY GRAPHICS FIGMA EDITION 1 — LEADERBOARD DATA
 * Generated: 2026-06-11 03:00:04
 *
 * STREAK RULES (admin override — FREEZE on miss):
 *   Form streak: freezes (does not reset) on missed form days
 *   Work streak: freezes (does not reset) on days without scored work
 *   submitted:true always implies workDone:true
 *
 * pts in days[D] = CUMULATIVE total as of that day
 * ptsToday (delta) is NOT stored here — UI derives it as pts - prevDay.pts
 */

export const DAY_LABELS = {
  D1: 'Day 1 — Monday, June 1, 2026',
  D2: 'Day 2 — Tuesday, June 2, 2026',
  D3: 'Day 3 — Wednesday, June 3, 2026',
  D4: 'Day 4 — Thursday, June 4, 2026',
  D5: 'Day 5 — Friday, June 5, 2026',
  D6: 'Day 6 — Monday, June 8, 2026',
  D7: 'Day 7 — Tuesday, June 9, 2026',
};

export const TIER_EMOJI = {
  PLATINUM: '🏆', GOLD: '🥇', SILVER: '🥈', BRONZE: '🥉', UNRANKED: '⬜'
};

export const PEOPLE = [
  {
    name: "Christine Choundong",
    role: "Ambassador",
    joinedDay: "D1",
    allTimeTotal: 272,
    tier: "GOLD",
    warnings: ["Check-in points stripped for D5 due to late submission (wrote D4)."],
    days: {
      D1: { pts: 90, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 136, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 168, submitted: true, streakDays: 3, workDone: true, workStreakDays: 3 },
      D4: { pts: 178, submitted: false, streakDays: 3, workDone: true, workStreakDays: 4 },
      D5: { pts: 223, submitted: false, streakDays: 3, workDone: true, workStreakDays: 5 },
      D6: { pts: 250, submitted: true, streakDays: 4, workDone: true, workStreakDays: 6 },
      D7: { pts: 272, submitted: true, streakDays: 5, workDone: true, workStreakDays: 7 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
        { label: "Referral \u00d7 2", pts: 50, earned: true, dayHits: null, desc: "You brought 2 new members in. +50 pts." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D1", "D2", "D3", "D6", "D7"], desc: "5 valid forms submitted. +50 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D1", "D2", "D3", "D4", "D5", "D6", "D7"], desc: "D1:10 \u00b7 D2:20 \u00b7 D3:5 \u00b7 D4:5 \u00b7 D5:10 \u00b7 D6:5 \u00b7 D7:5. Total: +60." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D1", "D2", "D3", "D5", "D6", "D7"], desc: "Image uploaded on D1, D2, D3, D5, D6, D7. +35 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Asked a genuine question", pts: 3, earned: true, dayHits: ["D2"], desc: "+3 total." },
        { label: "First to post check-in in group", pts: 5, earned: true, dayHits: ["D2", "D3", "D4"], desc: "+15 total." },
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D1", "D3"], desc: "+10 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1", "D3", "D6", "D7"], desc: "+8 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
        { label: "Welcomed a new member", pts: 3, earned: true, dayHits: ["D2"], desc: "+3 total." },
      ]},
      { section: "BONUSES", items: [
        { label: "Phase Completion (W1)", pts: 20, earned: true, dayHits: ["D5"], desc: "5/5 days work completed. +20." },
        { label: "Special Bonus (D5)", pts: 10, earned: true, dayHits: ["D5"], desc: "FB interaction bonus confirmed. +10." },
      ]},
    ],
    roast: `<p><strong>Christine.</strong> You are at the top of this board. Every day you show up, you pull further ahead. 100% attendance. That is the standard. Hold it.</p>`,
  },
  {
    name: "Emmanuel Karol Tchouani",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 205,
    tier: "SILVER",
    warnings: [],
    days: {
      D1: { pts: 60, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 85, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 105, submitted: true, streakDays: 3, workDone: true, workStreakDays: 3 },
      D4: { pts: 127, submitted: true, streakDays: 4, workDone: true, workStreakDays: 4 },
      D5: { pts: 185, submitted: true, streakDays: 5, workDone: true, workStreakDays: 5 },
      D6: { pts: 185, submitted: false, streakDays: 5, workDone: false, workStreakDays: 5 },
      D7: { pts: 205, submitted: true, streakDays: 6, workDone: true, workStreakDays: 6 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
        { label: "Referral \u00d7 1", pts: 25, earned: true, dayHits: null, desc: "You brought 1 new member in. +25 pts." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D1", "D2", "D3", "D4", "D5", "D7"], desc: "6 valid forms submitted. +60 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D1", "D2", "D3", "D4", "D5", "D7"], desc: "D1:10 \u00b7 D2:10 \u00b7 D3:5 \u00b7 D4:5 \u00b7 D5:5 \u00b7 D7:5. Total: +40." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D1", "D2", "D3", "D4", "D5", "D7"], desc: "Image uploaded on D1, D2, D3, D4, D5, D7. +30 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1", "D4"], desc: "+4 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
        { label: "Welcomed a new member", pts: 3, earned: true, dayHits: ["D5"], desc: "+3 total." },
      ]},
      { section: "BONUSES", items: [
        { label: "Perfect Week (W1)", pts: 15, earned: true, dayHits: ["D5"], desc: "5/5 valid same-day forms. +15." },
        { label: "Phase Completion (W1)", pts: 20, earned: true, dayHits: ["D5"], desc: "5/5 days work completed. +20." },
      ]},
    ],
    roast: `<p><strong>Emmanuel.</strong> You are in the upper half. Close to Gold. 6-day streak — keep that going.</p>`,
  },
  {
    name: "Oluwasegun Daniel Osawore",
    role: "Ambassador",
    joinedDay: "D1",
    allTimeTotal: 195,
    tier: "SILVER",
    warnings: [],
    days: {
      D1: { pts: 98, submitted: false, streakDays: 0, workDone: true, workStreakDays: 1 },
      D2: { pts: 133, submitted: true, streakDays: 1, workDone: true, workStreakDays: 2 },
      D3: { pts: 160, submitted: true, streakDays: 2, workDone: true, workStreakDays: 3 },
      D4: { pts: 165, submitted: false, streakDays: 2, workDone: false, workStreakDays: 3 },
      D5: { pts: 185, submitted: false, streakDays: 2, workDone: true, workStreakDays: 4 },
      D6: { pts: 190, submitted: false, streakDays: 2, workDone: true, workStreakDays: 5 },
      D7: { pts: 195, submitted: false, streakDays: 2, workDone: true, workStreakDays: 6 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
        { label: "Referral \u00d7 3", pts: 75, earned: true, dayHits: null, desc: "You brought 3 new members in. +75 pts." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D2", "D3"], desc: "2 valid forms submitted. +20 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D1", "D2", "D3", "D5", "D6", "D7"], desc: "D1:10 \u00b7 D2:15 \u00b7 D3:10 \u00b7 D5:15 \u00b7 D6:5 \u00b7 D7:5. Total: +60." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D2", "D3"], desc: "Image uploaded on D2, D3. +10 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Asked a genuine question", pts: 3, earned: true, dayHits: ["D4"], desc: "+3 total." },
        { label: "First to post check-in in group", pts: 5, earned: true, dayHits: ["D1", "D5"], desc: "+10 total." },
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D2"], desc: "+5 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D3", "D4"], desc: "+4 total." },
        { label: "Welcomed a new member", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Oluwasegun.</strong> You are in the upper half. Close to Gold. You are leaving points on the table: 4 day(s) with work but no form.</p>`,
  },
  {
    name: "Abongnwi Chrioni-Opal Forba'",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 150,
    tier: "SILVER",
    warnings: [],
    days: {
      D1: { pts: 45, submitted: false, streakDays: 0, workDone: true, workStreakDays: 1 },
      D2: { pts: 45, submitted: false, streakDays: 0, workDone: false, workStreakDays: 1 },
      D3: { pts: 45, submitted: false, streakDays: 0, workDone: false, workStreakDays: 1 },
      D4: { pts: 52, submitted: false, streakDays: 0, workDone: true, workStreakDays: 2 },
      D5: { pts: 105, submitted: true, streakDays: 1, workDone: true, workStreakDays: 3 },
      D6: { pts: 110, submitted: false, streakDays: 1, workDone: true, workStreakDays: 4 },
      D7: { pts: 150, submitted: true, streakDays: 2, workDone: true, workStreakDays: 5 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
        { label: "Referral \u00d7 1", pts: 25, earned: true, dayHits: null, desc: "You brought 1 new member in. +25 pts." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D5", "D7"], desc: "2 valid forms submitted. +20 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D1", "D4", "D5", "D6", "D7"], desc: "D1:5 \u00b7 D4:5 \u00b7 D5:5 \u00b7 D6:5 \u00b7 D7:5. Total: +25." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D5", "D7"], desc: "Image uploaded on D5, D7. +50 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Asked a genuine question", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D1", "D5"], desc: "+10 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1", "D4", "D5"], desc: "+6 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D5"], desc: "+3 total." },
        { label: "Welcomed a new member", pts: 3, earned: true, dayHits: ["D5"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Abongnwi.</strong> You are in the upper half. Close to Gold. You are leaving points on the table: 3 day(s) with work but no form.</p>`,
  },
  {
    name: "Faith Emmanuella Busari",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 129,
    tier: "BRONZE",
    warnings: [],
    days: {
      D1: { pts: 65, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 107, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 109, submitted: false, streakDays: 2, workDone: false, workStreakDays: 2 },
      D4: { pts: 109, submitted: false, streakDays: 2, workDone: false, workStreakDays: 2 },
      D5: { pts: 129, submitted: true, streakDays: 3, workDone: true, workStreakDays: 3 },
      D6: { pts: 129, submitted: false, streakDays: 3, workDone: false, workStreakDays: 3 },
      D7: { pts: 129, submitted: false, streakDays: 3, workDone: false, workStreakDays: 3 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
        { label: "Referral \u00d7 1", pts: 25, earned: true, dayHits: null, desc: "You brought 1 new member in. +25 pts." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D1", "D2", "D5"], desc: "3 valid forms submitted. +30 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D1", "D2", "D5"], desc: "D1:10 \u00b7 D2:20 \u00b7 D5:5. Total: +35." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D1", "D2", "D5"], desc: "Image uploaded on D1, D2, D5. +20 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Asked a genuine question", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D2"], desc: "+5 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1", "D2", "D3"], desc: "+6 total." },
      ]},
    ],
    roast: `<p><strong>Faith.</strong> You have made it onto the board. But barely.</p>`,
  },
  {
    name: "Frank Emmanuel",
    role: "Ambassador",
    joinedDay: "D1",
    allTimeTotal: 99,
    tier: "BRONZE",
    warnings: [],
    days: {
      D1: { pts: 58, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 58, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 58, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 63, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 63, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 99, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D7: { pts: 99, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
        { label: "Referral \u00d7 2", pts: 50, earned: true, dayHits: null, desc: "You brought 2 new members in. +50 pts." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D6"], desc: "1 valid form submitted. +10 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D6"], desc: "D6:5. Total: +5." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D6"], desc: "Image uploaded on D6. +5 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Asked a genuine question", pts: 3, earned: true, dayHits: ["D6"], desc: "+3 total." },
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D6"], desc: "+5 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D4", "D6"], desc: "+4 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D4", "D6"], desc: "+6 total." },
        { label: "Welcomed a new member", pts: 3, earned: true, dayHits: ["D1", "D6"], desc: "+6 total." },
      ]},
    ],
    roast: `<p><strong>Frank.</strong> You have made it onto the board. But barely.</p>`,
  },
  {
    name: "Mbiydzenyuy Patience Dzekem",
    role: "Ambassador",
    joinedDay: "D1",
    allTimeTotal: 97,
    tier: "BRONZE",
    warnings: ["Check-in points stripped for D6 due to late submission (wrote D2)."],
    days: {
      D1: { pts: 30, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 67, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 69, submitted: false, streakDays: 2, workDone: false, workStreakDays: 2 },
      D4: { pts: 71, submitted: false, streakDays: 2, workDone: false, workStreakDays: 2 },
      D5: { pts: 71, submitted: false, streakDays: 2, workDone: false, workStreakDays: 2 },
      D6: { pts: 97, submitted: false, streakDays: 2, workDone: true, workStreakDays: 3 },
      D7: { pts: 97, submitted: false, streakDays: 2, workDone: false, workStreakDays: 3 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D1", "D2"], desc: "2 valid forms submitted. +20 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D1", "D2", "D6"], desc: "D1:10 \u00b7 D2:15 \u00b7 D6:5. Total: +30." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D1", "D2", "D6"], desc: "Image uploaded on D1, D2, D6. +25 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Asked a genuine question", pts: 3, earned: true, dayHits: ["D6"], desc: "+3 total." },
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D6"], desc: "+5 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D2", "D3", "D4"], desc: "+6 total." },
        { label: "Welcomed a new member", pts: 3, earned: true, dayHits: ["D6"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Mbiydzenyuy.</strong> You have made it onto the board. But barely.</p>`,
  },
  {
    name: "Irinyemi Adedayo Juliet",
    role: "Ambassador",
    joinedDay: "D1",
    allTimeTotal: 95,
    tier: "BRONZE",
    warnings: [],
    days: {
      D1: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 50, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D3: { pts: 50, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D4: { pts: 70, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D5: { pts: 70, submitted: false, streakDays: 2, workDone: false, workStreakDays: 2 },
      D6: { pts: 75, submitted: false, streakDays: 2, workDone: true, workStreakDays: 3 },
      D7: { pts: 95, submitted: true, streakDays: 3, workDone: true, workStreakDays: 4 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D2", "D4", "D7"], desc: "3 valid forms submitted. +30 total." },
        { label: "Early submission bonus", pts: 5, earned: true, dayHits: ["D2"], desc: "Submitted before 3PM on D2. +5 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D6", "D7"], desc: "D6:5 \u00b7 D7:5. Total: +10." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D2", "D4", "D7"], desc: "Image uploaded on D2, D4, D7. +40 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1"], desc: "+2 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Irinyemi.</strong> You have made it onto the board. But barely.</p>`,
  },
  {
    name: "Amaazee Ivanna Therese Fundoh",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 85,
    tier: "BRONZE",
    warnings: ["New joiner recovery form (D1 written on D6) -- counted as D6 pending admin decision."],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 45, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D7: { pts: 85, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D6", "D7"], desc: "2 valid forms submitted. +20 total." },
        { label: "Early submission bonus", pts: 5, earned: true, dayHits: ["D6", "D7"], desc: "Submitted before 3PM on D6, D7. +10 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D6", "D7"], desc: "D6:10 \u00b7 D7:10. Total: +20." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D6", "D7"], desc: "Image uploaded on D6, D7. +15 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D7"], desc: "+5 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D6", "D7"], desc: "+4 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D6", "D7"], desc: "+6 total." },
      ]},
    ],
    roast: `<p><strong>Amaazee.</strong> You have made it onto the board. But barely. You have only shown up 2 of 7 days. Consistency is the whole game here.</p>`,
  },
  {
    name: "Malialia Celine Bride",
    role: "Ambassador",
    joinedDay: "D1",
    allTimeTotal: 82,
    tier: "BRONZE",
    warnings: [],
    days: {
      D1: { pts: 82, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 82, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 82, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 82, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 82, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 82, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 82, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
        { label: "Referral \u00d7 3", pts: 75, earned: true, dayHits: null, desc: "You brought 3 new members in. +75 pts." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1"], desc: "+2 total." },
      ]},
    ],
    roast: `<p><strong>Malialia.</strong> You have made it onto the board. But barely. You have only shown up 1 of 7 days. Consistency is the whole game here.</p>`,
  },
  {
    name: "Dorothy Joyce Priscille",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 47,
    tier: "UNRANKED",
    warnings: ["New joiner recovery form (D1 written on D6) -- counted as D6 pending admin decision."],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 27, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D7: { pts: 47, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D6", "D7"], desc: "2 valid forms submitted. +20 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D6", "D7"], desc: "D6:5 \u00b7 D7:5. Total: +10." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D6", "D7"], desc: "Image uploaded on D6, D7. +10 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D6"], desc: "+2 total." },
      ]},
    ],
    roast: `<p><strong>Dorothy.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Ranjoy-Bryan",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 30,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 30, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D3: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D4: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D5: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D6: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D7: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D1"], desc: "1 valid form submitted. +10 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: true, dayHits: ["D1"], desc: "D1:10. Total: +10." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D1"], desc: "Image uploaded on D1. +5 total." },
      ]},
    ],
    roast: `<p><strong>Ranjoy-Bryan.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Asonganyi Adel Quin",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 22,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 22, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 22, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D3: { pts: 22, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D4: { pts: 22, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D5: { pts: 22, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D6: { pts: 22, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
      D7: { pts: 22, submitted: false, streakDays: 1, workDone: false, workStreakDays: 1 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: true, dayHits: ["D1"], desc: "1 valid form submitted. +10 total." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WORK POST", items: [
        { label: "Work post (image uploaded)", pts: 5, earned: true, dayHits: ["D1"], desc: "Image uploaded on D1. +5 total." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1"], desc: "+2 total." },
      ]},
    ],
    roast: `<p><strong>Asonganyi.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Moh Blessing Kebul",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 15,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 15, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 15, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 15, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 15, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 15, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D3"], desc: "+5 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D3"], desc: "+2 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D3"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Moh.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Favour Hanatu Bako",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 13,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Asked a genuine question", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1"], desc: "+2 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Favour.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Nzameyo Mba",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 13,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 13, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Asked a genuine question", pts: 3, earned: true, dayHits: ["D6"], desc: "+3 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D6"], desc: "+2 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D6"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Nzameyo.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Suilabayu Olga Simolen",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 12,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 12, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 12, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 12, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 12, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 12, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 12, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Helped another member", pts: 5, earned: true, dayHits: ["D2"], desc: "+5 total." },
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D2"], desc: "+2 total." },
      ]},
    ],
    roast: `<p><strong>Suilabayu.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Ngum-nchung Blessing Kah Geh",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 10,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1"], desc: "+2 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Ngum-nchung.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Tchouala Ange",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 10,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 10, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1"], desc: "+2 total." },
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Tchouala.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Fonyuy Berinyuy Tarkighan",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 9,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 9, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 9, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 9, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 9, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 9, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1", "D3"], desc: "+4 total." },
      ]},
    ],
    roast: `<p><strong>Fonyuy.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Chunga Daina",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 8,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Chunga.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Meghiou Nganka Los Esther",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 8,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Meghiou.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Percy Visiy",
    role: "Ambassador",
    joinedDay: "D1",
    allTimeTotal: 8,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 8, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Shared a useful tip or resource", pts: 3, earned: true, dayHits: ["D1"], desc: "+3 total." },
      ]},
    ],
    roast: `<p><strong>Percy.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Bih Cherish Anne",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 7,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1"], desc: "+2 total." },
      ]},
    ],
    roast: `<p><strong>Bih.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Touossoc Ange",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 7,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 7, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
      { section: "WHATSAPP ENGAGEMENT", items: [
        { label: "Posted encouragement that got reactions", pts: 2, earned: true, dayHits: ["D1"], desc: "+2 total." },
      ]},
    ],
    roast: `<p><strong>Touossoc.</strong> You are on this board because you pledged. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Christine",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 5,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
    ],
    roast: `<p><strong>Christine.</strong> You are on this board because you pledged. But pledging was the easy part. You have not submitted a single day yet. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Daniel",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 5,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
    ],
    roast: `<p><strong>Daniel.</strong> You are on this board because you pledged. But pledging was the easy part. You have not submitted a single day yet. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Emmanuel",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 5,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
    ],
    roast: `<p><strong>Emmanuel.</strong> You are on this board because you pledged. But pledging was the easy part. You have not submitted a single day yet. Every day you sit this out, someone else is climbing past you.</p>`,
  },
  {
    name: "Faith",
    role: "Participant",
    joinedDay: "D1",
    allTimeTotal: 5,
    tier: "UNRANKED",
    warnings: [],
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D6: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D7: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
    },
    breakdown: [
      { section: "PRE-PROGRAMME", items: [
        { label: "Pledge", pts: 5, earned: true, dayHits: null, desc: "You committed to the programme. +5 for your pledge." },
      ]},
      { section: "DAILY CHECK-INS", items: [
        { label: "Form submission", pts: 10, earned: false, dayHits: null, desc: "No valid form submissions yet." },
      ]},
      { section: "FIGMA WORK", items: [
        { label: "Creativity scores", pts: null, earned: false, dayHits: null, desc: "No creativity scores awarded yet." },
      ]},
    ],
    roast: `<p><strong>Faith.</strong> You are on this board because you pledged. But pledging was the easy part. You have not submitted a single day yet. Every day you sit this out, someone else is climbing past you.</p>`,
  },
];
export const RULES = [
  { title: "The Check-in Rule", content: "Only the Google Form determines a check-in point (+10) and early bonus (+5 before 3PM). WhatsApp posts alone do not count as check-ins." },
  { title: "Same-Day Requirement", content: "Forms must be submitted on the actual calendar date of the task. Late submissions for past days are disqualified and earn +0 check-in points." },
  { title: "Weekly Milestone (+20)", content: "Awarded on Friday for submitting Figma work in the WhatsApp group during that week. A form submission is not required for the milestone." },
  { title: "Perfect Week (+15)", content: "Awarded on Friday for submitting 5 out of 5 valid same-day check-in forms (Monday to Friday). All 5 must be on the correct day." },
  { title: "Creativity Bonus", content: "Admin-assigned per day: Standard (+5), Good (+10), Impressive (+15), Extraordinary (+20). Only one score per person per day." },
  { title: "Public Interaction", content: "First to post in group (+5), helping a member (+5), asking a genuine question (+3), welcoming a new member (+3), sharing a tip (+3), encouragement with reactions (+2)." },
  { title: "Referral Bonus", content: "Each new member who joins the programme and pledges earns the referring person +25 points, applied once when the pledge is confirmed." },
  { title: "Work Post Bonus (+5)", content: "Awarded once per day when the check-in form shows at least one image uploaded. WhatsApp media alone does not trigger this bonus." },
];
