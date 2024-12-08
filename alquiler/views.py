from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cliente 

# Vista para la página de inicio
# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Renderiza el archivo index.html desde templates


# Vista Clientes

from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

#vista equipos

from django.shortcuts import render
from .models import Equipo

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/lista_equipos.html', {'equipos': equipos})

#vista alquileres

from django.shortcuts import render
from .models import Alquiler

def lista_alquileres(request):
    alquileres = Alquiler.objects.all()
    return render(request, 'alquileres/lista_alquileres.html', {'alquileres': alquileres})

#vista factura

from django.shortcuts import render
from .models import Factura

def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturas/lista_facturas.html', {'facturas': facturas})

#vista mantenimiento

from django.shortcuts import render
from .models import Mantenimiento

def lista_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'mantenimientos/lista_mantenimientos.html', {'mantenimientos': mantenimientos})

#vista reporte de daños
from django.shortcuts import render
from .models import ReporteDanio

def lista_reportes_danos(request):
    reportes = ReporteDanio.objects.all()
    return render(request, 'reportes_danos/lista_reportes_danos.html', {'reportes': reportes})

# Registro usuarios
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        ciudad = request.POST['ciudad']
        celular = request.POST['celular']
        usuario = request.POST['usuario']
        password = request.POST['password']

        # Validación simple (puedes agregar más validaciones si es necesario)
        if User.objects.filter(username=usuario).exists():
            messages.error(request, "El usuario ya existe.")
            return redirect('register')

        # Crear el usuario
        user = User.objects.create_user(username=usuario, password=password)
        user.first_name = nombre
        user.last_name = apellido
        user.save()

        messages.success(request, "Te has registrado exitosamente. Ahora puedes iniciar sesión.")
        return redirect('login')

    return render(request, 'register.html')

# login
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si el usuario es válido, iniciar sesión
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio o al dashboard
        else:
            # Si no se autentica, mostrar un mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')


# vista home 

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')




# Vista para la gestión de clientes
def gestion_clientes(request):
    return render(request, 'gestion_clientes.html', {
        'title': 'Gestión de Clientes',
        'description': 'Administra los datos de tus clientes y su información de contacto.',
    })
#vista agregar clientes
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        Cliente.objects.create(nombre=nombre, correo=correo, telefono=telefono)
        return redirect('gestion_clientes')  # Redirige a la lista de clientes
    return render(request, 'gestion_clientes.html')

#vista editar cliente 
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.correo = request.POST['correo']
        cliente.telefono = request.POST['telefono']
        cliente.save()
        return redirect('gestion_clientes')  # Redirige a la lista de clientes

    return render(request, 'editar_cliente.html', {'cliente': cliente})


#vista eliminar cliente 

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()  # Elimina el cliente de la base de datos
        return redirect('gestion_clientes')  # Redirige a la lista de clientes

    return render(request, 'confirmar_eliminacion.html', {'cliente': cliente})

# Vista para la gestión de equipos
def gestion_equipos(request):
    return render(request, 'gestion_equipos.html', {
        'title': 'Gestión de Equipos',
        'description': 'Gestiona los equipos disponibles para alquiler.',
    })

# Vista para la gestión de alquileres
def gestion_alquileres(request):
    return render(request, 'gestion_alquileres.html', {
        'title': 'Gestión de Alquileres',
        'description': 'Administra los alquileres realizados y su seguimiento.',
    })

# Vista para la gestión de facturas
def gestion_facturas(request):
    return render(request, 'gestion_facturas.html', {
        'title': 'Gestión de Facturas',
        'description': 'Emite y gestiona las facturas generadas por los alquileres.',
    })

# Vista para la gestión de mantenimientos
def gestion_mantenimientos(request):
    return render(request, 'gestion_mantenimientos.html', {
        'title': 'Gestión de Mantenimientos',
        'description': 'Administra los mantenimientos de los equipos.',
    })

# Vista para el reporte de daños
def reporte_danos(request):
    return render(request, 'reporte_danos.html', {
        'title': 'Reporte de Daños',
        'description': 'Registra y gestiona los daños ocurridos en los equipos.',
    })
