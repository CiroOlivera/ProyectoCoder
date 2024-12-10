
from django.db import models
from socios.models import Socio

class Actividad(models.Model):
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField()  
    fecha = models.DateTimeField()  
    creador = models.ForeignKey(Socio, on_delete=models.CASCADE)  
    max_socios = models.IntegerField(default=10) 

    def __str__(self):
        return self.nombre



class Inscripcion(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE) 
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE) 
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)  

    class Meta:
        unique_together = ('actividad', 'socio') 

    def __str__(self):
        return f"{self.socio.username} se inscribió en {self.actividad.nombre}"