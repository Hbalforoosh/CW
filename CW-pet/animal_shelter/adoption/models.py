
from django.db import models

# Create your models here


class Adopter(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"Adopter by name : {self.name} | Phone: {self.phone}"

    class Meta:
        verbose_name = 'adopter'
        verbose_name_plural = 'adopters'
        ordering = ('name')


class Pet(models.Model):
    name = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    adopter_name = models.ForeignKey(Adopter, on_delete=models.PROTECT)
    adopted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'pet'
        verbose_name_plural = 'pets'
        ordering = ('name')
