from django.shortcuts import render, redirect
from .models import Socio
from .forms import RegistroUsuarioForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def lista_socios(request):
    list_socios= Socio.objects.all()
    return render(request, "socios/socios.html",{"socios":list_socios}) 

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  
            return redirect("socios:list_socios")  
    else:
        form = RegistroUsuarioForm()

    return render(request, "socios/nuevo_socio.html", {"form": form})

def login_vista(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())  
            return redirect("myapp:index")
        
    else:
        form = AuthenticationForm()
    return render(request, "socios/login.html", {"form": form})

def logout_vista(request):
    logout(request)
    return redirect("myapp:index")