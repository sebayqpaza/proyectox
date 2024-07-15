from django.db import models
from django.contrib.auth.models import User
from productos.models import Zapatilla

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    zapatillas = models.ManyToManyField(Zapatilla)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"
