from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    puede_tener_promociones = models.BooleanField()
    

    def __str__(self):
        return self.nombre


class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    descuento = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    esta_activa = models.BooleanField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="producto_promocion")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_promocion")
    

    def __str__(self):
        return f"{self.usuario.nombre} - {self.producto.nombre}"
    
