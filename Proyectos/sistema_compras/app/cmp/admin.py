from django.contrib import admin
from .models import *
from import_export import resources  
from import_export.admin import ImportExportModelAdmin

# Register your models here.



# class ProveedorResource(resources.ModelResource):
#     class Meta:
#         model = Proveedor


# class ProveedorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#     search_fields = ['descripcion'] #buscador filtrado por nombre
#     list_display = ('descripcion')
#     resource_class=ProveedorResource
    
    
admin.site.register(Proveedor)