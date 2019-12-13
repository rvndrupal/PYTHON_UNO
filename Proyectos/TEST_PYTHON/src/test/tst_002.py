import unittest
import time


class test_002(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_002(self): #super importante que se inicie con test
        self.a = 10
        self.b = 20
        #self.r =a+b
        
        self.assertEqual(self.a, self.b, "Los valores son Distintos")
        
        
    def test_003(self): #super importante que se inicie con test
        self.a = 10
        self.b = 10
        #self.r =a+b
        
        self.assertEqual(self.a, self.b, "Los valores son Distintos")
        
        
    def test_004(self): #super importante que se inicie con test
        self.a = 10
        self.b = 10
        #self.r =a+b        
        self.assertNotEqual(self.a, self.b, "Los valores son iguales") 
        
    def test_005(self): #super importante que se inicie con test
        self.a = False    #esta esperando un True  
        self.assertTrue(self.a, f"La variable {self.a}") 
        
    def test_006(self): #super importante que se inicie con test
        self.a = 20.1 
        
        if self.a > 20:
            self.r=True  
        else:
            self.r=False
            
        self.assertTrue(self.r, f"La variable no es True es: {self.r}") 
        
    def test_007(self): #super importante que se inicie con test
        self.buscar ="paco" 
        self.texto ="El ing rodrigo esta programando en Python" 
                    
        self.assertIn(self.buscar, self.texto , f"No se encontro {self.buscar}") 
    

        

    def tearDown(self): 
        pass
       
        
        

        
        
if __name__ == '__main__':
    unittest.main()