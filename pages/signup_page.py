from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        wait = WebDriverWait(self.driver, 10)
        # Target the div with text "Join"
        join_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Join']")))
        join_button.click()

