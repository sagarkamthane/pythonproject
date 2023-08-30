from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
sort_button = driver.find_element(By.XPATH, "(//span[contains(@class, 'sort-icon')])[1]")
sort_button.click()
sort_button_html = sort_button.get_attribute('outerHTML')
print(sort_button_html)
assert 'ascending' in str(sort_button_html)

table_rows = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")

row_elements = []

for row in table_rows:
    row_elements.append(row.text)

print(row_elements, sorted(row_elements))
assert row_elements == sorted(row_elements)

driver.quit()