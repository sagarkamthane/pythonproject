import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.naukri.com")

driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
driver.save_screenshot('ss.png')

time.sleep(2)
ele = driver.find_element(By.XPATH, "//a[@class = 'btn2']")
driver.execute_script("arguments[0].scrollIntoView();", ele)

time.sleep(5)

# driver.execute_script("document.getElementById('elementId').value = 'New Value';")
driver.quit()



driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
driver.execute_script('arguments[0].scrollIntoView();', ele)