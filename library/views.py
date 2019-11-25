from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#importe de la clase
from .modeloDominio.Usuario import Usuario



def hora():
    fechaActual=datetime.datetime.now()
    return fechaActual
def saludo(request): #Primera VISTA
    return HttpResponse(hora())

# toda petición tiene que tener una respuesta
def recibedatosGet(request,nombre,anio): 
    print(anio)
    print(nombre)
    return HttpResponse(anio)

@csrf_exempt #decorador para csrf
def recibeDatosPost(request):
    received_json_data=json.loads(request.body)
    reciclador = Usuario(received_json_data["nombres"], received_json_data["apellidos"])
    if request.method == "POST":
         print(reciclador.getApellidos())
         try:
             return HttpResponse(reciclador.getApellidos())
         except:
             print("algo ocurrió")
    



