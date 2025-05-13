from django.db import models

class Terreno(models.Model):
    departamento = models.CharField(),
    provincia = models.CharField(),
    distrito = models.CharField(),

    def __str__(self):
        return self.departamento
    

class Producto(models.Model):
    nombre = models.CharField(),
    tipo = models.CharField(),
    peso = models.FloatField(),
    humedad = models.CharField(),
    contenido_grasa = models.CharField()
    fecha_cosecha = models.CharField()
    estado_calidad = models.CharField()

