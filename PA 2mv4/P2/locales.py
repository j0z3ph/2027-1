

def funcion():
    var = 1
    def funcion2():
        nonlocal var
        var = 3
    
    funcion2()
    print(var)
    
funcion()