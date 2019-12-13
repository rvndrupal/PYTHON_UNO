from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class test_004(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
        self.driver.implicitly_wait(10) #espera un evento
        self.driver.maximize_window
        self.Ap="Villanueva"
        self.mail="rodrigophyton1@gmail.com"
        
        
    def test_004(self): #super importante que se inicie con test
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id("firstName").send_keys("Rodrigo")
        time.sleep(3)
        self.driver.find_element_by_id("lastName").clear()
        self.driver.find_element_by_id("lastName").send_keys(self.Ap)
        time.sleep(3)
        
        self.driver.find_element_by_xpath("//*[@id='username']").clear()
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys(self.mail)
        time.sleep(3)
        
        
        
        

        

    def tearDown(self): 
        self.driver.quit()
       
        
        

        
        
if __name__ == '__main__':
    unittest.main()