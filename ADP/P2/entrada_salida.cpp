/**
 * @file entrada_salida.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi segundo programa en C Plus Plus
 * @version 0.1
 * @date 2026-10-26
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>

using namespace std;

int main()
{
    int numero;
    cout << "Usuario, ingresa un numero entero positivo: ";

    cin >> numero;

    cout << "El doble de " << numero << " es " << (numero * 2) << "." << endl;

    return 0;
}
