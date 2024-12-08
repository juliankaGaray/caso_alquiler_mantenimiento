# clientes/models.py
from django.db import models

# clientes/models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    class Meta:
        db_table = 'clientes_cliente'  #

