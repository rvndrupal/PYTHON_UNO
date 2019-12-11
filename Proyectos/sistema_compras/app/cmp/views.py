from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import json

from django.contrib.auth.decorators import login_required, permission_required
from bases.views import SinPrivilegios

from django.contrib.auth.decorators import login_required

from .models import Proveedor
from .forms import ProveedorForm

class ProveedorView(SinPrivilegios, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    permission_required="cmp.view_proveedor"

class ProveedorNew(SinPrivilegios, generic.CreateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    permission_required="cmp.add_proveedor"
   

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)
    
class ProveedorEdit(SinPrivilegios, generic.UpdateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    permission_required="cmp.edit_proveedor"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)
    
    
@login_required(login_url="/login/")
@permission_required("cmp.change_proveedor",login_url="/login/")    
def proveedorInactivar(request,id):
    template_name='cmp/inactivar_prv.html'
    contexto={}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id))

    if request.method=='GET':
        contexto={'obj':prv}

    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj':'OK'}  #manda el obj  y una respuesta de ok  esto por import json
        return HttpResponse('Proveedor Inactivado')

    return render(request,template_name,contexto)