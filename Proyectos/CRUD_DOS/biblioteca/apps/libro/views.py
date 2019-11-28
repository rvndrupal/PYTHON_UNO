from django.shortcuts import render,redirect
from .forms import AutorForm
from .models import Autor
from django.core.exceptions import ObjectDoesNotExist

def Home(request):
    return render(request,'index.html')


# def crearAutor(request):
#     if request.method == 'POST':
#        autor_form = AutorForm(request.POST) #del form
#       # print(autor_form) comprobar el envio
#        if autor_form.is_valid():
#            autor_form.save()
#            return redirect('index')
#     else:
#         autor_form=AutorForm()
#     return render(request, 'libro/crear_autor.html', {'autor_form':autor_form})

#Segunda Manera.
def crearAutor(request):
    if request.method == 'POST':
       autor_form = AutorForm(request.POST) #del form
      # print(autor_form) comprobar el envio
       if autor_form.is_valid():
           autor_form.save()
           return redirect('index')
    else:
        autor_form=AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form':autor_form})


        
#Listar normal
# def listarAutor(request):
#     autores= Autor.objects.all()
#     return render(request,'libro/listar_autor.html', {'autores':autores})

#Listar lógico
def listarAutor(request):
    autores= Autor.objects.filter(estado = True)
    return render(request,'libro/listar_autor.html', {'autores':autores})




def editarAutor(request,id):
    autor_form = None
    error = None
    try:
        autor= Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form=AutorForm(instance = autor)
        else:
            autor_form=AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor')        
    except ObjectDoesNotExist as e:
        error = e    
    return render(request, 'Libro/crear_autor.html',{'autor_form':autor_form, 'error':error})
    

#Eliminar simple
# def eliminarAutor(request, id):
#     autor= Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('libro:listar_autor')

#Eliminar Pregunta
# def eliminarAutor(request, id):
#     autor= Autor.objects.get(id=id)
#     if request.method == 'POST':
#         autor.delete()
#         return redirect('libro:listar_autor')
#     return render(request,'libro/eliminar_autor.html', {'autor':autor})

#Eliminar Logica
def eliminarAutor(request, id):
    autor= Autor.objects.get(id=id)
    if request.method == 'POST':
        autor.estado=False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request,'libro/eliminar_autor.html', {'autor':autor})
    
    