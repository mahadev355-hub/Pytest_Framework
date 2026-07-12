"""this is a page object for the admin page where the locators and actions are defined in this page which then will be
called in other .py files."""

from selenium.webdriver.common.by import By

class LoginAdminPage:
    username_name = "username"
    password_name = "password"
    btn_login_path = "//button[@type = 'submit']"


    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_name).clear()
        self.driver.find_element(By.NAME, self.username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_name).clear()
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def click_button(self):
        self.driver.find_element(By.XPATH, self.btn_login_path).click()

