
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
        driver.get("file:///C:/Python/Proyectos/TEST_PYTHON/alert.html")
        time.sleep(self.tiempo)
        push=driver.find_element_by_xpath("//button[@name='alert'][contains(.,'Click')]")
        push.click()
        time.sleep(self.tiempo)
        alert_simple=driver.switch_to_alert()
        alert_simple.dismiss() #cuando solo hay un solo boton para presionar un solo boton
        time.sleep(self.tiempo)
        
        
       
        
        
        
      
       
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()