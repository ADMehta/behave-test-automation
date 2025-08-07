from selenium.webdriver.common.by import By # For locating elements
from selenium.webdriver.support.ui import WebDriverWait # For explicit waits
from selenium.webdriver.support import expected_conditions as EC # For wait conditions


class FunctionSignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_join(self):
        try:
                        # Wait until the "Join" button is clickable and click it
            join_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Join']")))
            join_button.click()
        except Exception as e:
            print(f"❌ Error clicking Join button: {e}")
            raise

    def enter_email_and_code(self, email, code):
        try:
                        # Wait until the email input is clickable and enter the email
            email_input = self.wait.until(EC.element_to_be_clickable((By.ID, "email")))
            email_input.send_keys(email)
            self.wait.until(EC.visibility_of_element_located((By.ID, "accessCode"))).value = code
        except Exception as e:
            print(f"❌ Error entering email/access code: {e}")
            raise

    def enter_name(self, first, last):
        try:
            # Scroll to the first name field to ensure it's in view
            element_to_scroll = self.driver.find_element(By.ID, "firstName")
            self.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll)
            
            # Enter first and last name
            self.wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys(first)
            self.wait.until(EC.visibility_of_element_located((By.ID, "lastName"))).send_keys(last)
        except Exception as e:
            print(f"❌ Error entering name: {e}")
            raise

    def enter_phone(self, phone):
        try:
            # Enter phone number once the field is visible
            self.wait.until(EC.visibility_of_element_located((By.ID, "phoneNumber"))).send_keys(phone)
        except Exception as e:
            print(f"❌ Error entering phone number: {e}")
            raise

    def enter_dob(self, dob):
        try:
            # Wait for the DOB field and enter the date        
            self.wait.until(EC.visibility_of_element_located((By.ID, "dateOfBirth"))).value = dob
        except Exception as e:
            print(f"❌ Error entering date of birth: {e}")
            raise

    def select_sex(self, sex):
        try:
            # Convert input to uppercase for comparison  # Normalize input 
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
            # Save a screenshot for debugging
            self.driver.save_screenshot("sex_radio_error.png")
            print(f"❌ Error selecting biological sex: {e}")
            raise

    def select_location(self, location):
        try:
            # Wait for the location dropdown and enter the location
            dropdown = self.wait.until(EC.visibility_of_element_located((By.ID, "state")))
            dropdown.send_keys(location)
        except Exception as e:
            print(f"❌ Error selecting location: {e}")
            raise

    def agree_to_terms(self):
        try:
            # Click all required checkboxes using JavaScript to avoid interaction issues
            checkbox1 = self.driver.find_element(By.ID, "agreeTermsAndPrivacy")
            self.driver.execute_script("arguments[0].click();", checkbox1)
            
            checkbox2 = self.driver.find_element(By.ID, "agreeUseMedicalInformation")
            self.driver.execute_script("arguments[0].click();", checkbox2)           
            
            checkbox3 = self.driver.find_element(By.ID, "agreeLabResults")
            self.driver.execute_script("arguments[0].click();", checkbox3)
        except Exception as e:
            print(f"❌ Error agreeing to terms: {e}")
            raise  # ✅ Correct


    def click_continue(self):
        try:
            #Wait until the Continue button is clickable and click it
            self.wait.until(EC.element_to_be_clickable((By.ID, "signup-submit"))).click()
        except Exception as e:
            print(f"❌ Error clicking Continue button: {e}")
            raise
