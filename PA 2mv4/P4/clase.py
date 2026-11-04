
class Persona:
    
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre # Por si no quedo claro: PROTEGIDO
        self.__edad = edad
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad:int):
        self.__edad = nueva_edad
 
    
    def __str__(self):
        return f"{self._nombre} soy {self.__edad}"
    
    def saluda(self):
        print(f"{self._nombre} soy {self.__edad}")
    
    @classmethod    
    def metodo_de_clase(cls):
        print("Holi crayoli")
    
    @staticmethod
    def metodo_estatico():
        print("Cualquier cosa")

objeto = Persona("Vitela", 26)
Persona.metodo_de_clase()

objeto.edad = 5

#objeto._nombre = "Cachirulo"
#objeto.__edad = -100
#objeto._Persona__edad = -50

#objeto.nombre = "Otra cadena"
#objeto.edad = "Otro entero"

print(objeto)