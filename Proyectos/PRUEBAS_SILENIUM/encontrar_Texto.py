import unittest
from selenium import webdriver

class FindByIdName (unittest.TestCase):
    
    def setUp(self): #Inicia las pruebas.
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.goodstartbooks.com/pruebas")




    def testLinkText(self): #por xpath
        elementoLt=driver.find_element_by_link_text("Pagina 2")
        if elementoLt is not None:
            print("El elemento con texto Pagina 2 fue encontrado")
    
    def testParcialText(self):      
        elementoPt=driver.find_element_by_partial_link_text("agina")
        if elementoPt is not None:
            print("Se encontro el elemento parcial Pagina dos")
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()