
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import HtmlTestRunner

class Test_001(unittest.TestCase):
   


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()    
        self.tiempo=2
            
       
      

    def test_001(self):
        driver=self.driver

        
        #INGRESO A LA APP DE REGISTRO
        driver.get("http://gmail.com")
        time.sleep(self.tiempo)
        
        driver.get("http://google.com")
        time.sleep(self.tiempo)
        
        driver.get("http://youtuberre.com")
        time.sleep(self.tiempo)
        
        driver.back()
        time.sleep(self.tiempo)
        driver.back()
        time.sleep(self.tiempo)
        driver.forward() #adelante
        time.sleep(self.tiempo)
       
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Python\\Proyectos\\TEST_PYTHON\\src\\reportes'))