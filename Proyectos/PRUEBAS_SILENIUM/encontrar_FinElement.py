import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName (unittest.TestCase):
    
    def setUp(self): #Inicia las pruebas.
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.goodstartbooks.com/pruebas")




    def testTagName(self): #por xpath
        elementoTn=driver.find_element_by_tag_name("h3")
        if elementoTn is not None:
            print("Se encontro el h3")
    
    def testFe(self):      
        elementoFE=driver.find_element(By.XPATH, "//*[@id='noImportante']")
        if elementoFE is not None:
            print("Se encontro el ID por File element")
            
   
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()