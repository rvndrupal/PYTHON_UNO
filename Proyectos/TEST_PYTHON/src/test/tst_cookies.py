
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
        driver.get("https://www.w3schools.com/python/")
        time.sleep(self.tiempo)
        all_cookies=driver.get_cookies()
        
        print(all_cookies)
        time.sleep(self.tiempo)
        
        
        
        
       
        
        
        
      
       
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()