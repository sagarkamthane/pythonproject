import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Safari(service = Service())
driver.maximize_window()
driver.get("https://www.flipkart.com/")

driver.implicitly_wait(0.1)
# cross_button = driver.find_element(By.XPATH, "//button[@class = '_2KpZ6l _2doB4z']")
# if implicitly_wait is 10 sec and explicit wait is 5 sec. if element is not found in 5 sec it waits until 10 sec
# if implicit wait is 1 sec and explicit wait is 5 sec. if element is not found in 1 sec script fails
# implicit wait overloads explicit wait
wait = WebDriverWait(driver, 5)
cross_button = driver.find_element(By.XPATH, "//button[@class = '_2KpZ6l _2doB4z']")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = '_2KpZ6l _2doB4z']")))
cross_button.click()

hover_element = driver.find_element(By.XPATH, "//div[@class='xtXmba' and contains(text(),'Home')]")

actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()




wait.until(EC.alert_is_present())