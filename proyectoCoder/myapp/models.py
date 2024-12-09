from django.db import models

# Create your models here.
class Socio(models.Model):
    
    nombre=models.CharField(max_length=50)
    mail= models.CharField(max_length=50)
    tel=models.IntegerField()
    member=models.CharField(max_length=50)
    pagoOk=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class actividad(models.Model):
    pass