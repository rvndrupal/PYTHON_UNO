# classmethod
#staticmethod
# property


class Prueba(object):
    def __init__(self,radio):
        self.radio=radio
        pass
    
    @classmethod #nos ayuda a usar una funcion sin que antes las clase sea atribuida a un objeto
    def saludo(cls, nombre):
        print("hola {}".format(nombre))
        
    @staticmethod
    def saludo_static():
        print("Bienvenido")
        
    @property
    def area_circulo(self):
        return 3.1416*(self.radio**2)
    
    
        

def main():
    # nom=input("Nombre: ")
    # Prueba.saludo(nom) #sin crear el objeto
    
    # c= Prueba()
    # c.saludo_static()
    
    c=  Prueba(5)
    area= c.area_circulo
    print(area)    
    
    
    
    
if __name__ == '__main__':
    main()