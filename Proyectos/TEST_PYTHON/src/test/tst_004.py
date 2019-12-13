# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time
from selenium import webdriver

class Test_004(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "rodrigo"
        self.APELLIDO = "Villanueva"
        self.USERNAME = "rodrigopython1"
        self.PASSWORD = "rorro131319"

    def test_004(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        
        #COLOCAR NOMBRE
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id("firstName").send_keys(self.NOMBRE)
        nombre=self.driver.find_element_by_id("firstName")
        nom = nombre.get_attribute("value")
        if nom == "rodrigo":
            print("Saludos Rodrigo Bienvenido")
        time.sleep(2)
        
        
        #COLOCAR APELLIDO
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").clear()
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").send_keys(self.APELLIDO)
        print("Apellidos ok")
        time.sleep(2)
        
        #COLOCAR USERNAME
        self.driver.find_element_by_name("Username").clear()
        self.driver.find_element_by_name("Username").send_keys(self.USERNAME)
        print("Email ok")
        time.sleep(2)
        
        #COLOCAR PASSWORD
        self.driver.find_element_by_xpath("(//*[@jsname='YPqjbf'])[5]").clear()
        self.driver.find_element_by_xpath("(//*[@jsname='YPqjbf'])[5]").send_keys(self.PASSWORD)
        print("Password ok")
        time.sleep(2)
        
        #COLOCAR CONFIRMACION DE  PASSWORD
        self.driver.find_element_by_xpath("(//*[@jsname='YPqjbf'])[7]").clear() #crear tu propio elemento
        self.driver.find_element_by_xpath("(//*[@jsname='YPqjbf'])[7]").send_keys(self.PASSWORD)
        print("Confirm ok")
        time.sleep(2)
        
        # self.driver.find_element_by_partial_link_text("Acceder a tu cuenta en su lugar").click() 
        #accede por un link de texto        
        
        #BOTON NEXT
        self.driver.find_element_by_xpath("//*[@id='accountDetailsNext']").click()
        print("Click ok")
        time.sleep(2)
        
        
        
        # #MENSAJE DE VALIDACION
        # MENSAJE_ERROR = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[1]/div/h1").text
       
        # print(MENSAJE_ERROR)
    
        # assert MENSAJE_ERROR == "Verifica tu teléfono", "No coinciden"
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()