import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class FindByIdName (unittest.TestCase):
    
    def setUp(self): #Inicia las pruebas.
        global driver
        driver = webdriver.Firefox()
        #driver = webdriver.Chrome()
        #driver = webdriver.Ie()
        driver.get("file:///C:/Python/Proyectos/PRUEBAS_SILENIUM/index.html")




    def testUno(self): #por xpath busca la liga
                       
        
        #Primer valor de Prueba
        nombre=driver.find_element_by_id("nombre") #busca el campo y escribe
        if nombre is not None:
            time.sleep(1)
            nombre.send_keys("Rodrigo")
            time.sleep(1)
            nom = nombre.get_attribute("value")
            print("Nombre: ", nom)
            time.sleep(2)
            if nom == "Rodrigo":
                print("Bienvenido Rodrigo todo ok")
            
           
            
        
        ap=driver.find_element_by_id("ap") #busca el campo y escribe
        if ap is not None:
            ap.send_keys("Villanueva")
            time.sleep(1)
        
        am=driver.find_element_by_id("am") #busca el campo y escribe
        if am is not None:
            am.send_keys("Nieto")
            time.sleep(1)
            
            
            time.sleep(1)
            
        radio=driver.find_element_by_id("RadioGroup1_0")
        if radio is not None:
            radio.click()
            time.sleep(1)
            
        radio2=driver.find_element_by_id("RadioGroup1_1")
        if radio2 is not None:
            radio2.click()
            time.sleep(1)
            
        check1=driver.find_element_by_id("CheckboxGroup1_0")
        if check1 is not None:
            check1.click()
            time.sleep(1)
            
        check2=driver.find_element_by_id("CheckboxGroup1_1")
        if check2 is not None:
            check2.click()
            time.sleep(1)
        
        check3=driver.find_element_by_id("CheckboxGroup1_2")
        if check3 is not None:
            check3.click()
            time.sleep(1)
            
        ingredientes=driver.find_element_by_name("ingrediente")
        if ingredientes is not None:
            ingreSel=Select(ingredientes)
            ingreSel.select_by_value("cebolla")
            time.sleep(1)
            
        frutas=driver.find_element_by_name("Select1")
        if frutas is not None:
            frutaSel=Select(frutas)
            frutaSel.select_by_index(1)
            frutaSel.select_by_visible_text("Sandia")
            time.sleep(1)
                
       
        
            
            
        
        
     
            
   
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()
    
    


