from typing import List
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse


from jmespath import *
from django.db.models import Q

from app.forms import contactoFormulario, alumnoFormulario, pagosFormulario
from app.models import Alumno
from app.models import contacto
from app.models import pagos

# Create your views here.
def gimnasio(request):

      return render(request, "index.html")

def registro(request):
        return render(request, "gym.html")

def registro2(request):
        return render(request, "index2.html")
      
            
      
def ClaseFormulario(request):
      if request.method == "POST":
      
            miformulario = alumnoFormulario(request.POST)
            print(miformulario)
                
            if miformulario.is_valid():
                  informacion=miformulario.cleaned_data
                  clase = Alumno(nombre=informacion['nombres'], apellido=informacion['apellidos'], documento=informacion['documentos'], telefono=informacion['telefonos'])
                  clase.save()
                  return render(request, "index.html")      
      else:
            miformulario=alumnoFormulario()
      return render(request, "gym.html",{"miformulario:":miformulario})

def ContactoFormulario(request):
      if request.method == "POST":
      
            micontacto = contactoFormulario(request.POST)
            print(micontacto)
                
            if micontacto.is_valid():
                  informacioncontacto=micontacto.cleaned_data
                  clasecontacto = contacto(name=informacioncontacto['names'], email=informacioncontacto['emails'], sujeto=informacioncontacto['sujetos'], mensaje=informacioncontacto['mensajes'])
                  clasecontacto.save()
                  return render(request, "index.html")      
      else:
            micontacto=contactoFormulario()
      return render(request, "index.html",{"micontacto:":micontacto})           


def busqueda(request):
      if request.method =="POST":
            search = request.POST["search"]
            
            if search !="":
                  busqueda=Alumno.objects.filter(Q(nombre__icontains=search)|Q(apellido__icontains=search)|Q(documento__icontains=search)|Q(telefono__icontains=search)).values()
                  return render (request, "index2.html",{"busquedas":busqueda, "search":True, "busqueda":search })
      busqueda=Alumno.objects.all()
      return render(request, "index2.html",{"busquedas":busqueda})


def Pagosformularios(request):
      if request.method == "POST":
      
            mispagos = pagosFormulario(request.POST)
            print(mispagos)
                
            if mispagos.is_valid():
                  informacionpagos=mispagos.cleaned_data
                  clasepagos = pagos(fechaPago=informacionpagos['fechapagos'], clasesDisponibles=informacionpagos['clasesdisponibless'], numeroDeregistro=informacionpagos['numeroderegistros'], montoAbonado=informacionpagos['montoabonados'])
                  clasepagos.save()
                  return render(request, "index.html")      
      else:
            mispagos=pagosFormulario()
      return render(request, "pagos.html",{"mispagos:":mispagos})   