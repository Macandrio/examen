from django.contrib import admin
from .models import *


# Registrar todos los modelos de manera básica
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Promocion)