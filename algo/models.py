from django.db import models


class Inscricao(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    celular = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    plano = models.CharField(max_length=50)

    finalizado = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome