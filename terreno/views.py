from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Terreno
from .forms import TerrenoForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from accounts.models import CustomUser

@login_required
def crear_terreno(request):
    if request.user.rol != 'ingeniero':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    if request.method == 'POST':
        form = TerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TerrenoForm()
    return render(request, 'terreno/create.html', {'form': form})

@login_required
def mis_terrenos(request):
    if request.user.rol != 'agricultor':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    terrenos = Terreno.objects.filter(agricultor=request.user)
    return render(request, 'terreno/mis_terrenos.html', {'terrenos': terrenos})
@login_required
def ver_agricultores(request):
    if not request.user.is_authenticated or request.user.rol != 'ingeniero':
        return HttpResponseForbidden('No tienes permiso para accceder a esta pagina')
    agricultores = CustomUser.objects.filter(rol = 'agricultor')
    return render(request, 'terreno/agricultores.html', {'agricultores': agricultores})

@login_required
def terreno_por_agricultor(request, id):
    # Solo los ingenieros pueden acceder
    if request.user.rol != 'ingeniero':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    # Buscamos al agricultor por ID o devolvemos 404 si no existe
    agricultor = get_object_or_404(CustomUser, id=id, rol='agricultor')

    # Obtenemos los terrenos asociados a ese agricultor
    terrenos = Terreno.objects.filter(agricultor=agricultor)


    # Enviamos al template el agricultor y sus terrenos
    return render(request, 'terreno/terrenos_por_agricultor.html', {
        'agricultor': agricultor,
        'terrenos': terrenos
    })