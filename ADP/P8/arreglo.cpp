/**
 * @file arreglo.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Punteros y arreglos
 * @version 0.1
 * @date 2026-11-19
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>

using namespace std;


int main()
{
    int arr[10];
    arr[0] = 9;

    int *p;

    cout << &arr << endl;
    cout << arr << endl;
    cout << *arr << endl;

    return 0;
}
