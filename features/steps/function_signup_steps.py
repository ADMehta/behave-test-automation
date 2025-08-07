from behave import given, when, then
from pages.function_signup_page import FunctionSignupPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I navigate to "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    context.signup_page = FunctionSignupPage(context.driver)

@given('I click on the "Join" button')
def step_impl(context):
    context.signup_page.click_join()

@when('I enter email "{email}" and access code "{code}"')
def step_impl(context, email, code):
    context.signup_page.enter_email_and_code(email, code)

@when('I enter legal name "{first}" and "{last}"')
def step_impl(context, first, last):
    context.signup_page.enter_name(first, last)

@when('I enter US phone number "{phone}"')
def step_impl(context, phone):
    context.signup_page.enter_phone(phone)

@when('I enter date of birth "{dob}"')
def step_impl(context, dob):
    context.signup_page.enter_dob(dob)

@when('I select biological sex "{sex}"')
def step_impl(context, sex):
    context.signup_page.select_sex(sex)

@when('I answer pregnancy question with "{answer}"')
def step_impl(context, answer):
    context.signup_page.answer_pregnancy(answer)

@when('I select testing location "{location}"')
def step_impl(context, location):
    context.signup_page.select_location(location)

@when('I agree to all terms and policies')
def step_impl(context):
    context.signup_page.agree_to_terms()

@then('I click on the "Continue" button')
def step_impl(context):
    context.signup_page.click_continue()

@then('I should see a confirmation message "Account created successfully"')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    success_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Account created successfully')]"))
    )
    assert success_message.is_displayed()

@when('I wait for 10 seconds')
def step_impl(context):
    print("Waiting for 10 seconds...")
    time.sleep(10) # Pause execution for 10 seconds
    print("Wait completed.")

@then('I wait for 10 second')
def step_impl(context):
    print("Waiting for 10 seconds...")
    time.sleep(10) # Pause execution for 10 seconds
    print("Wait completed.")