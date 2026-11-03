

class Persona:
    
    def __init__(self, nombre:str, edad:int ):
        self._nombre = nombre
        self.__edad = edad
        
    def __str__(self):
        return f"{self._nombre}, {self.__edad}"
        
instancia = Persona("Ian Carlo", 67)
instancia._Persona__edad = 10
print(instancia)
print(f"{instancia._nombre}, {instancia._Persona__edad}")