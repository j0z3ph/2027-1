/**
 * @file dinamico.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief MUY dinamico
 * @version 0.1
 * @date 2026-11-26
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>

using namespace std;

int main()
{
    {
        int* a = new int;
        *a = 10;
        delete a;

        int *arr = new int[100];
        delete[] arr;
    }

    cout << a << endl; // Aqui ya no furula
    
    return 0;
}
