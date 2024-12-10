from django.urls import path
from . import views

app_name = 'actividades'

urlpatterns = [
    path('crear_actividad/', views.crear_actividad, name='crear_actividad'),
    path('lista_actividades/', views.lista_actividades, name='lista_actividades'),
]