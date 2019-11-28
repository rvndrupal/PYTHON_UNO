#Escribir dentro de un nuevo archivo.

archivo = open("archivo1.txt", "w") #write

nombre=input("Nombre: ")
edad=input("Edad: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)

print("Los datos estan guardados")

archivo.close()
