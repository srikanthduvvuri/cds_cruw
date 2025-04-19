Feature: Credit Underwriting Rules Evaluation

  Scenario: Rejected due to high risk
    Given an applicant with income "50000", loan amount "200000" and risk score "350"
    When the underwriting rules are evaluated
    Then the decision status should be "rejected"
    And the decision reason should be "High risk score"
    And the interest rate should be "None"

  Scenario: Rejected due to low income
    Given an applicant with income "20000", loan amount "50000" and risk score "600"
    When the underwriting rules are evaluated
    Then the decision status should be "rejected"
    And the decision reason should be "Insufficient income for requested loan"
    And the interest rate should be "None"

  Scenario: Approved with lower rate
    Given an applicant with income "100000", loan amount "200000" and risk score "720"
    When the underwriting rules are evaluated
    Then the decision status should be "approved"
    And the decision reason should be "Approved with interest rate 0.1"
    And the interest rate should be "0.1"

  Scenario: Approved with higher rate
    Given an applicant with income "60000", loan amount "100000" and risk score "650"
    When the underwriting rules are evaluated
    Then the decision status should be "approved"
    And the decision reason should be "Approved with interest rate 0.15"
    And the interest rate should be "0.15"
