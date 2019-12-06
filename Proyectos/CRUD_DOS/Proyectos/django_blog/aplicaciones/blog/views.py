from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q


def home(request):
    queryB=request.GET.get("buscar")
    posts=Post.objects.filter(estado= True)
    
    if queryB:
        posts=Post.objects.filter(
            Q(titulo__icontains = queryB) |
            Q(descripcion__icontains = queryB)
        ).distinct()
    
    
    #print(posts)
    return render(request,'index.html',{'posts':posts})

def detallePost(request,slug):
    # post=Post.objects.get(
    #     slug=slug
    # )
    post=get_object_or_404(Post,slug = slug)  #valida si la ruta existe en las url sino regresa un 404
    return render(request,'post.html',{'dp':post})
    

def generales(request):
    #posts=Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__exact = 'Generales'))
    #Valida el exact que el valor sea exactamente identico
    posts=Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact = 'Generales')) #no importan las mayusculas
    return render(request,'generales.html',{'posts':posts})

def programacion(request):
    posts=Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact = 'Programación'))
    return render(request,'programacion.html',{'posts':posts})

def tutoriales(request):
    posts=Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    return render(request,'tutoriales.html',{'posts':posts})


def tecnologia(request):
    posts=Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact = 'Tecnologia'))
    return render(request,'tecnologia.html',{'posts':posts})


def videojuegos(request):
    posts=Post.objects.filter(estado=True, categoria= Categoria.objects.get(nombre__iexact = 'Videojuegos'))
    return render(request,'videojuegos.html',{'posts':posts})

