Feature: Function Health Member Signup

  Scenario: User completes the member signup form successfully by clicking join button.
    Given I navigate to "<url>"
    And I click on the "<join_button>" button
    When I enter email "<email>" and access code "<access_code>"
    And I wait for <wait_time> seconds
    And I enter legal name "<first_name>" and "<last_name>"
    And I enter US phone number "<phone_number>"
    And I enter date of birth "<dob>"
    And I select biological sex "<sex>"
    And I select testing location "<location>"
    And I agree to all terms and policies
    Then I click on the "<continue_button>" button

  Examples:
    | url                          | join_button | email               | access_code                             | wait_time | first_name | last_name | phone_number | dob       | sex    | location   | continue_button |
    | https://functionhealth.com   | Join        | John.Doe@example.com | 928AA4E1CD199B9D73A1A3B7DBC7F4F7        | 10        | John        | Doe       | 5102821900   | 02022001  | Female | California | Continue        |

