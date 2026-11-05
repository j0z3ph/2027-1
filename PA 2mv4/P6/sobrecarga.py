from multimethod import multimethod

class Clase:
    
    @multimethod
    def habla(self, msj):
        print(msj)
    
    @multimethod
    def habla(self):
        print("Holi")
        
o = Clase()

o.habla("3")
o.habla()