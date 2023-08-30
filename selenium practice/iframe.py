import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tinymce")
iframe = driver.find_element(By.XPATH, "//iframe[@id='mce_0_ifr']")
driver.switch_to.frame(iframe)
text_ele = driver.find_element(By.XPATH, "//body[@id='tinymce']/p")
new_text = text_ele.text

time.sleep(2)
action = ActionChains(driver)
for i in new_text:
    text_ele.send_keys(Keys.BACKSPACE)


driver.switch_to.default_content()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@title='Bold']").click()

iframe = driver.find_element(By.XPATH, "//iframe[@id='mce_0_ifr']")
driver.switch_to.frame(iframe)
text_ele.send_keys(new_text)
driver.switch_to.frame('')
time.sleep(5)
driver.quit()
