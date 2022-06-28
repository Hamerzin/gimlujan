from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
from django.template.defaultfilters import slugify



# Create your models here.
class Alumno(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.IntegerField()
    telefono = models.IntegerField()


class pagos(models.Model):
        fechaPago=models.CharField(max_length=40)
        clasesDisponibles=models.IntegerField()
        numeroDeregistro=models.IntegerField()
        montoAbonado=models.IntegerField(default=2500)


class contacto(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=250)
    sujeto= models.CharField(max_length=50)
    mensaje = models.CharField(max_length=50) 


   



