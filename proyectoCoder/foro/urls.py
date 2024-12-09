from django.urls import path
from . import views
app_name="foro"
urlpatterns = [
    path("foro/", views.lista_public, name="list_public"),
    path("nueva_publi/", views.nueva_public, name="nueva_public")
    
]
