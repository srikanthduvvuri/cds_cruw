def evaluate(applicant_info, risk_score):
    # Example underwriting logic
    income = applicant_info.get('income', 0)
    amount = applicant_info.get('loan_amount', 0)
    if risk_score < 400:
        status = 'rejected'
        reason = 'High risk score'
    elif income < 25000 or amount > income * 5:
        status = 'rejected'
        reason = 'Insufficient income for requested loan'
    else:
        status = 'approved'
        interest_rate = 0.1 if risk_score > 700 else 0.15
        reason = f'Approved with interest rate {interest_rate}'
    return {
        'status': status,
        'interest_rate': interest_rate if status == 'approved' else None,
        'reason': reason
    }