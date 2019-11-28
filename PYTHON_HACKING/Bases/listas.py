# lista=list() #lista
lista=[] #lista  los valores deben de estar ceparados por comas

lista=[1,2,3,4,5,"a","b","c"]
print(type(lista))

print(lista)

print(lista[4]) #inicia desde el cero

print(len(lista)) #numero de elementos de la lista

print(lista[len(lista)-1]) #imprime el ultimo elemento de la lista

del lista[2] #borra la dos

print(lista)


print(lista[0:3])

for n in range(90,100):
    lista.append(n) #agrega los valores


print(lista)

####################################3

lista2=["ro","dri","go"]
nom=''.join(lista2) #une lo de la lista

print(nom)