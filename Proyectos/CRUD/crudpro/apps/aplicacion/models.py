from django.db import models

class Persona(models.Model):
    id=models.AutoField(primary_key = True)
    nombre=models.CharField(max_length = 100)
    apellidos=models.CharField(max_length = 100)
    edad=models.IntegerField()
    telefono=models.CharField(max_length = 12)
    
    def __str__(self):
        return self.nombre  #Retorna del objeto el nombre
    
class Mascota(models.Model):
    id=models.AutoField(primary_key = True)
    nombre=models.CharField(max_length = 100)
    edad=models.IntegerField()
    persona=models.ForeignKey(Persona, on_delete=models.CASCADE) #Relacion uno a muchos
    
    def __str__(self):
        return self.nombre  #Retorna del objeto el nombre
    
    
    
