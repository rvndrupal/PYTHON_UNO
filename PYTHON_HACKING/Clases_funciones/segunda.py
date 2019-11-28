
def saludo(nom,ed):
    print("Hola {} tienes: {}" .format(nom,ed))




def main():
    nombre=input("Nombre: ")
    edad=int(input("Edad: "))
    
    saludo(nombre,edad)
    
        

if __name__ == '__main__':
    main()