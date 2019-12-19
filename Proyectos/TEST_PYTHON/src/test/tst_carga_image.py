
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os

class Test_001(unittest.TestCase):
   


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()    
        self.tiempo=3
            
       
      

    def test_001(self):
        driver=self.driver

        
        #INGRESO A LA APP DE REGISTRO
        driver.get("http://the-internet.herokuapp.com/upload")
        time.sleep(self.tiempo)
        driver.find_element_by_xpath("//input[@id='file-upload']").send_keys("C:\\Users\\rodrigo.villanueva.c\\Pictures\\python.jpg")
        time.sleep(self.tiempo)
        driver.find_element_by_xpath("//input[@id='file-submit']").click()
        time.sleep(self.tiempo)
     
        

    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()