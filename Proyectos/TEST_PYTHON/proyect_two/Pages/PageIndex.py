import time
from selenium.webdriver.support.ui import Select
from Pages.Buscar import *

class PageIndex:
    def __init__(self,myDriver):
        self.driver=myDriver
        
    def click_register(self):
        self.driver.find_element_by_xpath("//a[contains(.,'REGISTER')]").click()
        time.sleep(2)
        
    def login(self, nombre , password):
        user=self.driver.find_element_by_xpath("//input[contains(@name,'userName')]")
        password=self.driver.find_element_by_xpath("//input[@type='password']")
        boton=self.driver.find_element_by_xpath("//input[@value='Login']")
        user.send_keys(str(nombre))
        password.send_keys(str(password))
        boton.click()
        time.sleep(2)   
        
    def entrada(self):
        link_reg=self.driver.find_element_by_link_text("registration form")
        self.assertEquals(link_reg.text, "registration form")