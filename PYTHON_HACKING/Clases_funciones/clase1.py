class Carro(object):
    def __init__(self,m):
        self.color="rojo"
        self.puertas=4
        self.tipo="Deportivo"
        self.m=m
    
    def movilidad(self):
        if self.m == True:
            print("Acelerar") 
        else:
            print("Frenar")       
        
def main():
    while True:
        print("1.- Acelerar: ")
        print("2.- Frenar: ")
        opc=int(input("Opcion: "))
        
        if opc == 1:
            c= Carro(True)
            c.movilidad()
        elif opc == 2:
            c = Carro(False)
            c.movilidad()
        else:
            exit()
        
        
    
    




if __name__ == '__main__':
    main()