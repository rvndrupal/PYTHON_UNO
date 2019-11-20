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
        driver.get("http://www.goodstartbooks.com/pruebas")




    def testLiga(self): #por xpath busca la liga
        
        time.sleep(4)
                
        
        #Seleccion boton verde menu
        botontMenu=driver.find_element_by_class_name("dropbtn")
        if botontMenu is not None:
            acciones=ActionChains(driver)
            acciones.move_to_element(botontMenu).perform() #la accion se va al boton menu
            
            liga=driver.find_element_by_link_text("Link 2")
            if liga is not None:
                acciones.move_to_element(liga)
                acciones.click()
                acciones.perform()#para que se ejecuten
                time.sleep(4)
                
       
        
            
            
        
        
        check1=driver.find_element_by_id("CheckboxGroup1_0")
        if check1 is not None:
            time.sleep(2)
            check1.click()
            time.sleep(2)
            
        check2=driver.find_element_by_id("CheckboxGroup1_1")
        if check2 is not None:
            check2.click()
            time.sleep(2)
        
        
        
        
        radio=driver.find_element_by_id("RadioGroup1_0")
        if radio is not None:
            radio.click()
            time.sleep(2)
            
        radio2=driver.find_element_by_id("RadioGroup1_1")
        if radio2 is not None:
            radio2.click()
            time.sleep(2)
            
        
        ingredientes=driver.find_element_by_name("ingrediente")
        if ingredientes is not None:
            ingreSel=Select(ingredientes)
            ingreSel.select_by_value("cilantro")
            print("Se Activa el combo con la selección de Cilantro")
            time.sleep(5)
            
        frutas=driver.find_element_by_name("Select1")
        if frutas is not None:
            frutaSel=Select(frutas)
            frutaSel.select_by_index(1)
            frutaSel.select_by_visible_text("Sandia")
            time.sleep(2)
            
        #Obteniendo los valores.
        opcion1=driver.find_element_by_xpath("//*[@id='noImportante']/td[2]")
        if opcion1 is not None:
            print("el valor de la opcion es: ", opcion1.text)
            time.sleep(2)
            
        opcion2=driver.find_element_by_id("importante")
        if opcion2 is not None:
            valAtri=opcion2.get_attribute("class")
            print("La clase es: ", valAtri)
            time.sleep(2)
            
        #boton modal
            
        modal=driver.find_element_by_xpath("//*[@id='center']/button")
        if modal is not None:
            modal.click()
            time.sleep(2)
            #aceptar modal
            alert=driver.switch_to_alert()
            
            alert.accept()
            time.sleep(2)    
            
        # #Iframe de la aplicación
        # Iframe=driver.find_element_by_id("pruebas-iframe")
        # if Iframe is not None:
        #     driver.switch_to.frame(Iframe)
        #     nomseg=driver.find_element_by_id("Segundo")
        #     if nomseg is not None:
        #         nomseg.send_keys("Texto uno")
        #         time.sleep(5)
            
            
        
        liga=driver.find_element(By.XPATH, "//a[contains(text(),'Pagina 2')]")
        if liga is not None:
            print("Liga ok")
            time.sleep(2)
            liga.click()  
            
            
            
        nombre=driver.find_element_by_id("Segundo") #busca el campo y escribe
        if nombre is not None:
            print("nombre ok")
            time.sleep(3)
            
            nombre.send_keys("Noemi se quedo con el ojo cuadrado")
            
            time.sleep(2)        
            print("Termina la Prueba")
            
            
    
   
            
   
              

    
    def tearDown(self): #Final
        driver.quit()
        
if __name__=="__main__": 
    unittest.main()