# test_login.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("invalid_user")
    login_page.enter_password("invalid_pass")
    login_page.click_login()

    error_message = login_page.get_error_message()
    assert error_message == "Invalid credentials", f"Expected error message, but got: {error_message}"
