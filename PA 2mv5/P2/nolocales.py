

def funcion():
    variable = 1
    def otra_funcion():
        nonlocal variable
        variable = 2
        def f():
            nonlocal variable
            variable = 3
        f()
    
    otra_funcion()
    print(variable)
    
funcion()