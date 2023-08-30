from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service())
driver.get('https://staging-portal.kristal.ai/login#')
driver.implicitly_wait(10)

email_input = driver.find_element(By.XPATH, "//input[@name='email']")
email_input.send_keys("sagar.k+7023@kristal.ai")

pass_input = driver.find_element(By.XPATH, "//input[@type='password']")
pass_input.send_keys("Admin@12345")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

login_button.click()

dashboard = driver.find_element(By.XPATH, "//div[text()='Portfolio']")
dashboard.click()

driver.quit()