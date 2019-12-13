import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
from random import randint

class Test_osiap(unittest.TestCase):
    
   


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.NOMBRE = "rodrigo"
        self.PASSWORD = "rorro131319+"
        self.tiempo=1.5
        
        

    def test_001(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("http://localhost:8000/")
        
        print("Iniciando Test")
        time.sleep(.5)
        #COLOCAR NOMBRE
        self.driver.find_element_by_xpath("//*[@id='id_username']").clear()
        self.driver.find_element_by_xpath("//*[@id='id_username']").send_keys(self.NOMBRE)              
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='id_password']").clear()
        self.driver.find_element_by_xpath("//*[@id='id_password']").send_keys(self.PASSWORD)
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='accordionSidebar']/li[2]/a/span").click()
        time.sleep(self.tiempo)
        
        #click nuevo
        self.driver.find_element_by_xpath("//*[@id='collapseTwo']/div/a[1]").click()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='dropdownMenuLink']/i").click()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div/a").click()
        time.sleep(self.tiempo)
        
        # self.nueva=random.choice("AEIOUBCDEFGRTYUEHFTRHDGETSWOEIIOEIDJKKJKKJJDENEHFYTHRK")
        # self.nueva2=randint(1,10000)
        self.driver.find_element_by_xpath("//*[@id='id_descripcion']").send_keys("NuevaTest")
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='id_estado']").click()
        time.sleep(self.tiempo)
        
        #cancelar
        self.driver.find_element_by_xpath("//*[@id='content']/form/div/div/div/div/div/div[5]/div/a").click()
        time.sleep(self.tiempo)
        
        #para agregar ok
        self.driver.find_element_by_xpath(" //*[@id='dropdownMenuLink']/i").click()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div/a").click()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='id_descripcion']").send_keys("NuevaTest")        
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='id_estado']").click()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='content']/form/div/div/div/div/div/div[5]/div/button").click()
        time.sleep(self.tiempo)
                   
        self.driver.find_element_by_xpath("//*[@id='page-top']/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button").click()
        time.sleep(self.tiempo)
        #termina agregar
        
        #inicia buscar
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").clear()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("NuevaTest")
        time.sleep(self.tiempo)
        
        #Limpia
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").clear()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("pyt")
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("NuevaTest")
        time.sleep(self.tiempo)
        
        editar = self.driver.find_element_by_xpath("//*[@id='cat_edit']/i")
        editar.click()    
        time.sleep(self.tiempo)
        
        #editando 
        self.driver.find_element_by_xpath("//*[@id='id_descripcion']").clear()   
        editar = self.driver.find_element_by_xpath("//*[@id='id_descripcion']").send_keys("python"+str(self.nueva2))   
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='content']/form/div/div/div/div/div/div[5]/div/button").click() 
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button").click() 
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").clear()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("pyt")
        time.sleep(self.tiempo)
        
        
        #eliminar
        # eliminar = driver.find_element_by_css_selector('[href^=http://somelink.com/]')
        self.driver.find_element_by_xpath("//*[@id='cat_delit']/i").click()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='content']/form/div/div/div/div/div[1]/button").click()
        time.sleep(self.tiempo)
        
        
        
        
        
        
        
       
        
        
        
        
        print("FIN DEL TEST")
        time.sleep(self.tiempo)
        
       
        
        
       
        
        
        
        
        
        
        
       
        
        
        
        
        
       
       
        
     
        
        
       
        
        
       
        
        
       
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()