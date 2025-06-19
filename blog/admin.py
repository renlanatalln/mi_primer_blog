from django.contrib import admin
from .models import Publicacion
from .models import Cartelera

admin.site.register(Publicacion)
admin.site.register(Cartelera)