
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
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(self.tiempo)
        
        sel=Select(driver.find_element_by_xpath("//body/div[@id='belowtopnav']/div[@class='w3-row w3-white']/div[@id='main']/div[@class='w3-row']/div[@class='w3-col m6']/select[1]"))
        sel.select_by_value("8")
        time.sleep(self.tiempo)
        
        
        
      
       
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()