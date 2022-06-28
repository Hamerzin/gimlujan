from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView
from django.views import View


from app import views




urlpatterns = [   
    path('', views.gimnasio, name="Inicio"), #esta era nuestra primer view
    path('gym', views.registro, name="Gym"),
    path('alumno', views.ClaseFormulario, name="alumno"),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('registro', views.registro2, name="Registro"),
    path('contacto/',views.ContactoFormulario, name="Contacto"),
    path('pagos', views.Pagosformularios, name="Pagos")
    ]
    


