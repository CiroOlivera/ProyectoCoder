from django.shortcuts import render
from .models import publicacion


# Create your views here.
def lista_public(request):
    list_public= publicacion.objects.all()
    print (list_public)
    return render(request, 'foro/foro.html', {"publics":list_public})
