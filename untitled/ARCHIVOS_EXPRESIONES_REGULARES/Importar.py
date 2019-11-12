import re
# Importa expresiones regulares.
# Pagina para las expresiones regulares https://regexr.com/
archivo=open("sample.txt", encoding="utf-8")

informacion= archivo.read()

archivo.close()

print(informacion)

buscaruno=re.search("demo@gmail.com ",informacion)

##Buscar  esto +1-(800)-(555)-(2468)
# se pone  "\+\d-\(\d\d\d)-\(\d\d\d)-\(\d\d\d\d)"
# el \ sirve para escapar ejemplo primero + luego \d un numero luego - \(\d\d\d)  el importante es el de escape  \d es para un numero
buscardos=re.search("\+\d-\(\d\d\d\)-\(\d\d\d\)-\(\d\d\d\d\)",informacion)

#cuantificadores

buscadortres=re.search("\+\d-\(\d{3}\)-\(\d{3}\)-\(\d{4}\)",informacion) #busca una coencidencia
#le dice cuantas \d tiene que tener por campo

buscadorcuatro=re.findall("\+\d-\(\d{3}\)-\(\d{3}\)-\(\d{4}\)",informacion)  #busca todos

print("----------Datos encontrados--------------")
print()

# print(buscaruno)
#
# print(buscardos)

#print(buscadortres)

print(buscadorcuatro)


