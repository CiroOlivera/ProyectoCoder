from django.urls import path
from . import views
app_name="socios"
urlpatterns = [
    path("socios/", views.lista_socios, name="list_socios"),
    path("nuevo_socio/", views.registro_usuario, name="registro_usuario") ,
    path("login/", views.login_vista, name="login"),
    path("logout/", views.logout_vista, name="logout"),
]