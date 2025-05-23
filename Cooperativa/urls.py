from django.urls import path
from . import views

urlpatterns = [
    path('asignar/', views.asignar_agricultores, name='asignar_agricultores'),
]