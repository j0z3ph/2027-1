from abc import ABCMeta, abstractmethod

class Abstracta(metaclass=ABCMeta):
    
    @abstractmethod
    def metodo_abstracto():
        pass
    
class Clase(Abstracta):
    def metodo_abstracto():
        print('hola')
    
#obj = Abstracta()
obj2 = Clase()