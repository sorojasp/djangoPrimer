
class Usuario:
    def __init__(self, nombres: str, apellidos: str):
        self.__nombres=nombres
        self.__apellidos=apellidos
    
    
    def getNombres(self)->str:
        return self.__nombres

    
    def setNombres(self, nombres_):
        self.__nombres=nombres_
    
    
    def getApellidos(self)->str:
        return self.__apellidos
    
    

    





