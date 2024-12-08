from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente 

def index(request):
    return HttpResponse("Bienvenido a la sección de clientes")
#vista lista clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Ajusta esto según tu modelo
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})



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
