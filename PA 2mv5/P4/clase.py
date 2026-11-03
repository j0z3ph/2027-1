

class Persona:
    algo = None
    
    def __init__(self, n:str, b:int):
        self.boleta = b
        self.nombre = n
        
    def __str__(self):
        return f'Soy el objeto {self.boleta} y digo {self.nombre}'
    
    @classmethod
    def metodo_de_clase(cls):
        cls.algo = 'algo'
        print(cls.algo)
    
    @staticmethod
    def metodo_estatico():
        print("Soy estatico")

objeto = Persona("Ulises y Toño", 67)
Persona.nombre = "Luis"
print(objeto)

Persona.metodo_de_clase()
Persona.metodo_estatico()