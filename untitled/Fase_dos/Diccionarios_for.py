#recorrer los valores de un diccionario

cali={"rodrigo":8,"juan":10,"pedro":9}

for cal in cali:
    print(cal) #imprime los nombre

for calk in cali.keys():
    print(calk) #imprime los nombres

for calv in cali.values():
    print(calv)  #imprime los valores


for calItem in cali.items():
    print(calItem)