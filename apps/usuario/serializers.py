from rest_framework import serializers
from .models import UsuarioModel

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsuarioModel # se importa el módelo
        fields = ('nombres', 'apellidos')