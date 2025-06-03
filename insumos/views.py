# insumos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Insumo
from .forms import InsumoForm

@login_required
def crear_insumo(request):
    if request.user.rol != 'agricultor':
        return HttpResponseForbidden("Solo los agricultores pueden crear insumos.")

    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            insumo = form.save(commit=False)
            insumo.agricultor = request.user  # asignar el usuario logueado
            insumo.save()
            messages.success(request, "Insumo creado correctamente.")
            return redirect('listar_insumos')
    else:
        form = InsumoForm()

    return render(request, 'insumo/crear_insumo.html', {'form': form})


@login_required
def editar_insumo(request, insumo_id):
    try:
        insumo = Insumo.objects.get(id=insumo_id)
    except Insumo.DoesNotExist:
        messages.error(request, "Insumo no encontrado.")
        return redirect('listar_insumos')

    if insumo.agricultor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este insumo.")

    if request.method == 'POST':
        form = InsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            messages.success(request, "Insumo editado correctamente.")
            return redirect('listar_insumos')
    else:
        form = InsumoForm(instance=insumo)

    return render(request, 'insumo/editar_insumo.html', {'form': form, 'insumo': insumo})

@login_required
def eliminar_insumo(request, insumo_id):
    try:
        insumo = Insumo.objects.get(id=insumo_id)
    except Insumo.DoesNotExist:
        messages.error(request, "Insumo no encontrado.")
        return redirect('listar_insumos')

    if insumo.agricultor != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este insumo.")

    if request.method == 'POST':
        insumo.delete()
        messages.success(request, "Insumo eliminado correctamente.")
        return redirect('listar_insumos')

    return render(request, 'insumo/eliminar_insumo.html', {'insumo': insumo})


#
@login_required
def listar_insumos(request):
    # Solo insumos creados por el usuario logueado
    insumos = Insumo.objects.filter(agricultor=request.user).order_by('-fecha_creacion')
    return render(request, 'insumo/listar_insumos.html', {'insumos': insumos})

