#nos permiten identificar los elementos por una clabe o ke


diccionario=dict(nom="rodrigo",ap="Villanueva",tel="576576")

print(diccionario)

print(diccionario["nom"])

dic={} #diccionario vacio

#items
print("se imprimen las duplas")
print(diccionario.items())

#copy

b=diccionario.copy()

print(" se imprime el valor de b")

print(b)

#keys o llaves

print("Se imprime los keys")
print(diccionario.keys())

#values

print("Se imprime los valores de las llaves")
print(diccionario.values())