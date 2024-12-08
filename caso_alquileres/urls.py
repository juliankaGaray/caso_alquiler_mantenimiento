from django.urls import include
from django.urls import path
from alquiler import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'), 
    path('home/', views.home, name='home'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('alquileres/', views.lista_alquileres, name='lista_alquileres'),
    path('facturas/', views.lista_facturas, name='lista_facturas'),
    path('mantenimientos/', views.lista_mantenimientos, name='lista_mantenimientos'),
    path('reportes-danos/', views.lista_reportes_danos, name='lista_reportes_danos'),
    path('register/', views.register, name='register'),
    
    path('gestion/equipos/', views.gestion_equipos, name='gestion_equipos'),
    path('gestion/alquileres/', views.gestion_alquileres, name='gestion_alquileres'),
    path('gestion/facturas/', views.gestion_facturas, name='gestion_facturas'),
    path('gestion/mantenimientos/', views.gestion_mantenimientos, name='gestion_mantenimientos'),
    path('gestion/danos/', views.reporte_danos, name='reporte_danos'),
    path('admin/', admin.site.urls),
    path('gestion/', include('clientes.urls')),  # Esto incluye las rutas de la aplicación 'clientes'
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
