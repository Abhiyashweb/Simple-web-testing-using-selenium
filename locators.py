from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
