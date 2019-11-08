Lista= [1,2,3,4,5]

print(Lista)

Lista+=[6,7,8]

print(Lista)

Lista.append(9) #solo Permite Agregar uno
Lista.append(10)

print(Lista)

Lista.append(["Nuevo","Dato"]) #Agrega un nuevo array

print(Lista)

Lista.extend([11,12,13]) #Con este si ya puedes agregar más campos

print(Lista)

Lista.remove(9)

print(Lista)