/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi primer memoria dinamica
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
    int *ptr = new int;
    int *arr = new int[100];

    arr[0] = 1;
    arr[1] = 10;

    *ptr = 10;

    cout << ptr << "," << *ptr<< endl;
    cout << arr << ", " << arr[0] << ", " << *(arr + 1) << endl; 

    
    return 0;
}
