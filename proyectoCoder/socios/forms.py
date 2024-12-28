from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Socio

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    is_staff = forms.BooleanField(required=False, initial=True)
    is_superuser = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = Socio
        fields = ['username', 'email', 'password1', 'password2', 'tel', 'member', 'pagoOk','is_staff','is_superuser']

class UpdatePerfilForm(UserChangeForm):
    # Excluir la contraseña actual del modelo porque la gestionaremos de manera explícita
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Socio
        fields = ['first_name', 'last_name', 'email', 'tel', 'member', 'password']
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password:
            return password
        return None