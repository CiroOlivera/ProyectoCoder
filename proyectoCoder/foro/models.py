from django.db import models
from socios.models import Socio
# Create your models here.
class publicacion(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.TextField()
    fecha_post=models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name='publicaciones')
    
    def __str__(self):
        return self.titulo
    