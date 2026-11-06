#include <stdio.h>

struct Fecha
{
    int dia;
    int mes;
    int anio;
};

typedef struct Alumno
{
    int boleta;
    char nombre[100];
    char apellido1[100];
    char apellido2[100];
    struct Fecha fecha_nacimiento;
} Alumno;

typedef int Entero;

void habla()
{
    printf("Hola\n");
}

int main()
{
    Entero entero;
    float flotante;
    double doble;
    char caracter;
    Alumno alumno1;

    Alumno lista[100];

    entero = 9;
    alumno1.boleta = 0;

    printf("%d\n", alumno1.boleta);

    return 0;
}
