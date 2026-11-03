#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    fork();
    fork();
    fork();

    printf("Hola\n");
    
    return 0;
}
