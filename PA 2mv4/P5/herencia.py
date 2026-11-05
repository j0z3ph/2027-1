
class Papa:
    def __init__(self, nombre: str):
        self._nombre = nombre
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
class Hije(Papa):
    pass


hije = Hije("Prudencia")

print(hije.nombre)