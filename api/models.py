from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=150, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, default='')
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=80)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    propietario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='tiendas',
    )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, default='')
    stock = models.PositiveIntegerField(default=0)
    tienda = models.ForeignKey(
        Tienda,
        on_delete=models.SET_NULL,
        related_name='productos',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nombre
