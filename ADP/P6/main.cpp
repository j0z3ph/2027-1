/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi primer clase (otra vez)
 * @version 0.1
 * @date 2026-11-09
 *
 * @copyright Copyright (c) 2026
 *
 */
#include <iostream>

using namespace std;

class Fecha
{
private:
    int dia;
    int mes;
    int anio;

    // Metodos
public:
    // Contructor
    Fecha(int dia, int mes, int anio) {
        this->dia = dia;
        this->mes = mes;
        this->anio = anio;
    }



    // Getters
    int getDia() { return dia; }
    int getMes() { return mes; }
    int getAnio() { return anio; }

    // Setters
    void setDia(int dia) { this->dia = dia; }
    void setMes(int mes) { this->mes = mes; }
    void setAnio(int anio) { this->anio = anio; }
};

class Persona
{
private:
    string nombre;
    string apellido1;
    string apellido2;
    Fecha *fecha_nacimiento;

    // Metodos
public:
    // Constructor
    Persona(string nom, string ap, string am, int dia, int mes, int anio) {
        this->fecha_nacimiento = new Fecha(dia, mes, anio);
        this->nombre = nom;
        this->apellido1 = ap;
        this->apellido2 = am;
    }

    // Getters
    string getNombre() { return this->nombre; }
    string getAPaterno() { return this->apellido1; }
    string getAMaterno() { return this->apellido2; }

    Fecha getFNacimiento() { return *(this->fecha_nacimiento); }

    // Setters
    void setNombre(string nombre) { this->nombre = nombre; }
    void setAPaterno(string ap) { this->apellido1 = ap; }
    void setAMaterno(string am) { this->apellido2 = am; }
    void setFNacimiento(int dia, int mes, int anio)
    {
        this->fecha_nacimiento->setDia(dia);
        this->fecha_nacimiento->setMes(mes);
        this->fecha_nacimiento->setAnio(anio);
    }
    int edad;
};

int main()
{
    Persona p("Leonardo", "Perez", "Frausto", 28, 02, 1985);


    // p.setNombre("Oliver");
    // p.setAPaterno("Rosario");
    // p.setAMaterno("Vega");
    // p.setFNacimiento(20, 4, -2007);

    cout << "Nombre: " << p.getNombre() << endl;

    return 0;
}
