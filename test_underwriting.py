def test_approved_case():
    from underwriting_rules import evaluate
    info = {'income': 50000, 'loan_amount': 100000}
    decision = evaluate(info, 750)
    assert decision['status'] == 'approved'
    assert decision['interest_rate'] == 0.1

def test_rejected_case_risk():
    from underwriting_rules import evaluate
    info = {'income': 50000, 'loan_amount': 100000}
    decision = evaluate(info, 350)
    assert decision['status'] == 'rejected'
    assert 'High risk score' in decision['reason']