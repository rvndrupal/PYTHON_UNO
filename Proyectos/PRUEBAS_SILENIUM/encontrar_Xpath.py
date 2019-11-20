import unittest
from selenium import webdriver

class FindByIdName (unittest.TestCase):
    
    def setUp(self): #Inicia las pruebas.
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.goodstartbooks.com/pruebas")




    def testXpath(self): #por xpath
        elementoXpath=driver.find_element_by_xpath("//tr[@id='noImportante']")
        if elementoXpath is not None:
            print("El elemento Xpath fue encontrado")
    
    def testClase(self):      
        elementoClass=driver.find_element_by_class_name("rojo")
        if elementoClass is not None:
            print("El elemento por clase fue encontrado")
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()