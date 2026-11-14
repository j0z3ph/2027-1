#include <stdio.h>

int main()
{
    FILE *archi = fopen("archi", "wb");
    int a = 1;

    fwrite(&a, sizeof(a), 1, archi);

    fclose(archi);

    return 0;
}
