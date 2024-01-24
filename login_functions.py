from selenium.webdriver.common.keys import Keys
from utils.webdriver_utils import setup_webdriver, teardown_webdriver

def forgot_password_test():
    driver = setup_webdriver()

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element_by_link_text("Forgot your password?").click()

        # Use the common test username "Admin"
        driver.find_element_by_id("securityAuthentication_userName").send_keys("Admin")
        driver.find_element_by_id("btnSearchValues").click()

        success_message = driver.find_element_by_css_selector(".message.success").text
        assert "Reset password link sent successfully" in success_message
    finally:
        teardown_webdriver(driver)

if __name__ == "__main__":
    forgot_password_test()
