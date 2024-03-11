from django.db import models

# Create your models here.


class Armaduras(models.Model):

    nombre_armadura = models.CharField(max_length=30)
    tipo_armadura = models.CharField(max_length=30)
    lv_armadura = models.IntegerField()

class Personajes (models.Model):
    nombre = models.CharField(max_length = 60)
    raza = models.CharField(max_length = 60)
    averno = models.CharField(max_length = 60)

    def __str__(self):
        return f"{self.nombre}---{self.raza}---{self.averno}"

class Build(models.Model):
    nombre = models.CharField(max_length = 60)
    tipo_daño = models.CharField(max_length = 60)
    Total_daño = models.IntegerField()
