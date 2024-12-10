from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Socio

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Socio
        fields = ['username', 'email', 'password1', 'password2', 'tel', 'member', 'pagoOk']