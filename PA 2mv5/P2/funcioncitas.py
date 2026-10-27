import math as m


def suma(a: int, b: int, c: int = 0, d: int = 0) -> float:
    """Esta funcion suma

    Args:
        a (int): A
        b (int): B
        c (int, optional): Pus C. Defaults to 0.
        d (int, optional): Pus D. Defaults to 0.

    Returns:
        float: Resultado
    """
    return a + b + c + d

numA = int(input("Ingresa un valor: "))
numB = int(input("Ingresa un valor: "))

print(suma(b=numA, d=numB, a=1, c=2))


def otra_suma(*numeros):
    for i in numeros:
        print(i)
        
otra_suma(1,2,3,4,5)

mas_sumas = lambda a, b: a+b

print(mas_sumas(2,3))