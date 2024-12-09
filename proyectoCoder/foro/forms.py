from django import forms
from .models import publicacion
class public_form(forms.ModelForm):
    class Meta:
        model = publicacion
        fields= ["titulo", "contenido"]