import unittest
from selenium import webdriver

class FindByIdName (unittest.TestCase):
    
    def setUp(self): #Inicia las pruebas.
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.goodstartbooks.com/pruebas")




    def testName(self): #La prueba tiene que empezar con test
        elementoName=driver.find_element_by_name("ultimo")
        if elementoName is not None:
            print("El elemento con name ultimo fue encontrado")
    
    def testId(self):      
        elementoId=driver.find_element_by_id("noImportante")
        if elementoId is not None:
            print("El elemento id noImportante fue encontrado")
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()