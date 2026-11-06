/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi primer clase :D
 * @version 0.1
 * @date 2026-11-05
 *
 * @copyright Copyright (c) 2026
 *
 */
#include <iostream>

class Fecha
{
    int dia;
    int mes;
    int anio;
};

class Alumno
{
    int boleta;
    char nombre[100];
    char apellido1[100];
    char apellido2[100];
    Fecha fecha_nacimiento;
    void habla()
    {
        printf("Hola\n");
    }
};

int main()
{
    Alumno al;
    al.habla();

    return 0;
}
