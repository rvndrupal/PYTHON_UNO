import unittest


class test_001(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 50
        self.Variable_B = 500

    def test_001(self):

        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self): #super importante que se inicie con test
        self.assertTrue(self.RESULTADO >= 100, f"El valor no es 100, es {self.RESULTADO}")
        
        
class test_002(unittest.TestCase):
    
    def setUp(self):
        self.Variable_A = 'Mervin '
        self.Variable_B = 'Alberto'

    def test_001(self):

        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self):
        self.assertEqual("Mervin Alber", self.RESULTADO, f"El resultado es diferente al esperado: {self.RESULTADO}")
        
        
if __name__ == '__main__':
    unittest.main()