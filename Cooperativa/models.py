from django.db import models
from accounts.models import CustomUser

# Create your models here.

class IngenieroAgricultores(models.Model):
    ingeniero = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name= 'agricultores_asignados')
    agricultores = models.ManyToManyField(CustomUser, related_name='ingenieros_asignados')

    def __str__(self):
        return f"Ingeniero: {self.ingeniero.get_full_name()} - {self.agricultores.count()} agricultores"
