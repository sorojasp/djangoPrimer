from rest_framework import serializers
from .apps.usuario import Usuario

class DuckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Usuario
        fields= ('nombres', 'apellidos')