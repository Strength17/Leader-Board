/**
 * ============================================================
 * SKY GRAPHICS FIGMA EDITION 1 — LEADERBOARD DATA
 * ============================================================
 *
 * STREAK RULES (ENFORCED THROUGHOUT THIS FILE):
 * ──────────────────────────────────────────────
 *
 * RULE 1 — FORM STREAK (streakDays):
 *   Tracks consecutive days the check-in form was submitted.
 *   submitted: true  → streakDays increments by 1
 *   submitted: false → streakDays stops incrementing (does not reset)
 *
 * RULE 2 — WORK STREAK (workDone + workStreakDays):
 *   Tracks consecutive days a student did scored Figma work.
 *   Work is confirmed if a creativity score was awarded that day:
 *   Standard (+5), Good (+10), Impressive (+15), or Extraordinary (+20).
 *   Work CAN be done WITHOUT submitting the form (e.g. posted in WhatsApp).
 *   workDone: true  → student received a creativity score that day
 *   workDone: false → no scored work on that day
 *   workStreakDays  → increments when workDone=true, resets to 0 when workDone=false
 *
 * RULE 3 — FORM IMPLIES WORK:
 *   Every form submission implies work was done.
 *   submitted: true always means workDone: true.
 *   The reverse is NOT true — work can exist without a form submission.
 *
 * ============================================================
 */

export const DAY_LABELS = {
  D1: 'Day 1 — June 1, 2026',
  D2: 'Day 2 — June 2, 2026',
  D3: 'Day 3 — June 3, 2026',
  D4: 'Day 4 — June 4, 2026',
  D5: 'Day 5 — June 5, 2026',
  D6: 'Day 6 — Locked',
  D7: 'Day 7 — Locked',
  D8: 'Day 8 — Locked',
  D9: 'Day 9 — Locked',
  D10: 'Day 10 — Locked'
};

export const TIER_EMOJI = {
  PLATINUM: '🏆',
  GOLD: '🥇',
  SILVER: '🥈',
  BRONZE: '🥉',
  UNRANKED: '⬜'
};

export const PEOPLE = [
  {
    name: "Christine Choundong", role: "Ambassador", allTimeTotal: 220, tier: "SILVER",
    days: {
      D1: { pts: 80, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 120, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 145, submitted: true, streakDays: 3, workDone: true, workStreakDays: 3 },
      D4: { pts: 170, submitted: true, streakDays: 4, workDone: true, workStreakDays: 4 },
      D5: { pts: 220, submitted: true, streakDays: 5, workDone: true, workStreakDays: 5 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed to the programme and joined officially. +5 for your pledge." },
          { label: "Referral × 2", pts: 50, earned: true, days: null, desc: "You referred 2 members who joined the programme. +25 per referral = +50." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D3", "D4", "D5"], desc: "You submitted the daily check-in form. +10 automatic per day." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for the +5 early bonus." }
        ]
      },
      {
        section: "SECTION 2 — WHATSAPP GROUP", items: [
          { label: "First to post check-in in group", pts: 5, earned: true, days: ["D1", "D2", "D3", "D4"], dayHits: ["D2", "D3", "D4"], desc: "You were the first member to post your check-in update in the WhatsApp group." },
          { label: "Asked a genuine question", pts: 3, earned: false, days: null, desc: "Ask one real question per day about the course or Figma. +3 pts." },
          { label: "Helped another member", pts: 5, earned: false, days: null, desc: "Give a real helpful answer to someone else's question. +5 pts." },
          { label: "Welcomed a new member", pts: 3, earned: false, days: null, desc: "Greet a new member who just joined before the admin does. +3 pts." },
          { label: "Shared a useful tip or resource", pts: 3, earned: false, days: null, desc: "Share something helpful — a shortcut, trick or link without being asked. +3 pts." },
          { label: "Posted encouragement with reactions", pts: 2, earned: false, days: null, desc: "Post genuine encouragement that gets reactions from others. +2 pts." }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D3", "D4", "D5"], desc: "D1: Good +10 · D2: Extraordinary +20 (StudyBuddy app) · D3: Standard +5 · D4: Standard +5 · D5: Standard +5" }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D3", "D4", "D5"], desc: "You uploaded your Figma screenshot each day. +5 automatic per image." },
          { label: "Heart + Comment + Share screenshot (+10 extra)", pts: 10, earned: false, days: null, desc: "Screenshot proving all 3 Facebook actions earns +10 extra." },
          { label: "Group share screenshot (+5 extra)", pts: 5, earned: false, days: null, desc: "Facebook group share screenshot earns +5 extra." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Referral bonus", pts: 50, earned: true, days: null, desc: "You referred 2 members. +50." },
          { label: "Phase completion", pts: 20, earned: true, days: null, desc: "Confirmed by admin on phase completion. Week 1 Mastered! +20 pts." },
          { label: "Perfect week (5-day streak)", pts: 15, earned: true, days: null, desc: "Submit every day Mon–Fri. Awarded on Friday. +15 pts." },
          { label: "Special bonus", pts: 0, earned: false, days: null, desc: "Special bonuses announced by instructor. Varies." }
        ]
      }
    ],
    roast: `<p>Let's be real for a second, Christine.</p><p>You finished Week 1 with 220 points. You are the Gold standard (literally, almost GOLD tier). You got the Perfect Week bonus and Phase Completion. You are dominating the Ambassador board.</p><p>But those Facebook interaction points are still at zero. Imagine if you had those extra 75 points from Hearting, commenting, and sharing every day. You would be at 295 — well into the GOLD tier already.</p><p>Week 2 is a fresh start. Don't just build extraordinary designs; build an untouchable score. The Facebook points are the easiest points in the game. Take them.</p>`
  },
  {
    name: "Oluwasegun Daniel Osawore", role: "Ambassador", allTimeTotal: 175, tier: "SILVER",
    days: {
      D1: { pts: 85, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 115, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 140, submitted: true, streakDays: 3, workDone: true, workStreakDays: 3 },
      D4: { pts: 140, submitted: false, streakDays: 3, workDone: false, workStreakDays: 0 },
      D5: { pts: 175, submitted: true, streakDays: 4, workDone: true, workStreakDays: 1 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed to the programme and joined officially. +5 for your pledge." },
          { label: "Referral × 3", pts: 75, earned: true, days: null, desc: "You referred 3 members (including +25 Day 5 bonus referral). +75." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D3", "D5"], desc: "Submitted Days 1, 2, 3, 5. +10 per day." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for +5 early bonus." }
        ]
      },
      {
        section: "SECTION 2 — WHATSAPP GROUP", items: [
          { label: "First to post check-in in group", pts: 5, earned: true, days: ["D1", "D5"], dayHits: ["D1", "D5"], desc: "You were the first to post on Day 1 and Day 5. +5 each." },
          { label: "Asked a genuine question", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Helped another member", pts: 5, earned: false, days: null, desc: "+5 pts." },
          { label: "Welcomed a new member", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Shared a useful tip", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Posted encouragement with reactions", pts: 2, earned: false, days: null, desc: "+2 pts." }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D3", "D5"], desc: "D1: Good +10 · D2: Impressive +15 · D3: Good +10 · D5: Standard +5." }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: true, days: ["D1", "D2", "D3", "D5"], dayHits: ["D1", "D2", "D3", "D5"], desc: "Uploaded screenshots. +5 each." },
          { label: "Heart + Comment + Share screenshot (+10 extra)", pts: 10, earned: false, days: null, desc: "+10 extra." },
          { label: "Group share screenshot (+5 extra)", pts: 5, earned: false, days: null, desc: "+5 extra." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Referral bonus", pts: 75, earned: true, days: null, desc: "3 referrals × +25 = +75. (Final referral bonus added Day 5)." },
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Missed Day 4 submission." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "Missed Day 4 submission." },
          { label: "Special bonus", pts: 0, earned: false, days: null, desc: "Varies." }
        ]
      }
    ],
    roast: `<p>Oluwasegun. You finished the week with a strong Day 5 comeback. You hit the SILVER tier (175 points) and added a 3rd referral. You were the first to post check-in twice this week. Excellent leadership energy.</p><p>But that Day 4 gap cost you the Perfect Week (+15) and Phase Completion (+20) bonuses. That's 35 points you left on the table. You'd be at 210 points right now if you hadn't missed that one form.</p><p>Week 2 is your chance to go for the full streak. And remember — upgrade those photo credits to Facebook interaction screenshots for an extra +10 per day. You're too close to the top to be leaving points behind.</p>`
  },
  {
    name: "Malialia Celine Bride", role: "Ambassador", allTimeTotal: 85, tier: "BRONZE",
    days: {
      D1: { pts: 85, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 85, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 85, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 85, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 85, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially. +5." },
          { label: "Referral × 3", pts: 75, earned: true, days: null, desc: "You referred 3 members who joined. +75." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "No forms submitted yet. +10 per submission." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for +5 bonus." }
        ]
      },
      {
        section: "SECTION 2 — WHATSAPP GROUP", items: [
          { label: "First to post check-in in group", pts: 5, earned: true, days: ["D1"], dayHits: ["D1"], desc: "First to post on Day 1. +5." },
          { label: "Asked a genuine question", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Helped another member", pts: 5, earned: false, days: null, desc: "+5 pts." },
          { label: "Welcomed a new member", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Shared a useful tip", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Posted encouragement with reactions", pts: 2, earned: false, days: null, desc: "+2 pts." }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "No work submitted." }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: false, days: null, desc: "+5 each." },
          { label: "Heart + Comment + Share screenshot (+10 extra)", pts: 10, earned: false, days: null, desc: "+10 extra." },
          { label: "Group share screenshot (+5 extra)", pts: 5, earned: false, days: null, desc: "+5 extra." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Referral bonus", pts: 75, earned: true, days: null, desc: "3 referrals × +25 = +75." },
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Incomplete week." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "No streak." },
          { label: "Special bonus", pts: 0, earned: false, days: null, desc: "Varies." }
        ]
      }
    ],
    roast: `<p>Malialia. You started with 85 points from referrals and a pledge. You were the first to post on Day 1. You have 3 active recruits in this programme.</p><p>But you have not submitted a single check-in form all week. Not one. You are sitting at the bottom of the active Ambassador board while your referrals are climbing toward Silver.</p><p>Week 2 is a clean slate. Show your recruits how it's done. Three minutes a day for the form. That's all it takes to start moving again.</p>`
  },
  {
    name: "Mbiydzenyuy Patience Dzekem", role: "Ambassador", allTimeTotal: 65, tier: "BRONZE",
    days: {
      D1: { pts: 35, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 65, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 65, submitted: false, streakDays: 2, workDone: false, workStreakDays: 0 },
      D4: { pts: 65, submitted: false, streakDays: 2, workDone: false, workStreakDays: 0 },
      D5: { pts: 65, submitted: false, streakDays: 2, workDone: false, workStreakDays: 0 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2"], desc: "Submitted Days 1 & 2. Missed Days 3, 4, 5." },
          { label: "First to submit check-in form", pts: 5, earned: true, days: ["D1"], dayHits: ["D1"], desc: "First to submit form Day 1. +5." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for +5 bonus." }
        ]
      },
      {
        section: "SECTION 2 — WHATSAPP GROUP", items: [
          { label: "First to post check-in in group", pts: 5, earned: false, days: null, desc: "+5 pts." },
          { label: "Asked a genuine question", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Helped another member", pts: 5, earned: false, days: null, desc: "+5 pts." },
          { label: "Welcomed a new member", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Shared a useful tip", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Posted encouragement with reactions", pts: 2, earned: false, days: null, desc: "+2 pts." }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2"], desc: "D1: Good +10 · D2: Impressive +15 · D3–D5: No submission." }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2"], desc: "Uploaded screenshots D1 & D2. +5 each." },
          { label: "Heart + Comment + Share screenshot (+10 extra)", pts: 10, earned: false, days: null, desc: "+15 total per screenshot." },
          { label: "Group share screenshot (+5 extra)", pts: 5, earned: false, days: null, desc: "+10 total per group share screenshot." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Incomplete week." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "Streak broken Day 3." },
          { label: "Special bonus", pts: 0, earned: false, days: null, desc: "Varies." }
        ]
      }
    ],
    roast: `<p>Patience. You were the fastest to the form on Day 1. You hit Impressive work on Day 2. You have the raw talent to lead this board.</p><p>But talent doesn't win if you don't show up. You missed the last three days of Week 1. You're sitting at 65 points while others are crossing 200.</p><p>Week 2 is your reset button. Use that speed and quality every day, not just the first two. Let's see you hit Silver by next Wednesday.</p>`
  },
  {
    name: "Irinyemi Adedayo Juliet", role: "Ambassador", allTimeTotal: 50, tier: "BRONZE",
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 25, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D3: { pts: 25, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 },
      D4: { pts: 50, submitted: true, streakDays: 2, workDone: true, workStreakDays: 1 },
      D5: { pts: 50, submitted: false, streakDays: 2, workDone: false, workStreakDays: 0 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D2", "D4"], desc: "Submitted Days 2 & 4. Missed Days 1, 3, 5." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for +5 bonus." }
        ]
      },
      {
        section: "SECTION 2 — WHATSAPP GROUP", items: [
          { label: "First to post check-in in group", pts: 5, earned: false, days: null, desc: "+5 pts." },
          { label: "Asked a genuine question", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Helped another member", pts: 5, earned: false, days: null, desc: "+5 pts." },
          { label: "Welcomed a new member", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Shared a useful tip", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Posted encouragement with reactions", pts: 2, earned: false, days: null, desc: "+2 pts." }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D2", "D4"], desc: "D2: Standard +5 · D4: Good +10." }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D2", "D4"], desc: "Uploaded screenshots D2 & D4. +5 each." },
          { label: "Heart + Comment + Share screenshot (+10 extra)", pts: 10, earned: false, days: null, desc: "+10 extra." },
          { label: "Group share screenshot (+5 extra)", pts: 5, earned: false, days: null, desc: "+5 extra." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Incomplete week." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "No streak." },
          { label: "Special bonus", pts: 0, earned: false, days: null, desc: "Varies." }
        ]
      }
    ],
    roast: `<p>Juliet. You hit Bronze (50 points) just in time. Your Day 4 work was Good. You're making progress.</p><p>But the "every-other-day" habit is holding you back. You missed Day 5, which means you missed the chance to build momentum heading into Week 2.</p><p>Don't just aim for Bronze. Aim for Silver. It starts with submitting the form every single day. No exceptions.</p>`
  },
  {
    name: "Frank Emmanuel", role: "Ambassador", allTimeTotal: 5, tier: "UNRANKED",
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "No forms submitted yet." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for +5 bonus." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Incomplete week." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "No streak." },
          { label: "Special bonus", pts: 0, earned: false, days: null, desc: "Varies." }
        ]
      }
    ],
    roast: `<p>Frank. 5 points. Week 1 is over and you haven't moved since the pledge. As an Ambassador, your team is looking for you on the board. Week 2 starts Monday — be there.</p>`
  },
  {
    name: "Percy Visiy", role: "Ambassador", allTimeTotal: 5, tier: "UNRANKED",
    days: {
      D1: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 5, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Incomplete week." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "No streak." }
        ]
      }
    ],
    roast: `<p>Percy. 5 points. One week down. Time to step up for Week 2. Don't let the board leave you behind.</p>`
  },
  {
    name: "Faith Emmanuella Busari", role: "Participant", allTimeTotal: 110, tier: "BRONZE",
    days: {
      D1: { pts: 95, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 95, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 95, submitted: false, streakDays: 2, workDone: false, workStreakDays: 0 },
      D4: { pts: 95, submitted: false, streakDays: 2, workDone: false, workStreakDays: 0 },
      D5: { pts: 110, submitted: true, streakDays: 3, workDone: true, workStreakDays: 1 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." },
          { label: "Referral × 1", pts: 25, earned: true, days: null, desc: "You referred 1 member. +25." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D5"], desc: "D1: +10 · D2: +10 · D5: +10." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Late D1 submission (17:36). No early bonus." }
        ]
      },
      {
        section: "SECTION 2 — WHATSAPP GROUP", items: [
          { label: "First to post check-in in group", pts: 5, earned: false, days: null, desc: "+5 pts." },
          { label: "Asked a genuine question", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Helped another member", pts: 5, earned: false, days: null, desc: "+5 pts." },
          { label: "Welcomed a new member", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Shared a useful tip", pts: 3, earned: false, days: null, desc: "+3 pts." },
          { label: "Posted encouragement with reactions", pts: 2, earned: false, days: null, desc: "+2 pts." }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D5"], desc: "D1: Good +10 · D2: Extraordinary +20 · D5: Standard +5." }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D5"], desc: "D1: +10 · D2: +5 · D5: +5." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Referral bonus", pts: 25, earned: true, days: null, desc: "Referred 1 member. +25." },
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Missed work D3 & D4." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "Streak broken Day 3." },
          { label: "Special bonus", pts: 0, earned: false, days: null, desc: "Varies." }
        ]
      }
    ],
    roast: `<p>Faith. You finished Week 1 with 110 points. You're the top participant, but you're only 10 points ahead of Silver. You hit an Extraordinary score on Day 2, proving you have the skills to be #1.</p><p>But the two-day gap in the middle of the week cost you the Phase Completion and Perfect Week bonuses. That's 35 points missed. You could be at 145 right now — one point away from Silver.</p><p>Week 2 is about consistency. Don't let your talent go to waste by missing days. Show up every day, submit before 3PM, and let's see you hit Silver by Tuesday.</p>`
  },
  {
    name: "Emmanuel Karol Tchouani", role: "Participant", allTimeTotal: 165, tier: "SILVER",
    days: {
      D1: { pts: 55, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 80, submitted: true, streakDays: 2, workDone: true, workStreakDays: 2 },
      D3: { pts: 100, submitted: true, streakDays: 3, workDone: true, workStreakDays: 3 },
      D4: { pts: 115, submitted: true, streakDays: 4, workDone: true, workStreakDays: 4 },
      D5: { pts: 165, submitted: true, streakDays: 5, workDone: true, workStreakDays: 5 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." },
          { label: "Referral × 1", pts: 25, earned: true, days: null, desc: "You referred 1 member. +25." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D3", "D4", "D5"], desc: "Submitted all 5 days. Perfect attendance! +10 per day." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Late submissions each day. Set an alarm for +5 extra per day!" }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D3", "D4", "D5"], desc: "D1: Good +10 · D2: Good +10 · D3: Standard +5 · D4: Standard +5 · D5: Standard +5." }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1", "D2", "D3", "D4", "D5"], desc: "Uploaded screenshots all 5 days. +5 each." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Referral bonus", pts: 25, earned: true, days: null, desc: "Referred 1 member. +25." },
          { label: "Phase completion", pts: 20, earned: true, days: null, desc: "You participated in every single day of Week 1! +20 bonus." },
          { label: "Perfect week (5-day streak)", pts: 15, earned: true, days: null, desc: "A 5-day streak of form submissions! Excellent! +15 bonus." },
          { label: "Special bonus", pts: 0, earned: false, days: null, desc: "Varies." }
        ]
      }
    ],
    roast: `<p>Emmanuel. Look at you! 165 points. Silver tier. You are the only participant to hit Silver in Week 1. You got the Perfect Week AND Phase Completion bonuses. That is pure discipline.</p><p>You're only 85 points away from GOLD. If you keep this exact same energy in Week 2 and start submitting before 3PM, you'll be at 250 by next Friday easily.</p><p>One small tip: those photo credits can be +15 points instead of +5 if you upload a screenshot showing a Heart, comment, and share. Do that for 5 days in Week 2 and you'll add another +50 points to your total. Don't leave points on the table.</p>`
  },
  {
    name: "Abongnwi Chrioni-Opal Forba'", role: "Participant", allTimeTotal: 90, tier: "BRONZE",
    days: {
      D1: { pts: 30, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 35, submitted: false, streakDays: 0, workDone: true, workStreakDays: 1 },
      D3: { pts: 45, submitted: false, streakDays: 0, workDone: true, workStreakDays: 2 },
      D4: { pts: 55, submitted: false, streakDays: 0, workDone: true, workStreakDays: 3 },
      D5: { pts: 90, submitted: true, streakDays: 1, workDone: true, workStreakDays: 4 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." },
          { label: "Referral × 1", pts: 25, earned: true, days: null, desc: "You referred 1 member. +25." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D5"], desc: "Submitted form Day 5. +10. (Built work D2-D4 but missed forms)." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for +5 bonus." }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D2", "D3", "D4", "D5"], desc: "D1: Missed · D2: Standard +5 · D3: Good +10 · D4: Standard +5 · D5: Standard +5." }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D4", "D5"], desc: "Uploaded D4 & D5 screenshots. +5 each." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Referral bonus", pts: 25, earned: true, days: null, desc: "Referred 1 member. +25." },
          { label: "Phase completion", pts: 20, earned: true, days: null, desc: "Participated (Work or Form) every day! +20 bonus." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "Missed check-in forms D1-D4." },
          { label: "Special bonus", pts: 5, earned: true, days: null, desc: "D4 Photo credit bonus. +5." }
        ]
      }
    ],
    roast: `<p>Chrioni. You hit 90 points and Bronze tier! You got the Phase Completion bonus because you built something every single day this week. That shows real commitment to the craft.</p><p>But imagine where you'd be if you had actually submitted the form those first four days. You'd have another 40 points in automatic check-ins. You'd be at 130 — 20 points from Silver.</p><p>You did the hard part (the work) but skipped the easy part (the form). Week 2 is for doing both. Every day. Let's see you hit Silver by next Thursday.</p>`
  },
  {
    name: "Mbishitehnyi Ryan", role: "Participant", allTimeTotal: 25, tier: "UNRANKED",
    days: {
      D1: { pts: 25, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D2: { pts: 25, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D3: { pts: 25, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D4: { pts: 25, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 },
      D5: { pts: 25, submitted: false, streakDays: 0, workDone: false, workStreakDays: 0 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Referral × 1", pts: 25, earned: true, days: null, desc: "You referred 1 member who joined. +25." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "No submissions yet. Each form = +10 pts." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for +5 bonus." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Incomplete week." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "No streak." }
        ]
      }
    ],
    roast: `<p>Ryan. 25 points. Week 1 is done. You referred someone, so you're part of the team. Now it's time to actually show up on the board. Week 2 starts Monday. Three minutes a day for the form. Let's get to Bronze.</p>`
  },
  {
    name: "Ranjoy-Bryan", role: "Participant", allTimeTotal: 30, tier: "UNRANKED",
    days: {
      D1: { pts: 30, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 },
      D3: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 },
      D4: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 },
      D5: { pts: 30, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1"], desc: "Submitted Day 1 only. +10. Missed Days 2-5." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "Submit before 3PM for +5 bonus." }
        ]
      },
      {
        section: "SECTION 3 — FIGMA WORK CREATIVITY", items: [
          { label: "Work scored per day", pts: null, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1"], desc: "D1: Good +10. Excellent start." }
        ]
      },
      {
        section: "SECTION 4 — FACEBOOK INTERACTIONS", items: [
          { label: "Image uploaded (base +5 each)", pts: 5, earned: true, days: ["D1"], dayHits: ["D1"], desc: "Uploaded D1 screenshot. +5." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Incomplete week." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "No streak." }
        ]
      }
    ],
    roast: `<p>Ranjoy. You hit a "Good" score on Day 1. You have the skills. But you've been silent for 4 days. Week 2 is your reset. Show us that Day 1 energy every day. Bronze is only 20 points away.</p>`
  },
  {
    name: "Asonganyi Adel Quin", role: "Participant", allTimeTotal: 15, tier: "UNRANKED",
    days: {
      D1: { pts: 15, submitted: true, streakDays: 1, workDone: true, workStreakDays: 1 },
      D2: { pts: 15, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 },
      D3: { pts: 15, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 },
      D4: { pts: 15, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 },
      D5: { pts: 15, submitted: false, streakDays: 1, workDone: false, workStreakDays: 0 }
    },
    breakdown: [
      {
        section: "PRE-PROGRAMME", items: [
          { label: "Pledge", pts: 5, earned: true, days: null, desc: "You committed officially." }
        ]
      },
      {
        section: "SECTION 1 — DAILY CHECK-IN (Automatic)", items: [
          { label: "Check-in form submission", pts: 10, earned: true, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: ["D1"], desc: "Submitted Day 1 only. +10." },
          { label: "Early submission (before 3PM)", pts: 5, earned: false, days: ["D1", "D2", "D3", "D4", "D5"], dayHits: [], desc: "+5 early bonus available daily." }
        ]
      },
      {
        section: "SECTION 5 — BONUS POINTS", items: [
          { label: "Phase completion", pts: 20, earned: false, days: null, desc: "Incomplete week." },
          { label: "Perfect week", pts: 15, earned: false, days: null, desc: "No streak." }
        ]
      }
    ],
    roast: `<p>Adel. 15 points. Week 1 is over. Time to lock in for Week 2. You only need 35 points for Bronze. You can do that in two days. See you Monday.</p>`
  }
];

// Pledge-only participants
export const PLEDGE_ONLY = [
  "Moh Blessing Kebul", "Chi Yoland Sah", "Nkongmi Loise Asonyuy", "Assaah Nzota",
  "Binda Joel", "Open Bryan", "Kemni Samuel Bemsimbom", "Andin Blanch",
  "Kelly Brenda Keafon", "Nkwain Harzel", "Tsopmo Precious", "Touossoc Ange",
  "Suilabayu Olga Simolen", "Fonyuy Berinyuy Tarkighan", "Akuchu Tohla Tchosi-Ambom"
];

export const SNAPSHOTS = {
  D1: {
    Ambassador: [
      { name: "Christine Choundong", pts: 80, tier: "BRONZE", submitted: true },
      { name: "Oluwasegun Daniel Osawore", pts: 85, tier: "BRONZE", submitted: true },
      { name: "Malialia Celine Bride", pts: 85, tier: "BRONZE", submitted: false },
      { name: "Mbiydzenyuy Patience Dzekem", pts: 35, tier: "UNRANKED", submitted: true },
      { name: "Irinyemi Adedayo Juliet", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Frank Emmanuel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Percy Visiy", pts: 5, tier: "UNRANKED", submitted: false }
    ],
    Participant: [
      { name: "Faith Emmanuella Busari", pts: 95, tier: "BRONZE", submitted: true },
      { name: "Emmanuel Karol Tchouani", pts: 55, tier: "BRONZE", submitted: true },
      { name: "Abongnwi Chrioni-Opal Forba'", pts: 30, tier: "UNRANKED", submitted: false },
      { name: "Mbishitehnyi Ryan", pts: 25, tier: "UNRANKED", submitted: false },
      { name: "Ranjoy-Bryan", pts: 30, tier: "UNRANKED", submitted: true },
      { name: "Asonganyi Adel Quin", pts: 15, tier: "UNRANKED", submitted: true },
      { name: "Chi Yoland Sah", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkongmi Loise Asonyuy", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Assaah Nzota", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Binda Joel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Open Bryan", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kemni Samuel Bemsimbom", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Andin Blanch", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kelly Brenda Keafon", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkwain Harzel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Tsopmo Precious", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Touossoc Ange", pts: 5, tier: "UNRANKED", submitted: false },
    ]
  },
  D2: {
    Ambassador: [
      { name: "Christine Choundong", pts: 120, tier: "BRONZE", submitted: true },
      { name: "Oluwasegun Daniel Osawore", pts: 115, tier: "BRONZE", submitted: true },
      { name: "Malialia Celine Bride", pts: 85, tier: "BRONZE", submitted: false },
      { name: "Mbiydzenyuy Patience Dzekem", pts: 65, tier: "BRONZE", submitted: true },
      { name: "Irinyemi Adedayo Juliet", pts: 25, tier: "UNRANKED", submitted: true },
      { name: "Frank Emmanuel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Percy Visiy", pts: 5, tier: "UNRANKED", submitted: false }
    ],
    Participant: [
      { name: "Faith Emmanuella Busari", pts: 95, tier: "BRONZE", submitted: true },
      { name: "Emmanuel Karol Tchouani", pts: 80, tier: "BRONZE", submitted: true },
      { name: "Abongnwi Chrioni-Opal Forba'", pts: 35, tier: "UNRANKED", submitted: false },
      { name: "Mbishitehnyi Ryan", pts: 25, tier: "UNRANKED", submitted: false },
      { name: "Ranjoy-Bryan", pts: 30, tier: "UNRANKED", submitted: false },
      { name: "Suilabayu Olga Simolen", pts: 5, tier: "UNRANKED", submitted: true },
      { name: "Asonganyi Adel Quin", pts: 15, tier: "UNRANKED", submitted: false },
      { name: "Chi Yoland Sah", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkongmi Loise Asonyuy", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Assaah Nzota", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Binda Joel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Open Bryan", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kemni Samuel Bemsimbom", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Andin Blanch", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kelly Brenda Keafon", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkwain Harzel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Tsopmo Precious", pts: 5, tier: "UNRANKED", submitted: false },
    ]
  },
  D3: {
    Ambassador: [
      { name: "Christine Choundong", pts: 145, tier: "BRONZE", submitted: true },
      { name: "Oluwasegun Daniel Osawore", pts: 140, tier: "BRONZE", submitted: true },
      { name: "Malialia Celine Bride", pts: 85, tier: "BRONZE", submitted: false },
      { name: "Mbiydzenyuy Patience Dzekem", pts: 65, tier: "BRONZE", submitted: false },
      { name: "Irinyemi Adedayo Juliet", pts: 25, tier: "UNRANKED", submitted: false },
      { name: "Frank Emmanuel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Percy Visiy", pts: 5, tier: "UNRANKED", submitted: false }
    ],
    Participant: [
      { name: "Faith Emmanuella Busari", pts: 95, tier: "BRONZE", submitted: false },
      { name: "Emmanuel Karol Tchouani", pts: 100, tier: "BRONZE", submitted: true },
      { name: "Abongnwi Chrioni-Opal Forba'", pts: 45, tier: "UNRANKED", submitted: false },
      { name: "Mbishitehnyi Ryan", pts: 25, tier: "UNRANKED", submitted: false },
      { name: "Ranjoy-Bryan", pts: 30, tier: "UNRANKED", submitted: false },
      { name: "Asonganyi Adel Quin", pts: 15, tier: "UNRANKED", submitted: false },
      { name: "Moh Blessing Kebul", pts: 5, tier: "UNRANKED", submitted: true },
      { name: "Fonyuy Berinyuy Tarkighan", pts: 5, tier: "UNRANKED", submitted: true },
      { name: "Akuchu Tohla Tchosi-Ambom", pts: 5, tier: "UNRANKED", submitted: true },
      { name: "Chi Yoland Sah", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkongmi Loise Asonyuy", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Assaah Nzota", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Binda Joel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Open Bryan", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kemni Samuel Bemsimbom", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Andin Blanch", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kelly Brenda Keafon", pts: 5, tier: "UNRANKED", submitted: false },
    ]
  },
  D4: {
    Ambassador: [
      { name: "Christine Choundong", pts: 170, tier: "SILVER", submitted: true },
      { name: "Oluwasegun Daniel Osawore", pts: 140, tier: "BRONZE", submitted: false },
      { name: "Malialia Celine Bride", pts: 85, tier: "BRONZE", submitted: false },
      { name: "Mbiydzenyuy Patience Dzekem", pts: 65, tier: "BRONZE", submitted: false },
      { name: "Irinyemi Adedayo Juliet", pts: 50, tier: "BRONZE", submitted: true },
      { name: "Frank Emmanuel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Percy Visiy", pts: 5, tier: "UNRANKED", submitted: false }
    ],
    Participant: [
      { name: "Emmanuel Karol Tchouani", pts: 115, tier: "BRONZE", submitted: true },
      { name: "Faith Emmanuella Busari", pts: 95, tier: "BRONZE", submitted: false },
      { name: "Abongnwi Chrioni-Opal Forba'", pts: 55, tier: "BRONZE", submitted: false },
      { name: "Mbishitehnyi Ryan", pts: 25, tier: "UNRANKED", submitted: false },
      { name: "Ranjoy-Bryan", pts: 30, tier: "UNRANKED", submitted: false },
      { name: "Asonganyi Adel Quin", pts: 15, tier: "UNRANKED", submitted: false },
      { name: "Moh Blessing Kebul", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Chi Yoland Sah", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkongmi Loise Asonyuy", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Assaah Nzota", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Binda Joel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Open Bryan", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kemni Samuel Bemsimbom", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Andin Blanch", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kelly Brenda Keafon", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkwain Harzel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Tsopmo Precious", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Touossoc Ange", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Suilabayu Olga Simolen", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Fonyuy Berinyuy Tarkighan", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Akuchu Tohla Tchosi-Ambom", pts: 5, tier: "UNRANKED", submitted: false },
    ]
  },
  D5: {
    Ambassador: [
      { name: "Christine Choundong", pts: 220, tier: "SILVER", submitted: true },
      { name: "Oluwasegun Daniel Osawore", pts: 175, tier: "SILVER", submitted: true },
      { name: "Malialia Celine Bride", pts: 85, tier: "BRONZE", submitted: false },
      { name: "Mbiydzenyuy Patience Dzekem", pts: 65, tier: "BRONZE", submitted: false },
      { name: "Irinyemi Adedayo Juliet", pts: 50, tier: "BRONZE", submitted: false },
      { name: "Frank Emmanuel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Percy Visiy", pts: 5, tier: "UNRANKED", submitted: false }
    ],
    Participant: [
      { name: "Emmanuel Karol Tchouani", pts: 165, tier: "SILVER", submitted: true },
      { name: "Faith Emmanuella Busari", pts: 110, tier: "BRONZE", submitted: true },
      { name: "Abongnwi Chrioni-Opal Forba'", pts: 95, tier: "BRONZE", submitted: true },
      { name: "Ranjoy-Bryan", pts: 30, tier: "UNRANKED", submitted: false },
      { name: "Mbishitehnyi Ryan", pts: 25, tier: "UNRANKED", submitted: false },
      { name: "Asonganyi Adel Quin", pts: 15, tier: "UNRANKED", submitted: false },
      { name: "Moh Blessing Kebul", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Chi Yoland Sah", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkongmi Loise Asonyuy", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Assaah Nzota", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Binda Joel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Open Bryan", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kemni Samuel Bemsimbom", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Andin Blanch", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Kelly Brenda Keafon", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Nkwain Harzel", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Tsopmo Precious", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Touossoc Ange", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Suilabayu Olga Simolen", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Fonyuy Berinyuy Tarkighan", pts: 5, tier: "UNRANKED", submitted: false },
      { name: "Akuchu Tohla Tchosi-Ambom", pts: 5, tier: "UNRANKED", submitted: false },
    ]
  }
};
