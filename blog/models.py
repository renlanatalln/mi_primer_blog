from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    hora_creacion = models.DateTimeField(blank=True, null=True)

    
class Cartelera(models.Model):
    usuario=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre_de_la_pelicula = models.TextField(blank=True, null=True)
    estreno_categoria_duracion = models.TextField(blank=True, null=True)
    reseña = models.TextField(blank=True, null=True)
    clasificacion = models.TextField(blank=True, null=True)
    imagen = models.URLField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    hora_creacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre_de_la_pelicula or "sin titulo"
        
    