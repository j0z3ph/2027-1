

class Clase:
    
    def __init__(self, texto: str, numero: int):
        self.__texto = texto
        self.__numero = numero
    
    def get_numero(self):
        return self.__numero    
    
    def set_numero(self, numero):
        self.__numero = numero
        
        
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
        
    def metodo(self):
        pass
    
        
objeto = Clase("Texto", 78)

objeto.set_numero(-100)
objeto.numero = 6
objeto.metodo()

print(objeto.get_numero())