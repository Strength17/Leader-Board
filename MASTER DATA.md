# MASTER LEADERBOARD TRUTH (Audit Trail)

This file represents the absolute truth as derived from raw chat logs, form data, and manual admin overrides. 

---

## 1. Christine Choundong (Ambassador)
**Status**: ACTIVE
- **Pre-Programme**: 
    - Pledge: +5 (May 31)
    - Referrals: 2 (Confirmed in Manual file): +50
- **Daily Performance**:
    - **D1**: Form (✅), Early (❌), Work Post (✅), Creativity (+10). Pts: 10 + 5 + 10 = 25. Cum: 80.
    - **D2**: Form (✅), Early (❌), Work Post (✅), Creativity (+20). Pts: 10 + 5 + 20 = 35. Cum: 115.
    - **D3**: Form (✅), Early (❌), Work Post (✅), Creativity (+5). Pts: 10 + 5 + 5 = 20. Cum: 135.
    - **D4**: Form (❌ - submitted late on D5), Work (✅), Creativity (+5). Pts: 5. Cum: 140.
    - **D5**: Form (❌ - DQ'd), Work (✅), Creativity (+10). Pts: 10. Cum: 150.
    - **D6**: Form (✅), Early (❌), Work Post (✅), Creativity (+5). Pts: 10 + 5 + 5 = 20. Cum: 170.
    - **D7**: Form (✅), Early (❌), Work Post (✅), Creativity (+5). Pts: 10 + 5 + 5 = 20. Cum: 190.
- **Bonuses/Overlays**:
    - FB Interaction (+10)
    - First-to-post (D2, D3, D4 = +15)
    - Welcomed members (+3)
    - Weekly Milestone (+20)
    - Perfect Week (+15) -- *Note: Legacy data (data.js) awarded this, but technically D4 was late.*
- **Total Expected (D7)**: ~253 pts.
- **Current Data2.js**: 145 pts.
- **Discrepancy**: **-108 pts**. 
- **Cause**: Automation is failing to add Referral bonus (+50), Milestone (+20), Perfect Week (+15), and FB/Interaction points (+28) to the cumulative total.

## 2. Oluwasegun Daniel Osawore (Ambassador)
**Status**: ACTIVE
- **Pre-Programme**: 
    - Pledge: +5
    - Referrals: 3 (Confirmed): +75
- **Daily Performance**:
    - **D1**: Form (❌ - First to post WA but no form D1?), Creativity (+10). Pts: 5 + 10 = 15. Cum: 95.
    - **D2**: Form (✅), Early (❌), Work Post (✅), Creativity (+15). Pts: 10 + 5 + 15 = 30. Cum: 125.
    - **D3**: Form (✅), Early (❌), Work Post (✅), Creativity (+10). Pts: 10 + 5 + 10 = 25. Cum: 150.
    - **D5**: Form (❌), Work (✅), Creativity (+15), First-to-post (+5). Pts: 20. Cum: 170.
    - **D6**: Form (❌), Work (✅), Creativity (+5). Pts: 5. Cum: 175.
    - **D7**: Form (❌), Work (✅), Creativity (+5). Pts: 5. Cum: 180.
- **Total Expected (D7)**: 180 pts.
- **Current Data2.js**: 180 pts.
- **Verdict**: Daniel is CORRECT in data2.js.

## 3. Emmanuel Karol Tchouani (Participant)
**Status**: ACTIVE
- **Expected Total (D7)**: 175 pts (Same as Data2.js).
- **Verdict**: Emmanuel is CORRECT in data2.js.

## 4. Percy Visiy (Ambassador)
**Status**: SILENT
- **Pledge**: +5 (May 31)
- **Total**: 5 pts.
- **Current Data2.js**: MISSING.
- **Cause**: Automation skips users who only have a pledge and no interaction flags or forms.

## 5. Mbishitehnyi Ryan (Participant)
**Status**: SILENT
- **Referral**: Referred Richard Nathan Enana (+25 pts).
- **Total**: 25 pts.
- **Current Data2.js**: MISSING.
- **Cause**: Automation skips users who only have manual referral points but no forms or WA interactions.

## 6. Broken Entries
- **Christine**, **Daniel**, **Emmanuel**, **and Faith**:
- **Cause**: The regex splitting logic in `leaderboard_sync.py` for "Milestone Points" is splitting the list of names and creating partial name entries instead of mapping them to the full canonical names (e.g., "Christine Choundong").
