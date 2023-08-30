import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.remote.webdriver import WebDriver : if we have multiple browsers we can use this

@pytest.mark.usefixtures('setup')
class BaseClass:
    driver: WebDriver