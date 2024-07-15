from django.db import models

class Zapatilla(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='zapatillas/')
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
