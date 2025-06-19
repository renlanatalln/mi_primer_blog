from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
from .models import Cartelera

def lista_public(request):
    publicaciones=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/lista_public.html',{'publicaciones':publicaciones})

def lista_cartelera(request):
    cartelera=Cartelera.objects.all()
    return render(request,'blog/lista_cartelera.html',{'cartelera':cartelera})