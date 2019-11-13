numeros=[1,2,3,4,5,6,7,8,9,10]

del numeros[0:4]

print(numeros)

numeros[6:]=[11,12,13]

print(numeros)

numeros[0:1]=[55] #el pirmero es 55


print(numeros)

numeros[9:10]=[100,100] #doce y trece pasan a 100

print(numeros)

numeros[9:10]=[14,15]

print(numeros)

del numeros[11]

print(numeros)