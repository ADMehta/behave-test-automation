# Import Behave step decorators
from behave import given, when, then

# Import the page object for signup functionality
from pages.function_signup_page import FunctionSignupPage

# Import Selenium modules for optional direct interactions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import time module for explicit delays
import time

# Step: Navigate to the specified URL and initialize the signup page object
@given('I navigate to "{url}"')
def navigate_to_url(context, url):
    context.driver.get(url)  # Open the target URL in the browser
    context.signup_page = FunctionSignupPage(context.driver)  # Instantiate the page object

# Step: Click the "Join" button to start the signup process
@given('I click on the "Join" button')
def click_join_button(context):
    context.signup_page.click_join()

# Step: Enter email address and access code into the form
@when('I enter email "{email}" and access code "{code}"')
def enter_email_and_code(context, email, code):
    context.signup_page.enter_email_and_code(email, code)

# Step: Enter user's legal first and last name
@when('I enter legal name "{first}" and "{last}"')
def enter_legal_name(context, first, last):
    context.signup_page.enter_name(first, last)

# Step: Enter a valid US phone number
@when('I enter US phone number "{phone}"')
def enter_us_phone_number(context, phone):
    context.signup_page.enter_phone(phone)

# Step: Enter user's date of birth
@when('I enter date of birth "{dob}"')
def enter_date_of_birth(context, dob):
    context.signup_page.enter_dob(dob)

# Step: Select biological sex from available options
@when('I select biological sex "{sex}"')
def select_biological_sex(context, sex):
    context.signup_page.select_sex(sex)

# Step: Answer the pregnancy-related question (if applicable)
@when('I answer pregnancy question with "{answer}"')
def answer_pregnancy_question(context, answer):
    context.signup_page.answer_pregnancy(answer)

# Step: Choose a testing location from the dropdown or list
@when('I select testing location "{location}"')
def select_testing_location(context, location):
    context.signup_page.select_location(location)

# Step: Agree to all terms, conditions, and privacy policies
@when('I agree to all terms and policies')
def agree_to_terms_and_policies(context):
    context.signup_page.agree_to_terms()

# Step: Click the "Continue" button to proceed to the next step
@then('I click on the "Continue" button')
def click_continue_button(context):
    context.signup_page.click_continue()

# Step: Wait for 10 seconds (used for debugging or slow page loads)
@when('I wait for 10 seconds')
def wait_for_10_seconds_when(context):
    print("Waiting for 10 seconds...")
    time.sleep(10)  # Pause execution for 10 seconds
    print("Wait completed.")

