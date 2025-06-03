from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Terreno
from .forms import TerrenoForm
from accounts.models import CustomUser
from Cooperativa.models import IngenieroAgricultores  # Importamos la asignación

@login_required
def crear_terreno(request,id):
    if request.user.rol != 'ingeniero':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    # Obtener todas las relaciones de este ingeniero
    relaciones = IngenieroAgricultores.objects.filter(ingeniero=request.user)

    # Crear una lista para almacenar todos los agricultores asignados
    agricultores_asignados = []
    for relacion in relaciones:
        agricultores_asignados.extend(relacion.agricultores.all())

    # Convertimos la lista a un queryset sin duplicados
    agricultores_qs = CustomUser.objects.filter(id__in=[a.id for a in agricultores_asignados]).distinct()

    if request.method == 'POST':
        form = TerrenoForm(request.POST)

        if form.is_valid():
            terreno = form.save(commit=False)

            # Validamos que el agricultor esté asignado al ingeniero
            if terreno.agricultor in agricultores_qs:
                terreno.save()
                messages.success(request, 'Terreno creado exitosamente.')
                return redirect('home')
            else:
                messages.error(request, 'No puedes asignar un terreno a un agricultor que no te fue asignado.')
    else:
        form = TerrenoForm()
        form.fields['agricultor'].queryset = agricultores_qs  # Limitamos los agricultores en el formulario

    return render(request, 'terreno/create.html', {'form': form})


@login_required
def mis_terrenos(request):
    if request.user.rol != 'agricultor':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    terrenos = Terreno.objects.filter(agricultor=request.user)
    return render(request, 'terreno/mis_terrenos.html', {'terrenos': terrenos})

@login_required
def ver_agricultores(request):
    if request.user.rol != 'ingeniero':
        return HttpResponseForbidden('No tienes permiso para acceder a esta página.')

    # Obtenemos todas las relaciones de agricultores asignadas a este ingeniero
    relaciones = IngenieroAgricultores.objects.filter(ingeniero=request.user)

    # Unimos todos los agricultores de todas las relaciones en un solo queryset
    agricultores = CustomUser.objects.filter(
        id__in=[agricultor.id for relacion in relaciones for agricultor in relacion.agricultores.all()]
    ).distinct()

    return render(request, 'terreno/agricultores.html', {'agricultores': agricultores})


@login_required
def terreno_por_agricultor(request, id):
    # Solo los ingenieros pueden acceder
    if request.user.rol != 'ingeniero':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    # Buscar al agricultor por ID
    agricultor = get_object_or_404(CustomUser, id=id, rol='agricultor')

    # Obtener todas las relaciones del ingeniero actual
    relaciones = IngenieroAgricultores.objects.filter(ingeniero=request.user)

    # Obtener todos los agricultores asignados a ese ingeniero
    agricultores_asignados = []
    for relacion in relaciones:
        agricultores_asignados.extend(relacion.agricultores.all())

    # Verificar si el agricultor está dentro de los asignados
    if agricultor not in agricultores_asignados:
        return HttpResponseForbidden("No tienes permiso para ver los terrenos de este agricultor.")

    # Buscar terrenos del agricultor
    terrenos = Terreno.objects.filter(agricultor=agricultor)

    # Renderizar la vista
    return render(request, 'terreno/terrenos_por_agricultor.html', {
        'agricultor': agricultor,
        'terrenos': terrenos
    })
@login_required
def detalle_terreno(request, id):
    terreno = get_object_or_404(Terreno, id=id)
    
    if request.user.rol == 'ingeniero':
        relaciones = IngenieroAgricultores.objects.filter(ingeniero=request.user)
        agricultores_asignados = CustomUser.objects.filter(
            id__in=[a.id for rel in relaciones for a in rel.agricultores.all()]
        )
        if terreno.agricultor not in agricultores_asignados:
            return HttpResponseForbidden("No tienes permiso para ver este terreno.")

    elif request.user.rol == 'agricultor':
        if terreno.agricultor != request.user:
            return HttpResponseForbidden("No tienes permiso para ver este terreno.")

    else:
        return HttpResponseForbidden("No tienes permiso para ver este terreno.")

    return render(request, 'terreno/detalle_terreno.html', {'terreno': terreno})
