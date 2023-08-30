from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    login_page_username_xpath = (By.XPATH, "//input[contains(@id, 'join_neu_email_field')]")
    login_page_password_xpath = (By.XPATH, "//input[contains(@id, 'join_neu_password_field')]")
    login_page_login_button_xpath = (By.XPATH, "//button[@value = 'sign-in']")

    def __init__(self, driver):
        self.driver = driver

    def login_page_email_input(self) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            LoginPage.login_page_username_xpath))
        return self.driver.find_element(*LoginPage.login_page_username_xpath)

    def login_page_password_input(self) -> WebElement:
        return self.driver.find_element(*LoginPage.login_page_password_xpath)

    def login_page_login_button(self) -> WebElement:
        return self.driver.find_element(*LoginPage.login_page_login_button_xpath)
