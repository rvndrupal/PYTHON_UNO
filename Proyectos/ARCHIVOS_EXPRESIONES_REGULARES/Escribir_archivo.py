def agregar(dat):
    archivo = open("archivo.txt", "a")
    archivo.write(dat)
    archivo.close()


dato=input("Dato a agregar en el archivo: ")
agregar(dato)