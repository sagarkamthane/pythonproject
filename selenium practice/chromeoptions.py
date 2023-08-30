import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
# both chrome_options = Options() and chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--use-fake-ui-for-media-stream") #disables the browser's default permission prompts for media devices, including the microphone.
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(), options=chrome_options)
driver.get("https://www.google.com")

driver.find_element(By.XPATH, "//div[@jscontroller='unV4T']").click()
driver.quit()