Feature: Function Health Member Signup

  Scenario: User completes the member signup form successfully
    Given I navigate to "https://functionhealth.com"
    And I click on the "Join" button
    When I enter email "charlie@example.com" and access code "928AA4E1CD199B9D73A1A3B7DBC7F4F7"
    And I wait for 10 seconds
    And I enter legal name "Aaa" and "bbb"
    And I enter US phone number "5102821900"
    And I enter date of birth "02022001"
    And I select biological sex "Female"
    And I select testing location "California"
    And I agree to all terms and policies
    Then I click on the "Continue" button
