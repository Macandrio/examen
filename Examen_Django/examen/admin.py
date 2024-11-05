from django.contrib import admin
from .models import (
    Juguete, Juguetería , Cliente, 
    Votacion , Banco
)


# Registrar todos los modelos de manera básica
admin.site.register(Juguete)
admin.site.register(Juguetería)
admin.site.register(Cliente)
admin.site.register(Votacion)
admin.site.register(Banco)