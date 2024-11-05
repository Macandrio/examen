from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voto-cliente/<int:id_juguete>/', views.ultimo_voto, name='ultimo_voto'),
    path('voto-3/<int:id_cliente>/', views.voto_clietne, name='voto_clietne'),
    path('clientes-sin-voto/', views.Clientes_sin_voto, name='Clientes_sin_voto'),
    path('cuentas-bancarias/', views.Cuentas_bancarias, name='Cuentas_bancarias'),
    path('clientes-sin-bancos/', views.Votos_2023, name='Votos_2023'),
    path('media/', views.Media_voto, name='Media_voto'),


]