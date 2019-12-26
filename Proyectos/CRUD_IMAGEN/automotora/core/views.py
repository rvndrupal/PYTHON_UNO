from django.shortcuts import render,redirect
from .models import Marca,Automovil
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):
    marcas=Marca.objects.all()
    variables={'marcas':marcas}
    
    if request.POST:
        auto=Automovil()
        auto.patente=request.POST.get('txtPatente')
        auto.modelo=request.POST.get('txtModelo')
        auto.anio=request.POST.get('txtAnio')
        marca=Marca()
        marca.id=request.POST.get('cboMarca')
        auto.marca=marca  #del select
        auto.imagen=request.FILES.get('txtImagen') #Ojo con el Files
        
        try:
            auto.save()
            variables['mensaje']='Guardado correctamente'
        except:
            variables['mensaje']='No se Guardo'
            
        
    
    
    return render(request, 'core/formulario.html',variables)

####Crud automovil

def listar_automovil(request):
    autos=Automovil.objects.all()
    return render(request, 'core/listar_automoviles.html',{'autos':autos})

def eliminar_automovil(request, id):
    auto=Automovil.objects.get(id=id)
    
    try:
        auto.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request,mensaje)
        
    return redirect('listar_automovil')


def modificar_automovil(request, id):
    auto=Automovil.objects.get(id=id)
    marcas=Marca.objects.all()
    
    variables={
        'auto':auto,
        'marcas':marcas
    }
    
    if request.POST:
        auto=Automovil()
        auto.id=request.POST.get('txtId')
        auto.patente=request.POST.get('txtPatente')
        auto.modelo=request.POST.get('txtModelo')
        auto.anio=request.POST.get('txtAnio')
        marca=Marca()
        marca.id=request.POST.get('cboMarca')
        auto.marca=marca  #del select
        auto.imagen=request.FILES.get('txtImagen') #Ojo con el Files
        
        try:
            auto.save()
            messages.success(request,'Modificado Correctamente')
        except:
            messages.error(request,'Error al Modificar')
        return redirect('listar_automovil')

    
    return render(request,'core/modificar_automovil.html', variables)
    


