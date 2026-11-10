from abc import ABCMeta, abstractmethod

class Abstracta(metaclass=ABCMeta):
    @abstractmethod
    def metodo_abstracto(self):
        pass
    
class Clase(Abstracta):
    def metodo_abstracto(self):
        print("Hola")

obj = Clase()
obk2 = Abstracta()

obj.metodo_abstracto()