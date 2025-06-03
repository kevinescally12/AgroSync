# insumos/models.py
from django.db import models
from terreno.models import Terreno
from accounts.models import CustomUser

class Insumo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    terreno = models.ForeignKey(Terreno, on_delete=models.CASCADE, related_name='insumos', blank=True, null=True)
    agricultor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mis_insumos', null=True, blank=True)

    def __str__(self):
        return self.nombre
