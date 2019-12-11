from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo): #con solo hacer esto ya heredo de la clase modelo
    descripcion=models.CharField(
        max_length=100,
        help_text='Descripción de la Ctaegoría',
        unique=True
    )
    
    def __str__(self): #cuando se hace referencia a este campo tome el valor de descripcion
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion=self.descripcion.upper() #pongo en mayuscula la descripción.add()
        super(Categoria, self).save() #Para guardar
        
    class Meta:
        verbose_name_plural="Categorias"
    
    

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural= "Sub Categorias"
        unique_together = ('categoria','descripcion') #no se repita la categoria
        
        
        
class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"
        


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"