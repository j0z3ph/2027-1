
class ClaseA:
    def habla(self):
        print("Fierro pariente")
        
class ClaseB:
    def habla(self):
        print("Bomba")

class ClaseC:
    def habla(self):
        print("Wey")
        
class ClaseD(ClaseC, ClaseA, ClaseB):
    def habla(self):
        print("Holi")
        
    def habla(self, msg:str):
        print(msg)
        
objeto = ClaseD()

objeto.habla("El Problema")  
