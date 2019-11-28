#Agregar datos a un archivo


archivo=open("archivo1.txt", 'a')

tra=input("Trabajo: ")
empresa=input("Empresa: ")
idioma=input("Idioma: ")

archivo.write("Nuevos datos: \n")

archivo.write(tra)
archivo.write(tra)
archivo.write(tra)
archivo.write("\n")
archivo.write(idioma)
archivo.write("\n")


archivo.close()
