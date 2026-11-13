#include <stdio.h>
#include <stdlib.h>

int main()
{
    int * ptr;
    int a = 10;

    ptr = &a;
    *ptr += 10;

    *(ptr-1) = 666;

    printf("%p - %p\n%i - %i\n", ptr-1, &a, *(ptr-1), a);


    return 0;
}
