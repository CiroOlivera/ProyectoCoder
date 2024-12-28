from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from django.http import Http404
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import publicacion
from .forms import public_form

# Vista para listar las publicaciones
class ListaPublicacionesView(ListView):
    model = publicacion
    template_name = 'foro/foro.html'
    context_object_name = 'publics'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            return publicacion.objects.filter(titulo__icontains=search_query) | publicacion.objects.filter(contenido__icontains=search_query)
        return publicacion.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

# Vista para crear una nueva publicación (requiere estar logueado)
class NuevaPublicacionView(LoginRequiredMixin, CreateView):
    model = publicacion
    form_class = public_form
    template_name = 'foro/nueva_publi.html'
    success_url = reverse_lazy('foro:list_public')  # Redirige a la lista de publicaciones

    # Asigna el autor de la publicación al usuario logueado antes de guardar
    def form_valid(self, form):
        public = form.save(commit=False)
        public.autor = self.request.user  # Asigna el autor como el usuario autenticado
        public.save()
        return super().form_valid(form)

    # Si el formulario es inválido, muestra el error de login necesario
    def form_invalid(self, form):
        form.add_error(None, "Necesitas estar logueado")
        return super().form_invalid(form)

# Decorador para asegurar que el usuario esté logueado antes de acceder a la vista de nueva publicación
nueva_public = login_required(NuevaPublicacionView.as_view())

class EditarPublicacionView(LoginRequiredMixin, UpdateView):
    model = publicacion
    form_class = public_form
    template_name = 'foro/editar_publi.html'

    def get_success_url(self):
        return reverse_lazy('foro:list_public')  # Redirige a la lista de publicaciones

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.autor != self.request.user:  # Verifica que el usuario autenticado sea el autor de la publicación
            raise Http404("No tienes permiso para editar esta publicación.")
        return obj
    
class BorrarPublicacionView(LoginRequiredMixin, DeleteView):
    model = publicacion
    template_name = 'foro/borrar_publi.html'
    success_url = reverse_lazy('foro:list_public')

    def get_object(self, queryset=None):
        # Obtiene el objeto a borrar y verifica si el usuario es el autor
        obj = super().get_object(queryset)
        if obj.autor != self.request.user:  # Verifica si el autor es el socio del usuario logueado
            raise Http404("No tienes permiso para borrar esta publicación.")
        return obj