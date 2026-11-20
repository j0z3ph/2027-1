/**
 * @file referencias.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Pasos de parametros
 * @version 0.1
 * @date 2026-11-19
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>

using namespace std;

void suma(int a, int b, int *res) {
    *res = a + b;
}

int main()
{
    int a = 6, b = 7, res;

    suma(a,b,&res);

    cout << res << endl;

    
    return 0;
}
