
class A:
    def habla(self):
        print("Fierro pariente")
        
class B:
    def habla(self):
        print("Quien me jalo mi cabeello")
        
class C:
    def habla(self):
        print("Que milanesas que no bisteces")
        
class D(C,A,B):
    pass

class E(B,C,A):
    def habla(self):
        print("Holi") #sobreescritura


o = E()
o.habla()