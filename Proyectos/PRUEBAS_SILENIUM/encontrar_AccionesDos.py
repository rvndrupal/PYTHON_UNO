import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class FindByIdName (unittest.TestCase):
    
    def setUp(self): #Inicia las pruebas.
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.goodstartbooks.com/pruebas")




    def testLiga(self): #por xpath busca la liga
        
        
        check1=driver.find_element_by_id("CheckboxGroup1_0")
        if check1 is not None:
            check1.click()
            time.sleep(3)
            
        check2=driver.find_element_by_id("CheckboxGroup1_1")
        if check2 is not None:
            check2.click()
            time.sleep(3)
        
        
        
        
        radio=driver.find_element_by_id("RadioGroup1_0")
        if radio is not None:
            radio.click()
            time.sleep(3)
            
        radio2=driver.find_element_by_id("RadioGroup1_1")
        if radio2 is not None:
            radio2.click()
            time.sleep(3)
            
        
        ingredientes=driver.find_element_by_name("ingrediente")
        if ingredientes is not None:
            ingreSel=Select(ingredientes)
            ingreSel.select_by_value("cebolla")
            time.sleep(4)
            
        frutas=driver.find_element_by_name("Select1")
        if frutas is not None:
            frutaSel=Select(frutas)
            frutaSel.select_by_index(1)
            frutaSel.select_by_visible_text("Sandia")
            time.sleep(4)
              
        
        
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
            print("Termina la Prueba")
            
            
    
   
            
   
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()