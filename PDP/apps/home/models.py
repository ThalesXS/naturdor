# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Collaborators(models.Model):
    Nome = models.CharField(max_length=100, default="N/A")
    Apelido = models.CharField(max_length=100, default="N/A")
    Departamento = models.CharField(max_length=100, default="N/A")
    NumColab = models.IntegerField(default=0)
    NumAvali = models.IntegerField(default=0)
    Func = models.CharField(max_length=100, default="N/A")
    Data = models.DateField(default=timezone.now)
    Grupo = models.CharField(max_length=100, default="N/A")
    DirUni = models.IntegerField(default=0)
    Pin = models.CharField(max_length=4,default="0000")
    Ano = models.DateField(default=timezone.now)
    FaltaJust = models.FloatField(default=0)
    FaltaInjust = models.FloatField(default=0)

    def __str__(self):
        return "[" + str(self.NumColab) + "]: " + self.Nome + " " + self.Apelido
    
class Avaliação(models.Model):
    processCode = models.CharField(max_length=10, default="TI-03-2024")
    numAvaliador = models.IntegerField(default=0)
    grupoAvaliação = []
    avalTerminadas = []
    
    