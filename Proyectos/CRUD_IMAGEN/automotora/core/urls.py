from django.urls import path
from .views import home, galeria, formulario, listar_automovil, eliminar_automovil,modificar_automovil

urlpatterns = [
    path("", home, name="home"),
    path("galeria/", galeria, name="galeria"),
    path("formulario/", formulario, name="formulario"),
    path("listar_autos/", listar_automovil, name="listar_automovil"),
    path("eliminar-auto/<id>/", eliminar_automovil, name="eliminar_automovil"),
    path("modificar-auto/<id>/", modificar_automovil, name="modificar_automovil"),
]
