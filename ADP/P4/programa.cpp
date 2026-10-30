/**
 * @file programa.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Sobrecarga de funciones
 * @version 0.1
 * @date 2026-10-29
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>

using namespace std;

int suma(int a, int b, int c = 0, int d = 0) {
    return a + b + c + d;
}

float suma(float a, float b) {
    return a + b;
}

// int suma(int a, int b , int c) {
//     return a + b + c;
// }

// int suma(int a, int b , int c, int d) {
//     return a + b + c + d;
// }

int main()
{
    suma(4,5);
    
    return 0;
}
