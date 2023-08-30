import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Safari(service=Service())
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)

# checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[(@type = 'checkbox') and starts-with(@id, 'check')]/parent::label")

for checkbox in checkboxes:
    print(checkbox.text)
    if 'Option1' in checkbox.text:
        print(checkbox.text)
        checkbox.find_element(By.XPATH, "input").click()
        assert checkbox.find_element(By.XPATH, "input").is_selected()
        break

# radiobutton
time.sleep(1)
radios = driver.find_elements(By.XPATH, "//label[contains(@for, 'radio')]")

for radio in radios:
    if 'Radio1' in radio.text:
        radio.find_element(By.XPATH, "input").click()
        print(radio.find_element(By.XPATH, "input").is_selected())
    print(radio.find_element(By.XPATH, "input").is_selected())


# id_displayed
assert driver.find_element(By.XPATH, "//input[@id= 'displayed-text']").is_displayed()
driver.find_element(By.XPATH, "//input[@id= 'hide-textbox']").click()
assert not driver.find_element(By.XPATH, "//input[@id= 'displayed-text']").is_displayed()

