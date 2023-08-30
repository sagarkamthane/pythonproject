import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service

driver = webdriver.Safari(service=Service())
driver.get("https://www.flipkart.com/")
driver.maximize_window()

time.sleep(2)
try: driver.find_element(By.XPATH, "//button[@class = '_2KpZ6l _2doB4z']").click()
except: pass


# element_to_scroll = driver.find_element(By.XPATH, "//a[starts-with(@href, 'tel')]")
# driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll)

time.sleep(2)
hover_element = driver.find_element(By.XPATH, "//div[@class='xtXmba' and contains(text(),'Home')]")

actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()


time.sleep(2)
dropdown_opts = driver.find_elements(By.XPATH, "//div[@class = '_3XS_gI _7qr1OC']/a")
for dropdown in dropdown_opts:
    if "Home Furnishings" in dropdown.text:
        dropdown.click()
        break

time.sleep(2)
sub_dropdown_opts = driver.find_elements(By.XPATH, "//div[@class = '_3XS_gI']/span[contains(text(), 'more in Home Furnishings')]/../a")
for dropdown in sub_dropdown_opts:
    if "Curtains & Accessories" in dropdown.text:
        dropdown.click()

time.sleep(10)


driver.quit()
