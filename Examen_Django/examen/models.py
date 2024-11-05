from django.db import models
from django.utils  import timezone

#Modelo Jueguete
class Juguete(models.Model):
    nombre_juguete = models.CharField(max_length=100)
    edad_juego = models.IntegerField()
    cantidad_juguete = models.IntegerField()
    
    def __str__(self):
        return self.nombre_juguete

# Modelo Juguetería
class Juguetería(models.Model):
    nombre_tienda = models.CharField(max_length=100)
    juguetes_vendidos = models.IntegerField()
    juguetes_devueltos = models.IntegerField()

    juguete = models.ManyToManyField(Juguete, related_name='juguete_tienda') # Modelo ManyToMany

    def __str__(self):
        return self.nombre_tienda


# Modelo Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.IntegerField()

    juguetería = models.ForeignKey(Juguetería, on_delete=models.CASCADE , related_name='jugueteria_cliente') # Modelo ManyToOne
    juguete = models.ManyToManyField(Juguete , related_name='juguete_cliente') # Modelo ManyToMany

    def __str__(self):
        return self.nombre

# Modelo Votacion
class Votacion(models.Model):
    puntuacion = models.IntegerField()
    comentario = models.CharField(max_length=100)
    fecha_voto = models.DateTimeField(default=timezone.now)

    juguete = models.ForeignKey(Juguete, on_delete=models.CASCADE , related_name='voto_jugete') # Modelo ManyToOne
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE , related_name='cliente_voto')  # Modelo ManyToOne


# Modelo Banco
class Banco(models.Model):
    Sucursal = [
        ('C', 'CAIXA'),
        ('B', 'BBVA'),
        ('U', 'UNICAJA'),
        ('I', 'ING'),
    ]

    banco = models.CharField(max_length=1,choices=Sucursal)
    cliente = models.OneToOneField(Cliente , on_delete=models.CASCADE , related_name = 'banco_cliente')
