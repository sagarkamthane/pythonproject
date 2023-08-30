import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

chrome_options = Options()
# chrome_options.add_argument("--use-fake-ui-for-media-stream")


driver = webdriver.Chrome(service=Service(), options=chrome_options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)
driver.find_element(By.XPATH, "//input[@id= 'name']").send_keys(random.choice(['sagar', 'neha', 'neha', 'neha']))
driver.find_element(By.XPATH, "//input[@id= 'confirmbtn']").click()

alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
if 'sagar' in alert.text:
    alert.accept()
else: alert.dismiss()

# alert = Alert(driver)
# alert.accept()
# alert.dismiss()
# text1 = alert.text
# alert.send_keys('send')

# driver.get("https://www.google.com")
#
# time.sleep(5)
# driver.find_element(By.XPATH, "//div[@jscontroller='unV4T']").click()
# time.sleep(1)
#
#
# action = ActionChains(driver)
# action.send_keys(Keys.ENTER).perform()
#
# time.sleep(5)
driver.quit()

#to handle non javascript alerts tools like AutoIt (for Windows) or SikuliX (cross-platform) are used

