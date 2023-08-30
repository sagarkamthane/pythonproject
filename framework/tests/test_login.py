from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from framework.pagefactory.landingpage import LandingPage
from framework.pagefactory.loginpage import LoginPage
from framework.utils.baseclass import BaseClass


class TestLogin(BaseClass):

    def test_login_from_landing_page(self):
        landing_page = LandingPage(self.driver)
        landing_page.landing_page_login_button().click()

    def test_input_username_on_login_page(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_page_email_input().send_keys('saagark13121998@gmail.com')

    def test_input_password_on_login_page(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_page_password_input().send_keys('Sagark@13121998')

    def test_login_page_login_button(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_page_login_button().click()
