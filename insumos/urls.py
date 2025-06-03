# insumos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_insumos, name='listar_insumos'),
    path('crear/', views.crear_insumo, name='crear_insumo'),
    path('editar/<int:insumo_id>/', views.editar_insumo, name='editar_insumo'),
    path('eliminar/<int:insumo_id>/', views.eliminar_insumo, name='eliminar_insumo'),
]
