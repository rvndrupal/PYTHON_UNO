from django.shortcuts import render, redirect
from .models import *
from .forms import MascotaForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request,'index.html')

#Metodo uno

# def crearMascota(request):
#     if request.method == 'POST':
#         form=MascotaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form=MascotaForm()
#     return render(request,'aplicacion/crear_mascota.html', {'form':form})
        

def listarMascota(request):
    mascota=Mascota.objects.all()
    context = {'mascota':mascota}
    return render(request,'aplicacion/listar_mascota.html', context)

# def editarMascota(request, id):
#     mascota=Mascota.objects.get(id = id)
#     if request.method == 'GET':
#         form =MascotaForm(instance = mascota)
#     else:
#         form=MascotaForm(request.POST, instance=mascota)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_mascota')
#     return render(request,'aplicacion/crear_mascota.html', {'form':form})
        
# def eliminarMascota(request, id):
#     mascota=Mascota.objects.get(id = id)
#     if request.method == 'POST':
#         mascota.delete()
#         return redirect('listar_mascota')
           
#     return render(request,'aplicacion/eliminar_mascota.html',{'mascota':mascota})


#Metodo Dos

class CreateMascota(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'aplicacion/crear_mascota.html'
    success_url = reverse_lazy('listar_mascota')
    
class ListMascota(ListView):
    model = Mascota
    template_name = 'aplicacion/listar_mascota.html'
    
class UpdateMascota(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'aplicacion/crear_mascota.html'
    success_url = reverse_lazy('listar_mascota')

class DeleteMascota(DeleteView):
    model = Mascota    
    template_name = 'aplicacion/eliminar_mascota.html'
    success_url = reverse_lazy('listar_mascota')