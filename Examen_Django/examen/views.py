from django.shortcuts import render
from django.db.models import Prefetch, Q , Avg
from .models import (
    Juguete, Juguetería, Cliente, Votacion, Banco
)


def index(request):
    return render(request, 'index.html') 

# El último voto que se realizó en un modelo principal en concreto, y mostrar el comentario,
#  la votación e información del usuario o cliente que lo realizó: 1.5 puntos

def ultimo_voto(request, id_juguete):
    comentario = Votacion.objects.select_related('cliente' , 'juguete')
    comentario = comentario.filter(juguete__id = id_juguete).order_by('-fecha_voto').first() # solo coje un dato

    return render(request, 'ultimo-voto.html', {'comentario': comentario})

#Todos los modelos principales que tengan votos con una puntuación numérica menor a 3 y 
# que realizó un usuario o cliente en concreto: 1.5 puntos

def voto_clietne(request, id_cliente):
    votos = Votacion.objects.select_related('cliente', 'juguete')
    votos = votos.filter(cliente__id = id_cliente , puntuacion = 3)

    return render(request, 'voto-usuario.html', {'votos': votos})


#Todos los usuarios o clientes que no han votado nunca y mostrar información sobre estos usuarios y clientes al completo: 1.5 puntos

#pasajero sin votos
def Clientes_sin_voto(request):
    cliente = Cliente.objects.prefetch_related(Prefetch('cliente_voto'))
    cliente = cliente.filter(cliente_voto__isnull = True)
    return render(request, 'pasajero-sin-votos.html', {'cliente': cliente})

#Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el propietario tenga un nombre que contenga un texto en concreto,
#  por ejemplo “Juan”: 1.5 puntos

def Cuentas_bancarias(request):
    cuenta = Banco.objects.select_related('cliente')
    cuenta = cuenta.filter(Q(banco = 'C') | Q(banco = 'U') , cliente__nombre__icontains = 'Juan')
    return render(request, 'cuentas-bancaria.html', {'cuenta': cuenta})


#Obtener los votos de los usuarios que hayan votado a partir del 2023 
# con una puntuación numérica igual a 5  y que tengan asociada una cuenta bancaria. 1.5 puntos

def Votos_2023(request):
    votos = Votacion.objects.select_related('cliente').prefetch_related(Prefetch('banco_cliente'))
    votos = votos.filter( fecha_voto__year__gt = 2023 , cliente__banco_cliente__isnull =True,
                         puntuacion__gt = 5)
    return render(request, 'Votos_2023.html', {'votos': votos})


#Obtener todos los modelos principales que tengan una media de votaciones mayor del 2,5: 1.5 punto
def Media_voto(request):
    juguete = Juguete.objects.annotate(media_puntuacion=Avg('voto_jugete__puntuacion')).filter(media_puntuacion__gt=2.5) #añade un campo adicional a cada objeto del queryset que representa el resultado del cálculo
    return render(request, 'media.html', {'juguete': juguete})


# Error 400 - Solicitud Incorrecta
def error_400(request, exception):
    return render(request, 'errors/400.html', status=400)

# Error 403 - Prohibido
def error_403(request, exception):
    return render(request, 'errors/403.html', status=403)

# Error 404 - No Encontrado
def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

# Error 500 - Error Interno del Servidor
def error_500(request):
    return render(request, 'errors/500.html', status=500)
