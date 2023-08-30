from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement


class LandingPage:

    landing_page_login_button_xpath = (By.XPATH, "//button[contains(@class, 'select-signin')]")

    def __init__(self, driver):
        self.driver = driver

    def landing_page_login_button(self) -> WebElement:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            LandingPage.landing_page_login_button_xpath))
        return self.driver.find_element(*LandingPage.landing_page_login_button_xpath)
