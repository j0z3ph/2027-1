/**
 * @file programa.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi primer programa con funciones
 * @version 0.1
 * @date 2026-10-26
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>
#include "calculadora.hpp"
#include "calculadora.hpp"

using namespace std;

int main()
{
    int numa, numb;
    cout << "Usuario, ingresa el valor A: ";
    cin >> numa;
    cout << "Usuario, ingresa el valor B: ";
    cin >> numb;

    cout << "La suma es: " << suma(numa, numb) << endl;

    return 0;
}


