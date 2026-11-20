/**
 * @file lista.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de lista
 * @version 0.1
 * @date 2026-11-19
 * 
 * @copyright Copyright (c) 2026
 * 
 */
#include <iostream>
#include <vector>

using namespace std;

class Cosa {

};

int main()
{
    vector<int> lista;
    vector<Cosa> listaAsistencia;

    lista.push_back(2);
    lista.push_back(6);
    lista.push_back(5);
    lista.push_back(0);

    for (size_t i = 0; i < lista.size(); i++)
    {
        cout << lista[i] << endl;
    }
    

    
    return 0;
}
