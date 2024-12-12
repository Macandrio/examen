from django.shortcuts import render, redirect
from django.db.models import Prefetch, Q, Sum, Count
from .models import *
from .forms import * # El * Coge todos los modelos es lo mismo que hacer lo de from .models import
from django.contrib import messages

def index(request):
    return render(request, 'index.html') 

def Crear_Promocio(request):
    if request.method == "POST":
        formulario = CrearPromocioform(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.success(request, "la promocion se creó exitosamente.")
                #return redirect("lista_aeropuerto")
            except Exception as error:
                messages.error(request, f"Error inesperado al guardar el aeropuerto: {error}")
        else:
            # Mensaje de error si el formulario no es válido
            messages.error(request, "Ya existe una promocion con el mismo nombre. Verifica los datos ingresados.")
    else:
        formulario = CrearPromocioform()

    return render(request, 'Formulario/crear_promocion.html', {"formulario": formulario})


def promocion_buscar_avanzado(request):
    formulario = BusquedaAvanzadaPromocion(request.GET)
    promocions = Promocion.objects.all()
    usuario = Usuario.objects.all()
    promocion = Promocion.objects.all()

    if request.GET:
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            descripcion = formulario.cleaned_data.get('descripcion')
            descuento = formulario.cleaned_data.get('descuento')
            fecha_inicio = formulario.cleaned_data.get('fecha_inicio')
            fecha_fin = formulario.cleaned_data.get('fecha_fin')
            esta_activa = formulario.cleaned_data.get('esta_activa')
            producto = formulario.cleaned_data.get('producto')
            usuario = formulario.cleaned_data.get('usuario')

            if nombre:
                promocions = promocions.filter(nombre__icontains=nombre)

            if descripcion:
                promocions = promocions.filter(descripcion__icontains=descripcion)

            if descuento:
                 promocions = promocions.filter(descuento > descuento)

        else:
            return render (request, 'Formulario/busqueda_avanzada.html', {
                'formulario': formulario,
                'promocions': []
            })

    return render (request, 'Formulario/busqueda_avanzada.html', {
        'formulario': formulario,
        'promocions': promocions
    })


def editar_promocion(request, id):
    aeropuerto = Promocion.objects.get(id=id)  # Obtiene el aeropuerto por ID
    if request.method == 'POST':
        formulario = CrearPromocioform(request.POST, instance=aeropuerto)
        if formulario.is_valid():
            formulario.save()
            return redirect('promocion_buscar_avanzado')  # Redirige a la lista después de actualizar
    else:
        formulario = CrearPromocioform(instance=aeropuerto)

    return render(request, 'Formulario/editar_promocion.html', {'formulario': formulario, 'aeropuerto': aeropuerto})