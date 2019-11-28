from django.db import models
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    id =models.AutoField(primary_key = True)
    nombre=models.CharField('Nombre de la Categoria', max_length=100, null = False, blank = False)
    estado=models.BooleanField('Categoria Activa/Categoria no Activada', default = True)
    fecha_creacion=models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True) #solo cuando se hace la primera vez
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id =models.AutoField(primary_key = True)
    nombres=models.CharField('Nombres Autor', max_length=100, null = False, blank = False)
    apellidos=models.CharField('Apellidos', max_length=100, null = False, blank = False)
    facebook=models.URLField('Facebbok', null=True, blank=True) #pueden dejarlo en blanco
    twitter=models.URLField('Twitter', null=True, blank=True) #pueden dejarlo en blanco
    instagram=models.URLField('Instagram', null=True, blank=True) #pueden dejarlo en blanco
    web=models.URLField('Web', null=True, blank=True) #pueden dejarlo en blanco
    correo=models.EmailField('Email', null=True , blank=True)
    estado=models.BooleanField('Autor Activo/Autor no Activo', default = True)
    fecha_creacion=models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True) #solo cuando se hace la primera vez
    
    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'
        
    def __str__(self):
        return "{0},{1}".format(self.nombres,self.apellidos)
    
class Post(models.Model):
    id =models.AutoField(primary_key = True)
    titulo=models.CharField('Título', max_length=100, null = False, blank = False)
    slug=models.CharField('Slug', max_length=100, null = False, blank = False)
    descripcion=models.CharField('Descripción', max_length=110, null = False, blank = False)
    contenido=RichTextField()  #crea el ckeditor
    imagen=models.URLField('Imagen',max_length=255, null = False, blank=False)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado=models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion=models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
        
    def __str__(self):
        return self.titulo
    
    
    
    
    
