# clientes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),  # Para listar los clientes
    path('gestion/', views.gestion_clientes, name='gestion_clientes'),  # Ruta para la gestión
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
]
