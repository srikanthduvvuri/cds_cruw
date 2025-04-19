from behave import given, when, then
from underwriting_rules import evaluate

@given('an applicant with income "{income:d}", loan amount "{amount:d}" and risk score "{risk_score:d}"')
def step_given_applicant_data(context, income, amount, risk_score):
    context.applicant_info = {
        'income': income,
        'loan_amount': amount
    }
    context.risk_score = risk_score

@when('the underwriting rules are evaluated')
def step_when_evaluate_rules(context):
    context.result = evaluate(context.applicant_info, context.risk_score)

@then('the decision status should be "{expected_status}"')
def step_then_status(context, expected_status):
    assert context.result['status'] == expected_status, f"Expected status {expected_status}, got {context.result['status']}"

@then('the decision reason should be "{expected_reason}"')
def step_then_reason(context, expected_reason):
    assert context.result['reason'] == expected_reason, f"Expected reason '{expected_reason}', got '{context.result['reason']}'"

@then('the interest rate should be "{expected_rate}"')
def step_then_interest_rate(context, expected_rate):
    actual = context.result.get('interest_rate')
    expected = float(expected_rate) if expected_rate != "None" else None
    assert actual == expected, f"Expected interest rate {expected}, got {actual}"
