from behave import given, when, then
from selenium import webdriver
from pages.signup_page import SignupPage

@given('I open the Function Health homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.functionhealth.com/")
    context.page = SignupPage(context.driver)

@when('I click on the Member Sign Up button')
def step_impl(context):
    context.page.click_signup_button()

@then('I should be redirected to the signup page')
def step_impl(context):
    assert "signup" in context.driver.current_url
    context.driver.quit()
