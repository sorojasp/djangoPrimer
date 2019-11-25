from django.shortcuts import render

# Create your views here.


#importe de las librerias de serializador
from rest_framework import generics
from .serializers import UsuarioSerializer
from django.shortcuts import get_object_or_404


#importe del serializador
from .serializers import UsuarioSerializer

#importe del Modelo
from apps.usuario.models import UsuarioModel

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