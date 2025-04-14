Feature: Credit Underwriting
  Scenario: Approve high-income low-risk applicant
    Given applicant has high income and good risk score
    When underwriting is performed
    Then application should be approved with low interest rate

  Scenario: Reject high-risk applicant
    Given applicant has high income but poor risk score
    When underwriting is performed
    Then application should be rejected due to high risk