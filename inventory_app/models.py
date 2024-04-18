from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
