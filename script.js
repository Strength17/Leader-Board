import { PEOPLE, DAY_LABELS, TIER_EMOJI, RULES } from './data.js';

/* ─────────────────────────────────────────────────
   STATE
───────────────────────────────────────────────── */
let currentWeek = 1;
let currentDay  = 'D1';
let currentTab  = 'participants';
let currentPTab = 'breakdown';

const TOTAL_WEEKS = 6;       /* number of week pills shown in nav */
const DAYS_PER_WEEK = 5;      /* days per week */

/* ─────────────────────────────────────────────────
   HELPERS
───────────────────────────────────────────────── */
function tierClass(t){ return t || 'UNRANKED'; }
function ptsColor(r){ return r===1?'var(--amber)':r===2?'#CBD5E1':r===3?'#CD7F32':'var(--white)'; }
function rowClass(r){ return r===1?'rank-1':r===2?'rank-2':r===3?'rank-3':''; }
function safeName(n){ return n.replace(/\\/g,'\\\\').replace(/'/g,"\\'"); }

/* ─────────────────────────────────────────────────
   DYNAMIC DAY/WEEK UNLOCKING
───────────────────────────────────────────────── */
function getCanonicalDayOrder(){
  let order = [];
  if (typeof DAY_LABELS !== 'undefined' && DAY_LABELS) {
    order = Object.keys(DAY_LABELS);
  }
  const need = TOTAL_WEEKS * DAYS_PER_WEEK;
  for (let i = 1; i <= need; i++) {
    const key = 'D' + i;
    if (!order.includes(key)) order.push(key);
  }
  order.sort((a,b) => parseInt(a.slice(1),10) - parseInt(b.slice(1),10));
  return order;
}

function computeLiveDays(){
  const set = new Set();
  (PEOPLE || []).forEach(p => {
    if (p.days) Object.keys(p.days).forEach(d => set.add(d));
  });
  return set;
}

function getLatestDayNum(liveSet){
  let max = 0;
  liveSet.forEach(d => {
    const n = parseInt(d.slice(1),10);
    if (!isNaN(n) && n > max) max = n;
  });
  return max;
}

function buildWeekDays(order){
  const weeks = {};
  for (let w = 1; w <= TOTAL_WEEKS; w++) {
    const start = (w-1) * DAYS_PER_WEEK;
    weeks[w] = order.slice(start, start + DAYS_PER_WEEK);
  }
  return weeks;
}

const CANONICAL_DAY_ORDER = getCanonicalDayOrder();
const WEEK_DAYS  = buildWeekDays(CANONICAL_DAY_ORDER);
const LIVE_DAYS  = computeLiveDays();
const LATEST_DAY_NUM = getLatestDayNum(LIVE_DAYS);

/* ─────────────────────────────────────────────────
   WARNING TOGGLE
───────────────────────────────────────────────── */
window.toggleWarning = function(btn) {
  const details = btn.parentElement.nextElementSibling;
  const isExpanded = details.style.display === 'block';
  details.style.display = isExpanded ? 'none' : 'block';
  btn.textContent = isExpanded ? 'Details ▼' : 'Details ▲';
};

/* ─────────────────────────────────────────────────
   WEEK/DAY SELECTORS & RENDERING
───────────────────────────────────────────────── */
function renderWeekSelector(){
  const row = document.getElementById('week-row');
  if (!row) return;
  let html = '';
  for (let w = 1; w <= TOTAL_WEEKS; w++) {
    const days     = WEEK_DAYS[w];
    const firstNum = parseInt(days[0].slice(1),10);
    const lastNum  = parseInt(days[days.length-1].slice(1),10);
    let status;
    if (LATEST_DAY_NUM >= lastNum)       status = 'done';
    else if (LATEST_DAY_NUM >= firstNum) status = 'live';
    else                                  status = 'locked';

    if (status === 'locked') {
      html += `<div class="week-pill locked">Week ${w} 🔒</div>`;
    } else {
      const isActive = w === currentWeek;
      const badge = status === 'live' ? '<span class="week-badge live">Live</span>' : '<span class="week-badge">Done</span>';
      html += `<div class="week-pill${isActive?' active':''}" data-week="${w}" onclick="window.setWeek(${w})">Week ${w} ${badge}</div>`;
    }
  }
  row.innerHTML = html;
}

window.setWeek = function(week) {
  const days = WEEK_DAYS[week];
  if (!days) return;
  const firstNum = parseInt(days[0].slice(1),10);
  if (LATEST_DAY_NUM < firstNum) return;
  currentWeek = week;
  renderWeekSelector();
  renderDaySelector();
  const liveDays = days.filter(d => LIVE_DAYS.has(d));
  const defaultDay = liveDays.length ? liveDays[liveDays.length-1] : days[0];
  window.setDay(defaultDay);
};

function renderDaySelector() {
  const tray = document.getElementById('day-selector');
  if (!tray) return;
  tray.classList.remove('day-tray');
  void tray.offsetWidth;
  tray.classList.add('day-tray');
  const days = WEEK_DAYS[currentWeek];
  let html = '';
  days.forEach((dKey, idx) => {
    const dayNum    = parseInt(dKey.slice(1));
    const isLocked  = !LIVE_DAYS.has(dKey);
    const isActive  = currentDay === dKey;
    const isMile    = (idx+1) % 5 === 0;
    html += `<button class="day-pill${isActive?' active':''}${isMile?' milestone':''}${isLocked?' locked':''}" data-day="${dKey}" ${isLocked ? 'disabled' : `onclick="window.setDay('${dKey}')"`}>${isLocked?'🔒 ':''}Day ${dayNum}</button>`;
  });
  tray.innerHTML = html;
}

window.setDay = function(day) {
  if (!LIVE_DAYS.has(day)) return;
  currentDay = day;
  document.querySelectorAll('.day-pill').forEach(p => p.classList.toggle('active', p.dataset.day === day));
  const dayNum  = parseInt(day.slice(1));
  const weekPos = ((dayNum-1) % 5) + 1;
  document.body.classList.toggle('essence-golden', weekPos === 5);
  const label = (DAY_LABELS && DAY_LABELS[day]) || ('Day ' + dayNum);
  const badge = document.getElementById('current-day-badge');
  if(badge) badge.textContent = '📅 ' + label;
  renderBoard();
  const weekPos2 = ((dayNum-1) % 5) + 1;
  const btn = document.querySelector('.celebrate-btn');
  if (btn) btn.style.display = weekPos2 === 5 ? 'flex' : 'none';
};

window.switchTab = function(tab) {
  currentTab = tab;
  document.querySelectorAll('.tab').forEach(t => t.classList.toggle('active', t.dataset.tab===tab));
  document.querySelectorAll('.board').forEach(b => b.classList.remove('active'));
  const el = document.getElementById('board-'+tab);
  if (el) el.classList.add('active');
  renderBoard();
};

/* ─────────────────────────────────────────────────
   BOARD RENDER
───────────────────────────────────────────────── */
function renderBoard() {
  ['participants','ambassadors'].forEach(tabKey => {
    const role      = tabKey === 'ambassadors' ? 'Ambassador' : 'Participant';
    const container = document.getElementById('rows-'+tabKey);
    if (!container) return;
    const dayNum_board = parseInt(currentDay.slice(1));
    const pool = PEOPLE.filter(p => {
      if (p.role !== role) return false;
      if (p.joinedDay) {
        const joinedNum = parseInt(p.joinedDay.slice(1));
        if (dayNum_board < joinedNum) return false;
      }
      return true;
    });

    const ptsAsOf = (p, dayNum) => {
      for (let n = dayNum; n >= 1; n--) {
        const d = p.days?.['D'+n];
        if (d) return d.pts;
      }
      return 0;
    };

    const enriched = pool.map(p => {
      const dayData = p.days?.[currentDay] || null;
      const pts     = dayData ? dayData.pts : ptsAsOf(p, dayNum_board - 1);
      const prevPts = currentDay === 'D1' ? 0 : ptsAsOf(p, dayNum_board - 1);
      const delta   = pts - prevPts;
      return { ...p, pts, delta, dayData: dayData || {} };
    });

    const active   = enriched.filter(p => p.delta > 0).sort((a,b) => b.pts-a.pts);
    const inactive = enriched.filter(p => p.delta <= 0).sort((a,b) => a.name.localeCompare(b.name));

    let html = '', rank = 1;
    if (active.length > 0) html += `<div class="active-label">Active — ${active.length} member${active.length!==1?'s':''}</div>`;
    active.forEach((p, i) => {
      const rc         = rowClass(rank);
      const formStreak = p.dayData.streakDays    || 0;
      const workStreak = p.dayData.workStreakDays || 0;
      const workDone   = p.dayData.workDone       || false;
      const subNote    = p.dayData.submitted ? `📋 ${formStreak}-day form · ✏️ ${workStreak}-day work` : workDone ? `✏️ Work done · form not submitted` : `+${p.delta} pts today`;
      html += `<div class="row ${rc}" style="animation-delay:${i*0.05}s" onclick="window.openPanel('${safeName(p.name)}')">
        <div class="rank-num" style="color:${ptsColor(rank)}">${rank}</div>
        <div class="name-col"><div class="name">${p.name}</div><div class="name-sub">${subNote}</div></div>
        <div><div class="pts" style="color:${ptsColor(rank)}">${p.pts}</div><div class="pts-label">points</div></div>
        <div class="tier ${tierClass(p.tier)}">${(TIER_EMOJI&&TIER_EMOJI[p.tier])||''} ${p.tier||'UNRANKED'}</div>
        <div><div class="streak">${formStreak}</div><div class="streak-label">📋 form</div></div>
        <div><div class="work-streak" data-done="${workDone}" title="${workDone ? 'Active work streak' : (workStreak > 0 ? 'Streak paused — not lost' : 'No work streak yet')}">${workStreak}${!workDone && workStreak > 0 ? '<span style="font-size:9px;opacity:.5;display:block;line-height:1">⏸</span>' : ''}</div><div class="work-streak-label">✏️ work</div></div>
      </div>`;
      rank++;
    });
    if (inactive.length > 0) {
      html += `<div class="not-active-label">Not Active This Day — ${inactive.length} member${inactive.length!==1?'s':''}</div>`;
      inactive.forEach((p,i) => {
        html += `<div class="row dns" style="animation-delay:${(active.length+i)*0.04}s" onclick="window.openPanel('${safeName(p.name)}')">
          <div class="rank-num" style="color:var(--muted)">—</div>
          <div class="name-col"><div class="name">${p.name}</div><div class="name-sub">Total: ${p.pts} pts · no activity today</div></div>
          <div><div class="pts" style="color:var(--muted)">${p.pts}</div><div class="pts-label">total</div></div>
          <div class="tier ${tierClass(p.tier)}">${(TIER_EMOJI&&TIER_EMOJI[p.tier])||''} ${p.tier||'UNRANKED'}</div>
          <div><div class="streak" style="color:var(--muted)">0</div><div class="streak-label">📋 form</div></div>
          <div><div class="work-streak" data-done="false">0</div><div class="work-streak-label">✏️ work</div></div>
        </div>`;
      });
    }
    container.innerHTML = html;
  });
}

/* ─────────────────────────────────────────────────
   PROFILE PANEL
───────────────────────────────────────────────── */
window.openPanel = function(name) {
  const p = PEOPLE.find(x => x.name === name);
  if (!p) return;

  document.getElementById('panel-name').textContent = p.name;
  const rb = document.getElementById('panel-role');
  rb.textContent = p.role; rb.className = 'role-badge ' + p.role;
  document.getElementById('panel-pts').textContent = p.allTimeTotal + ' pts';
  const tb = document.getElementById('panel-tier');
  tb.textContent = ((TIER_EMOJI&&TIER_EMOJI[p.tier])||'') + ' ' + (p.tier||'UNRANKED');
  tb.className = 'tier ' + tierClass(p.tier);

  /* Breakdown */
  let bdHtml = '<div class="streak-explain"><div class="streak-explain-title">How your streaks work</div><p style="font-size:13px;color:var(--off);margin-bottom:10px;"><strong style="color:var(--amber)">📋 Form Streak</strong> — every consecutive day you submitted the check-in form on time. Miss one and it pauses at zero until you submit again.</p><p style="font-size:13px;color:var(--off);margin-bottom:0;"><strong style="color:var(--mint)">✏️ Work Streak</strong> — every consecutive day you received a creativity score for your Figma work, with or without the form. If you built something and it was scored, it counts.</p></div>';
  (p.breakdown || []).forEach(sec => {
    bdHtml += `<div class="section-title">${sec.section}</div>`;
    (sec.items || []).forEach(item => {
      const cls = item.earned ? 'earned' : 'missed';
      const icon = item.earned ? '<span style="color:var(--mint)">✓</span>' : '<span style="color:var(--coral)">✗</span>';
      bdHtml += `<div class="bk-row ${cls}"><div class="bk-icon">${icon}</div><div class="bk-body"><div class="bk-label">${item.label}</div><div class="bk-desc">${item.desc||''}</div></div><div class="bk-pts">${item.pts !== null && item.pts !== undefined ? '+'+item.pts : ''}</div></div>`;
    });
  });
  bdHtml += `<div class="total-bar"><div class="total-label">All-Time Total</div><div class="total-num">${p.allTimeTotal}</div></div>`;
  document.getElementById('pboard-breakdown').innerHTML = bdHtml;

  /* Roast */
  document.getElementById('pboard-roast').innerHTML = `<div class="roast-fire">🔥</div><div class="roast-box">${p.roast || '<p>No roast yet. Check back soon.</p>'}</div>`;

  /* Warnings */
  const warnTab = document.querySelector('.ptab[data-ptab="warnings"]');
  const warns = p.warnings || [];
  if (warns.length) {
    if(warnTab) warnTab.classList.add('has-warn');
    let wHtml = `<div class="warn-box-container">`;
    warns.forEach(w => {
      wHtml += `
        <div class="warn-box">
          <div class="warn-header" onclick="window.toggleWarning(this.querySelector('.details-btn'))">
            <div class="warn-summary">${w.title}</div>
            <button class="details-btn">Details ▼</button>
          </div>
          <div class="warn-details">${w.details}</div>
        </div>`;
    });
    wHtml += `</div><p style="font-size:12px;color:var(--muted);line-height:1.8;margin-top:8px;">These warnings are visible only to you. They reflect rulings made by the admin about your points — disqualifications, special awards, or pending verifications. If you believe a warning is incorrect, contact the admin.</p>`;
    document.getElementById('pboard-warnings').innerHTML = wHtml;
  } else {
    if(warnTab) warnTab.classList.remove('has-warn');
    document.getElementById('pboard-warnings').innerHTML = `<div class="no-warn"><div class="no-warn-icon">✅</div><div>No warnings on your account.<br><span style="font-size:12px;color:var(--muted)">Keep it clean.</span></div></div>`;
  }

  /* Rules */
  const rulesData = (typeof RULES !== 'undefined' && RULES) ? RULES : [];
  let rHtml = rulesData.length ? rulesData.map(r => `<div class="rule-item"><div class="rule-title">${r.title}</div><div class="rule-body">${r.content}</div></div>`).join('') : '<p style="color:var(--muted);font-size:13px;">Rules not available.</p>';
  document.getElementById('pboard-rules').innerHTML = rHtml;

  window.switchPTab('breakdown');
  const overlay = document.getElementById('overlay');
  if(overlay) overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
};

window.closePanel = function() {
  const overlay = document.getElementById('overlay');
  if(overlay) overlay.classList.remove('open');
  document.body.style.overflow = '';
};

window.handleOverlayClick = function(e) {
  const overlay = document.getElementById('overlay');
  if (e.target===overlay || (e.target.classList && e.target.classList.contains('overlay-bg'))) window.closePanel();
};

window.switchPTab = function(tab) {
  currentPTab = tab;
  document.querySelectorAll('.ptab').forEach(t => t.classList.toggle('active', t.dataset.ptab===tab));
  document.querySelectorAll('.pboard').forEach(b => b.classList.remove('active'));
  const pb = document.getElementById('pboard-'+tab);
  if (pb) pb.classList.add('active');
};

/* Celebration & Init */
window.triggerCelebration = function(duration) { /* ... */ };
function initApp() {
  let initWeek = 1, initDay = CANONICAL_DAY_ORDER[0];
  if (LATEST_DAY_NUM > 0) {
    for (let w = 1; w <= TOTAL_WEEKS; w++) {
      const days     = WEEK_DAYS[w];
      const firstNum = parseInt(days[0].slice(1),10);
      const lastNum  = parseInt(days[days.length-1].slice(1),10);
      if (LATEST_DAY_NUM >= firstNum) {
        initWeek = w;
        initDay  = LATEST_DAY_NUM <= lastNum ? ('D'+LATEST_DAY_NUM) : days[days.length-1];
      }
    }
  }
  currentWeek = initWeek;
  renderWeekSelector();
  renderDaySelector();
  window.setDay(initDay);
}
if(document.readyState==='loading'){ document.addEventListener('DOMContentLoaded', initApp); } else { initApp(); }
