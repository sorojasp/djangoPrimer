"""RecyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from library.views import *

from .modeloDominio.Usuario import Usuario
from .modeloDominio.Reciclador import Reciclador





usuario=Usuario("Stiven Orlando", "Rojas Pulido")
print(usuario.getApellidos())

reciclador:Reciclador = Reciclador("JUAN CARLOS", "PULIDO PAEZ")
print(reciclador.getApellidos())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('primer/<anio>/<nombre>', recibedatosGet),
    path('datosPost/', recibeDatosPost),
    path('us/', include('apps.usuario.urls'))
]
