#include <stdio.h>
#include <stdlib.h>

int main()
{
    while (1)
    {
        int *ptr = malloc(sizeof(int));
        *ptr = 10;
        free(ptr);
    }
    // printf("%p\n", ptr);

    // while(100) {
    //     int a;
    //     a = 10;
    // }

    return 0;
}
