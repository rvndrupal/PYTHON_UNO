import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Test_osiap(unittest.TestCase):
    
   


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.NOMBRE = "rodrigo"
        self.PASSWORD = "Rorro131319++"
        
        

    def test_001(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("http://localhost/senasica/user")
        
        #COLOCAR NOMBRE
        self.driver.find_element_by_id("edit-name").clear()
        self.driver.find_element_by_id("edit-name").send_keys(self.NOMBRE)
        time.sleep(.5)
        
          #COLOCAR NOMBRE
        self.driver.find_element_by_id("edit-pass").clear()
        self.driver.find_element_by_id("edit-pass").send_keys(self.PASSWORD)
        time.sleep(.5)
        
        self.driver.find_element_by_id("edit-submit").click()
        time.sleep(.5)  
        
        
        self.driver.find_element_by_xpath("//*[@id='block-system-main']/div/div[1]/div/div[2]/div/div[13]/div/div[2]/div/a[1]").click()  
        time.sleep(5)  
        
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div/form/div/div[1]/input").send_keys("hola")
        time.sleep(5)
        
        #Ver el numero de Ventanas
        
        
        
       
        
        
       
        
        
       
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()