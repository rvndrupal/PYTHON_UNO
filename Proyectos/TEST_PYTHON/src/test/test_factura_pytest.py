import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random
from random import randint

import allure
import pytest


    
#pytest test_factura_pytest.py --alluredir  C:\Python\Proyectos\TEST_PYTHON\src\reports

#crear en carpeta reportes
#allure generate C:\Python\Proyectos\TEST_PYTHON\src\reports  --clean      


        
        
def test_001():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver=driver
    tiempo=.5
    time.sleep(tiempo)
    driver.get("http://localhost:8000/")
    
    driver.find_element_by_xpath("//*[@id='id_username']").clear() 
    #driver.find_element_by_xpath("//*[@id='id_username']").send_keys("")             
    driver.find_element_by_xpath("//*[@id='id_usernamerr']").send_keys("") 
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)  #error prueba           
        
    driver.find_element_by_xpath("//*[@id='id_password']").clear()
    driver.find_element_by_xpath("//*[@id='id_password']").send_keys("demo")
    time.sleep(tiempo)
    
    driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
    time.sleep(tiempo)
    
    
    print("Fin test Usuario Vacio")
    time.sleep(tiempo)
    
        
def test_002():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver=driver
    tiempo=.5
    time.sleep(tiempo)
    driver.get("http://localhost:8000/")
    
    driver.find_element_by_xpath("//*[@id='id_username']").clear() 
    driver.find_element_by_xpath("//*[@id='id_username']").send_keys("juan")             
    time.sleep(tiempo)
    
    driver.find_element_by_xpath("//*[@id='id_password']").clear()
    driver.find_element_by_xpath("//*[@id='id_password']").send_keys("demojuan")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    
    driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
    time.sleep(tiempo)
    

    print("Fin test usuario invalido")
    time.sleep(tiempo)
    
        
def test_003():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver=driver
    tiempo=.5
    time.sleep(tiempo)
    driver.get("http://localhost:8000/")
    
    driver.find_element_by_xpath("//*[@id='id_username']").clear() 
    driver.find_element_by_xpath("//*[@id='id_username']").send_keys("juan")             
    time.sleep(tiempo)
    
    driver.find_element_by_xpath("//*[@id='id_password']").clear()
    driver.find_element_by_xpath("//*[@id='id_password']").send_keys("")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    
    driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
    time.sleep(tiempo)
    
    
    print("Fin test password invalido")
    time.sleep(tiempo)
        
    
def test_004():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver=driver
    tiempo=.5
    time.sleep(tiempo)
    driver.get("http://localhost:8000/")

    driver.find_element_by_xpath("//*[@id='id_username']").clear() 
    driver.find_element_by_xpath("//*[@id='id_username']").send_keys("ro33456")             
    time.sleep(tiempo)

    driver.find_element_by_xpath("//*[@id='id_password']").clear()
    driver.find_element_by_xpath("//*[@id='id_password']").send_keys("rodrigo")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)

    driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
    time.sleep(tiempo)

    print("Fin test nombre numeros")
    time.sleep(tiempo)



def test_Categorias():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()  
    driver=driver 
    tiempo=.5     
    #INGRESO A LA APP DE REGISTRO
    driver.get("http://localhost:8000/")

    #COLOCAR NOMBRE
    driver.find_element_by_xpath("//*[@id='id_username']").clear()
    driver.find_element_by_xpath("//*[@id='id_username']").send_keys("rodrigo")              
    time.sleep(tiempo)

    driver.find_element_by_xpath("//*[@id='id_password']").clear()
    driver.find_element_by_xpath("//*[@id='id_password']").send_keys("rorro131319+")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Carga ok")


    driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
    time.sleep(tiempo)

    driver.find_element_by_xpath("//*[@id='accordionSidebar']/li[2]/a/span").click()
    time.sleep(tiempo)

    #click nuevo
    driver.find_element_by_xpath("//*[@id='collapseTwo']/div/a[1]").click()
    time.sleep(tiempo)


    driver.find_element_by_xpath(" //*[@id='dropdownMenuLink']/i").click()
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Menu nuevo ok")
    

    driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div/a").click()
    time.sleep(tiempo)

    nueva=random.choice("AEIOUBCDEFGRTYUEHFTRHDGETSWOEIIOEIDJKKJKKJJDENEHFYTHRK")
    nueva2=randint(1,1000000)
    driver.find_element_by_xpath("//*[@id='id_descripcion']").send_keys("NuevaTest")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Carga nuevo texto NuevaTest")
    

    driver.find_element_by_xpath("//*[@id='id_estado']").click()
    time.sleep(tiempo)

    #cancelar
    driver.find_element_by_xpath("//*[@id='content']/form/div/div/div/div/div/div[5]/div/a").click()
    time.sleep(tiempo)

    #para agregar ok
    driver.find_element_by_xpath(" //*[@id='dropdownMenuLink']/i").click()
    time.sleep(tiempo)

    driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div/a").click()
    time.sleep(tiempo)

    driver.find_element_by_xpath("//*[@id='id_descripcion']").send_keys("Nueva" + str(nueva2))        
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Carga del nuevo texto a Guardar")
    

    

    driver.find_element_by_xpath("//*[@id='id_estado']").click()
    time.sleep(tiempo)

    driver.find_element_by_xpath("//*[@id='content']/form/div/div/div/div/div/div[5]/div/button").click()
    time.sleep(tiempo)
                
    driver.find_element_by_xpath("//*[@id='page-top']/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button").click()
    time.sleep(tiempo)
    #termina agregar

    #inicia buscar
    driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").clear()
    time.sleep(tiempo)

    driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("Nueva")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Buscando la palabra Nueva ok")
    

    #Limpia
    driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").clear()
    time.sleep(tiempo)

    driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("pyt")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Buscando la palabra pyt ok")
    


    editar = driver.find_element_by_xpath("//*[@id='cat_edit']/i")
    editar.click()    
    time.sleep(tiempo)

    #editando 
    driver.find_element_by_xpath("//*[@id='id_descripcion']").clear()   
    editar = driver.find_element_by_xpath("//*[@id='id_descripcion']").send_keys("python"+str(nueva2))   
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Se modifica la palabra python ok")
    

    driver.find_element_by_xpath("//*[@id='content']/form/div/div/div/div/div/div[5]/div/button").click() 
    time.sleep(tiempo)

    driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button").click() 
    time.sleep(tiempo)

    driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").clear()
    time.sleep(tiempo)

    driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("pyt")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Se muestra ultima busqueda python ok")
    
    
def test_Subcategorias():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()  
    driver=driver  
    tiempo=.5    
    #INGRESO A LA APP DE REGISTRO
    driver.get("http://localhost:8000/")
    
     #COLOCAR NOMBRE
    driver.find_element_by_xpath("//*[@id='id_username']").clear()
    driver.find_element_by_xpath("//*[@id='id_username']").send_keys("rodrigo")              
    time.sleep(tiempo)

    driver.find_element_by_xpath("//*[@id='id_password']").clear()
    driver.find_element_by_xpath("//*[@id='id_password']").send_keys("rorro131319+")
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
    time.sleep(tiempo)
    print("Carga ok")
    
    driver.find_element_by_xpath("//span[contains(.,'Catálogos')]").click()
    time.sleep(tiempo)
    driver.find_element_by_xpath("//a[contains(.,'Sub Categorias')]").click()
    time.sleep(tiempo)
    print("click subcategoria ok")
    driver.find_element_by_xpath("//a[contains(.,'Nueva')]").click()
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    time.sleep(tiempo)
    print("Clck nueva Subcategoria ok")

