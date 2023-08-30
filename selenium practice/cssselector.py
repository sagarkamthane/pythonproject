from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

driver = webdriver.Chrome(service = Service(), options=chrome_options)
driver.get("https://www.google.com")


#css selector

# tag
#  syntax: tagname
#  ex: div

#byclass name
driver.find_element(By.CSS_SELECTOR(".rc-segmented-control-item.rc-segmented-control-with-violator"))
# if class attribute value has space in it then replace space with . "rs-bundleselection-contentsection as-l-container"

#by id
driver.find_element(By.CSS_SELECTOR("#globalnav-menubutton-link-store"))

# Tag and ID
# syntax: tag#id
# ex: input#email

# Tag and class
# tag.class
# input.inputtext


# Tag and ID:
# Example CSS Selector: tag#id
# Example XPath: //tag[@id='id']

# Tag and Class:
# Example CSS Selector: tag.class
# Example XPath: //tag[@class='class']

# Tag and Attribute:
# Example CSS Selector: tag[attribute='value']
# Example XPath: //tag[@attribute='value']

# Tag, Class, and Attribute:
# Example CSS Selector: tag.class[attribute='value']
# Example XPath: //tag[@class='class' and @attribute='value']

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# tag Selector
element = driver.find_element(By.CSS_SELECTOR("p"))
print(element.text)

# ID Selector
element = driver.find_element(By.CSS_SELECTOR("#header"))
print(element.text)

# Class Selector
element = driver.find_element(By.CSS_SELECTOR(".highlight"))
print(element.text)

# Attribute Selector
element = driver.find_element(By.CSS_SELECTOR("[type]"))
print(element.get_attribute("type"))

# Attribute Value Selector
element = driver.find_element(By.CSS_SELECTOR("[data-category='fruit']"))
print(element.text)


driver.quit()
