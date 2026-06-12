
# Scoring Rules Definition
# -----------------------
# Pledge: 5 pts
# Referral: 25 pts each
# Form Submission: 10 pts
# Early Bonus: 5 pts (if form submitted before 3 PM)
# Work Streak: 5 pts per day with confirmed work
# Engagement: Varies (Welcomes, Tips, Help) - 3-5 pts depending on admin judgement

def compute_points(participant_data, rules):
    """
    Computes points breakdown based on provided data and rules.
    participant_data: dict with 'pledge', 'referrals', 'forms', 'work_days', 'engagement'
    """
    total = 0
    breakdown = {}

    # 1. Pledge
    if participant_data.get('pledge'):
        total += 5
        breakdown['Pledge'] = 5

    # 2. Referrals
    referrals = participant_data.get('referrals', 0)
    total += (referrals * 25)
    breakdown['Referrals'] = referrals * 25

    # 3. Forms
    forms = participant_data.get('forms', [])
    for form in forms:
        total += 10
        if form.get('early_bonus'):
            total += 5
    breakdown['Forms'] = len(forms) * 10 + sum(1 for f in forms if f.get('early_bonus')) * 5

    # 4. Work Streak
    work_days = participant_data.get('work_days', [])
    total += (len(work_days) * 5)
    breakdown['Work Streak'] = len(work_days) * 5

    # 5. Engagement
    engagement = participant_data.get('engagement', [])
    for eng in engagement:
        total += eng.get('pts', 0)
    breakdown['Engagement'] = sum(e.get('pts', 0) for e in engagement)

    return total, breakdown

# --- TESTING ---
if __name__ == "__main__":
    # Test case: Christine-like data
    test_data = {
        'pledge': True,
        'referrals': 2,
        'forms': [{'early_bonus': False}, {'early_bonus': False}],
        'work_days': ['D1', 'D2', 'D3'],
        'engagement': [{'pts': 5}, {'pts': 3}]
    }
    
    expected_total = 5 + (2*25) + (2*10) + (3*5) + (5+3)
    # 5 + 50 + 20 + 15 + 8 = 98
    
    total, breakdown = compute_points(test_data, {})
    
    assert total == expected_total, f"Expected {expected_total}, got {total}"
    print("Test passed: Points computed correctly.")
