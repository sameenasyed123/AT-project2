from utils.webdriver_utils import setup_webdriver, teardown_webdriver

def admin_page_menu_validation_test():
    driver = setup_webdriver()

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Login steps...
        # ...

        driver.find_element_by_id("menu_admin_viewAdminModule").click()

        menus = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
        for menu in menus:
            assert driver.find_element_by_link_text(menu).is_displayed()

    finally:
        teardown_webdriver(driver)

if __name__ == "__main__":
    admin_page_menu_validation_test()
