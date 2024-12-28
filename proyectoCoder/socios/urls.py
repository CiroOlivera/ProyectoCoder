from django.urls import path
from . import views

app_name = "socios"

urlpatterns = [
    path("socios/", views.ListaSociosView.as_view(), name="list_socios"),
    path("nuevo_socio/", views.RegistroUsuarioView.as_view(), name="registro_usuario"),
    path("login/", views.LoginVistaView.as_view(), name="login"),
    path("logout/", views.LogoutVistaView.as_view(), name="logout"),
    path("perfil/<int:pk>/", views.DetallePerfilView.as_view(), name="detalle_perfil"),
    path("editar_perfil/<pk>/", views.EditarPerfilView.as_view(), name="editar_perfil"),  # URL para editar el perfil
    path("eliminar_cuenta/", views.eliminar_cuenta, name="eliminar_cuenta"),  # URL para eliminar la cuenta
]