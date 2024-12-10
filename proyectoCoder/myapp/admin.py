from django.contrib import admin
from socios.models import Socio
from foro.models import publicacion

# Register your models here.


admin.site.register(Socio)
admin.site.register(publicacion)