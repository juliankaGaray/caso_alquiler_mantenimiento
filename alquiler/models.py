from django.db import models

# Modelo cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

# Modelo equipo
class Equipo(models.Model):
    TIPO_CHOICES = [
        ('camara', 'Cámara'),
        ('luces', 'Luces'),
        ('grip', 'Grip'),
        ('soporte', 'Soporte'),
    ]
    
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('en_alquiler', 'En alquiler'),
        ('en_mantenimiento', 'En mantenimiento'),
        ('dañado', 'Dañado'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='disponible')
    descripcion = models.TextField(blank=True, null=True)
    costo_diario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


# Modelo Alquiler
class Alquiler(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return f'Alquiler {self.id} - {self.cliente.nombre}'


# Modelo factura
class Factura(models.Model):
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f'Factura {self.id} - {self.alquiler.cliente.nombre}'


# Modelo Mantenimiento
class Mantenimiento(models.Model):
    ESTADO_CHOICES = [
        ('programado', 'Programado'),
        ('en_proceso', 'En proceso'),
        ('completado', 'Completado'),
    ]
    
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='programado')

    def __str__(self):
        return f'Mantenimiento {self.id} - {self.equipo.nombre}'


# Modelo reporte de daños
class ReporteDanio(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('completado', 'Completado'),
    ]
    
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE)
    fecha_reporte = models.DateField()
    descripcion = models.TextField()
    estado_reparacion = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f'Reporte de daño {self.id} - Alquiler {self.alquiler.id}'
