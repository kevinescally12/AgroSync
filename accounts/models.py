# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('agricultor', 'Agricultor'),
        ('ingeniero', 'Ingeniero'),
        ('cooperativa', 'Cooperativa'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='agricultor')
