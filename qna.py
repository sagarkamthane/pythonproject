'''
Q: im inheriting base class in test classes, but by this approach pycharm doesn't give me selenium give me code suggestions while writing tests in test methods
A: By importing the WebDriver class and using it as a type hint for the driver attribute, you're providing PyCharm with the necessary information to offer code suggestions based on the Selenium API.
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest

@pytest.mark.usefixtures('setup')
class BaseClass:
    driver: WebDriver

'''