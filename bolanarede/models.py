from django.db import models

from uploader.models import Image

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

...

class Time(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"


class Camisa(models.Model):
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    time = models.ForeignKey(
        Time, on_delete=models.PROTECT, related_name="camisa"
    )
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )


    def __str__(self):
        return f"{self.descricao} ({self.quantidade})"
