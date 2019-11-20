import unittest
from selenium import webdriver

class FindByIdName (unittest.TestCase):
    
    def setUp(self): #Inicia las pruebas.
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.goodstartbooks.com/pruebas")




    def testTagName(self): #por xpath
        elementoTn=driver.find_element_by_tag_name("h3")
        if elementoTn is not None:
            print("Se encontro el h3")
    
    def testCssSelector(self):      
        elementoCss=driver.find_element_by_css_selector("#primera")
        if elementoCss is not None:
            print("Se encontro el id primera")
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()