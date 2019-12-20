
import cv2
import pytesseract



imagen=cv2.imread("carloss.jpg") #lee la imagen
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
texto=pytesseract.image_to_string(imagen)
print(texto)

        
        
        
        
       
        
        
        
      
       
    
        
