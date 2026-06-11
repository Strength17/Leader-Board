# Daily State Audit (D1 - D6)

This audit maps every participant's status for every day. 
- **YES**: Points earned.
- **NO**: No points earned.
- **-**: Not yet joined.

| Name | D1 | D2 | D3 | D4 | D5 | D6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Christine Choundong | YES | YES | YES | YES | YES | YES |
| Oluwasegun Daniel O | YES | YES | YES | NO | YES | YES |
| Emmanuel Karol T | YES | YES | YES | YES | YES | NO |
| Abongnwi Chrioni-O | YES | YES | YES | YES | YES | YES |
| Mbiydzenyuy Patience | YES | YES | YES | YES | YES | YES |
| Faith Emmanuella B | YES | YES | NO | NO | YES | NO |
| Frank Emmanuel | - | - | - | - | - | YES |
| Malialia Celine B | NO | NO | NO | NO | NO | NO |
| Amaazee Ivanna T | YES | NO | NO | NO | NO | YES |
| Asonganyi Adel Q | YES | NO | NO | NO | NO | NO |
| Ranjoy-Bryan | YES | NO | NO | NO | NO | NO |
| Dorothy Joyce P | - | - | - | - | - | YES |
| Nzameyo Mba | - | - | - | - | - | NO |

*(All Pledge-Only participants are NO for D1-D6)*

---
**Audit Logic Verified**:
- Points today (`ptsToday`) > 0 = YES.
- Points today == 0 = NO.
- JoinedDay constraint enforced.
- Streak preservation logic (freeze-not-reset) applied.
