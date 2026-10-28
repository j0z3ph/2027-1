import math as m
from math import pow, sqrt, sin, cos



def suma(a: int,b: int, c:int = 0, d:int = 0) -> float:
    """Suma cosas

    Args:
        a (int): Pus A
        b (int): Pus B
        c (int, optional): Pus c. Defaults to 0.
        d (int, optional): Pus d. Defaults to 0.

    Returns:
        float: Pus resultado
    """
    return a + b + c + d

numa = 5
numb = 7
print(suma(c=numa, d=numb, b = 9, a = 10))


def otra():
    print("XD")
    
import numpy as np


def otra_funcion(*numeros):
    for i in numeros:
        print(i)
        
otra_funcion(1,2,3,4,5,'Adios')


otra_suma = lambda a,b: a + b

print(otra_suma(3,4))

