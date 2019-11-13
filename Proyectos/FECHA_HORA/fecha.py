import datetime

dir(datetime)

print(datetime.datetime.now())

now=datetime.datetime.now()

print(now.day)

print(now.minute)

print(now.second)

print(now.year)

print(now.month)

##Remplazar un valor

now=now.replace(minute=0)

print(now)

#Verifcar el tiempo transcurrido

tiempo=datetime.datetime.now() - now

print(tiempo)
