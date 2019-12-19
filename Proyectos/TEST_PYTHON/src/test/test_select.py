
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import allure

import pytest





horaGlobal = time.strftime("%H%M%S")



def test_select():   
    with allure.step('Prueba uno del select'):   
        driver = webdriver.Firefox()
        driver.implicitly_wait(15)
        driver.maximize_window()    
        tiempo=1
        
        driver=driver        
        #INGRESO A LA APP DE REGISTRO
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(tiempo)
        
        sel=Select(driver.find_element_by_xpath("//body/div[@id='belowtopnav']/div[@class='w3-row w3-white']/div[@id='main']/div[@class='w3-row']/div[@class='w3-col m6']/select[1]"))
        sel.select_by_value("8")
        allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        time.sleep(tiempo)
    
            
def test_Caja_texto():
    with allure.step('Prueba de la caja de texto'):  
        driver = webdriver.Firefox()
        driver.implicitly_wait(15)
        driver.maximize_window()    
        tiempo=1
        driver=driver        
        #INGRESO A LA APP DE REGISTRO
        driver.get("https://www.w3schools.com/html/html_forms.asp")
        time.sleep(tiempo)
        
        sel=driver.find_element_by_xpath("(//input[contains(@type,'text')])[2]")
        sel.clear()
        sel.send_keys("Rodrigo")       
        allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        time.sleep(tiempo)
    

        
         
            
       
        
        
        
      
       
    
