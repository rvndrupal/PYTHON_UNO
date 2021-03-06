from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre =models.CharField(max_length =200, blank = False , null = False) #Recibir campo en blanco y nulo
    apellidos =models.CharField(max_length =200, blank = False , null = False) #Recibir campo en blanco y nulo
    nacionalidad =models.CharField(max_length =100, blank = False , null = False) #Recibir campo en blanco y nulo
    descripcion = models.TextField(blank = False, null= False)
    estado = models.BooleanField('Estado' , default= True)
    fecha_creacion=models.DateField('Fecha de Creación', auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name='Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre  #que cada objeto de aplicación muestre el nombre
    
    
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo=models.CharField('Título', max_length =200, blank = False , null = False) #Recibir campo en blanco y nulo
    fecha_publicacion=models.DateField('Fecha de publicación', blank = False , null = False)
    #autor_id=models.OneToOneField(Autor, on_delete=models.CASCADE) #relacion uno a uno
    #autor_id=models.ForeignKey(Autor, on_delete=models.CASCADE) #relacion uno a mucho
    autor_id=models.ManyToManyField(Autor) #relacion muchos a muchos  no necesita el delete cascada
    fecha_creacion=models.DateField('Fecha de Creación', auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name='Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
        
    def __str__(self):
        return self.titulo  #que cada objeto de aplicación muestre el nombre
    