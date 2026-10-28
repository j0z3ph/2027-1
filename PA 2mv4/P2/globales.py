

una_variable_global = 4

def la_funcion():
    global una_variable_global
    una_variable_global = 5
    

    
la_funcion()
print(una_variable_global)