
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2

#instalar la libreria opencv-python
#pip install opencv-python

class Test_001(unittest.TestCase):
   


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()    
        self.tiempo=2
            
       
      

    def test_001(self):
        driver=self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot('img2.PNG')
        time.sleep(self.tiempo)
        
    def test_comparando_imagenes(self):
        img1=cv2.imread('img1.PNG')
        img2=cv2.imread('img2.PNG')
        
        diferencia= cv2.absdiff(img1, img2)
        imagen_gris=cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY) #ESCALA DE GRIS
        contours,_ = cv2.findContours(imagen_gris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        for c in contours:
            if cv2.contourArea(c) >= 20:
                posicion_x,posicion_y,ancho,alto = cv2.boundingRect(c)
                cv2.rectangle(img1,(posicion_x,posicion_y),(posicion_x+ancho,posicion_y+alto),(0,0,255),2)
                
        while(1):
            cv2.imshow('Imagen1', img1)
            cv2.imshow('Imagen2', img2)
            cv2.imshow('Diferencias detectadas', diferencia)
            teclado=cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        cv2.destroyAllWindows()
            
            
       
       
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()