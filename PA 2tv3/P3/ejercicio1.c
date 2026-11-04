#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main()
{
    int hijos = 1;
    pid_t pid = fork();
    if (pid < 0)
        printf("Error :(\n");
    else if (pid == 0)
        printf("Hijo %d\n", hijos);
    else
    {
        // Creamos un segundo hijo
        hijos++;
        pid = fork();
        if (pid < 0)
            printf("Error :(\n");
        else if (pid == 0)
            printf("Hijo %d\n", hijos);
        else
            printf("Padre\n");
    }

    return 0;
}
