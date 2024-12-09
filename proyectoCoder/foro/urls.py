from django.urls import path
from . import views
app_name="foro"
urlpatterns = [
    path("foro/", views.lista_public, name="list_public")
]
