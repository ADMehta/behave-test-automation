from selenium import webdriver  # Import Selenium WebDriver to control the browser

def before_all(context):
    # This function runs before all tests start
    print("✅ environment.py loaded")  # Log to confirm environment setup

    # Create Chrome options to customize browser behavior
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Start browser in maximized window

    # Initialize the Chrome WebDriver with the specified options
    context.driver = webdriver.Chrome(options=options)

def after_all(context):
    # This function runs after all tests finish
    context.driver.quit()  # Close the browser and end the WebDriver session
