from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Socio(AbstractUser):
    
    tel=models.IntegerField()
    member=models.CharField(max_length=50)
    pagoOk=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
