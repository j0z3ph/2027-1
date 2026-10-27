
la_variable = 10

def la_funcion():
    global la_variable
    la_variable = 11
    
la_funcion()

print(la_variable)