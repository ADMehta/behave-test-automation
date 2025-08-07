from selenium import webdriver

def before_all(context):
    # You can customize options here (e.g., headless, incognito)
    print("✅ environment.py loaded")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)

def after_all(context):
    context.driver.quit()
