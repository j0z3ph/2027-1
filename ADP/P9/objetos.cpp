/**
 * @file objetos.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Y que onda con los objetos?
 * @version 0.1
 * @date 2026-11-26
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>

using namespace std;

class Persona {
    private:
    string nombre;
    string ap1;
    string ap2;

    public:
    // Getters
    string getNombre() { return this->nombre; }
    string getApellidoPaterno() { return this->ap1; }
    string getApellidoMaterno() { return this->ap2; }

    // Setters
    void setNombre(string nombre) { this->nombre = nombre; }
    void setApellidoPaterno(string ap) { this->ap1 = ap; }
    void setApellidoMaterno(string am) { this->ap2 = am; }

};

int main()
{
    Persona* p;

    p = new Persona();

    (*p).setNombre("Oliver");
    p->setApellidoPaterno("Zamora");
    p->setApellidoMaterno("Gomez");

    
    
    return 0;
}
