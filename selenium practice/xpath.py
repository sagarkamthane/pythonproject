import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

driver = webdriver.Chrome(service = Service(), options=chrome_options)
driver.get("https://www.google.com")

driver.find_element(By.XPATH, "//div[@aria-label = 'Search by voice']").click() #normalxpath

# Xpaths
Search_icon = "//div[@class='SDkEP']/div[1]/div"
contsins = "(//input[contains(@value, 'Google Search')])[2]"
text = "//a[text()='Gmail']"
starts_with = "//a[starts-with(@aria-label, 'Search')]"
and_in_xpath = "//*[contains(@class, 'rc-segmented-control-button') and @data-autom='filterButton-13inchm1']"
or_in_xpath = "//*[(text()='13-inch (13-inch (M2 chip))') or @data-autom='filterButton-13inchm2']"

driver.quit()

# Axes
# parent --> xpath/..
# child --> xpath/childtag    --> child tag refers to tag of chilod element
# following sibling --> xpath/following-sibling::tag
# preceding sibling --> xpath/preceding-sibling::tag

# how t find xpath under shadow dom
element = driver.find_element(By.TAG_NAME, 'your-shadow-host-element')
# Get the shadow root
shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
# Find the shadow DOM element using traditional WebDriver methods
shadow_element = shadow_root.find_element(By.XPATH, '//your-xpath-inside-shadow-root')
# Interact with the shadow DOM element
shadow_element.click()
