#ciclos

manzanas=10

# while manzanas > 0:
#     print("Estoy comiendo una manzana: " + str(manzanas))
#     manzanas -=1


lista=[1,2,3,4,5,6,7,8,9]

# for n in lista:
#     print("se muestra los numero: " + str(n))


# for n in lista:
#     if n > 5:
#         break  #lo rompe
#     print("Se imprime el numero hasta el " + str(n))

for n in lista:
    if n == 5:
        continue  #solo lo quita
    print("Se imprime el numero hasta el " + str(n))