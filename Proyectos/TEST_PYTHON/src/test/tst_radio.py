
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Test_001(unittest.TestCase):
   


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()    
        self.tiempo=2
            
       
      

    def test_001(self):
        driver=self.driver

        
        #INGRESO A LA APP DE REGISTRO
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(self.tiempo)
        
        radio="(//input[@type='checkbox'])[2]"
        check="(//span[@class='checkmark'])[3]"
        
        
        driver.find_element_by_xpath(radio).click()
        time.sleep(self.tiempo)
        
        driver.find_element_by_xpath(check).click()
        time.sleep(self.tiempo)
        
        
        
      
       
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()