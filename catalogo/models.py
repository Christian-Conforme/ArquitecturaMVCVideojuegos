# models.py
from django.db import models
from django.contrib.auth.models import User

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=50)
    género = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripción = models.TextField()
    imagen = models.URLField(max_length=200)  
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario} en {self.videojuego}'