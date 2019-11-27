from .views import UsarioList
from django.urls import path


urlpatterns = [
     #path('usuario/', UsarioList.as_view(), name='usuario')
     path('usuario/', UsarioList.get_objects2)

    ## UsarioList.as_view() trae UsuarioList como una vista
]