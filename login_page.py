# login_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.ID, 'username')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'loginBtn')
        self.error_message = (By.CLASS_NAME, 'error')

    def enter_username(self, username):
        self.enter_text(*self.username_field, username)

    def enter_password(self, password):
        self.enter_text(*self.password_field, password)

    def click_login(self):
        self.click(*self.login_button)

    def get_error_message(self):
        return self.get_text(*self.error_message)
