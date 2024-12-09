from django.db import models

# Create your models here.
class publicacion(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.TextField()
    fecha_post=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    