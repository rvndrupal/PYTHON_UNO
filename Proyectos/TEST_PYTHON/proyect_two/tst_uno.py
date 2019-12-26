import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://newtours.demoaut.com/')

user=driver.find_element_by_xpath("//input[contains(@name,'userName')]")
password=driver.find_element_by_xpath("//input[@type='password']")
boton=driver.find_element_by_xpath("//input[@value='Login']")

user.send_keys('test')
password.send_keys('test')
boton.click()
time.sleep(5)

driver.quit()
