from django.urls import path
from .views import ListaPublicacionesView, NuevaPublicacionView, EditarPublicacionView, BorrarPublicacionView

app_name = "foro"

urlpatterns = [
    path("foro/", ListaPublicacionesView.as_view(), name="list_public"),
    path("nueva_publi/", NuevaPublicacionView.as_view(), name="nueva_public"),
    path("editar_publi/<int:pk>/", EditarPublicacionView.as_view(), name="editar_public"),  # Ruta para editar
    path("borrar_publi/<int:pk>/", BorrarPublicacionView.as_view(), name="borrar_public"),  # Ruta para borrar
]