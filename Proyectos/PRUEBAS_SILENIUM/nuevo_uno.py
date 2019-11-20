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
            time.sleep(2)
            
            
            time.sleep(3)
                
       
        
            
            
        
        
     
            
   
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()