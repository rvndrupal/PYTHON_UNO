from django.urls import include, path
from .views import *

# urlpatterns = [
#     path('home/',home, name='index'),
#     path('crear_mascota/', crearMascota, name='crear_mascota'),
#     path('listar_mascota/', listarMascota, name='listar_mascota'),
#     path('editar_mascota/<int:id>', editarMascota, name='editar_mascota'),
#     path('eliminar_mascota/<int:id>', eliminarMascota, name='eliminar_mascota'),
   
# ]
#Metodo uno

#Metodo dos
urlpatterns = [
    path('home/',home, name='index'),
    path('crear_mascota/', CreateMascota.as_view(), name='crear_mascota'),
    path('listar_mascota/', ListMascota.as_view(), name='listar_mascota'),
    path('editar_mascota/<int:pk>', UpdateMascota.as_view(), name='editar_mascota'),
    path('eliminar_mascota/<int:pk>', DeleteMascota.as_view(), name='eliminar_mascota'),
   
]