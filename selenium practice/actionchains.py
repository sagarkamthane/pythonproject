import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service = Service())
driver.maximize_window()
actions = ActionChains(driver)


# driver.get("https://www.flipkart.com/")
# time.sleep(5)
# try: driver.find_element(By.XPATH, "//button[@class = '_2KpZ6l _2doB4z']").click()
# except: pass
#
# # element_to_scroll = driver.find_element(By.XPATH, "//a[starts-with(@href, 'tel')]")
# # driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll)
#
# time.sleep(2)
# hover_element = driver.find_element(By.XPATH, "//div[@class='xtXmba' and contains(text(),'Home')]")


# actions.move_to_element(hover_element).perform()

driver.get('https://www.google.com')
time.sleep(5)




# driver.find_element(By.XPATH,"//div[@jscontroller='lpsUAf']").click() #lens
# source = driver.find_element(By.XPATH,"//img[@class = 'lnXdpd']")
# target = driver.find_element(By.XPATH,"//div[@class='f6GA0']")
# time.sleep(1)
# actions.drag_and_drop_by_offset(source, target.location['x'], target.location['y'] ).perform()
# actions.click_and_hold(source).move_to_element(target).release().perform()

time.sleep(5)
driver.quit()


# actions.move_to_element(element).perform()
# actions.scroll_to_element(element).perform()
# Send the "Esc" key to dismiss the browser alert
# webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()