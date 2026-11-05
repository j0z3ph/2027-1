
class Papa:
    
    def metodo(self):
        print("Hace algo")
        
class Hije(Papa):
    pass


instancia = Hije()

instancia.metodo()