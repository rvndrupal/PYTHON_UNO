
import unittest
import time
from selenium import webdriver
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
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(self.tiempo)
        
        toggle=driver.find_element_by_xpath("(//div[contains(@class,'slider round')])[1]")
        toggle.click()
        time.sleep(self.tiempo)
        toggle.click()
        time.sleep(self.tiempo)
        
        
      
       
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()