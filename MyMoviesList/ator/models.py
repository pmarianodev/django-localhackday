from django.db import models

# Create your models here.


class Ator(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.PositiveIntegerField()
    salario = models.FloatField()
    dataNascimento = models.DateField()

    def __str__(self):
        return self.nome