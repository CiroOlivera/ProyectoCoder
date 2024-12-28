from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views import View
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Socio
from .forms import RegistroUsuarioForm, UpdatePerfilForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Lista de socios
class ListaSociosView(ListView):
    model = Socio
    template_name = 'socios/socios.html'
    context_object_name = 'socios'

# Registro de un nuevo usuario
class RegistroUsuarioView(CreateView):
    model = Socio
    form_class = RegistroUsuarioForm
    template_name = 'socios/nuevo_socio.html'
    success_url = reverse_lazy('socios:list_socios')

    def form_valid(self, form):
        if form.is_valid():  # Verificar que el formulario esté validado
            usuario = form.save(commit=False)
            if form.cleaned_data['is_staff']:
                usuario.is_staff = True
            if form.cleaned_data['is_superuser']:
                usuario.is_superuser = True
            usuario.save()  # Guardar el usuario después de asignar los valores

            login(self.request, usuario)  # Loguear al usuario

            return redirect(self.success_url)  # Redirigir al éxito
        else:
            return self.form_invalid(form)
# Vista para hacer login
class LoginVistaView(View):
    def get(self, request):
        # Si el usuario ya está autenticado, lo redirigimos a la página principal
        if request.user.is_authenticated:
            return redirect('myapp:index')
        
        form = AuthenticationForm()  # Creamos una nueva instancia del formulario de autenticación
        return render(request, "socios/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)  # Recibimos los datos del formulario
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Iniciamos sesión con el usuario
            return redirect('myapp:index')  # Redirigimos al index o página deseada
        return render(request, "socios/login.html", {"form": form})

# Vista para hacer logout
class LogoutVistaView(CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("myapp:index")

# Editar perfil de usuario
class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = Socio
    form_class = UpdatePerfilForm
    template_name = 'socios/editar_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('socios:detalle_perfil', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        user = form.save(commit=False)  # Guardamos el usuario, pero aún no lo guardamos en la base de datos

        # Si el campo de la contraseña fue editado, actualizamos la contraseña
        password = form.cleaned_data.get("password")
        if password:
            user.set_password(password)  # Establecemos la nueva contraseña de manera segura
            user.save()  # Guardamos el usuario con la nueva contraseña

            # Iniciamos sesión nuevamente con la nueva contraseña para mantener la sesión activa
            update_session_auth_hash(self.request, user)

        user.save()  # Guardamos el usuario finalmente
        return redirect(self.get_success_url())

# Eliminar cuenta del usuario
def eliminar_cuenta(request):
    user = request.user
    if request.method == "POST":
        # Eliminar el usuario y redirigir a la página de inicio
        user.delete()
        return redirect("myapp:index")
    return render(request, 'socios/eliminar_cuenta.html', {"user": user})

class DetallePerfilView(DetailView):
    model = Socio
    template_name = 'socios/detalle_perfil.html'
    context_object_name = 'socio'

    def get_object(self, queryset=None):
        return self.request.user