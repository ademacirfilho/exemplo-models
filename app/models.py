from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cidade = models.CharField(max_length=100)
    idade = models.IntegerField()