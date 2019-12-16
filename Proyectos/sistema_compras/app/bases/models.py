from django.db import models
from django.contrib.auth.models import User

#modelo del cual todos van a Heredar los mismos campos

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc=models.DateTimeField(auto_now_add=True) #fecha cuando el objeto se cree fc= fecha de creación
    fm=models.DateTimeField(auto_now=True) #fecha modificacion se modifica al update
    uc=models.ForeignKey(User, on_delete=models.CASCADE) #relacion de uno a muchos usuario creado
    um=models.IntegerField(blank=True, null=True) #valores nulos o vacios hasta que se modifique el usuario
    
    class Meta:
        abstract=True  #muy importante no hace la migración ya que solo lo vamos a tomar para heredar.


# class ClaseModelo2(models.Model):
#     estado = models.BooleanField(default=True)
#     fc = models.DateTimeField(auto_now_add=True)
#     fm = models.DateTimeField(auto_now=True)
#     # uc = models.ForeignKey(User, on_delete=models.CASCADE)
#     # um = models.IntegerField(blank=True,null=True)
#     uc = UserForeignKey(auto_user_add=True,related_name='+')
#     um = UserForeignKey(auto_user=True,related_name='+')

#     class Meta:
#         abstract=True