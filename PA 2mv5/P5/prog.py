
class Abstracta:
    
    def metodo_abstracto(self):
        raise NotImplementedError()
    
class Clase(Abstracta):
    pass

obj = Clase()

obj2 = Abstracta()

obj2.metodo_abstracto()

obj.metodo_abstracto()