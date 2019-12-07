from django.db import models
from ator.models import Ator


# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(max_length=45)
    diretor = models.CharField(max_length=45)
    minutos = models.IntegerField()
    dataLancamento = models.DateField()
    atores = models.ManyToManyField(Ator)

    def __str__(self):
        return self.titulo
