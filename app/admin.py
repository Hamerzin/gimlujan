from sqlite3 import Cursor
from django.contrib import admin

from app.views import *
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Alumno)
admin.site.register(pagos)

admin.site.register(contacto)


