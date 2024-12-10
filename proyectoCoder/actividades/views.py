from django.shortcuts import render, redirect
from .models import Actividad, Inscripcion
from .forms import ActividadForm
from django.contrib.auth.decorators import login_required

@login_required
def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.creador = request.user  
            actividad.save()
            return redirect('actividades:lista_actividades') 
    else:
        form = ActividadForm()

    return render(request, 'actividades/new_actividad.html', {'form': form})

def lista_actividades(request):
    actividades = Actividad.objects.all()


    inscrito_ids = []
    if request.user.is_authenticated:
  
        inscripciones = Inscripcion.objects.filter(socio=request.user)
        inscrito_ids = [inscripcion.actividad.id for inscripcion in inscripciones]

 
    if request.method == "POST" and request.user.is_authenticated:
        actividad_id = request.POST.get("actividad_id")
        actividad = Actividad.objects.get(id=actividad_id)
        
  
        if actividad.max_socios > Inscripcion.objects.filter(actividad=actividad).count() and actividad.id not in inscrito_ids:
            Inscripcion.objects.create(actividad=actividad, socio=request.user)
            return redirect('actividades:lista_actividades')

    return render(request, 'actividades/actividades.html', {
        'actividades': actividades,
        'inscrito_ids': inscrito_ids 
    })