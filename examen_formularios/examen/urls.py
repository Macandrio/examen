from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('promocion/crear/', views.Crear_Promocio, name='Crear_Promocio'),
    path('promocion/buscar/', views.promocion_buscar_avanzado, name='promocion_buscar_avanzado'),
    path('promocion/editar/<int:id>/', views.editar_promocion, name='editar_promocion'),
]
