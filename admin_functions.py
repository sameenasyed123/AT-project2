from utils.webdriver_utils import setup_webdriver, teardown_webdriver

def admin_page_header_validation_test():
    driver = setup_webdriver()

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Login steps...
        # ...

        driver.find_element_by_id("menu_admin_viewAdminModule").click()

        assert driver.title == "OrangeHRM"

        headers = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Banking", "Configuration"]
        for header in headers:
            assert driver.find_element_by_link_text(header).is_displayed()

    finally:
        teardown_webdriver(driver)

if __name__ == "__main__":
    admin_page_header_validation_test()
