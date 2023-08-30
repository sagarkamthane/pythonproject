import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@name = 'username']").clear() #elears if there is an existing value present
ele = driver.find_element(By.XPATH, "//input[@name = 'username']")
ele.screenshot('abc.png')
print(ele.value_of_css_property('height'))
driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


page_t = driver.title
assert page_t == 'OrangeHRM'

driver.close()