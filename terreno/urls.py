from django.urls import path, include
from . import views

urlpatterns = [
    path('terreno/crear/<int:id>', views.crear_terreno, name='crear_terreno'),
    path('mis-terrenos/', views.mis_terrenos, name='mis_terrenos'),
    path('agricultores/', views.ver_agricultores, name='ver_agricultores'),
    path('agricultores/<int:id>/terrenos/', views.terreno_por_agricultor, name='terrenos_por_agricultor'),
    path('terreno/<int:id>/', views.detalle_terreno, name='detalle_terreno'),
]
