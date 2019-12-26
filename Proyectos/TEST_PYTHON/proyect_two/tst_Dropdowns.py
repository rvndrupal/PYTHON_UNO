import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get('http://newtours.demoaut.com/')
t=2


bot_reg=driver.find_element_by_xpath("//a[contains(.,'REGISTER')]")
time.sleep(t)
bot_reg.click()


country=Select(driver.find_element_by_xpath("//select[@name='country']"))
# country.select_by_index(5)
# country.select_by_value("11")
country.select_by_visible_text("ARGENTINA")







time.sleep(t)
driver.quit()
