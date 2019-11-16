from selenium import webdriver

driver = webdriver.Ie()

driver.get("http://www.goodstartbooks.com")
           
driver.quit()