from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import AsignarAgricultoresForm

# Create your views here.

@login_required
def asignar_agricultores(request):
    if request.user.rol != 'coopertativa':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    if request.method == 'POST':
        form = AsignarAgricultoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asignar_agricultores')
    else:
        form = AsignarAgricultoresForm()
    return render(request, 'cooperativa/asignar_agricultores.html', {'form': form})
