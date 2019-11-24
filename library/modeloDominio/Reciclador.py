from .Usuario import Usuario

class Reciclador(Usuario):
    def __init__(self, nombres: str, apellidos: str):
        super().__init__(nombres, apellidos)

