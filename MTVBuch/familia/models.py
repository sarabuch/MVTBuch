from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.CharField(max_length=10)
    parentezco = models.CharField(max_length=20)