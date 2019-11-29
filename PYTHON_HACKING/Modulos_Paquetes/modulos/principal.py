from calculador import suma,resta,mul,div

def main():
    while True:
        print("Bienvenida al sistemita: \n")
        print("1.- suma \n")
        print("2.- resta \n")
        print("3.- Multi \n")
        print("4.- Divide \n")
        opcion=int(input("Selecciona una Opcion: "))
        
        if opcion == 1:
            val1=int(input("Valor uno: "))
            val2=int(input("Valor dos: "))
            suma(val1,val2)
        elif opcion == 2:
            val1=int(input("Valor uno: "))
            val2=int(input("Valor dos: "))
            resta(val1,val2)
        elif opcion == 3:
            val1=int(input("Valor uno: "))
            val2=int(input("Valor dos: "))
            mul(val1,val2)
        elif opcion == 4:
            val1=int(input("Valor uno: "))
            val2=int(input("Valor dos: "))
            div(val1,val2)
        elif opcion == 5:
            exit()
        else:
            print("opcion invalida")
            
        


if __name__ == '__main__':
    main()