from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from accounts.models import CustomUser

class Terreno(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    agricultor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'rol' : 'agricultor'})