import os
import time
from selenium import webdriver #selenium is package, webdriver is interface
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver-manager
from selenium.webdriver.chrome.service import Service #Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument("--start-maximized")


#webdriver has menthods and classes to intaract with different browsers
driver = webdriver.Chrome(service=Service(), options = option)
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

time.sleep(5)
element = driver.find_element(By.XPATH, "//select[@name = 'ctl00$mainContent$DropDownListCurrency']")

# static dropdown
dropdown = Select(element)
dropdown.select_by_value('USD')
time.sleep(2)
dropdown.select_by_index(0)
time.sleep(2)
dropdown.select_by_visible_text('AED')
time.sleep(5)



# dynamic dropdown [search value, then dropdown appears]

dropdown_search_box = driver.find_element(By.XPATH, "//input[@id = 'autosuggest']")
dropdown_search_box.send_keys('ind')
time.sleep(2)
drop_opts = driver.find_elements(By.XPATH, "//ul[contains(@class, 'ui-autocomplete')][1]/li")
drop_opts_list = []
for opts in drop_opts:
    drop_opts_list.append(opts.text)
    if opts.text == 'India':
        opts.click()

time.sleep(1)

#if we select any value from dropdown and that value gets updated in dom, then element.text won't work in that case, use element.get_attribute('value')_
print(dropdown_search_box.get_attribute("value"))
time.sleep(5)

driver.quit()
# Dropdown
# dropdown = "//select[@id='dropdown-class-example']"
# drop = Select(driver.find_element(By.XPATH(dropdown)))
# drop.select_by_visible_text('')
# drop.select_by_index(0)
# drop.select_by_value('')
# drop.deselect_all()
# opt = drop.options
# selected_options = drop.all_selected_options
# assert dropdown.is_multiple --> returns weather dropdown is multiselect 


