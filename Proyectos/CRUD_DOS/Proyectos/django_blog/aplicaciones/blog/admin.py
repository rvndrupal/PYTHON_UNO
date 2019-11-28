from django.contrib import admin
from .models import *
from import_export import resources  
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
        
class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre'] #buscador filtrado por nombre
    list_display = ('nombre','fecha_creacion','estado')
    resource_class=CategoriaResource
    
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    seacrh_fields = ['nombres','apellidos','correo']
    list_display = ('nombres','apellidos','correo','fecha_creacion','estado')
    resource_class=AutorResource
    


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post)
