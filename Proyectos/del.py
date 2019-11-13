#Del nos ayuda a borrar las variables enteras.

a="abcd"
lista=list(a)

numero=10

print(numero)

del numero

#print(numero) #manda el error dice que ya no esta definido

print(lista)

del lista[0]

print(lista)