class Abstracta:
    
    def metodo_abstracto(self):
        raise NotImplementedError()
    
class Clase(Abstracta):
    def metodo_abstracto(self):
        print('hola')

obj2 = Abstracta()

obj = Clase()
obj.metodo_abstracto()