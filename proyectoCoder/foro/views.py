from django.shortcuts import render, redirect
from .models import publicacion
from .forms import public_form

# Create your views here.
def lista_public(request):
    list_public= publicacion.objects.all()
    return render(request, 'foro/foro.html', {"publics":list_public})

def nueva_public(request):
    if request.method == "POST":
        form= public_form(request.POST)
        if form.is_valid():
            public= form.save(commit=False)
            if request.user.is_authenticated:
                public.autor= request.user
                public.save()
                return redirect("foro:list_public")
            else:
                form.add_error(None, "Necesitas estar logueado")        
    else :
        form = public_form()
    return render(request, 'foro/nueva_publi.html', context={"form":form})