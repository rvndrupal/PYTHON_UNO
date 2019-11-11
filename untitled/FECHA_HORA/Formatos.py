import datetime

now=datetime.datetime.now()

##pagina de los formatos
#  http://strftime.org/

print(now.strftime("%B %d, %Y - %H:%M"))

fecha_cadena="06/02/2019"

print(fecha_cadena)

fecha_convertir=datetime.datetime.strptime(fecha_cadena,"%d/%m/%Y")

print(fecha_convertir)