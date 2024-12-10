from django.contrib import admin
from .models import Actividad, Inscripcion



class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'creador', 'max_socios')
    search_fields = ('nombre', 'descripcion')

admin.site.register(Actividad, ActividadAdmin)

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('actividad', 'socio', 'fecha_inscripcion')
    search_fields = ('actividad__nombre', 'socio__username')

admin.site.register(Inscripcion, InscripcionAdmin)