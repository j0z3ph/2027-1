
class Punto:
    
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
    
    def __add__(self, other):
        x = self.__x + other.x
        y = self.__y + other.y
        return Punto(x, y)
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y


p1 = Punto(4,5)
p2 = Punto(6,7)

p3 = p1 + p2

print(p3)