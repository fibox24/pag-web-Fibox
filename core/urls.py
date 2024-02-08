
from django.urls import path, include
from .views import *

urlpatterns = [
    path('Inicio',Inicio, name='Inicio'),
    path('Planes',Planes, name='Planes'),
    path('Quienes_somos',Quienes_somos, name='Quienes_somos'),
    path('Contacto', include('contacto.urls'), name='Contacto'),
]


