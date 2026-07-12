import pytest
from selenium import webdriver
from base_pages.login_admin_page import LoginAdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_admin_login:
    url = Read_Config.login_url()
    Username = Read_Config.user_name()
    Password = Read_Config.pass_word()
    invalid_Username = Read_Config.in_valid()
    logger = Log_Maker.log_gen()

    #@pytest.mark.order(3)
    #@pytest.mark.parametrize("run", range(3))  #this decorator with parametrize will run this method for 3 times
    def test_title_verification(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.logger.info("****title-verification-started****")
        self.driver.implicitly_wait(5)
        actual_title = self.driver.title
        expected_title = "OrangeHRM"
        print(actual_title)

        if actual_title == expected_title:
            self.logger.info("****title_verified-successfully****")
            assert True
            self.driver.close()
        else:
            self.logger.error("****title_verified-failed****")
            self.driver.close()
            assert False

    #@pytest.mark.smoke
    #@pytest.mark.order(2)
    #@pytest.mark.dependency(depends=["test_invalid_admin_login"])
    def test_valid_admin_login(self, setup):
        self.driver = setup
        login = LoginAdminPage(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("****valid-admin-test-started****")
        self.driver.implicitly_wait(10)
        login.enter_username(self.Username)
        login.enter_password(self.Password)
        login.click_button()
        #screenshot = self.driver.save_screenshot(".//screenshots//login1_page.png") - this returns boolean value to understand if screenshot is captured or not
        #print(screenshot)
        admin_screen_text = self.driver.find_element(By.CLASS_NAME, "oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module").text
        self.driver.save_screenshot(".//screenshots//login1_page.png")
        #admin_screen_text = self.driver.find_element(By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module')]").text
        #admin_screen = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module')]")))
        #admin_screen.text
        #use any of the above two methods
        if admin_screen_text == "Dashboard":
            self.logger.info("****valid-admin-test-passed-successfully****")
            print(admin_screen_text)
            assert True
            self.driver.quit()
        else:
            self.logger.error("****valid-admin-test-failed****")
            self.driver.close()
            assert False

    #@pytest.mark.order(1)
    #@pytest.mark.dependency()
    def test_invalid_admin_login(self, setup):
        self.driver = setup
        login = LoginAdminPage(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("****invalid-admin-test-started****")
        self.driver.implicitly_wait(5)
        login.enter_username(self.invalid_Username)
        login.enter_password(self.Password)
        login.click_button()
        #explicit_wait = WebDriverWait(self.driver,10)
        #err_element = explicit_wait.until(EC.presence_of_element_located((By.XPATH,"//h6[contains(@class,'oxd-alert-content-text']")))
        #err_element.text
        err_msg = self.driver.find_element(By.CLASS_NAME, "oxd-text.oxd-text--p.oxd-alert-content-text").text
        self.driver.save_screenshot(".//screenshots//invalid_login.png")
        if err_msg == "Invalid credentials":
            self.logger.info("****invalid-admin-test-passed-successfully****")
            assert True
            #self.driver.save_screenshot(".\screenshots\invalid_login.jpeg")
            self.driver.close()
        else:
            self.logger.error("****invalid-admin-test-failed****")
            self.driver.close()
            assert False





