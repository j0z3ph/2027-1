/**
 * @file sobrecarga.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Sobre carga de operadores
 * @version 0.1
 * @date 2026-11-26
 *
 * @copyright Copyright (c) 2026
 *
 */
#include <iostream>

using namespace std;

class Punto
{
private:
    int x;
    int y;

public:
    // getters
    int getX() { return this->x; }
    int getY() { return this->y; }

    // setters
    void setX(int x) { this->x = x; }
    void setY(int y) { this->y = y; }

    Punto operator+(Punto &b)
    {
        Punto c;
        c.setX(this->getX() + b.getX());
        c.setY(this->getY() + b.getY());
        return c;
    }

    friend ostream &operator<<(ostream &os, Punto &p)
    {
        os << "(" << p.getX() << ", " << p.getY() << ")";
        return os;
    }
};

// ostream& operator<<(ostream &os, Punto &p)
// {
//     os << "(" << p.getX() << ", " << p.getY() << ")";
//     return os;
// }


// Punto operator+(Punto a, Punto b)
// {
//     Punto c;
//     c.setX(a.getX() + b.getX());
//     c.setY(a.getY() + b.getY());
//     return c;
// }

int main()
{
    Punto p1;
    Punto p2;

    p1.setX(5);
    p1.setY(8);

    p2.setX(3);
    p2.setY(6);

    Punto p3 = p1 + p2;

    cout << p3 << endl;

    return 0;
}
