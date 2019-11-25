from .views import UsarioList
from django.urls import path


urlpatterns = [
     path('usuario/', UsarioList.as_view(), name='usuario')
    ## UsarioList.as_view() trae UsuarioList como una vista
]