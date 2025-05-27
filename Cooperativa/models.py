from django.db import models
from accounts.models import CustomUser

class IngenieroAgricultores(models.Model):
    # Ingeniero: es un usuario con rol = 'ingeniero'
    ingeniero = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='agricultores_asignados',
        limit_choices_to={'rol': 'ingeniero'}  # Limita el queryset en el admin/formulario
    )

    # Agricultores: usuarios con rol = 'agricultor'
    agricultores = models.ManyToManyField(
        CustomUser,
        related_name='ingenieros_asignados',
        limit_choices_to={'rol': 'agricultor'}  # Lo mismo aquí
    )

    def __str__(self):
        return f"Ingeniero: {self.ingeniero.get_full_name()} - {self.agricultores.count()} agricultores"
