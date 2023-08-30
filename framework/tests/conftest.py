import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.safari.service import Service as SafariService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = 'chrome', help = "browser name")

@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("browser")
    if browser=='chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximised")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.etsy.com/")
        request.cls.driver = driver
        yield
        time.sleep(5)
        driver.close()
    elif browser=='safari':
        safari_options = webdriver.SafariOptions()
        driver = webdriver.Safari(service=SafariService(), options=safari_options)
        driver.maximize_window()
        driver.get("https://www.etsy.com/")
        request.cls.driver = driver
        yield
        time.sleep(5)
        driver.close()

@pytest.fixture(params=[('sam', '25'), ('tom', '27')])
def get_data(request):
    return request.param