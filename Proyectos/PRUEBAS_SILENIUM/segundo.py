from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.goodstartbooks.com")
           
driver.quit()