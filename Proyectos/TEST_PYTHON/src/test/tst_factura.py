import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
from random import randint
from selenium.common.exceptions import TimeoutException

horaGlobal = time.strftime("%H%M%S")

class Test_osiap(unittest.TestCase):
    
   


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.NOMBRE = "rodrigo"
        self.PASSWORD = "rorro131319+"
        self.tiempo=.1
        
        
    def test_001(self):
        print("Iniciando Test")
        time.sleep(self.tiempo)
        self.driver.get("http://localhost:8000/")
        
        self.driver.find_element_by_xpath("//*[@id='id_username']").clear() 
        self.driver.find_element_by_xpath("//*[@id='id_username']").send_keys("")             
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='id_password']").clear()
        self.driver.find_element_by_xpath("//*[@id='id_password']").send_keys(self.PASSWORD)
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
        time.sleep(self.tiempo)
        
        title="Nombre-vacio"        
        self.driver.get_screenshot_as_file(f"../data/capturas/password/{title}-{horaGlobal}.png")
        
        print("Fin test Usuario Vacio")
        time.sleep(self.tiempo)
        
        
    def test_002(self):
        print("Iniciando Test")
        time.sleep(self.tiempo)
        self.driver.get("http://localhost:8000/")
        
        self.driver.find_element_by_xpath("//*[@id='id_username']").clear() 
        self.driver.find_element_by_xpath("//*[@id='id_username']").send_keys("juan")             
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='id_password']").clear()
        self.driver.find_element_by_xpath("//*[@id='id_password']").send_keys("demojuan")
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
        time.sleep(self.tiempo)
        
        title="user-invalido"        
        self.driver.get_screenshot_as_file(f"../data/capturas/password/{title}-{horaGlobal}.png")
        
        print("Fin test usuario invalido")
        time.sleep(self.tiempo)
        
        
    def test_003(self):
        print("Iniciando Test")
        time.sleep(self.tiempo)
        self.driver.get("http://localhost:8000/")
        
        self.driver.find_element_by_xpath("//*[@id='id_username']").clear() 
        self.driver.find_element_by_xpath("//*[@id='id_username']").send_keys("juan")             
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='id_password']").clear()
        self.driver.find_element_by_xpath("//*[@id='id_password']").send_keys("")
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
        time.sleep(self.tiempo)
        
        title="password-Vacio"        
        self.driver.get_screenshot_as_file(f"../data/capturas/password/{title}-{horaGlobal}.png")
        
        print("Fin test password invalido")
        time.sleep(self.tiempo)
        
      

    def test_004(self):        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("http://localhost:8000/")
        
       
        #COLOCAR NOMBRE
        self.driver.find_element_by_xpath("//*[@id='id_username']").clear()
        self.driver.find_element_by_xpath("//*[@id='id_username']").send_keys(self.NOMBRE)              
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='id_password']").clear()
        self.driver.find_element_by_xpath("//*[@id='id_password']").send_keys(self.PASSWORD)
        time.sleep(self.tiempo)
        
        title="Password"        
        self.driver.get_screenshot_as_file(f"../data/capturas/password/{title}-{horaGlobal}.png")
        
        self.driver.find_element_by_xpath(" //*[@id='page-top']/div[2]/div/div/div/div/div/div[2]/div/form/button").click()
        time.sleep(self.tiempo)
        
      
        
        self.driver.find_element_by_xpath("//*[@id='accordionSidebar']/li[2]/a/span").click()
        time.sleep(self.tiempo)
        
        
        
        #click nuevo
        self.driver.find_element_by_xpath("//*[@id='collapseTwo']/div/a[1]").click()
        time.sleep(self.tiempo)
        
        title="Catalogos"        
        self.driver.get_screenshot_as_file(f"../data/capturas/catalogos/{title}-{horaGlobal}.png")
        
        self.driver.find_element_by_xpath(" //*[@id='dropdownMenuLink']/i").click()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div/a").click()
        time.sleep(self.tiempo)
        
        self.nueva=random.choice("AEIOUBCDEFGRTYUEHFTRHDGETSWOEIIOEIDJKKJKKJJDENEHFYTHRK")
        self.nueva2=randint(1,1000000)
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
        
        self.driver.find_element_by_xpath("//*[@id='id_descripcion']").send_keys("Nueva" + str(self.nueva2))        
        time.sleep(self.tiempo)
        
        title="Guardar"        
        self.driver.get_screenshot_as_file(f"../data/capturas/guardar/{title}-{horaGlobal}.png")
        
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
        
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("Nueva")
        time.sleep(self.tiempo)
        
        #Limpia
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").clear()
        time.sleep(self.tiempo)
        
        self.driver.find_element_by_xpath(" //*[@id='DataTables_Table_0_filter']/label/input").send_keys("pyt")
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
        # self.driver.find_element_by_xpath("//*[@id='cat_delit']/i").click()
        # time.sleep(self.tiempo)
        
        # self.driver.find_element_by_xpath("//*[@id='content']/form/div/div/div/div/div[1]/button").click()
        # time.sleep(self.tiempo)
        
    
        
        print("TERMINAN TODAS LAS PRUEBAS")
        time.sleep(self.tiempo)
        
       
        
        
       
        
        
        
        
        
        
        
       
        
        
        
        
        
       
       
        
     
        
        
       
        
        
       
        
        
       
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()