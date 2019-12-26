from django.contrib import admin
from .models import Marca,Automovil
# Register your models here.


class AutomovilAdmin(admin.ModelAdmin):
    list_display=('patente','marca','anio','modelo','imagen')
    search_fields=('patente','modelo')
    list_filter=('marca','modelo')

admin.site.register(Marca)
admin.site.register(Automovil, AutomovilAdmin)
