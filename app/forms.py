from email.policy import default
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class alumnoFormulario(forms.Form):

    #Especificar los campos
    nombres = forms.CharField()
    apellidos = forms.CharField()
    documentos= forms.IntegerField()
    telefonos= forms.IntegerField()

class pagosFormulario(forms.Form):
    fechapagos=forms.CharField(max_length=50)
    clasesdisponibless=forms.IntegerField()
    numeroderegistros=forms.IntegerField()
    montoabonados=forms.IntegerField()

class contactoFormulario(forms.Form):
    names = forms.CharField(max_length=50)
    emails = forms.EmailField()
    sujetos= forms.CharField(max_length=50)
    mensajes= forms.CharField(max_length=50)



