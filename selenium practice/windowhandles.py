import time
import webdriver_manager.drivers.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Privacy Policy']")))
# driver.find_element(By.XPATH, "//a[text()='Privacy Policy']").click()

driver.switch_to.new_window('tab')
driver.get('https://www.google.com')
windowh = driver.window_handles
print(windowh)
driver.switch_to.window(windowh[1])

# time.sleep(2)
# window_h = driver.window_handles
# driver.switch_to.window(window_h[0])

time.sleep(5)
driver.quit()

