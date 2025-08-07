from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FunctionSignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_join(self):
        try:
             # Target the div with text "Join"
            join_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Join']")))
            join_button.click()
        except Exception as e:
            print(f"❌ Error clicking Join button: {e}")
            raise

    def enter_email_and_code(self, email, code):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "email"))).value = email
            self.wait.until(EC.visibility_of_element_located((By.ID, "accessCode"))).value = code
        except Exception as e:
            print(f"❌ Error entering email/access code: {e}")
            raise

    def enter_name(self, first, last):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys(first)
            self.wait.until(EC.visibility_of_element_located((By.ID, "lastName"))).send_keys(last)
        except Exception as e:
            print(f"❌ Error entering name: {e}")
            raise

    def enter_phone(self, phone):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "phoneNumber"))).send_keys(phone)
        except Exception as e:
            print(f"❌ Error entering phone number: {e}")
            raise

    def enter_dob(self, dob):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "dateOfBirth"))).value = dob
        except Exception as e:
            print(f"❌ Error entering date of birth: {e}")
            raise

    # def select_sex(self, sex): 
    #     try:
    #         if sex.lower() == "female":
                
    #             #self.wait.until(EC.element_to_be_clickable((By.ID, "sex"))).click()
    #             (By.XPATH, "//div[@data-value='female']")
    #         else:
    #             self.wait.until(EC.element_to_be_clickable((By.ID, "male"))).click()
    #     except Exception as e:
    #         print(f"❌ Error selecting biological sex: {e}")
    #         raise

    def select_sex(self, sex):
        try:
            # Normalize input
            sex = sex.upper()

            # Wait for the radio group to be present
            radio_group = self.wait.until(EC.presence_of_element_located((By.ID, "sex")))

            # Find all label elements inside the radio group
            labels = radio_group.find_elements(By.CLASS_NAME, "ant-radio-button-wrapper")

            # Loop through labels to find the one matching the desired sex
            for label in labels:
                label_text = label.find_element(By.CLASS_NAME, "ant-radio-button-label").text.upper()
                if label_text == sex:
                    label.click()
                    break
            else:
                raise Exception(f"Sex option '{sex}' not found.")

        except Exception as e:
            self.driver.save_screenshot("sex_radio_error.png")
            print(f"❌ Error selecting biological sex: {e}")
            raise

    def select_location(self, location):
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located((By.ID, "state")))
            dropdown.send_keys(location)
        except Exception as e:
            print(f"❌ Error selecting location: {e}")
            raise

    def agree_to_terms(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, "agreeTermsAndPrivacy"))).click()
            self.wait.until(EC.element_to_be_clickable((By.ID, "agreeUseMedicalInformation"))).click()
            self.wait.until(EC.element_to_be_clickable((By.ID, "agreeLabResults"))).click()
        except Exception as e:
            print(f"❌ Error agreeing to terms: {e}")
            raise

    def click_continue(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, "signup-submit"))).click()
        except Exception as e:
            print(f"❌ Error clicking Continue button: {e}")
            raise
