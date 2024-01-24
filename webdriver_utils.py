from selenium import webdriver

def setup_webdriver():
    return webdriver.Chrome()

def teardown_webdriver(driver):
    driver.quit()
