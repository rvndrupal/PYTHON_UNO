import matplotlib.pyplot as plt 
import numpy as np

np.random.seed(123)

x=np.arange(0,100,1)  #de cero hasta 100 de 1 en 1

y=np.random.randint(0,10,100) + x  #genera valores del 0 al 10 , 100 valores + el valor de x


plt.plot(x,y)

plt.title("Grafica de Lineas")

plt.xlabel("Tiempo")
plt.ylabel("Eventos")

print(plt.style.available)

plt.show()
