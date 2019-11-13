import datetime

now=datetime.datetime.now()

print(now)

agregarD=now + datetime.timedelta(days=5)

print(agregarD)

agregarDos=now + datetime.timedelta(days=10, minutes=20, hours=10)

print(agregarDos)

quitarD=now - datetime.timedelta(days=8)

print(quitarD)

##Ver la fecha solamente.

print(now.date())

#ver solo la hora

print(now.time())