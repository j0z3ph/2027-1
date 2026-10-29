#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *puntero = malloc(sizeof(int));
    *puntero = 0;

    pid_t pid;
    pid = fork();

    *puntero = 666;

    printf("%d - (%d) - (%d)\n", *puntero, getpid(), pid);
    
    return 0;
}
