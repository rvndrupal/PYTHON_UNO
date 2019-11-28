#Leer el archivo

leer=open("wordlist.lst", 'r')

#print(leer.readlines())

# for l in leer.readlines():
#     print(l)

# for l in leer.read().split('\n'):   #split quita los \n
#     print(l)

lista=leer.read().split('\n')

print(len(lista))

for n in lista:
    print(n)