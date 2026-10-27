/**
 * @file programa.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Los strings XD
 * @version 0.1
 * @date 2026-10-26
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string nombre;

    cout << "Usuario, ingresa tu nombre: ";

    getline(cin, nombre);
    //cin >> nombre;

    cout << "El texto ingresado es: " << nombre << endl;
    return 0;
}
