from django.shortcuts import render

# Create your views here.


#importe de las librerias de serializador
from rest_framework import generics
from .serializers import UsuarioSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

#importe del serializador
from .serializers import UsuarioSerializer

#importe del Modelo
from apps.usuario.models import UsuarioModel

# importe de la librería para responder a las peticiones al servidor
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

class UsarioList(generics.ListCreateAPIView):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        queryset = self.get_queryset() #método para traer los objetos
        obj =get_object_or_404(
            queryset,
            nombres=self.kwargs['nombres'],
        )
        return obj
    
    @csrf_exempt #decorador para csrf para poder responder las peticiones que se le hace al servidor
    def get_objects2(request):
        print("hola")
        UsuarioModel.objects.create(nombres="Juan", apellidos="Perez Ramos")
        print(UsuarioModel.objects.filter(id=12))
        return HttpResponse(type(UsuarioModel.objects.all()[0]))
         