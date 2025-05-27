
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('agricultor', 'Agricultor'),
        ('ingeniero', 'Ingeniero'),

        ('coopertativa', 'Cooperativa'),
    ) 

    rol = models.CharField(max_length=20, choices=ROLES, default='agricultor')
