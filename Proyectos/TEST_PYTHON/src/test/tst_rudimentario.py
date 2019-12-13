from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title

time.sleep(3)
elem = driver.find_element_by_id("id-search-field")

elem.clear()

elem.send_keys("pycon") ###escribo pycon

time.sleep(3)

elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()