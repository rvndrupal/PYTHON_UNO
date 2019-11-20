import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindByIdName (unittest.TestCase):
    
    def setUp(self): #Inicia las pruebas.
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.goodstartbooks.com/pruebas")




    def testLiga(self): #por xpath busca la liga
        liga=driver.find_element(By.XPATH, "//a[contains(text(),'Pagina 2')]")
        if liga is not None:
            print("Liga ok")
            time.sleep(3)
            liga.click()            
            
            
            
        nombre=driver.find_element_by_id("Segundo") #busca el campo y escribe
        if nombre is not None:
            print("nombre ok")
            time.sleep(5)
            
            nombre.send_keys("Rodrigo Villanueva nieto")
            
            time.sleep(5)
            
            
    
   
            
   
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()