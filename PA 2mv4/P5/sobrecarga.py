from multimethod import multimethod

class Clase:
    @multimethod
    def habla(self):
        print("Holi")
    
    @multimethod
    def habla(self, msg: str):
        print(msg)
    
    @multimethod
    def habla(self, msg:str, repite:int):
        for i in range(repite):
            print(msg)
            
objeto = Clase()

objeto.habla()
objeto.habla("Crayoli")
objeto.habla("Kiuvo", 10)
