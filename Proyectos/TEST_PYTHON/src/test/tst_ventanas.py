# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_001(unittest.TestCase):
   


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()    
        self.tiempo=6    
       
      

    def test_001(self):
        driver=self.driver
        
        #INGRESO A LA APP DE REGISTRO
        driver.get("http://google.com")
        time.sleep=(self.tiempo)
        driver.execute_script("window.open('');")
        time.sleep=(self.tiempo)
        driver.switch_to_window(driver.window_handles[1])
        driver.get("http://localhost:8000/inv/categorias/")
        time.sleep=(self.tiempo)
        driver.switch_to_window(driver.window_handles[0])
        time.sleep=(self.tiempo)
        
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()