
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from Pages.PageIndex import *
from Pages.Buscar import *

class test_unit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://newtours.demoaut.com/')
        self.pi= PageIndex(self.driver)
        self.b=Buscar(self.driver)
        
       
        
        
    def test_drop(self): #super importante que se inicie con test
        self.pi.click_register()
        
        # country=Select(self.driver.find_element_by_xpath("//select[@name='country']"))
       
        #country=Select(self.b.bus_x("//select[@name='country']"))
        country=Select(self.b.bus_n("country"))
        # country.select_by_index(5)
        # country.select_by_value("11")
        country.select_by_visible_text("CONGO")
        self.assertEquals(country.first_selected_option.text.strip(),"CONGO")
        
    def test_entrada(self):
        self.pi.login('test','test')
        
        self.pi.entrada()
      
        
        

        

    def tearDown(self): 
        self.driver.quit()
       
       
       
        
if __name__ == '__main__':
    unittest.main()