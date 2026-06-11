### Data Structure Analysis (`data.js`)

The `PEOPLE` array in `data.js` is structured as follows for each participant:

```javascript
{
  name: "Participant Name",
  joinedDay: "D1", // or "D5", etc.
  allTimeTotal: 123,
  days: {
    "D1": { pts: 10, ... },
    "D2": { pts: 20, ... },
    // Only includes days with actual activity or presence.
  },
  // ...
}
```

### The Rendering Fix (`Frontend/script.js`)

The issue is that the current filtering logic only checks if a participant joined, but the UI loop might still attempt to render them in "Inactive" or "Active" rows for days they don't even have an entry for in their `days` object, even if they joined *before* that day.

To ensure accuracy, the rendering loop must be strictly gated by the `joinedDay`.

**Required Change in `renderBoard()` in `script.js`:**

```javascript
// Current Filtering (in renderBoard):
const pool = PEOPLE.filter(p => {
  if (p.role !== role) return false;
  // ...
  return true;
});

// REQUIRED Fix: Ensure that for a given currentDay, 
// we only show the participant IF:
// 1. They have joined by currentDay AND
// 2. We explicitly handle their presence on this day.

const pool = PEOPLE.filter(p => {
  if (p.role !== role) return false;

  // 1. GATE: Was the participant in the programme by currentDay?
  const joinedNum = parseInt(p.joinedDay.slice(1));
  const boardNum = parseInt(currentDay.slice(1));
  if (boardNum < joinedNum) return false; // Absolutely exclude them.

  return true;
});
```

With this logic, if `boardNum >= joinedNum` but they have no entry for `currentDay` in their `days` object, the rendering code for "Inactive" will correctly label them as "Not Active This Day" because they *were* expected to be there, but didn't perform, whereas previously they might have been excluded or mis-rendered entirely.
