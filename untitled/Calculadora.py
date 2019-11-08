
try:
    a = int(input("dame a: "))
    b = int(input("dame c: "))
except ValueError:
    print("No son numeros: ")
else:
    c=a+b
    print(c)